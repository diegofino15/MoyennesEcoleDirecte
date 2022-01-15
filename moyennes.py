#!/usr/bin/python3

# Import the needed modules for the program
import requests
import json
import getpass

# Define the different website types
website_part1 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moyennes Ecole Directe</title>
    <style>
        body, div, form, input, select, p { 
        padding: 0;
        margin: 0;
        outline: none;
        font-family: Roboto, Arial, sans-serif;
        font-size: 16px;
        color: #eee;
        }
        h1, h2 {
        text-transform: uppercase;
        font-weight: 600;
        font-size: xx-large;
        text-align: center;
        }
        h3 {
        text-align: center;
        }
        h2 {
        margin: 0 0 0 8px;
        }
        .main-block {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%;
        padding: 25px;
        background: rgba(0, 0, 0, 0.5); 
        }
        .left-part, form {
        padding: 25px;
        }
        .left-part {
        text-align: center;
        }
        form {
        background: rgba(0, 0, 0, 0.7); 
        }
        .title {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        }
        .info {
        display: flex;
        flex-direction: column;
        }
        option {
        background: black; 
        border: none;
        }
        @media (min-width: 900px) {
        html, body {
        height: 100%;
        }
        .main-block {
        flex-direction: row;
        height: max-content;
        }
        .left-part, form {
        flex: 1;
        height: auto;
        }
        }
        body {
        background-color: rgba(0, 0, 0, 0.8);
        }
        .emphasized { 
        font-style: italic;
        }
        .btn-item, button {
        padding: 10px 5px;
        margin-top: 20px;
        border-radius: 5px; 
        border: none;
        width: 100%;
        background: #26a9e0; 
        text-decoration: none;
        font-size: 15px;
        font-weight: 400;
        color: #fff;
        }
        .btn-item {
        display: inline-block;
        margin: 20px 5px 0;
        }
        .centered {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%;
        vertical-align:middle;
        }
    </style>
</head>
<body style="background-color: rgba(0, 0, 0, 0.8)">
'''

# Define a function to get the informations from the website
def login(username, password):
    # Initialize the session
    s = requests.Session()

    # The login url
    url = 'https://api.ecoledirecte.com/v3/login.awp?v=1.8.26'

    # The data that will be sended to the website
    payload = {
        'identifiant': username,
        'motdepasse': password
    }
    payload_string = 'data=' + json.dumps(payload)

    # Send the request to get the informations
    print('Connecting...')
    request = requests.Request('POST', url, data=payload_string)
    prepared_request = request.prepare()
    response = s.send(prepared_request)
    # Loads the response into a json
    json_response = json.loads(response.text)

    # Verify if there is no error
    if json_response['code'] == 200:
        print('Connected successfully !')
        # Get the needed informations
        student_id = json_response['data']['accounts'][0]['id']
        student_login_token = json_response['token']

        # The login url to get the average
        url_average = f'https://api.ecoledirecte.com/v3/eleves/{student_id}/notes.awp?verbe=get&v=1.8.26'

        # The data that will be sended to the url
        payload_average = {
            'x-token': student_login_token
        }

        # Send the request to get the informations
        print('Getting notes...')
        average_request = requests.Request('POST', url_average, headers=payload_average, data='data={}')
        prepared_average_request = average_request.prepare()
        average_response = s.send(prepared_average_request)
        # Loads the response into a json
        json_average_response = json.loads(average_response.text)

        # Verify if there is no error and return the informations
        if json_average_response['code'] == 200: return [json_average_response['data'], json_response]
        else: return None
    else: return None

# Gets the informations given to the script
username_received = input('Username : ')
password_received = getpass.getpass(prompt="Password : ")

# Try to connect to the website and get the informations
if username_received != '' and password_received != '':
    data = login(username_received, password_received)
    if data is not None:
        averages = data
        login_successful = True
    else: login_successful = False
else: login_successful = False

# If the login is successful, proceed the program
if login_successful:
    print('Notes got successfully !')
    print('Calculating averages...')
    # Gets the complete name of the user
    if averages[1]['data']['accounts'][0]['particule'] == '': space = ''
    else: space = ' '
    complete_name = averages[1]['data']['accounts'][0]['prenom'] + ' ' + averages[1]['data']['accounts'][0]['particule'] + space + averages[1]['data']['accounts'][0]['nom']

    # Define a function to round to the hundredth
    def r(x): return (round(x * 100) / 100)
    
    # Define a variable for the missing averages strings
    missing_average_string = '--:--'

    # Define a variable for the trimestres codes
    trimestres_codes = ['A001', 'A002', 'A003']
    # Define a variable for the materies codes
    subjects_codes = {
        'francais': 'FRANC',
        'latin': 'LCALA',
        'anglais': 'AGL1',
        'espagnol': 'ESP2',
        'allemand': 'ALL2',
        'histoire': 'HI-GE',
        'emc': 'EMC',
        'maths': 'MATHS',
        'physique': 'PH-CH',
        'svt': 'SVT',
        'technologie': 'TECHN',
        'sport': 'EPS',
        'arts': 'A-PLA',
        'musique': 'EDMUS',
        'chorale': 'CHKCO',
        'general': 'GENERAL'
    }
    # Define a variable where the averages will be stored
    results = {}

    # Load "results" with all of the materies in all of the trimestres
    for trimestre in trimestres_codes:
        for subject in subjects_codes.keys():
            subject_code = subjects_codes[subject]
            results.update({(trimestre, subject_code): [0, 0, 0, 0]})
    
    # Add-up the notes to get the average
    for element in averages[0]['notes']:
        # Verify if the note is a float
        if element['valeur'][0] == 'A': is_convertible = False
        else: is_convertible = True
        
        # Double the coeficient if the note is a DST
        if element['typeDevoir'] == 'DEVOIR SUR TABLE': coeficient = 2
        else: coeficient = 1

        # Do the average of the user if it is not Abs
        if is_convertible:
            # Store the index and the class note
            index = (element['codePeriode'], element['codeMatiere'])
            try:
                note = float(element['valeur'].replace(',', '.')) / float(element['noteSur']) * 20
                note_class = float(element['moyenneClasse'].replace(',', '.')) / float(element['noteSur']) * 20

                # Add the note to the results
                results[index][0] += note * coeficient
                results[index][1] += coeficient
                # Add-up to the class average
                results[index][2] += note_class * coeficient
                results[index][3] += coeficient
            except: pass
    
    # Add-up the notes to get the general average
    for index in results.keys():
        if index[1] != subjects_codes['general']:
            results[(index[0], subjects_codes['general'])][0] += results[index][0]
            results[(index[0], subjects_codes['general'])][1] += results[index][1]
            results[(index[0], subjects_codes['general'])][2] += results[index][2]
            results[(index[0], subjects_codes['general'])][3] += results[index][3]
    
    # Calculate the averages
    for index in results.keys():
        # Replace the void averages with a string
        if results[index] == [0, 0, 0, 0]: results[index] = [missing_average_string, missing_average_string]
        # Calculate the average
        else:
            average = str(r(results[index][0] / results[index][1]))
            class_average = str(r(results[index][2] / results[index][3]))

            results[index] = [average, class_average]
    
    # Get the averages into dedicated variables
    try:
        # Define a function to return the average from the results list
        def return_average(matiere_code, index=0): return [results[(trimestres_codes[0], matiere_code)][index], results[(trimestres_codes[1], matiere_code)][index], results[(trimestres_codes[2], matiere_code)][index]]

        # Gets the averages into dedicated variables
        general_averages = return_average(subjects_codes['general'])
        general_class_averages = return_average(subjects_codes['general'], index=1)
        francais = return_average(subjects_codes['francais'])
        latin = return_average(subjects_codes['latin'])
        anglais = return_average(subjects_codes['anglais'])
        espagnol = return_average(subjects_codes['espagnol'])
        allemand = return_average(subjects_codes['allemand'])
        histoire = return_average(subjects_codes['histoire'])
        emc = return_average(subjects_codes['emc'])
        maths = return_average(subjects_codes['maths'])
        physique = return_average(subjects_codes['physique'])
        svt = return_average(subjects_codes['svt'])
        techno = return_average(subjects_codes['technologie'])
        sport = return_average(subjects_codes['sport'])
        arts = return_average(subjects_codes['arts'])
        musique = return_average(subjects_codes['musique'])
        chorale = return_average(subjects_codes['chorale'])

        # Finally print the website
        website = f'''
            <div class="main-block" style="background-color: rgba(0, 0, 0, 0.2)">
                <div class="left-part">
                    <title>Moyennes</title>
                    <hr>
                    <h3>Moyennes de : {complete_name}</h3>
                    <hr>
                    <hr>
                    <h1>Moyenne generale</h1>
                    <h3>1er trimestre : {general_averages[0]}</h3>
                    <span class="emphasized">Classe : {general_class_averages[0]}</span>
                    <h3>2e trimestre : {general_averages[1]}</h3>
                    <span class="emphasized">Classe : {general_class_averages[1]}</span>
                    <h3>3e trimestre : {general_averages[2]}</h3>
                    <span class="emphasized">Classe : {general_class_averages[2]}</span>
                    <hr>
                    <hr>
                </div>
            </div>
            <div class="main-block" style="background-color: rgba(0, 0, 0, 0.2)">
                <div class="left-part">
                    <hr>
                    <h2>Francais</h2>
                    <h3>1er trimestre : {francais[0]}</h3>
                    <h3>2e trimestre : {francais[1]}</h3>
                    <h3>3e trimestre : {francais[2]}</h3>
                    <hr>
                    <h2>Latin</h2>
                    <h3>1er trimestre : {latin[0]}</h3>
                    <h3>2e trimestre : {latin[1]}</h3>
                    <h3>3e trimestre : {latin[2]}</h3>
                    <hr>
                    <h2>Anglais LV1</h2>
                    <h3>1er trimestre : {anglais[0]}</h3>
                    <h3>2e trimestre : {anglais[1]}</h3>
                    <h3>3e trimestre : {anglais[2]}</h3>
                    <hr>
                    <h2>Espagnol LV2</h2>
                    <h3>1er trimestre : {espagnol[0]}</h3>
                    <h3>2e trimestre : {espagnol[1]}</h3>
                    <h3>3e trimestre : {espagnol[2]}</h3>
                    <hr>
                    <h2>Allemand LV2</h2>
                    <h3>1er trimestre : {allemand[0]}</h3>
                    <h3>2e trimestre : {allemand[1]}</h3>
                    <h3>3e trimestre : {allemand[2]}</h3>
                    <hr>
                    <h2>Histoire - Geographie</h2>
                    <h3>1er trimestre : {histoire[0]}</h3>
                    <h3>2e trimestre : {histoire[1]}</h3>
                    <h3>3e trimestre : {histoire[2]}</h3>
                    <hr>
                    <h2>EMC</h2>
                    <h3>1er trimestre : {emc[0]}</h3>
                    <h3>2e trimestre : {emc[1]}</h3>
                    <h3>3e trimestre : {emc[2]}</h3>
                    <hr>
                </div>
                <div class="left-part">
                    <hr>
                    <h2>Mathematiques</h2>
                    <h3>1er trimestre : {maths[0]}</h3>
                    <h3>2e trimestre : {maths[1]}</h3>
                    <h3>3e trimestre : {maths[2]}</h3>
                    <hr>
                    <h2>Physique - Chimie</h2>
                    <h3>1er trimestre : {physique[0]}</h3>
                    <h3>2e trimestre : {physique[1]}</h3>
                    <h3>3e trimestre : {physique[2]}</h3>
                    <hr>
                    <h2>SVT</h2>
                    <h3>1er trimestre : {svt[0]}</h3>
                    <h3>2e trimestre : {svt[1]}</h3>
                    <h3>3e trimestre : {svt[2]}</h3>
                    <hr>
                    <h2>Technologie</h2>
                    <h3>1er trimestre : {techno[0]}</h3>
                    <h3>2e trimestre : {techno[1]}</h3>
                    <h3>3e trimestre : {techno[2]}</h3>
                    <hr>
                    <h2>EPS</h2>
                    <h3>1er trimestre : {sport[0]}</h3>
                    <h3>2e trimestre : {sport[1]}</h3>
                    <h3>3e trimestre : {sport[2]}</h3>
                    <hr>
                    <h2>Arts plastiques</h2>
                    <h3>1er trimestre : {arts[0]}</h3>
                    <h3>2e trimestre : {arts[1]}</h3>
                    <h3>3e trimestre : {arts[2]}</h3>
                    <hr>
                    <h2>Musique / Chorale</h2>
                    <h3>1er trimestre : {musique[0]}&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;{chorale[0]}</h3>
                    <h3>2e trimestre : {musique[1]}&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;{chorale[1]}</h3>
                    <h3>3e trimestre : {musique[2]}&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;{chorale[2]}</h3>
                    <hr>
                </div>
            </div>
            <div class="main-block" style="background-color: rgba(0, 0, 0, 0.2)">
                <div class="left-part">
                    <p>Site par : Diego Finocchiaro</p>
                    <p>&nbsp;</p>
                    <p>&nbsp;</p>
                    <span class="emphasized">Les moyennes affichées sont des approximations, elles ne sont pas exactes.</span>
                </div>
            </div>
        </body>
        </html>
        '''
        # Print the website
        final_website = website_part1 + website

        with open('./index.html', 'w') as file:
            file.write(final_website)
            file.close()

        print('Finished !\n')
        print('Open the "index.html" in your browser to see the website ! \n')
 
    except:
        # Print that there was an error
        print('There was an error, please contact the creator of this module.')

else:
    # Print that the login failed
    print('The connection to your account failed, try another username or another password.')

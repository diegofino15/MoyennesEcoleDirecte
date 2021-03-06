# Import the needed modules
import requests
import sys
import json
import getpass
import os
# Import the python script with the utilities
from utilities import *

# Define a function to get the variable names from a file
def get_custom_info():
    try:
        with open('./custom.json', 'r') as file:
            infos = json.load(file)
            file.close()

        return {
            'cache-file-name' : infos['cache-file-name'],
            'user-prefix' : infos['user-prefix'],
            'save-prefix' : infos['save-prefix'],
            'remove-prefix' : infos['remove-prefix'],

            'json-prefix' : infos['json-prefix'],
            'terminal-prefix' : infos['terminal-prefix'],
            'website-prefix' : infos['website-prefix']
        }

    except:
        infos = {
            'cache-file-name' : 'users',
            'user-prefix' : '-user',
            'save-prefix' : '-save',
            'remove-prefix' : '-remove',

            'json-prefix' : '-j',
            'terminal-prefix' : '-t',
            'website-prefix' : '-s'
        }

        with open("./custom.json", 'w') as file:
            json.dump(infos, file)
            file.close()
        
        return infos

# Define a function to search if there is a registered account
def auto_connect(cache_file_name):
    try:
        with open(f"./{cache_file_name}.json", 'r') as file:
            infos = json.load(file)
            file.close()
        
        username = infos['username']
        password = infos['password']

        print(f'Auto connecting to : {username}')

        return {
            'successful': True,
            'username': username,
            'password': password
        }
    except:
        return {
            'successful': False
        }

# Define a function to get the username and the password
def get_info(cache_file_name, terminal_prefix, webiste_prefix, json_prefix, save_prefix, remove_prefix, user_prefix):
    # Define the variables of the different input types
    return_types = [terminal_prefix, webiste_prefix, json_prefix]
    all_types = [terminal_prefix, webiste_prefix, json_prefix, save_prefix, remove_prefix, user_prefix]

    # Collect the informations given to the script
    infos_received = sys.argv

    # Define the basic variables
    username = ''
    given_username = False
    return_type = terminal_prefix
    save = False
    remove = False

    # Cycle trough the given informations and extract the needed infos
    for index in range(len(infos_received)):
        info = infos_received[index]
        
        # Detect the received info
        if info in return_types: return_type = info
        elif info == save_prefix: save = True
        elif info == remove_prefix: remove = True
        elif info == user_prefix:
            given_username = True
            username = infos_received[index + 1]
    
    # Verify that the given informations are logic
    if save and not given_username: sys.exit("Pas d'identifiant sp??cifi??")
    elif remove and not given_username: sys.exit("Pas d'identifiant sp??cifi??")
    if save: remove = False
    if remove: save = False

    # Try to auto-connect with a registered username
    if not given_username:
        infos = auto_connect(cache_file_name)
        if infos['successful']:
            return {
                'username': infos['username'],
                'password': infos['password'],
                'return_type': return_type,
                'save': False,
                'remove': False,
                'auto': True
            }
        else: sys.exit("Pas d'identifiant sp??cifi??")
    # Ask for the password normally
    else:
        if username not in all_types:
            return {
                'username': username,
                'password': getpass.getpass(prompt="Mot de passe : "),
                'return_type': return_type,
                'save': save,
                'remove': remove,
                'auto': False
            }
        else: sys.exit("Pas d'identifiant sp??cifi??")

# Define a function to save the account
def save_info(username, password, cache_file_name):
    data = {
        'username': username,
        'password': password
    }
    with open(f'./{cache_file_name}.json', 'w') as file:
        json.dump(data, file)
        file.close()
       
    print("Compte enregistr??")

# Define a function to remove and account given
def remove_account(username, cache_file_name):
    try: 
        with open(f'./{cache_file_name}.json', 'r') as file:
            infos = json.load(file)
            file.close()
        
        if username == infos['username']: os.remove("./users.json")
        else: sys.exit("Pas d'identifiant enregistr?? sous ce nom")
    except: sys.exit("Pas d'identifiant enregistr??")

# Define a function to login into Ecole Directe API and get the notes
def login(username, password):
    # The login url
    url = 'https://api.ecoledirecte.com/v3/login.awp?v=1.8.26'

    # Initialize the session
    s = requests.Session()

    # The data that will be sended to the website
    payload = {
        'identifiant': username,
        'motdepasse': password
    }
    payload_string = 'data=' + json.dumps(payload)

    # Send the request to get the informations
    request = requests.Request('POST', url, data=payload_string)
    prepared_request = request.prepare()
    response = s.send(prepared_request)
    # Loads the response into a json
    json_response = json.loads(response.text)

    # Verify if there is no error
    if json_response['code'] == 200:
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
        average_request = requests.Request('POST', url_average, headers=payload_average, data='data={}')
        prepared_average_request = average_request.prepare()
        average_response = s.send(prepared_average_request)
        # Loads the response into a json
        json_average_response = json.loads(average_response.text)

        # Verify if there is no error and return the informations
        if json_average_response['code'] == 200: return [json_average_response['data'], json_response]
        else: return None
    else: return None

# Define a function to verify that the username given is not None and that the login was successful
def verify_login(username, password):
    # Try to connect to the website and get the informations
    if username != '' and password != '':
        data = login(username, password)
        if data is not None:
            return [True, data]
        else: return [False]
    else: return [False]

# Define a function to calculate the averages and returning them
def calculate_averages(averages):
    # Gets the complete name of the user
    if averages[1]['data']['accounts'][0]['particule'] == '': space = ''
    else: space = ' '
    complete_name = averages[1]['data']['accounts'][0]['prenom'] + ' ' + averages[1]['data']['accounts'][0]['particule'] + space + averages[1]['data']['accounts'][0]['nom']

    # Define a function to round to the hundredth
    def r(x): return (round(x * 100) / 100)

    # Define a variable for the missing averages strings
    missing_average_string = '--:--'

    trimestres_codes = get_codes()['trimetres_codes']
    subjects_codes = get_codes()['subjects_codes']

    # Define a variable where the averages will be stored
    results = {}

    # Load "results" with all of the materies in all of the trimestres
    for trimestre in trimestres_codes:
        for subject in subjects_codes.keys():
            subject_code = subjects_codes[subject]['code']
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
        if index[1] != subjects_codes['general']['code']:
            # Get the coeficient of the subject
            for subject in subjects_codes.keys():
                subject_code = subjects_codes[subject]
                if subject_code['code'] == index[1]:
                    coeficient = subject_code['coef']
                    break
            
            results[(index[0], subjects_codes['general']['code'])][0] += results[index][0] * coeficient
            results[(index[0], subjects_codes['general']['code'])][1] += results[index][1] * coeficient
            results[(index[0], subjects_codes['general']['code'])][2] += results[index][2] * coeficient
            results[(index[0], subjects_codes['general']['code'])][3] += results[index][3] * coeficient

    # Calculate the averages
    for index in results.keys():
        # Replace the void averages with a string
        if results[index] == [0, 0, 0, 0]: results[index] = [missing_average_string, missing_average_string]
        # Calculate the average
        else:
            average = str(r(results[index][0] / results[index][1]))
            class_average = str(r(results[index][2] / results[index][3]))

            if average[1] == '.': average = f'0{average}'
            if len(average) == 4: average = f'{average}0'
                
            if class_average[1] == '.': class_average = f'0{class_average}'
            if len(class_average) == 4: class_average = f'{class_average}0'

            results[index] = [average, class_average]

    def return_average(matiere_code, index=0): return [results[(trimestres_codes[0], matiere_code['code'])][index], results[(trimestres_codes[1], matiere_code['code'])][index], results[(trimestres_codes[2], matiere_code['code'])][index]]

    return {
        # Gets the averages into dedicated variables
        "complete_name": complete_name,
        "general_averages" : return_average(subjects_codes['general']),
        "general_class_averages" : return_average(subjects_codes['general'], index=1),
        "francais" : return_average(subjects_codes['francais']),
        "latin" : return_average(subjects_codes['latin']),
        "anglais" : return_average(subjects_codes['anglais']),
        "espagnol" : return_average(subjects_codes['espagnol']),
        "allemand" : return_average(subjects_codes['allemand']),
        "histoire" : return_average(subjects_codes['histoire']),
        "emc" : return_average(subjects_codes['emc']),
        "maths" : return_average(subjects_codes['maths']),
        "physique" : return_average(subjects_codes['physique']),
        "svt" : return_average(subjects_codes['svt']),
        "techno" : return_average(subjects_codes['technologie']),
        "sport" : return_average(subjects_codes['sport']),
        "arts" : return_average(subjects_codes['arts']),
        "musique" : return_average(subjects_codes['musique']),
        "chorale" : return_average(subjects_codes['chorale'])
    }

# Define a function to return the wanted result
def return_results(parameters, custom_infos, return_type):
    if return_type == custom_infos['website-prefix']:
        with open('./index.html', 'w') as file:
            file.write(print_website(parameters))
            file.close()
        sys.exit('Site internet sauvegard?? dans "./index.html" !')

    elif return_type == custom_infos['terminal-prefix']:
        for i in range(3):
            print(return_terminal(parameters, i))
        sys.exit()
    
    elif return_type == custom_infos['json-prefix']:
        print(json.dumps(parameters))
        sys.exit()

# Define a main function, who is the principal program
def run():
    # Get the informations
    prefixes = get_custom_info()
    informations = get_info(prefixes['cache-file-name'], prefixes['terminal-prefix'], prefixes['website-prefix'], prefixes['json-prefix'], prefixes['save-prefix'], prefixes['remove-prefix'], prefixes['user-prefix'])
    reponse = verify_login(informations['username'], informations['password'])
    # Verify that the login was successful
    if reponse[0]:
        averages = calculate_averages(reponse[1])
        # Return the wanted result
        if informations['save']: save_info(informations['username'], informations['password'], prefixes['cache-file-name'])

        if informations['remove']: 
            remove_account(informations['username'], prefixes['cache-file-name'])
            print(f"L'identifiant {informations['username']} n'est maintenant plus enregistr??")
        else: return_results(averages, prefixes, informations['return_type'])
        sys.exit()
    else:
        if informations['auto']:
            remove_account(informations['username'], prefixes['cache-file-name'])
            sys.exit("Cet identifiant et ce mot de passe sont invalides, suppression de la sauvegarde")
        sys.exit('Identifiant ou mot de passe invalide.')


if __name__ == '__main__': run()

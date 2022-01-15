# This file is for returning the full website already finished
def print_website(parameters):
    return ('''
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
    <body style="background-color: rgba(0, 0, 0, 0.8)">''' + f'''
        <div class="main-block" style="background-color: rgba(0, 0, 0, 0.2)">
            <div class="left-part">
                <title>Moyennes</title>
                <hr>
                <h3>Moyennes de : {parameters['complete_name']}</h3>
                <hr>
                <hr>
                <h1>Moyenne generale</h1>
                <h3>1er trimestre : {parameters['general_averages'][0]}</h3>
                <span class="emphasized">Classe : {parameters['general_class_averages'][0]}</span>
                <h3>2e trimestre : {parameters['general_averages'][1]}</h3>
                <span class="emphasized">Classe : {parameters['general_class_averages'][1]}</span>
                <h3>3e trimestre : {parameters['general_averages'][2]}</h3>
                <span class="emphasized">Classe : {parameters['general_class_averages'][2]}</span>
                <hr>
                <hr>
            </div>
        </div>
        <div class="main-block" style="background-color: rgba(0, 0, 0, 0.2)">
            <div class="left-part">
                <hr>
                <h2>Francais</h2>
                <h3>1er trimestre : {parameters['francais'][0]}</h3>
                <h3>2e trimestre : {parameters['francais'][1]}</h3>
                <h3>3e trimestre : {parameters['francais'][2]}</h3>
                <hr>
                <h2>Latin</h2>
                <h3>1er trimestre : {parameters['latin'][0]}</h3>
                <h3>2e trimestre : {parameters['latin'][1]}</h3>
                <h3>3e trimestre : {parameters['latin'][2]}</h3>
                <hr>
                <h2>Anglais LV1</h2>
                <h3>1er trimestre : {parameters['anglais'][0]}</h3>
                <h3>2e trimestre : {parameters['anglais'][1]}</h3>
                <h3>3e trimestre : {parameters['anglais'][2]}</h3>
                <hr>
                <h2>Espagnol LV2</h2>
                <h3>1er trimestre : {parameters['espagnol'][0]}</h3>
                <h3>2e trimestre : {parameters['espagnol'][1]}</h3>
                <h3>3e trimestre : {parameters['espagnol'][2]}</h3>
                <hr>
                <h2>Allemand LV2</h2>
                <h3>1er trimestre : {parameters['allemand'][0]}</h3>
                <h3>2e trimestre : {parameters['allemand'][1]}</h3>
                <h3>3e trimestre : {parameters['allemand'][2]}</h3>
                <hr>
                <h2>Histoire - Geographie</h2>
                <h3>1er trimestre : {parameters['histoire'][0]}</h3>
                <h3>2e trimestre : {parameters['histoire'][1]}</h3>
                <h3>3e trimestre : {parameters['histoire'][2]}</h3>
                <hr>
                <h2>EMC</h2>
                <h3>1er trimestre : {parameters['emc'][0]}</h3>
                <h3>2e trimestre : {parameters['emc'][1]}</h3>
                <h3>3e trimestre : {parameters['emc'][2]}</h3>
                <hr>
            </div>
            <div class="left-part">
                <hr>
                <h2>Mathematiques</h2>
                <h3>1er trimestre : {parameters['maths'][0]}</h3>
                <h3>2e trimestre : {parameters['maths'][1]}</h3>
                <h3>3e trimestre : {parameters['maths'][2]}</h3>
                <hr>
                <h2>Physique - Chimie</h2>
                <h3>1er trimestre : {parameters['physique'][0]}</h3>
                <h3>2e trimestre : {parameters['physique'][1]}</h3>
                <h3>3e trimestre : {parameters['physique'][2]}</h3>
                <hr>
                <h2>SVT</h2>
                <h3>1er trimestre : {parameters['svt'][0]}</h3>
                <h3>2e trimestre : {parameters['svt'][1]}</h3>
                <h3>3e trimestre : {parameters['svt'][2]}</h3>
                <hr>
                <h2>Technologie</h2>
                <h3>1er trimestre : {parameters['techno'][0]}</h3>
                <h3>2e trimestre : {parameters['techno'][1]}</h3>
                <h3>3e trimestre : {parameters['techno'][2]}</h3>
                <hr>
                <h2>EPS</h2>
                <h3>1er trimestre : {parameters['sport'][0]}</h3>
                <h3>2e trimestre : {parameters['sport'][1]}</h3>
                <h3>3e trimestre : {parameters['sport'][2]}</h3>
                <hr>
                <h2>Arts plastiques</h2>
                <h3>1er trimestre : {parameters['arts'][0]}</h3>
                <h3>2e trimestre : {parameters['arts'][1]}</h3>
                <h3>3e trimestre : {parameters['arts'][2]}</h3>
                <hr>
                <h2>Musique / Chorale</h2>
                <h3>1er trimestre : {parameters['musique'][0]}&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;{parameters['chorale'][0]}</h3>
                <h3>2e trimestre : {parameters['musique'][1]}&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;{parameters['chorale'][1]}</h3>
                <h3>3e trimestre : {parameters['musique'][2]}&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;{parameters['chorale'][2]}</h3>
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
''')

# This is for returning the averages in the terminal
def return_terminal(parameters, index):
    return f'''
 ___________________________________
|                                   |
|           Trimestre {index + 1}             |
|                                   |
|      Moyenne générale : {parameters['general_averages'][index]}     |
|   Moyenne générale classe : {parameters['general_class_averages'][index]} |
|                                   |
|   Français : {parameters['francais'][index]}                |
|   Latin : {parameters['latin'][index]}                   |
|   Anglais : {parameters['anglais'][index]}                 |
|   Espagnol : {parameters['espagnol'][index]}                |
|   Allemand : {parameters['allemand'][index]}                |
|   Histoire-Géo : {parameters['histoire'][index]}            |
|   EMC : {parameters['emc'][index]}                     |
|   Maths : {parameters['maths'][index]}                   |
|   Physique : {parameters['physique'][index]}                |
|   SVT : {parameters['svt'][index]}                     |
|   Techno : {parameters['techno'][index]}                  |
|   Sport : {parameters['sport'][index]}                   |
|   Arts-Pla : {parameters['arts'][index]}                |
|   Musique : {parameters['musique'][index]}                 |
|   Chorale : {parameters['chorale'][index]}                 |
 ___________________________________
'''

# This is for returning the codes of the subjects and the trimetres
def get_codes():
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

    return {
        'trimetres_codes': trimestres_codes,
        'subjects_codes': subjects_codes
    }




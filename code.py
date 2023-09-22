import pandas as pd
import numpy as np

# print(t.columns)
headers = [
    # 'Code service CH',
    # 'Reference document',
    # '1 Articles CGI',
    # '2 Articles CGI',
    # '3 Articles CGI',
    # '4 Articles CGI',
    # '5 Articles CGI',
    'No disposition',
    'Date mutation',
    'Nature mutation',
    'Valeur fonciere',
    'No voie',
    'B/T/Q',
    'Type de voie',
    'Code voie',
    'Voie',
    'Code postal',
    'Commune',
    'Code departement',
    'Code commune',
    'Prefixe de section',
    'Section',
    'No plan',
    # 'No Volume',
    # '1er lot',
    # 'Surface Carrez du 1er lot',
    # '2eme lot',
    # 'Surface Carrez du 2eme lot',
    # '3eme lot',
    # 'Surface Carrez du 3eme lot',
    # '4eme lot',
    # 'Surface Carrez du 4eme lot',
    # '5eme lot',
    # 'Surface Carrez du 5eme lot',
    'Nombre de lots',
    'Code type local',
    'Type local',
    # 'Identifiant local',
    'Surface reelle bati',
    'Nombre pieces principales',
    'Nature culture',
    'Nature culture speciale',
    'Surface terrain'
]
t = pd.read_csv('valeursfoncieres-2021.txt',
                # nrows=100,
                delimiter='|')
t = t[headers]
pd.set_option('display.max_columns', None)
print(t.count())
t = t.dropna(subset=['Surface terrain', 'Nature culture', 'Valeur fonciere'])
print(t.count())
# t = t[~t['Surface terrain'].isna()]
# t = t[~t['Valeur fonciere'].isna()]
print(t['Nature culture'].value_counts())
# print(t['Code postal'].value_counts())
# f = t[cp_str.str.startswith('14') & cp_str.str.len() == 7]
t['prix'] = pd.to_numeric(t['Valeur fonciere'].str.replace(',', '.'))
print('')
print(t['Valeur fonciere'].value_counts(dropna=False))
print(t['prix'].value_counts(dropna=False))
t = t[t['Surface terrain'] != 0]
print(t['Surface terrain'].min())
print('')
# print(t['Surface terrain'].value_counts(dropna=False))
t['m2'] = t['prix'] / t['Surface terrain']
t['prix_m2'] = t['prix'] / t['Surface terrain']
print(t['prix_m2'].value_counts(dropna=False))

t['constructible'] = t['Nature culture'].apply(str).str.startswith('A') | (t['Nature culture'].apply(str) == 'S')
# t['constructible'] = t['Nature culture'].apply(str) == 'S'
print(t.groupby('constructible')['prix_m2'].value_counts())
print(t.groupby('Nature culture')['prix_m2'].mean())
# print(t.groupby('constructible')['prix_m2'].transform('mean'))
print(t.head())

 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
#import matplotlib.pyplot as plt
import json
import os
from pygments import highlight, lexers, formatters
import pprint

basedir = os.path.abspath(os.path.dirname(__file__))



#from .models import charge_df

# Pour afficher les graphiques inline
#%matplotlib inline

def charge_df():
    #FILE = os.path.join(basedir, 'datas/movie_metadata.csv')
    FILE = os.path.join(basedir, 'datas/movie_metadata_nettoye_1.csv')
    
    #FILE = 'datas/movie_metadata.csv'
    df = pd.read_csv(FILE)
    
    return df

MA_BASE = charge_df()


'''
def get_df_value(mon_id):
    #u = MA_BASE.loc[nb,['director_name','movie_title']]
    #return resultat(MA_BASE, 1)


    #colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
    formatted_json = json.dumps(resultat(MA_BASE, mon_id), indent=4)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)

    #return json.dumps(resultat(MA_BASE, 1), indent=4)
    return pprint.pformat(formatted_json)
'''

'''def get_df_value(mon_id):
    ma_recherche = resultat(MA_BASE, mon_id)
    return ma_recherche
'''

def get_df_value(mon_id):
    ma_recherche = resultat(MA_BASE, mon_id)
    return str(ma_recherche)

def get_df_value2(mon_id):
    ma_recherche = resultat(MA_BASE, mon_id)
    
    #colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
    formatted_json = json.dumps(str(ma_recherche), indent=4)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)

    return pprint.pformat(formatted_json)


'''
def retourne_resultat_fichier(m_dataframe, id):
    film_name = m_dataframe[m_dataframe['id']==id]['movie_title'].values[0]   
    return {"id": id, "name":film_name}
'''
'''
def resultat(m_dataframe, id):
    res = []
    for i in [1, 2, 3, 4, 5]:
        res.append(retourne_resultat_fichier(m_dataframe, i))
    
    return { "_results": res}
'''
    
def retourne_resultat_fichier(m_dataframe, id):
    film_name = m_dataframe[m_dataframe['id']==id]['movie_title'].values[0]
    return {"id": id, "name":film_name}

def resultat(m_dataframe, id):
    film_label = m_dataframe[m_dataframe['id']==id]['label'].values[0]
    res = []
    
    # On recherche les données ayant le même label
    m_df_tmp = m_dataframe[m_dataframe['label']==film_label]\
            .sort_values('imdb_score',ascending=False).head(5)
    for i in m_df_tmp['id'].get_values():
        res.append(retourne_resultat_fichier(m_dataframe, i))
    
    return { "_results": res}
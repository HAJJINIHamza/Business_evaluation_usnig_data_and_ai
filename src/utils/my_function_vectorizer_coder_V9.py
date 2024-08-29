#Importation des bibliothèques
import nltk
import numpy as np
import re
from copy import deepcopy
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pandas as pd

#La fonction vectorizer_coder (colonne, vocabulary) | input : colonne contenant des paragraphes et un vocabulaire sur lequel va se baser pour coder
#---------------------------------------------------> output : copy_vocabulaire: Dataframe contenant les mot du vocabulaire comme colonnes et les valeurs (1,0) 
#                                                     business_description_vectorizer: les textes de colonne vectorizer 

def vectorizer_coder (colonne, vocabulaire):
    #vocabulaire_business est une dataframe de 0 lignes (shape : 0,nbr de mot dans le vocab)
    #Ajoutons n = len(colonne) lignes de valeurs 0 à la dataframe vocabulaire_business
    print ('Ajoutons n = len(colonne) lignes de valeurs 0 à la dataframe vocabulaire_business')
    copy_vocabulaire = deepcopy(vocabulaire)
    zeros = np.zeros ( (len(colonne), len(vocabulaire.columns)) )
    copy_vocabulaire = pd.DataFrame( zeros, columns = [copy_vocabulaire] )


    #La fonction vectorise d'abord la colonne | input : colonne --------> output : la ligne de chaque colonne vectoriser
    #download des stopwords
    nltk.download('stopwords')
    #Liste des stopwords
    liststopwords = stopwords.words("english")

    #appliquant le preprocesseing à la nouvelle colonne
    print ('''Entrain d'appliquer le preprocessing à la colonne''')    
    Business_description2 = []
    d = 0
    for description in colonne:
        print ('voctorization de la description :', d)
        d=d+1 
        #Enlever les ponctuations
        description = re.sub('[^a-zA-Z]', ' ',description)
        #Rendre tout les lettre en minuscule
        description = description.lower()
        #Split le text en mots
        description = description.split()
        #Enlever les stopwords
        description = [word for word in description if word not in liststopwords]
        #Reformant maintenant la phrase
        #description = ' '.join(description)
        #Appliquant le porterstemmer qui rend chaque mot en sa forme original
        #description = PorterStemmer().stem(description)
        #ajouter le mot à la nouvelle liste
        Business_description2.append(description)


    #-----------------------------------------------------------------------------------------------
    #La fonction qui vectorise une phrase                                                          |
    #la phrase doit etre déja passé par le preprocessing                                           |
    #def vectoriser (colonne):                                                                     |
        #return CountVectorizer().fit_transform(colonne).toarray()                                 |
    #-----------------------------------------------------------------------------------------------



    #Transformons Business_description2 en une dataframe
    print ('Entrain de transformer la colonne à une dataframe pour obtenir une colonne de description vectoriser')
    business_description_vectorizer = pd.DataFrame(columns = ['business_description_vectorizer'])
    for i in range (len(Business_description2)):
        print ('array to dataframe: ligne', i)
        business_description_vectorizer.loc[i] = [Business_description2[i]] 
    

    # Codons la colonne business_description_vectorizer vers la dataframe vocabulaire business 
    # Ligne par ligne de business_description_vectorizer, si un mot existe dans le vocabulaire 
    # business, nous allons mettre 1 dans la colonne et la ligne correspondant de 'vocabulaire_business', 
    # si non, nous allons mettre 0 
    print ('Entrain de coder la nouvelle colonne vectoriser vers le vocabulaire')
    
    #Entre '''...''' La version 0 du codage
    for ligne in range (len(business_description_vectorizer)):
        print ('codage de la ', ligne, '  ème ligne')
        #ligne : la ligne de business_description_vectorizer
        for word in business_description_vectorizer['business_description_vectorizer'][ligne]:
            if word in copy_vocabulaire.columns:
                #word : un mot parmi les mots de la ligne
                #print ('ajoutons ', word, ' to vocabulary')
                #Si le mot existe dans le vocabulaire la cellule correspondant dans le vocabulaire prend 1
                copy_vocabulaire.at[ligne, word] = 1
    
    #Version 1 du codage 
    # boucle sur chaque ligne et chaque mot de la colonne 'business_description_vectorizer'
    '''for ligne, vecteur in enumerate(business_description_vectorizer['business_description_vectorizer']):
        print('codage de la {} ème ligne'.format(ligne))
        # Créer un masque booléen pour les mots présents dans la ligne de vecteur
        masque = np.isin(copy_vocabulaire.columns, vecteur)
        # Mettre à jour la matrice de vocabulaire avec le masque
        copy_vocabulaire.iloc[ligne, 0:][masque] = 1'''
    

    
    return copy_vocabulaire, business_description_vectorizer
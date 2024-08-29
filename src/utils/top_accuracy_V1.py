#Packages 
import pandas as pd
import numpy as np


#Definons la fonction top_3_accuracy d'un module 
#Elle verifier si le vrai label existe parmi les x premièrs prediction du module
#la fonction top_3_accuracy ( prediction, true_labels, top_i, classes )  return la valeur du top3 accuracy
### Inputs:
##### prediction : Les probabilités des prédictions
##### true_labels : les vraies labels
##### top_i : top_i_accuracy doit etre entre 1 et le nombre de classes
##### classes : les labels des classes

def top_accuracy ( predictions, true_labels, classes,  top_i = 5 ):
    top = 0
    #Nombre de predict
    total = len ( predictions )
    print ( 'total = ', total )
    #Les classes


    for i in range ( total ):
        #la prediction i
        prediction = predictions [i]  #(1, 10)
        #le label i
        label = true_labels [i]       #(1, 1)
        
        #Transformons prediction en une dataframe d'index classes
        prediction_df = pd.DataFrame ( {'prediction' : prediction}, index = classes )
        #Trions les probabilités de la prediction i par ordre décroissant
        prediction_sorted = prediction_df.sort_values( 'prediction', ascending = False )


        #Si le label est présent dans les premières top_i probabilités ajouter 1 dans top
        if label in prediction_sorted[:top_i].index:
            top += 1 
    print ( 'top', top_i, ' =',  top )
    return (top/total)*100
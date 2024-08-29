Input : colonne contenant les descriptions et le vocabulaire des mots 

1. n = nombre de description dans la colonne
2. Ajoutons n lignes de valeurs 0 à la dataframe vocabulaire_business

3. Pour chaque description : 
        Enlever les ponctuations
        Rendre toutes les lettres en minuscule
        Split le texte en mots
        Enlever les stopwords
        Reformant maintenant la phrase  
        Rend chaque mot en sa forme original       
        Ajouter le mot à la nouvelle liste description_vectorizer       
        #Maintenant chaque description est vectorisée et stockée dans description_vectorizer
   Fin

#Boucle sur les descriptions, si un mot existe dans le vocabulaire business,  
#nous allons mettre 1 dans la colonne et la ligne correspondant de 'vocabulaire_business', 
#si non, nous allons mettre 0    
4. Pour chaque description dans description_vectorizer:    
        Pour chaque mot dans description :
            Si le mot existe dans vocabulaire_business:
                Mettre 1 dans la colonne correspondante
            Fin
        Fin
   Fin
   
Output : dataframe contenant les descriptions coder et Vecteur des description vectorisées.
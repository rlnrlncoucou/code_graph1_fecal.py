#programme pour trier les données

def displayFile(filepath, outpath):
    # ouvrir en lecture seule
    fd1 = open(filepath, 'r')
    
    # ouvrir en write-only mode 
    fd2 = open(outpath, 'w')

    line = '   '
        
    #récupérer toutes les lignes suivantes
    while line != '':
        # récupérer une seule ligne (la première ligne)
        line = fd1.readline()
        # retour à la ligne pour l'esthétique
        line = line.replace('\n', '')
        # séparer les différentes données par des ";" dans la ligne
        valueList = line.split(';')        
        # vérifier le nombre de colonnes total présentes
        if len(valueList) != 11:
            break
        # retirer 6 colonnes (filtrer celles voulues)
        filterList = [valueList[2]] + [valueList[4]] + [valueList[5]] + [valueList[7]] + [valueList[8]]      
        # rassembler les colonnes entre elles par des ":"
        result = ':'.join(filterList) 
        fd2.write(result + '\n')
    
    # fin de l'action
    # fermer le dossier
    fd1.close()

# afficher et faire apparaître le nouveau fichier dans le dossier sous le nom de 'Données filtrées à utiliser pour le graphique matière fécales.csv'
displayFile('data_real.csv', 'Données filtrées à utiliser pour le graphique matière fécales.csv')

#programme graphique fécal

import matplotlib.pyplot as plt
import math

# create graph data (instanciate graph) : crée la base du graphique (le corps)
figure, axes = plt.subplots()

# nommer les titres et les axes
axes.set_title('Bactérie vivante dans les matières fécales')
axes.set_ylabel('Bactérie vivante en log10 en g')
axes.set_xlabel('Nombre de jours avant et après le lavage des traitements')

graph = "fecal"

# initialiser les données
for mouse in range(17,33):
    x  = []
    y  = []

    # remplir avec les données issues du document
    fIN = open('data_filtrer.csv', 'r')
    line = fIN.readline()

    while line != '':
        line = fIN.readline()
        if line == '':
            break 
        # split line (séparer les données dans les lignes par ":")
        valueList = line.split(':')
        
        # récupérer les données
        sample_type = valueList[0]
        print(valueList)
        
        mouse_ID    = int(valueList[1].replace('ABX', ''))
        treatment   = valueList[2]    
        day         = valueList[3]
        bacteria    = math.log(float(valueList[4]))/math.log(10)

        # filtrer les lignes
        if mouse_ID == mouse and sample_type == graph :
            x.append(day)
            y.append(bacteria)        

    fIN.close()

    axes.plot(x,y)


figure.savefig('Résultat graphique des bactéries dans les matières fécales.png', dpi=300)

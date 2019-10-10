def choixFichier():
    nom_fichier = input("Choisir le nom du fichier : \n")
    return nom_fichier

def textFichier(nom_fichier):
    objet_fichier = open(nom_fichier,"a")
    texte = input("Ajouter votre texte : \n")
    objet_fichier.write(texte)
    objet_fichier.close()

def afficherFichier(nom_fichier):
    objet_fichier = open(nom_fichier,"r")
    print(objet_fichier.read())
    objet_fichier.close()

def supprimerContenuFichier(nom_fichier):
    objet_fichier = open(nom_fichier, "w")
    objet_fichier.close()

print("Bonjour tout le monde !")
print("Choix menu : \n")
print("1. Choisir un nom de fichier \n")
print("2. Ajouter un texte \n")
print("3. Afficher le fichier \n")
print("4. Vider le fichier \n")
print("9. Quitter le programme \n")
choix = int(input("Votre choix : \n"))

choixVerifier = True

while choixVerifier:
    if choix == 1:
        nom_fichier = choixFichier()

    if choix == 2:
        textFichier(nom_fichier)

    if choix == 3:
        afficherFichier(nom_fichier)

    if choix == 4:
        supprimerContenuFichier(nom_fichier)

    if choix == 9:
        choixVerifier = False

    choix = int(input("Votre choix : \n"))

# filename = input("Nom du fichier : ")
# text_fichier = open(filename+"txt","wtr")

# print(filename)
# text = input("Ajoutez votre texte : ")

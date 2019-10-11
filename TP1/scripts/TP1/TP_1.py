def choixFichier():
    fichier_verifier = True
    while fichier_verifier:
        try:
            nom_fic = input("Choisir le nom du fichier : \n")
            if nom_fic == "":
                assert False
            else:
                fichier_verifier = False

        except AssertionError:
            print("Saisissez un nom de fichier.")

    return nom_fic


def textFichier(nom_fichier):
    try:
        objet_fichier = open(nom_fichier, "a")
        texte_verifier = True
        while texte_verifier:
            try:
                texte = input("Ajouter votre texte : \n")
                if texte == "":
                    raise AssertionError
                else:
                    texte_verifier = False
            except AssertionError:
                print("Veillez saisir un texte.")

        objet_fichier.write(texte)
        objet_fichier.close()
    except FileNotFoundError:
        print("Le fichier est introuvable")
    else:
        print("Impossible d'écrire dans le fichier")


def afficherFichier(nom_fichier):
    try:
        objet_fichier = open(nom_fichier, "r")
        print(objet_fichier.read())
        objet_fichier.close()
    except FileNotFoundError:
        print("Le fichier est introuvable")
    else:
        print("Impossible de lire le fichier")


def supprimerContenuFichier(nom_fichier):
    try:
        objet_fichier = open(nom_fichier, "w")
        objet_fichier.close()
    except FileNotFoundError:
        print("Le fichier est introuvable")

if __name__ == '__main__':

    print("Bonjour tout le monde !")
    print("Choix menu : \n")
    print("1. Choisir un nom de fichier \n")
    print("2. Ajouter un texte \n")
    print("3. Afficher le fichier \n")
    print("4. Vider le fichier \n")
    print("9. Quitter le programme \n")
    choix_verifier = True
    nom_fichier = ""
    while choix_verifier:
        try:
            choix = int(input("Votre choix : \n"))

            if choix == 1:
                nom_fichier = choixFichier()

            if choix == 2:
                textFichier(nom_fichier)

            if choix == 3:
                afficherFichier(nom_fichier)

            if choix == 4:
                supprimerContenuFichier(nom_fichier)

            if choix == 9:
                choix_verifier = False

            if choix != 1 and choix != 2 and choix != 3 and choix != 4 and choix != 9:
                assert False

        except ValueError:
            print("La valeur saisie est invalide (Un chiffre est attendu).")
        except AssertionError:
            print("Le chiffre saisie est incorrect.")


# filename = input("Nom du fichier : ")
# text_fichier = open(filename+"txt","wtr")

# print(filename)
# text = input("Ajoutez votre texte : ")

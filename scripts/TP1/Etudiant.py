from scripts.TP1.Date import Date
import csv

class Etudiant:
    def __init__(self,prenom,nom,date):
        self.nom = nom
        self.prenom = prenom
        self.mail = prenom.lower()+"."+nom.lower()+"@etu.univ-tours.fr"
        self.dateN = date
        self.age = self.__calcAge__()

    def __calcAge__(self):
        age = 0
        date = Date(2,10,2019)
        if self.dateN < date:
            if self.dateN.mois <= date.mois:
                if self.dateN.jour <= date.jour and self.dateN.mois == date.mois:
                    age = date.annee - self.dateN.annee
                elif self.dateN.mois == date.mois:
                    age = date.annee - self.dateN.annee - 1
                else:
                    age = date.annee - self.dateN.annee
            else:
                age = date.annee - self.dateN.annee - 1

        return age


def creationListeEtudiantCSV(nom_fichier):
    liste_etudiant = []
    fichier = open(nom_fichier+".csv", "r")
    cr = csv.reader(fichier)

    for row in cr:
        chaine = row[0]
        liste = chaine.split(";")
        ligne = liste[2]
        date = ligne.split("/")
        liste_etudiant.append(Etudiant(liste[0],liste[1],Date(int(date[0]),int(date[1]),int(date[2]))))

    return liste_etudiant


etudiant = Etudiant("Vincent","Pozzi",Date(3,10,1997))
print(etudiant.age,etudiant.mail)
liste_final = creationListeEtudiantCSV("fichetu")
print(liste_final[5].mail,liste_final[5].prenom,liste_final[5].dateN,liste_final[5].age)


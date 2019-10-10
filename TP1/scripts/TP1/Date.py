class Date:

    def __init__(self, j, m, a):
        self.annee = a
        if m > 12 or m < 1:
            m = m%12
        self.mois = m

        if m == 2:
            if a%4 == 0:
                j = j%29
            else:
                j = j%28
        elif m < 8:
            if m%2 == 0:
                j = j%30
            else:
                j = j%31
        else:
            if m%2 == 0:
                j = j%31
            else:
                j = j%30

        self.jour = j

    #date1 == date2
    def __eq__(self, date):
        verifier = False
        if self.jour == date.jour:
            if self.mois == date.mois:
                if self.annee == date.annee:
                    verifier = True

        return verifier

    #date 1 < date2
    def __lt__(self, date):
        verifier = False
        if self.annee < date.annee:
            verifier = True
        elif self.mois < date.mois:
            verifier = True
        elif self.jour < date.jour:
            verifier = True

        return verifier

    def __str__(self):
        jour = str(self.jour)
        mois = str(self.mois)
        if self.jour < 10:
            jour = "0"+str(self.jour)
        if self.mois < 10:
            mois = "0"+str(self.mois)

        return jour+"/"+mois+"/"+str(self.annee)




ma_date = Date(6, 2, 1997)
ma_date2 = Date(3, 2, 1997)

print(ma_date)
if ma_date == ma_date2:
    print("yes")
if ma_date < ma_date2:
    print(" ma_date est < ma_date2")


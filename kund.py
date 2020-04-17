import faktura

class kunduppgifter:
    def __init__(self, fornamn, efternamn, gatuadress, postnummer, ort, kundnummer, telefon, epost, fakturor=[]):
        self.fornamn = fornamn
        self.efternamn = efternamn
        self.gatuadress = gatuadress
        self.postnummer = postnummer
        self.ort = ort
        self.kundnummer = kundnummer
        self.telefon = telefon
        self.epost = epost
        #fakturor tar en lista med faktura-objekt
        self.fakturor = fakturor

        def returnera_något():
            None

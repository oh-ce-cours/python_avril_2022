class Personne:
    AGE_MAJORITE = 18

    def __init__(self, naissance, nom) -> None:
        self.naissance = naissance
        self.nom = nom

    def est_majeur(self) -> bool:
        age = 2020 - self.naissance
        return age > self.AGE_MAJORITE

    def presentation(self):
        return f"Je suis {self.nom} et je suis majeur {self.est_majeur}"

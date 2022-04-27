class Personne:
    AGE_MAJORITE = 18

    def __init__(self, naissance, nom) -> None:
        self.naissance = naissance
        self.nom = nom
 
    def get_age(self):
        return 2022 - self.naissance

    def est_majeur(self) -> bool:
        return self.get_age() > self.AGE_MAJORITE

    def presentation(self):
        txt = "majeur" if self.est_majeur() else "mineur"
        return f"Je suis {self.nom}, j'ai {self.get_age()} ans et je suis {txt}"

    def __str__(self):
        return self.presentation()


p1 = Personne(2020, "Matthieu")
print(p1.presentation())
print(p1)

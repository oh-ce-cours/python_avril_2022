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


class Formation:
    def __init__(self, prof: Personne, eleves: list[Personne]):
        self.eleves = eleves
        self.prof = prof

    def personnes_presentes(self):
        return [self.prof] + self.eleves

    def __iter__(self):
        return iter(self.personnes_presentes())

    def __add__(self, other):
        if not self.prof == other.prof:
            raise NotImplemented("il faut le même prof pour fusioner les formations")
        self.eleves.extend(other.eleves)


# f1 + f2  => f1.__add__(f2)

p1 = Personne(1990, "Matthieu")
p2 = Personne(1990, "Yann")
p3 = Personne(1991, "Erwann")


f = Formation(prof=p1, eleves=[p2, p3])
# f = [p1, p2, p3]

for personne in f:
    print(personne)

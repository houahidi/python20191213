from functools import reduce


class Etudiant:
    def __init__(self, nom, note):
        self.nom = nom
        self.note = note
    def __radd__(self, other):
        print("__radd__", self, other)
        other += self.note
        return other
    def __add__(self, other):
        print("__add__", self, other)
        return other.note  + self.note
    def __str__(self):
        return "{} a {}".format(self.nom, self.note)
    def __lt__(self, other):
        return self.note < other.note

def filtrer(etud):
    return etud.note >= 15


if __name__ == "__main__":
    E1 = Etudiant("Pascal", 20)
    E2 = Etudiant("Eric", 10)
    E3 = Etudiant("Eric", 15)
    etudiants = [E1, E2, E3]
    print("somme :", sum(etudiants))
    print("min :", min(etudiants))
    print("max :", max(etudiants))
    print("E1 > E2", E1 > E2)
    notes = map(lambda etud: etud.note, etudiants)
    print("notes : ", list(notes))
    bons = filter( lambda etud: etud.note >= 15 , etudiants)
    for etudiant in bons:
        print(etudiant, "est un bon eleve")
    bons = filter(filtrer, etudiants)
    for etudiant in bons:
        print(etudiant, "est un bon eleve")
    print("_____")
    somme = reduce(lambda a, b: a + b, etudiants)
    print("somme :",somme)
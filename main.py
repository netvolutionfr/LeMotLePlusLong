import unidecode
import random


def stats_per_letter():
    stats = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        stats[letter] = 0
    with open("liste_francais.txt", "r") as f:
        for line in f:
            for letter in line:
                letter = unidecode.unidecode(letter).upper()
                if letter.isalpha():
                    stats[letter] += 1
    return stats


def tirage(choix=None):
    """
    Retourne une liste de lettres tirées au hasard
    """
    if choix is None:
        choix = ['c', 'v', 'c', 'v', 'c', 'c', 'c', 'v', 'c']

    lettres = []
    with open("liste_francais.txt", "r") as f:
        for line in f:
            for letter in line:
                letter = unidecode.unidecode(letter).upper()
                if letter.isalpha():
                    lettres.append(letter)

    random.shuffle(lettres)

    consonnes = "BCDFGHJKLMNPQRSTVWXZ"
    voyelles = "AEIOUY"
    tirage = []
    for choisi in choix:
        newLetter = random.choice(lettres)
        if choisi == "c":
            while newLetter not in consonnes:
                newLetter = random.choice(lettres)
        else:
            while newLetter not in voyelles:
                newLetter = random.choice(lettres)
        lettres.remove(newLetter)
        tirage.append(newLetter)
    return tirage

def tirage_avec_choix():
    choix = []
    while len(choix) < 9:
        choix = input("Consonne ou voyelle ? (c/v) ")
        if choix == "c":
            choix.append("c")
        elif choix == "v":
            choix.append("v")
        else:
            print("Choix invalide")
            break
    return tirage(choix)


def anagrammes(liste):
    """
    Retourne une liste de mots qui peuvent être formés à partir des lettres
    du tirage, en utilisant une fois chaque lettre maximum.
    """
    anagrammes = []
    with open("liste_francais.txt", "r") as f:
        for line in f:
            word = line.strip().upper()
            letters = list(word)
            if len(letters) > len(liste):
                continue
            if all([letter in liste for letter in letters]):
                # On vérifie qu'on a bien le bon nombre de lettres
                correct = True
                for letter in letters:
                    if letters.count(letter) > liste.count(letter):
                        correct = False
                        break
                if correct:
                    anagrammes.append(word)
    # On trie par longueur décroissante
    anagrammes.sort(key=lambda x: len(x), reverse=True)
    return anagrammes

def presenter_liste_mots(liste_mots):
    """
    Présente la liste des mots trouvés par ordre de longueur décroissante
    en les groupant par nombre de lettres
    """
    liste_mots.sort(key=lambda x: len(x), reverse=True)
    for i in range(len(liste_mots[0]), 2, -1):
        mots = [mot for mot in liste_mots if len(mot) == i]
        if mots:
            print(f"{i} lettres : {', '.join(mots)}")
    return


if __name__ == "__main__":
    mon_tirage = tirage()
    print(mon_tirage)
    presenter_liste_mots(anagrammes(mon_tirage))
    print(len(anagrammes(mon_tirage)))

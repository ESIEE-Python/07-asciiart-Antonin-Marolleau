"""
un jouuuuuuuuur mon prince viendraa
"""
import sys
sys.setrecursionlimit(1500) #je sais pas j'ai cherché a cause d'une erreur
#pourrie sur google sur la recursion max

#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne
     de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    if not s:
        return []

    c = [s[0]] #le 1er char de s est s[0], et donc
    o = [1]
    k = 1

    n = len(s)

    while k < n:
        if s[k] == s[k - 1]:
            o[-1] += 1
        else:
            c.append(s[k])
            o.append(1)
        k += 1

    return [(b, a) for a, b in list(zip(o, c))]


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de
     caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    #j'ai mis une 2eme fonction pour garder l'index
    def helper(s, index):
        # base
        if index >= len(s):
            return []

        chara = s[index]
        k = 1

        while index + k < len(s) and s[index + k] == chara:
            k += 1

        # récursivite
        return [(chara, k)] + helper(s, index + k)

    # récursivité encore oui
    return helper(s, 0)




#### Fonction principale


def main():
    """
    caca
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()

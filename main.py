""" exercice tuples """
#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
     passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    cmpt = 1
    tab=[]
    if s=="":
        return []
    for i in range(1,len(s)) :
        if s[i] == s[i-1] :
            cmpt = cmpt + 1
        else :
            tab.append((s[i-1],cmpt))
            cmpt = 1
    tab.append((s[-1], cmpt))
    return tab


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne
    de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    cmpt = 1
    i=1
    if s=="":
        return []
    while i< len(s) and s[i] == s[0] :
        cmpt = cmpt + 1
        i = i + 1
    return [(s[0],cmpt)] + artcode_r(s[i:])

#### Fonction principale

def main():
    "text iteratif et recursif"
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()

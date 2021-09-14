#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if len(string)%2==0:
        return True
    else:
        return False




def remove_third_char(string: str) -> str:
    longueur=len(string)
    chaine=""
    i=0
    while i<2:
        chaine+=string[i]
        i+=1
    i=3
    while i<longueur:
        chaine+=string[i]
        i+=1
    return chaine





def replace_char(string: str, old_char: str, new_char: str) -> str:
    longueur=len(string)
    chaine=""
    i=-1
    for lettre in string:
        i+=1
        if lettre==old_char:
            ordre_lettre=i
    i=0
    while i<ordre_lettre:
        chaine+=string[i]
        i+=1
    if i==ordre_lettre:
        chaine+=new_char
        i+=1

    while i<longueur:
        chaine+=string[i]
        i+=1
    return chaine


def get_number_of_char(string: str, char: str) -> int:
    number=-1
    for letter in string:
        if letter==char:
            number+=1
    return number



def get_number_of_words(sentence: str, word: str) -> int:
    i=0
    j=0
    compteur=0
    longueur_phrase=len(sentence)
    longueur_mot=len(word)

    while i<longueur_phrase:
        if sentence[i]==word[j] and j<longueur_mot:
            i, j = i + 1, 1 + j
            if j==longueur_mot-1:
                compteur+=1
                j=0

        else:
            i+=1
            j=0
    return compteur






def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()

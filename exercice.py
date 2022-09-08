#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    for i in range(len(mot)):
        if 97 <= ord(mot[i]) <= 122: # Alphabet normal en minuscule sans accents
            mot[i] += chr(ord(mot[i]) - 32)
        elif (0xE0 <= ord(mot[i]) <= 0xFE) & (ord(mot[i]) != 0xF7): # Lettres minuscules avec accents
            mot[i] += chr(ord(mot[i]) - 32)
        else: # Lettres déjà en majuscules ou autres caractères
            mot[i] += mot[i]
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

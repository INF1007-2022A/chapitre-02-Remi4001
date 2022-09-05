#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    mot_maj = ""
    for lettre in mot:
        if 97 <= ord(lettre) <= 122 | 0xE0 <= ord(lettre) <= 0xFE & ord(lettre) != 0xF7:
            mot_maj += chr(ord(lettre) - 32)
        else:
            mot_maj += lettre
    return mot_maj


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

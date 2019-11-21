"""
    1 - Créer le cadre de départ

        Initialisez un repo Git et envoyez-le sur Github.
        Commencez par créer le labyrinthe sans l’interface graphique. Quand la logique de votre labyrinthe est faite, 
    utilisez le module PyGame pour dessiner l’interface graphique.
        Puis intéressez-vous aux trois éléments principaux du jeu : le gardien, MacGyver et les objets. Comment les représenter dans votre programme ? 
    Où sont-ils placés au commencement du jeu ?  

    2 - Animer le personnage

        Le seul élément mouvant est MacGyver. Créez les méthodes de classe qui permettent de l'animer et de trouver la sortie. 
    Pour l'instant, faites une version simplifiée du jeu dans laquelle MacGyver gagne en arrivant face au gardien.
 
    3 - Récupérer les objets

        Ajoutez la gestion des objets. Comment MacGyver les ramasse-t-il ?  Ajoutez également un compteur qui les listera.
 
    4 - Gagner !

        Enfin, changez la fin du jeu : MacGyver gagne s'il a bien ramassé tous les objets et endormi le garde. Sinon, il perd.
"""

import pygame

from constantes import *
from classes import *

pygame.init()


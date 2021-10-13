import pygame
from pygame.locals import *

pygame.init()

#Paramètres de la fenêtre
nombre_sprite_largeur = 20
nombre_sprite_longueur = 30
taille_sprite = 30
cote_largeur = nombre_sprite_largeur * taille_sprite
cote_longueur = nombre_sprite_longueur * taille_sprite

#Personnalisation de la fenêtre
titre_fenetre = "Echo perdue dans les Abysses"
image_icone = "images/echo_bas.png"

#Images hors niveaux
image_accueil = "images/accueil.jpg"
image_FinN1 = "images/FinN1.jpg"
image_Fin = "images/Fin.jpg"

#Images communes à tous ou plusieurs niveaux
image_texte = "images/texte.png"
image_fond = "images/fond.jpg"
image_depart = "images/depart.jpg"
image_arrivee = "images/arrivee.jpg"
image_inventaire_vide = "images/inventaire_vide.jpg"

#Images niveau 1
image_mur = "images/mur.jpg"
image_eau = "images/eau.jpg"
image_cle1_1 = "images/cle1_1.png"
image_cle1_2 = "images/cle1_2.png"
image_inventaire_cle1_1 = "images/inventaire_cle1_1.jpg"
image_inventaire_cle1_2 = "images/inventaire_cle1_2.jpg"
image_buisson = "images/buisson.png"

#Images niveau 2
image_murn2 = "images/mur2.jpg"
image_eaun2 = "images/eau2.jpg"
image_cle2_1 = "images/cle2_1.png"
image_cle2_2 = "images/cle2_2.png"
image_inventaire_cle2_1 = "images/inventaire_cle2_1.jpg"
image_inventaire_cle2_2 = "images/inventaire_cle2_2.jpg"

#Images niveau 3
image_bon_coffre = "images/bon_coffre.png"
image_mauvais_coffre = "images/mauvais_coffre.png"
image_portail = "images/portail.png"

#Variables pour les clés
morceaucle1 = 0
morceaucle2 = 0

#Variables pour l'affichage
Niveau1 = 1
compt = 0
text_col = [255, 255, 255]
fenetre = pygame.display.set_mode((cote_longueur, cote_largeur))

#Musique et sons
Musique = pygame.mixer.Sound("Sons/Musique.wav")
Objet = pygame.mixer.Sound("Sons/Objet.wav")
Lancement = pygame.mixer.Sound("Sons/Lancement.wav")
Portail = pygame.mixer.Sound("Sons/Portail.wav")

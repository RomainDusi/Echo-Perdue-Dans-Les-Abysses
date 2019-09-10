import pygame
from pygame.locals import * 
from Constantes import *


#Initialisation
class Niveau:
        """Classe permettant de créer un niveau"""
        def __init__(self, fichier):
                self.fichier = fichier  #fichiers des niveaux n1, n2, n3
                self.structure = 0

#Génère les niveau
        def generer(self):
                with open(self.fichier, "r") as fichier:  #j'ouvre le fichier, r= on le lit en temps que variable fichier 
                        structure_niveau = []            #La structure du niveau 
        #On parcourt les lignes du fichier
                        for ligne in fichier:
                                ligne_niveau = []
        #On parcourt les sprites (lettres) contenus dans le fichier
                                for sprite in ligne:
        #On ignore les "\n" de fin de ligne
                                        if sprite != '\n':
        #On ajoute le sprite à la liste de la ligne
                                                ligne_niveau.append(sprite)
        #On ajoute la ligne à la liste du niveau
                                structure_niveau.append(ligne_niveau)
        #On sauvegarde cette structure
                        self.structure = structure_niveau #variable
                        
#On affiche le premier niveau
        def afficher(self, fenetre): #Affiche le premier niveau 
                """Méthode permettant d'afficher le niveau en fonction 
                de la liste de structure renvoyée par generer()"""
                #Chargement des images 
                mur = pygame.image.load(image_mur).convert()
                depart = pygame.image.load(image_depart).convert()
                arrivee = pygame.image.load(image_arrivee).convert()
                cle1_1 = pygame.image.load(image_cle1_1).convert_alpha()
                cle1_2 = pygame.image.load(image_cle1_2).convert_alpha()
                inventaire_vide = pygame.image.load(image_inventaire_vide).convert()
                inventaire_cle1_1 = pygame.image.load(image_inventaire_cle1_1).convert()
                inventaire_cle1_2 = pygame.image.load(image_inventaire_cle1_2).convert()

                #On parcourt la liste du niveau
                num_ligne = 0
                for ligne in self.structure:
                        #On parcourt les listes de lignes
                        num_case = 0
                        for sprite in ligne:
                                #On calcule la position réelle en pixels
                                x = num_case * taille_sprite
                                y = num_ligne * taille_sprite
                                if sprite == 'm':
                                        fenetre.blit(mur, (x,y))
                                elif sprite == '3':
                                        fenetre.blit(inventaire_cle1_1, (x,y))
                                elif sprite == '4':
                                        fenetre.blit(inventaire_cle1_2, (x,y))
                                elif sprite == 'd':
                                        fenetre.blit(depart, (x,y))
                                elif sprite == 'a':
                                        fenetre.blit(arrivee, (x,y))
                                elif sprite =='l':
                                        fenetre.blit(cle1_2, (x,y))
                                elif sprite == 'c':
                                        fenetre.blit(cle1_1, (x,y))
                                elif sprite == 'i' :
                                        fenetre.blit(inventaire_vide, (x,y))
                                elif sprite == 'n' :
                                        fenetre.blit(inventaire_vide, (x,y))
                                num_case += 1  #fait les cases une à une 
                        num_ligne += 1  #change de ligne 


#même chose avec le niveau 2
        def afficher2 (self, fenetre):
                cle2_1 = pygame.image.load(image_cle2_1).convert_alpha()
                cle2_2 = pygame.image.load(image_cle2_2).convert_alpha()
                depart = pygame.image.load(image_depart).convert()
                arrivee = pygame.image.load(image_arrivee).convert()
                mur = pygame.image.load(image_murn2).convert()
                inventaire_vide = pygame.image.load(image_inventaire_vide).convert()
                inventaire_cle2_1 = pygame.image.load(image_inventaire_cle2_1).convert()
                inventaire_cle2_2 = pygame.image.load(image_inventaire_cle2_2).convert()
                num_ligne = 0
                for ligne in self.structure:
                        #On parcourt les listes de lignes
                        num_case = 0
                        for sprite in ligne:
                                #On calcule la position réelle en pixels
                                x = num_case * taille_sprite
                                y = num_ligne * taille_sprite
                                if sprite == 'm':
                                        fenetre.blit(mur, (x,y))
                                elif sprite == '3':
                                        fenetre.blit(inventaire_cle2_1, (x,y))
                                elif sprite == '4':
                                        fenetre.blit(inventaire_cle2_2, (x,y))
                                elif sprite == 'd':
                                        fenetre.blit(depart, (x,y))
                                elif sprite == 'a':
                                        fenetre.blit(arrivee, (x,y))
                                elif sprite =='l':
                                        fenetre.blit(cle2_2, (x,y))
                                elif sprite == 'c':
                                        fenetre.blit(cle2_1, (x,y))
                                elif sprite == 'i' :
                                        fenetre.blit(inventaire_vide, (x,y))
                                elif sprite == 'n' :
                                        fenetre.blit(inventaire_vide, (x,y))
                                num_case += 1
                        num_ligne += 1
                        
#même chose avec le niveau 3
        def afficher3 (self, fenetre):
                depart = pygame.image.load(image_depart).convert()
                eau = pygame.image.load(image_eau).convert()
                mur = pygame.image.load(image_mur).convert()
                bon_coffre = pygame.image.load(image_bon_coffre).convert_alpha()
                mauvais_coffre = pygame.image.load(image_mauvais_coffre).convert_alpha()
                portail = pygame.image.load(image_portail).convert_alpha()
                num_ligne = 0
                for ligne in self.structure:
                        #On parcourt les listes de lignes
                        num_case = 0
                        for sprite in ligne:
                                #On calcule la position réelle en pixels
                                x = num_case * taille_sprite
                                y = num_ligne * taille_sprite
                                if sprite == 'm':
                                        fenetre.blit(mur, (x,y))
                                elif sprite == 'd':
                                        fenetre.blit(depart, (x,y))
                                elif sprite == 'o':
                                        fenetre.blit(eau, (x,y))
                                elif sprite == 'c':
                                        fenetre.blit(bon_coffre, (x,y))
                                elif sprite == 'k':
                                        fenetre.blit(mauvais_coffre, (x,y))
                                elif sprite == 'p':
                                        fenetre.blit(portail, (x,y))
                                elif sprite == 't':
                                        fenetre.blit(portail, (x,y))
                                num_case += 1
                        num_ligne += 1
                        

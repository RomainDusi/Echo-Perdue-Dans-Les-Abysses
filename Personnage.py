import pygame
from pygame.locals import * 
from Constantes import *

class Echo:
        def __init__(self, droite, droite2, gauche, gauche2, haut, haut2, bas, bas2, niveau):
        #Sprites du personnage
                self.droite = pygame.image.load(droite).convert_alpha()  #png
                self.droite2 = pygame.image.load(droite2).convert_alpha()
                self.gauche = pygame.image.load(gauche).convert_alpha()
                self.gauche2 = pygame.image.load(gauche2).convert_alpha()
                self.haut = pygame.image.load(haut).convert_alpha()
                self.haut2 = pygame.image.load(haut2).convert_alpha()
                self.bas = pygame.image.load(bas).convert_alpha()
                self.bas2 = pygame.image.load(bas2).convert_alpha()
                
                
                #Position du personnage en cases et en pixels
                self.case_x = 0     #ou ce trouve le personnage, relatif
                self.case_y = 0
                self.x = 0          #position réelle en pixel
                self.y = 0
                #Direction par défaut
                self.direction = self.bas
                #Niveau dans lequel le personnage se trouve 
                self.niveau = niveau
                self.posbas = 0       #par rapport au 2 sprites du personnage dans chaque direction
                self.poshaut = 0
                self.posgauche = 0
                self.posdroite = 0

        def deplacer(self, direction):
                
#Déplacement vers la droite
                if direction == 'droite':
#Pour ne pas dépasser l'écran
                        if self.case_x < (nombre_sprite_longueur - 1): #->taille niveau totale
                                if self.niveau.structure[self.case_y][self.case_x+1] != 'm': #éviter de marcher sur mur
                                        self.case_x += 1 #déplacer relatif
                                        self.x = self.case_x * taille_sprite #déplacement réel en pixel
                        if self.posdroite == 0 :
                                self.direction = self.droite
                                self.posdroite = 1
                        else :                                       #changement de pied a chaque déplacement
                                self.direction = self.droite2
                                self.posdroite = 0
                        

#Déplacement vers la gauche
                if direction == 'gauche':
                        if self.case_x > 0:
                                if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
                                        self.case_x -= 1
                                        self.x = self.case_x * taille_sprite
                        if self.posgauche == 0 :
                                self.direction = self.gauche
                                self.posgauche = 1
                        else :
                                self.direction = self.gauche2
                                self.posgauche = 0
                        
        
#Déplacement vers le haut
                if direction == 'haut':
                        if self.case_y > 0:
                                if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
                                        self.case_y -= 1
                                        self.y = self.case_y * taille_sprite
                        if self.poshaut == 0:
                                self.direction = self.haut
                                self.poshaut = 1
                        else:
                                self.direction = self.haut2
                                self.poshaut = 0

#Déplacement vers le bas
                if direction == 'bas':
                        if self.case_y < (nombre_sprite_largeur - 1):
                                if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                                        self.case_y += 1
                                        self.y = self.case_y * taille_sprite

                        if self.posbas == 0:
                                self.direction = self.bas
                                self.posbas = 1

                        else:
                                self.direction = self.bas2
                                self.posbas = 0


class Echo2:
        def __init__(self, droite, droite2, gauche, gauche2, haut, haut2, bas, bas2, niveau):
        #Sprites du personnage
                self.droite = pygame.image.load(droite).convert_alpha()
                self.droite2 = pygame.image.load(droite2).convert_alpha()
                self.gauche = pygame.image.load(gauche).convert_alpha()
                self.gauche2 = pygame.image.load(gauche2).convert_alpha()
                self.haut = pygame.image.load(haut).convert_alpha()
                self.haut2 = pygame.image.load(haut2).convert_alpha()
                self.bas = pygame.image.load(bas).convert_alpha()
                self.bas2 = pygame.image.load(bas2).convert_alpha()
                
                
                #Position du personnage en cases et en pixels
                self.case_x = 0       #changement d'entrée
                self.case_y = 19
                self.x = 0
                self.y = 570     #19 x 30
                #Direction par défaut
                self.direction = self.haut
                #Niveau dans lequel le personnage se trouve 
                self.niveau = niveau
                self.posbas = 0
                self.poshaut = 0
                self.posgauche = 0
                self.posdroite = 0


        def deplacer2(self, direction):
        
#Déplacement vers la droite
                if direction == 'droite':
#Pour ne pas dépasser l'écran
                        if self.case_x < (nombre_sprite_longueur - 1):
                                if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
                                        self.case_x += 1
                                        self.x = self.case_x * taille_sprite
                        if self.posdroite == 0 :
                                self.direction = self.droite
                                self.posdroite = 1
                        else :
                                self.direction = self.droite2
                                self.posdroite = 0
                        

#Déplacement vers la gauche
                if direction == 'gauche':
                        if self.case_x > 0:
                                if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
                                        self.case_x -= 1
                                        self.x = self.case_x * taille_sprite
                        if self.posgauche == 0 :
                                self.direction = self.gauche
                                self.posgauche = 1
                        else :
                                self.direction = self.gauche2
                                self.posgauche = 0
                        
        
#Déplacement vers le haut
                if direction == 'haut':
                        if self.case_y > 0:
                                if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
                                        self.case_y -= 1
                                        self.y = self.case_y * taille_sprite
                        if self.poshaut == 0:
                                self.direction = self.haut
                                self.poshaut = 1
                        else:
                                self.direction = self.haut2
                                self.poshaut = 0

#Déplacement vers le bas
                if direction == 'bas':
                        if self.case_y < (nombre_sprite_largeur - 1):
                                if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                                        self.case_y += 1
                                        self.y = self.case_y * taille_sprite

                        if self.posbas == 0:
                                self.direction = self.bas
                                self.posbas = 1
                        else:
                                self.direction = self.bas2
                                self.posbas = 0


class Echo3:
        def __init__(self, droite, droite2, gauche, gauche2, haut, haut2, bas, bas2, niveau):
        #Sprites du personnage
                self.droite = pygame.image.load(droite).convert_alpha()
                self.droite2 = pygame.image.load(droite2).convert_alpha()
                self.gauche = pygame.image.load(gauche).convert_alpha()
                self.gauche2 = pygame.image.load(gauche2).convert_alpha()
                self.haut = pygame.image.load(haut).convert_alpha()
                self.haut2 = pygame.image.load(haut2).convert_alpha()
                self.bas = pygame.image.load(bas).convert_alpha()
                self.bas2 = pygame.image.load(bas2).convert_alpha()
                
                
                #Position du personnage en cases et en pixels
                self.case_x = 15
                self.case_y = 0
                self.x = 450     #15 x 30
                self.y = 0
                #Direction par défaut
                self.direction = self.bas
                #Niveau dans lequel le personnage se trouve 
                self.niveau = niveau
                self.posbas = 0
                self.poshaut = 0
                self.posgauche = 0
                self.posdroite = 0


        def deplacer3(self, direction):
        
#Déplacement vers la droite
                if direction == 'droite':
#Pour ne pas dépasser l'écran
                        if self.case_x < (nombre_sprite_longueur - 1):
                                if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
                                        if self.niveau.structure[self.case_y][self.case_x+1] != 'o':
                                                self.case_x += 1
                                                self.x = self.case_x * taille_sprite
                        if self.posdroite == 0 :
                                self.direction = self.droite
                                self.posdroite = 1
                        else :
                                self.direction = self.droite2
                                self.posdroite = 0
                        

#Déplacement vers la gauche
                if direction == 'gauche':
                        if self.case_x > 0:
                                if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
                                        if self.niveau.structure[self.case_y][self.case_x-1] != 'o':
                                                self.case_x -= 1
                                                self.x = self.case_x * taille_sprite
                        if self.posgauche == 0 :
                                self.direction = self.gauche
                                self.posgauche = 1
                        else :
                                self.direction = self.gauche2
                                self.posgauche = 0
                        
        
#Déplacement vers le haut
                if direction == 'haut':
                        if self.case_y > 0:
                                if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
                                        if self.niveau.structure[self.case_y-1][self.case_x] != 'o':
                                                self.case_y -= 1
                                                self.y = self.case_y * taille_sprite
                        if self.poshaut == 0:
                                self.direction = self.haut
                                self.poshaut = 1
                        else:
                                self.direction = self.haut2
                                self.poshaut = 0

#Déplacement vers le bas
                if direction == 'bas':
                        if self.case_y < (nombre_sprite_largeur - 1):
                                if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                                        if self.niveau.structure[self.case_y+1][self.case_x] != 'o':
                                                self.case_y += 1
                                                self.y = self.case_y * taille_sprite

                        if self.posbas == 0:
                                self.direction = self.bas
                                self.posbas = 1
                        else:
                                self.direction = self.bas2
                                self.posbas = 0

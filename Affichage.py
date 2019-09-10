import pygame
from pygame.locals import *
from Constantes import *

from os import system

class Affichage:
    def texte1(variables):      #Accueil
        myfont = pygame.font.Font(None, 40)     #Définition de le style et de la taille du texte
        text = [myfont.render('Cliquez sur ENTREZ pour jouer.', True, text_col),        #Définition du texte
        myfont.render('                                ', True, text_col)]
        clignotement = 1     #Attribution des variables
        accueil = pygame.image.load(image_accueil).convert()
        tempo = 0
        while clignotement == 1:            #Boucle t'en que l'utilisateur ne clique pas
            fenetre.blit(accueil, (0,0))    #Affiche l'accueil
            my_image = text[tempo]          #Créer l'image à afficher à partir du texte
            rect = my_image.get_rect()      #Attribue la position de l'image à afficher
            rect.center = [400, 400]        #Définit la position de l'image
            fenetre.blit(my_image, rect)    #Affiche l'image
            pygame.display.flip()
            pygame.time.delay(1000)         #Attente entre chaque clignotement
            if tempo == 0:                  #Changement de texte entre 'Cliquez' et le vide, 0 = 'Cliquez', 1 = vide
                tempo = 1
            else:
                tempo = 0
            for event in pygame.event.get():        #Si l'utilisateur décide de jouer
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        clignotement = 0
                        Lancement.play()
                if event.type == QUIT:          #Si l'utilisateur quitte le jeu
                    clignotement = 0
                    pygame.quit()
                    
        
    def texte2(variables):      #Histoire du jeu
        Niveau1 = 1             #Initialise les variables
        compt = 0
        y = 150                 #Position en y du texte  
        Ligne1 = 1
        Ligne2 = 0
        Ligne3 = 0
        Ligne4 = 0
        Ligne5 = 0
        while Niveau1 == 1:
            myfont = pygame.font.Font(None, 40)     #Définit la police d'écriture et le style 
            texte = 'Il était une fois, une pauvre petite fille nommée Echo. Ses parents ne l\'aimaient pas, ils la haissaient même. Alors un triste jour de primptemps, Ils l\'abandonnèrent, dans une grotte quand elle dormait. L a pauvre fillette se réveilla seule, perdue, et apeurée. Pouvez-vous l\'aider à sortir de cette effrayante grotte ?'
            if compt == 0:
                for i in texte:         #Pour chaque caractère dans notre texte
                    x = 30 + 15*compt   #Position en x du texte
                    compt = compt + 1
                    test = i
                    if x== 855 and Ligne1 == 1:         #Ecrit notre première ligne puis retour à la ligne
                        compt = 0                       #Redéfinit les variables pour la ligne suivante
                        y = 200
                        Ligne2 = 1
                        Ligne1 = 0
                    if x== 840 and Ligne2 == 1:         #Ecrit notre 2ème ligne puis retour à la ligne
                        compt = 0                       #Redéfinit les variables pour la ligne suivante
                        x = 30
                        y = 250
                        Ligne3 = 1
                        Ligne2 = 0
                    if x == 555 and Ligne3 == 1:        #Ecrit notre 3ème ligne puis retour à la ligne
                        compt = 0                        #Redéfinit les variables pour la ligne suivante
                        y = 300
                        Ligne3 = 0
                        Ligne4 = 1
                    if  x == 885 and Ligne4 == 1:       #Ecrit notre 4ème ligne puis retour à la ligne
                        compt = 0                        #Redéfinit les variables pour la ligne suivante
                        x = 30
                        y = 350
                        Ligne4 = 0
                        Ligne5 = 1
                    if x == 885 and Ligne5 == 1:        #Ecrit notre 5ème ligne puis retour à la ligne
                        x = 30                          #Redéfinit les variables pour la ligne suivante
                        compt = 0
                        y = 400
                    text = [myfont.render(test, True, text_col)]   #Initialise dans la variable texte le caractère à écrire avec la couleur que l'on souhaite
                    my_image = text[0]                             #Créer une image avec notre lettre
                    rect = my_image.get_rect()                     #Attribue la position de l'image à afficher
                    rect.center = [x, y]                           #Positionne l'image selon la position x et y de notre lettre
                    fenetre.blit(my_image, rect)                   #Affiche l'image
                    pygame.display.flip()
                    pygame.time.delay(40)
                    for event in pygame.event.get():
                        if event.type == QUIT:          #Si l'utilisateur quitte
                            pygame.quit()
                compt = 1
                pygame.time.delay(3000)     #Pause
            Niveau1 = 0                  #On sort du while


    def texte3(variables):          #Transition
        myfont = pygame.font.Font(None, 40)             #Définition de le style et de la taille du texte
        text = [myfont.render('Cliquez sur ENTREZ pour jouer.', True, text_col),        #Définition du texte
        myfont.render('                                ', True, text_col)]
        clignotement = 1             #Définition des variables
        FinN1_2 = pygame.image.load(image_FinN1).convert()
        tempo = 0
        while clignotement == 1:
            fenetre.blit(FinN1_2, (0,0))    #Affiche le fond
            my_image = text[tempo]          #Créer l'image à afficher à partir du texte
            rect = my_image.get_rect()      #Attribue la position de l'image à afficher
            rect.center = [400, 500]        #Positionne l'image
            fenetre.blit(my_image, rect)    #Affiche l'image
            pygame.display.flip()
            pygame.time.delay(1000)         #Pause
            if tempo == 0:                  #Changement de texte entre 'Cliquez' et le vide, 0 = 'Cliquez', 1 = vide
                tempo = 1
            else:
                tempo = 0
            for event in pygame.event.get():        #Si l'utilisateur continue
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        clignotement = 0
                if event.type == QUIT:          #Si l'utilisateur quitte
                    pygame.quit()


    def texte4(variables):          #Fin du jeu
        myfont = pygame.font.Font(None, 80)         #Définition de le style et de la taille du texte
        text = [myfont.render('Bravo Echo est sortie !', True, text_col),       #Définition du texte
        myfont.render('                                ', True, text_col)]
        clignotement = 1        #Définition des variables
        Fin = pygame.image.load(image_Fin).convert()
        tempo = 0
        while clignotement == 1:
            fenetre.blit(Fin, (0,0))            #Affiche le fond
            my_image = text[tempo]              #Créer l'image à afficher à partir du texte
            rect = my_image.get_rect()          #Attribue la position de l'image à afficher
            rect.center = [450, 500]            #Positionne l'image
            fenetre.blit(my_image, rect)        #Affiche l'image
            pygame.display.flip()
            pygame.time.delay(1000)             #Pause
            if tempo == 0:                      #Changement de texte entre 'Cliquez' et le vide, 0 = 'Cliquez', 1 = vide
                tempo = 1
            else:
                tempo = 0
            for event in pygame.event.get():    #Si l'utilisateur continue
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        clignotement = 0
                if event.type == QUIT:          #Si l'utilisateur quitte
                    clignotement = 0
                    pygame.quit()
                    


    def texte5(variables):          #Fin 2 avec redémarrage
        Niveau1 = 1                 #Définition des variables
        compt = 0
        y = 150                     #Position en y du texte
        while Niveau1 == 1:
            myfont = pygame.font.Font(None, 40)
            texte = '  Dommage ! Echo est retournée au début de la grotte ;\'(                         Aide la de nouveau !'        #Définit le texte
            if compt == 0:
                for i in texte:         #Pour chaque caractère du texte
                    x = 20 + 15*compt   #Position en x du caractère
                    compt = compt + 1
                    test = i
                    if x == 905:        #Quand la ligne est écrite, retourne à la ligne
                        y = 300
                        compt = 0
                    text = [myfont.render(test, True, text_col)]        #Initialise dans la variable texte le caractère à écrire avec la couleur que l'on souhaite
                    my_image = text[0]                      #Créer une image avec notre lettre
                    rect = my_image.get_rect()              #Attribue la position de l'image à afficher
                    rect.center = [x, y]                    #Positionne l'image en fonctione de la position x et y de notre lettre
                    fenetre.blit(my_image, rect)            #Affiche l'image
                    pygame.display.flip()
                    pygame.time.delay(100)                  #Pause
                    for event in pygame.event.get():
                        if event.type == QUIT:          #Si l'utilisateur quitte
                            pygame.quit()
                compt = 1
            temps = pygame.time.delay(2000)                 #Pause
            Niveau1 = 0             #On sort de la boucle

# coding: utf-8

#Appel des fichiers nécessaire au jeu
from pygame.locals import *
from Niveau import *
from Personnage import *
from Affichage import *

pygame.init()


#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_longueur, cote_largeur))
#Définition de l'icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre de la fenêtre
pygame.display.set_caption(titre_fenetre)

#Variables
continuer = 1
continuer_jeu_n1 = 1    #Boucles des niveaux
continuer_jeu_n2 = 0
continuer_jeu_n3 = 0
choix = 'n1'		#On définit le niveau à charger
restart = 0             #Premier passage dans le jeu

#Boucle du jeu
while continuer:
    fond = pygame.image.load(image_fond).convert()
    texte = pygame.image.load(image_texte).convert()
    if restart == 0:
        Affichage.texte1(100)   #Affichage de l'image d'accueil et du texte clignotant
        fenetre.blit(texte, ( 0,0))
        Affichage.texte2(100)   #Affichage de l'histoire
        Musique.play()          #Lancement de la musique du jeu

	#Génération et affichage du niveau à partir de notre fichier
    niveau = Niveau(choix)
    niveau.generer()
    niveau.afficher(fenetre)

	#Création de Echo avec le fichier 'Personnage'
    echo = Echo("images/echo_droite.png", "images/echo_droite2.png", "images/echo_gauche.png", "images/echo_gauche2.png",
    "images/echo_haut.png","images/echo_haut2.png", "images/echo_bas.png", "images/echo_bas2.png", niveau)

    pygame.key.set_repeat(300, 80)
			
    #Boucle niveau 1
    while continuer_jeu_n1:
        for event in pygame.event.get():   #Récupération des actions utilisateur
            if event.type == QUIT:         #Si l'utilisateur quitte, ferme le niveau puis la boucle principale
                continuer_jeu_n1 = 0
                continuer = 0

            if event.type == KEYDOWN:      #Récupération des actions clavier
            	
            	#Touches de déplacements
                if event.key == K_RIGHT:
                    echo.deplacer('droite')
                if event.key == K_LEFT:
                    echo.deplacer('gauche')
                if event.key == K_UP:
                    echo.deplacer('haut')
                if event.key == K_DOWN:
                    echo.deplacer('bas')
			
	#Rafraichissement de la page
        fenetre.blit(fond, (0,0))
        niveau.afficher(fenetre)
        fenetre.blit(echo.direction, (echo.x, echo.y)) #Echo.direction = l'image du personnage dans la bonne direction
        pygame.display.flip()

        if niveau.structure[echo.case_y][echo.case_x] == 'l':       #Si Echo se trouve sur un morceau de clé
            if morceaucle1 == 0 :
                Objet.play()        #Bruit ramassage de la clé
            morceaucle1 = 1
            #Modification du fichier niveau pour faire disparaitre la clé
            f = open("n1", "r")                     #Lecture du fichier ( r = read )
            chaine = f.read()
            result = chaine.replace('l', '1')
            f = open("n1", "w")                     #Ecriture du changement ( w = write )
            f.write(result)
            f.close()
            f = open("n1", "r")
            chaine = f.read()
            result2 = chaine.replace('i', '3')
            f = open("n1", "w")
            f.write(result2)
            f.close()
            niveau.generer()                         #Regénération du niveau
            niveau.afficher(fenetre)                 #Affichage de ce dernier


   
        if niveau.structure[echo.case_y][echo.case_x] == 'c':           #Si Echo se trouve sur un morceau de clé
            if morceaucle2 == 0 :
                Objet.play()                #Bruit ramassage de la clé
            morceaucle2 = 1
            #Modification du fichier niveau pour faire disparaitre la clé
            f = open("n1", "r")                 #Lecture du fichier ( r = read )
            chaine = f.read()
            result = chaine.replace('c', '2')
            f = open("n1", "w")                 #Ecriture du changement ( w = write )
            f.write(result)
            f.close()
            f = open("n1", "r")
            chaine = f.read()
            result2 = chaine.replace('n', '4')
            f = open("n1", "w")
            f.write(result2)
            f.close()
            niveau.generer()                    #Regénération du niveau
            niveau.afficher(fenetre)            #Affichage de ce dernier


        #Victoire -> Retour à l'accueil
        if niveau.structure[echo.case_y][echo.case_x] == 'a' and morceaucle1 == 1 and morceaucle2 == 1:         #Condition de victoire = 2 morceaux de clé + Echo sur la sortie
            Affichage.texte3(100)       #Affichage de la transition
            continuer_jeu_n1 = 0        #Changement de boucle de niveau
            continuer_jeu_n2 = 1
            choix = 'n2'                #Définition du niveau à charger
            morceaucle1 = 0             #Remise à 0 des variables clé
            morceaucle2 = 0


    niveau = Niveau(choix)          #Regénération et affichage du niveau 2
    niveau.generer()
    niveau.afficher2(fenetre)
                            

    #Remise à l'origine du fichier du niveau 1 pour le réafficher comme à l'originel lors du prochain lancement
    f = open("n1", "r")
    chaine = f.read()
    result = chaine.replace('2', 'c')
    f = open ("n1", "w")
    f.write(result)
    f.close()
    f = open("n1", "r")
    chaine = f.read()
    result2 = chaine.replace('1', 'l')
    f = open ("n1", "w")
    f.write(result2)
    f.close()
    f = open("n1", "r")
    chaine = f.read()
    result3 = chaine.replace('3', 'i')
    f = open ("n1", "w")
    f.write(result3)
    f.close()
    f = open("n1", "r")
    chaine = f.read()
    result4 = chaine.replace('4', 'n')
    f = open ("n1", "w")
    f.write(result4)
    f.close()

    #Création de Echo du niveau 2 
    echo = Echo2("images/echo_droite.png", "images/echo_droite2.png", "images/echo_gauche.png", "images/echo_gauche2.png",
    "images/echo_haut.png","images/echo_haut2.png", "images/echo_bas.png", "images/echo_bas2.png", niveau)
                   
    while continuer_jeu_n2 :                #Boucle du niveau 2
        for event in pygame.event.get():    
            if event.type == QUIT:          #Si l'utilisateur ferme le jeu
                continuer_jeu_n2 = 0
                continuer = 0

            if event.type == KEYDOWN:
            	
            	#Touches de déplacement
                if event.key == K_RIGHT:
                    echo.deplacer2('droite')
                if event.key == K_LEFT:
                    echo.deplacer2('gauche')
                if event.key == K_UP:
                    echo.deplacer2('haut')
                if event.key == K_DOWN:
                    echo.deplacer2('bas')
			
	#Affichages aux nouvelles positions
        fenetre.blit(fond, (0,0))
        niveau.afficher2(fenetre)
        fenetre.blit(echo.direction, (echo.x, echo.y)) #Echo.direction = l'image du personnage dans la bonne direction
        pygame.display.flip()

        if niveau.structure[echo.case_y][echo.case_x] == 'l':       #Si Echo marche sur un morceau de clé
            if morceaucle1 == 0 :
                Objet.play()
            morceaucle1 = 1
            f = open("n2", "r")
            chaine = f.read()
            result = chaine.replace('l', '1')
            f = open("n2", "w")
            f.write(result)
            f.close()
            f = open("n2", "r")
            chaine = f.read()
            result2 = chaine.replace('i', '3')
            f = open("n2", "w")
            f.write(result2)
            f.close()
            niveau.generer()                #Regénération du niveau et affichage de celui ci
            niveau.afficher2(fenetre)


   
        if niveau.structure[echo.case_y][echo.case_x] == 'c':       # Si Echo marche sur un morceau de clé
            if morceaucle2 == 0 :
                Objet.play()
            morceaucle2 = 1
            f = open("n2", "r")
            chaine = f.read()
            result = chaine.replace('c', '2')
            f = open("n2", "w")
            f.write(result)
            f.close()
            f = open("n2", "r")
            chaine = f.read()
            result2 = chaine.replace('n', '4')
            f = open("n2", "w")
            f.write(result2)
            f.close()
            niveau.generer()                #Regénération du niveau et affichage de celui ci
            niveau.afficher2(fenetre)


        #Victoire -> Retour à l'accueil
        if niveau.structure[echo.case_y][echo.case_x] == 'a' and morceaucle1 == 1 and morceaucle2 == 1:     #Conditions de victoire
            Affichage.texte3(100)       #Affichage de la transition
            choix = 'n3'                #Choix du niveau
            continuer_jeu_n2 = 0        #Changement de variables de niveau
            continuer_jeu_n3 = 1


    niveau = Niveau(choix)          #Génération et affichage du niveau 3
    niveau.generer()
    niveau.afficher3(fenetre)


    #Remise à l'origine du fichier du niveau 2
    f = open("n2", "r")
    chaine = f.read()
    result = chaine.replace('2', 'c')
    f = open ("n2", "w")
    f.write(result)
    f.close()
    f = open("n2", "r")
    chaine = f.read()
    result2 = chaine.replace('1', 'l')
    f = open ("n2", "w")
    f.write(result2)
    f.close()
    f = open("n2", "r")
    chaine = f.read()
    result3 = chaine.replace('3', 'i')
    f = open ("n2", "w")
    f.write(result3)
    f.close()
    f = open("n2", "r")
    chaine = f.read()
    result4 = chaine.replace('4', 'n')
    f = open ("n2", "w")
    f.write(result4)
    f.close()

    #Création de Echo du niveau 3 ( salle finale )
    echo = Echo3("images/echo_droite.png", "images/echo_droite2.png", "images/echo_gauche.png", "images/echo_gauche2.png",
    "images/echo_haut.png","images/echo_haut2.png", "images/echo_bas.png", "images/echo_bas2.png", niveau)

    while continuer_jeu_n3 :            #Boucle salle finale ( niveau 3 )
        for event in pygame.event.get():
            if event.type == QUIT:      #Si l'utilisateur quitte
                continuer_jeu_n3 = 0
                continuer = 0

            if event.type == KEYDOWN:
            	
            	#Touches de déplacement
                if event.key == K_RIGHT:
                    echo.deplacer3('droite')
                if event.key == K_LEFT:
                    echo.deplacer3('gauche')
                if event.key == K_UP:
                    echo.deplacer3('haut')
                if event.key == K_DOWN:
                    echo.deplacer3('bas')
			
	#Affichages aux nouvelles positions
        fenetre.blit(fond, (0,0))
        niveau.afficher3(fenetre)
        fenetre.blit(echo.direction, (echo.x, echo.y)) #Echo.direction = l'image du personage dans la bonne direction
        pygame.display.flip()

        if niveau.structure[echo.case_y][echo.case_x] == 'c':       #Si Echo marche sur le coffre de droite
            f = open("n3", "r")
            chaine = f.read()
            result = chaine.replace('1', 'p')
            f = open("n3", "w")
            f.write(result)
            f.close()
            niveau.generer()                #Regénération et affichage du niveau
            niveau.afficher3(fenetre)

        if niveau.structure[echo.case_y][echo.case_x] == 'k':       #Si Echo marche sur le coffre de droite
            f = open("n3", "r")
            chaine = f.read()
            result = chaine.replace('2', 't')
            f = open("n3", "w")
            f.write(result)
            f.close()
            niveau.generer()                #Regénération et affichage du niveau
            niveau.afficher3(fenetre)

        if niveau.structure[echo.case_y][echo.case_x] == 'p':       #Si Echo marche sur le portail de gauche
            Portail.play()
            Affichage.texte4(100)           #Affichage de l'image de fin et du message de victoire
            continuer_jeu_n3 = 0            #Fermeture du jeu
            continuer = 0
            

        if niveau.structure[echo.case_y][echo.case_x] == 't':       #Si Echo marche sur le portail de droite
            Portail.play()
            fenetre.blit(texte, ( 0,0))
            Affichage.texte5(100)           #Affichage du message 'Echo s'est perdu et est retournée au début du jeu'
            continuer_jeu_n3 = 0            #Redéfinition des variables de boucles de niveau et relancement du niveau 1
            continuer_jeu_n1 = 1
            choix = 'n1'                    #Choix du niveau 1
            restart = 1                     #Eviter de réafficher l'accueil et l'histoire
                        


    #Remise à l'origine du fichier du niveau 3
    f = open("n3", "r")                     
    chaine = f.read()
    result = chaine.replace('p', '1')
    f = open("n3", "w")
    f.write(result)
    f.close()

    f = open("n3", "r")
    chaine = f.read()
    result = chaine.replace('t', '2')
    f = open("n3", "w")
    f.write(result)
    f.close()

#Fermeture du jeu			
pygame.quit()	

# ------------------------------------------------------------------------
# Laboratoires de programmation mathématique et physique 2
# ------------------------------------------------------------------------
#
# Programme : 7 segments.
#
# ------------------------------------------------------------------------
import math
import pygame
import sys
import numpy as np
import datetime as dt
### Constante(s)
NOIR = (0, 0, 0)
GRIS = (200, 200, 200)
ROUGE = (255, 0, 0)
### Variables Globales
def dessiner_arduino(sortie_arduino, sortie_CD4511, sortie_CD4028, sortie_bouton):
    fenetre.blit(image_arduino, pos_arduino)
    fenetre.blit(image_CD4511, pos_CD4511)
    fenetre.blit(image_bouton, pos_bouton)
    fenetre.blit(image_CD4028, pos_CD4028)


    for j in range(0, 2):
        if j == 0:
            off_ard = 285
            off_cd = 15
            pos_carte = pos_CD4511
            r = range(0, 4)

        if j == 1:
            off_ard = 194
            off_cd = 91
            pos_carte = pos_CD4028
            r = range(4, 8)

        for i in r:
            #print (sortie_arduino[i])
            if sortie_arduino[i] == 0:
                couleur = NOIR
            else:
                couleur = ROUGE

            pygame.draw.line(fenetre, couleur, (pos_arduino[0] + 280, pos_arduino[1] + off_ard),
                            (pos_carte[0] + 7, pos_carte[1] + off_cd), 5)
            off_ard = off_ard + 14
            off_cd = off_cd + 19
       



    off_cd = 15
    off_aff = 5
    i = 0
    for i in range(0, 7):
        if sortie_CD4511[i] == 0:
            couleur = NOIR
        else:
            couleur = ROUGE
        pygame.draw.line(fenetre, couleur, (pos_afficheur[0] + 591, pos_afficheur[1] + off_aff),
                        (pos_CD4511[0] + 102, pos_CD4511[1] + off_cd), 5)
        off_aff = off_aff + 19
        off_cd = off_cd + 19


    if sortie_bouton == 0:
        couleur = NOIR
    else:
        couleur = ROUGE
    pygame.draw.line(fenetre, couleur, (pos_arduino[0] + 279, pos_arduino[1] + 353),
                        (pos_bouton[0] + 13, pos_bouton[1] + 13), 5)

    i = 0
    off_cd = (102, 111)
    off_aff = 44
    for i in range(0, 6):
        if sortie_CD4028[i] == 0:
            couleur = NOIR
        else:
            couleur = ROUGE
        pygame.draw.line(fenetre, couleur, (pos_CD4028[0] + off_cd[0], pos_CD4028[1] + off_cd[1]),
                        (pos_afficheur[0] + off_aff, pos_CD4028[1] + off_cd[1]), 5)

        pygame.draw.line(fenetre, couleur, (pos_afficheur[0] + off_aff, pos_afficheur[1]),
                        (pos_afficheur[0] + off_aff, pos_CD4028[1] + off_cd[1] - 2), 5)
        off_cd = (off_cd[0], off_cd[1] - 20)
        off_aff = off_aff + 101

def dessiner_afficheur(sortie_CD4511, sortie_CD4028):
    global latence_mat
    positions_barres = [[32, 14], [89, 20], [87, 88], [28, 150],
                        [17, 88], [19, 20], [30, 82]]

    for j in range(0, 6):
        fenetre.blit(image_afficheur_s, (pos_afficheur[0] + j*101, pos_afficheur[1]))
        if sortie_CD4028[j] == 1:
            latence_mat[j] = sortie_CD4511
            i = 0
            for barre in positions_barres:
                if sortie_CD4511[i] == 0:
                    i = i + 1
                    continue
                x_b = j*101 + pos_afficheur[0] + int(round(barre[0]*(image_afficheur_s.get_width()/133)))
                y_b = pos_afficheur[1] + int(round(barre[1]*(image_afficheur_s.get_height()/192)))
                if i == 0 or i == 3 or i == 6:
                    fenetre.blit(barre_horizontale_s, (x_b, y_b))
                else:
                    fenetre.blit(barre_verticale_s, (x_b, y_b))
                i = i + 1
        else:
            i = 0
            for barre in positions_barres:
                if latence_mat[j][i] == 0:
                    i = i + 1
                    continue
                x_b = j*101 + pos_afficheur[0] + int(round(barre[0]*(image_afficheur_s.get_width()/133)))
                y_b = pos_afficheur[1] + int(round(barre[1]*(image_afficheur_s.get_height()/192)))
                if i == 0 or i == 3 or i == 6:
                    fenetre.blit(barre_horizontale_s, (x_b, y_b))
                else:
                    fenetre.blit(barre_verticale_s, (x_b, y_b))
                i = i + 1
    return
def composant_CD4511(entree):
    #print ("ton père",entree)
    tdv = 0 
    i=0
    while i < 4:
        #print (entree[7-i])
        tdv += entree[7-i]*(2**(3-i))
        i+=1
    #print("fin boucle")
    if tdv == 0:
        return np.array([1, 1, 1, 1, 1, 1, 0])
    if tdv == 1:
        return np.array([0, 1, 1, 0, 0, 0, 0])
    if tdv == 2:
        return np.array([1, 1, 0, 1, 1, 0, 1])
    if tdv == 3:
        return np.array([1, 1, 1, 1, 0, 0, 1])
    if tdv == 4:
        return np.array([0, 1, 1, 0, 0, 1, 1])
    if tdv == 5:
        return np.array([1, 0, 1, 1, 0, 1, 1])
    if tdv == 6:
        return np.array([1, 0, 1, 1, 1, 1, 1])
    if tdv == 7:
        return np.array([1, 1, 1, 0, 0, 0, 0])
    if tdv == 8:
        return np.array([1, 1, 1, 1, 1, 1, 1])
    if tdv == 9:
        return np.array([1, 1, 1, 1, 0, 1, 1])
def sortie_memorisee(valeur):
    global num_afficheur
    afficheur = num_afficheur
    liste = [0,0,0,0,0,0,0,0]
    i=0
    j=0
    while i<4:
        if valeur%2 == 0:
            liste[4+i] = 0
        else:
            liste[4+i] = 1
        valeur//=2
        i+=1
    while j<4:
        if afficheur%2 == 0:
            liste[j] = 0
        else:
            liste[j] = 1
        afficheur//=2
        j+=1
    #print ("ta mère", liste)
    return np.array(liste)
def gerer_click():
    return 0
def connexion_bouton(sortie_bouton):
    if sortie_bouton == 0:
        pygame.draw.line(fenetre, NOIR, pos_bouton, pos_arduino, 5)
    if sortie_bouton == 1:
        pygame.draw.line(fenetre, ROUGE, pos_bouton, pos_arduino, 5)
    return
def calculer_distance(point1, point2):
    ecart_horizontal = point2[0] - point1[0]
    ecart_vertical = point2[1] - point1[1]
    ecart_horizontal_au_carre = ecart_horizontal * ecart_horizontal
    ecart_vertical_au_carre = ecart_vertical * ecart_vertical
    distance = math.sqrt(ecart_horizontal_au_carre + ecart_vertical_au_carre)
    return distance # en pixels
def sortie_CD4028(entree):
    #print("ton père", entree)
    i = 0
    tdv = 0
    vecteur_de_retour = [0,0,0,0,0,0,0]
    while i < 4:
        tdv += entree[3-i]*(2**(3-i))
        i+=1
    if tdv == 0:
        vecteur_de_retour[6] = 1
        return np.array(vecteur_de_retour)
    if tdv == 1:
        vecteur_de_retour[5] = 1
        return np.array(vecteur_de_retour)
    if tdv == 2:
        vecteur_de_retour[4] = 1
        return np.array(vecteur_de_retour)
    if tdv == 3:
        vecteur_de_retour[3] = 1
        return np.array(vecteur_de_retour)
    if tdv == 4:
        vecteur_de_retour[2] = 1
        return np.array(vecteur_de_retour)
    if tdv == 5:
        vecteur_de_retour[1] = 1
        return np.array(vecteur_de_retour)
    if tdv == 6:
        vecteur_de_retour[0] = 1
        return np.array(vecteur_de_retour)
def chiffres_heure():
    global heure
    vecteur_de_retour = [0,0,0,0,0,0]
    i=0
    j=0
    while i<3:
        unite = heure[i]%10
        dizaine = heure[i]//10
        vecteur_de_retour[j] = dizaine
        vecteur_de_retour[j+1] = unite
        i+=1
        j+=2
    return vecteur_de_retour
    
### Paramètre(s)

dimensions_fenetre = (1100, 600)  # en pixels
images_par_seconde = 25
latence_mat = np.zeros((6, 7))
pos_arduino = (0, 70)
pos_CD4511 = (333, 340)
pos_CD4028 = (333, 128)
pos_afficheur = (500, 350)
pos_bouton = (333, 524)
pos_centre_bouton = (pos_bouton[0] + 51, pos_bouton[1] + 34)
rayon_bouton = 18
pin_arduino = (pos_arduino[0] + 279, pos_arduino[1] + 353)
pin_bouton = (pos_bouton[0] + 13, pos_bouton[1] + 13)
heure = [dt.datetime.now().hour,dt.datetime.now().minute,dt.datetime.now().second]
heure_chiffres = []
### Programme
# Initialisation
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.time.set_timer(pygame.USEREVENT + 1, 40)
fenetre = pygame.display.set_mode(dimensions_fenetre)
pygame.display.set_caption("Programme 7 segments")
horloge = pygame.time.Clock()
valeur_memorisee = 0
num_afficheur = 1
sortie_bouton = 7
sig_horloge = 0
sig_horloge_afficheur = 0
image_afficheur_s = pygame.image.load('images/7_seg_s.png').convert_alpha(fenetre)
barre_verticale_s = pygame.image.load('images/vertical_s.png').convert_alpha(fenetre)
barre_horizontale_s = pygame.image.load('images/horizontal_s.png').convert_alpha(fenetre)
image_afficheur = pygame.image.load('images/7_seg.png').convert_alpha(fenetre)
barre_verticale = pygame.image.load('images/vertical.png').convert_alpha(fenetre)
barre_horizontale = pygame.image.load('images/horizontal.png').convert_alpha(fenetre)
image_arduino = pygame.image.load('images/arduino.png').convert_alpha(fenetre)
image_CD4511 = pygame.image.load('images/CD4511.png').convert_alpha(fenetre)
image_CD4028 = pygame.image.load('images/CD4028.png').convert_alpha(fenetre)
image_bouton = pygame.image.load('images/bouton.png').convert_alpha(fenetre)
couleur_fond = GRIS

# Boucle principale

while True:
    heure = [dt.datetime.now().hour,dt.datetime.now().minute,dt.datetime.now().second]
    heure_chiffres = chiffres_heure()
    print(heure_chiffres)
    temps_maintenant = pygame.time.get_ticks()
    valeur_precedente_sortie_bouton = sortie_bouton
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        clic_gauche = pygame.mouse.get_pressed()[0]
        if clic_gauche:
            pos_x, pos_y = pygame.mouse.get_pos()
            if calculer_distance((pos_x, pos_y),pos_centre_bouton)<rayon_bouton:
                sortie_bouton = 1
        else:
            sortie_bouton = 0
        if evenement.type == pygame.USEREVENT:
            sig_horloge+=1
        if evenement.type == pygame.USEREVENT+1:
            sig_horloge_afficheur+=1
        if sig_horloge == 1:
            valeur_memorisee += 1
            sig_horloge = 0
        if sig_horloge_afficheur == 1:
            num_afficheur += 1
            sig_horloge_afficheur = 0
    if valeur_precedente_sortie_bouton == 0 and sortie_bouton == 1:
        valeur_memorisee += 1
    if valeur_memorisee >=10:
        valeur_memorisee = 0
    if num_afficheur>6:
        num_afficheur = 1
    fenetre.fill(couleur_fond)
    k=0
    num_afficheur = 1
    while k<6:
        sortie_CD4511 = composant_CD4511(sortie_memorisee(heure_chiffres[5-k]))
        dessiner_arduino(sortie_memorisee(heure_chiffres[5-k]), sortie_CD4511, sortie_CD4028(sortie_memorisee(heure_chiffres[5-k])) , sortie_bouton)
        dessiner_afficheur(sortie_CD4511, sortie_CD4028(sortie_memorisee(heure_chiffres[5-k])))
        k+=1
        num_afficheur+=1
    #print("###########################\n",latence_mat)
    pygame.display.flip()
    horloge.tick(images_par_seconde)
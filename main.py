import pygame
from pygame.locals import*
from random import randint


pygame.init()
window_ = pygame.display.set_mode([1024,758])
pygame.display.set_caption("USA")


back = pygame.image.load("usa_map.jpg").convert()
boite = pygame.image.load("boite.png").convert()
blanc = pygame.image.load("blanc.jpg").convert()
blanc2 = pygame.image.load("blanc2.png").convert()
skip = pygame.image.load("skip.png").convert()
menu_ = pygame.image.load("menu.png").convert()

cooper_font = pygame.font.SysFont(None,36)
NOIR =(0,0,0)

ok=True
menu=True
game1=False
game2=False
close=False

jouer=False

text=""


liste_=(["californie",(81,308),"CA",False,1],["nevada",(143,248),"NV",False,2],["oregon",(101,145),"OR",False,3],["washington",(133,67),"WA",False,4],["idaho",(212,170),"ID",False,5],["utah",(244,285),"UT",False,6],["arizona",(221,398),"AZ",False,7],["nouveau mexique",(325,398),"NM",False,8],["colorado",(341,295),"CO",False,9],["wyoming",(313,204),"WY",False,10],["montana",(289,107),"MT",False,11],["texas",(455,487),"TX",False,12],["oklahoma",(487,390),"OK",False,13],["kansas",(461,322),"KS",False,14],["nebraska",(453,253),"NE",False,15],["dakota du sud",(437,176),"SD",False,16],["dakota du nord",(439,106),"ND",False,17],["louisiane",(579,485),"LA",False,18],["arkansas",(574,403),"AR",False,19],["missouri",(567,320),"MO",False,20],["iowa",(548,233),"IA",False,21],["minnesota",(527,141),"MN",False,22],["mississippi",(631,444),"MS",False,23],["alabama",(687,440),"AL",False,24],["georgie",(752,439),"GA",False,25],["floride",(805,541),"FL",False,26],["caroline du sud",(793,406),"SC",False,27],["caroline du nord",(813,355),"NC",False,28],["tennessee",(682,375),"TN",False,29],["wisconsin",(602,174),"WI",False,30],["illinois",(625,277),"IL",False,31],["indiana",(680,276),"IN",False,32],["michigan",(690,162),"MI",False,33],["kentucky",(706,335),"KY",False,34],["ohio",(736,258),"OH",False,35],["virginie occidentale",(779,300),"WV",False,36],["virginie",(823,316),"VA",False,37],["maryland",(841,266),"MD",False,38],["delaware",(876,266),"DE",False,39],["new jersey",(892,243),"NJ",False,40],["pennsylvanie",(817,235),"PA",False,41],["etat de new york",(860,176),"NY",False,42],["connecticut",(907,200),"CT",False,43],["rhode island",(931,196),"RI",False,44],["massachusetts",(912,180),"MA",False,45],["vermont",(890,139),"VT",False,46],["new hampshire",(914,154),"NH",False,47],["maine",(937,103),"ME",False,48],["alaska",(224,607),"AK",False,49],["hawai",(694,675),"HI",False,50])



while ok:

    if menu:
        window_.blit(menu_,(0,0))
        pygame.display.flip()

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    close = True
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if 200<event.pos[0]<400 and 387<event.pos[1]<457:
                        menu = False
                        game1=True
                    if 600<event.pos[0]<800 and 387<event.pos[1]<457:
                        menu = False
                        game2=True




    if game1:
        compteur=0
        compte = cooper_font.render(str(compteur) + "/50", True , NOIR)
        window_.blit(back,(0,0))
        window_.blit(boite,(328.5,20))
        window_.blit(compte,(5,3))
        pygame.display.flip()
        for i in range(50):
            liste_[i][3]=False


        while game1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game1 = False
                    close = True

                click=False

                if event.type == KEYDOWN and event.key == K_a:
                    text=text+"a"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_b:
                    text=text+"b"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_c:
                    text=text+"c"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_d:
                    text=text+"d"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_e:
                    text=text+"e"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_f:
                    text=text+"f"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_g:
                    text=text+"g"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_h:
                    text=text+"h"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_i:
                    text=text+"i"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_j:
                    text=text+"j"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_k:
                    text=text+"k"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_l:
                    text=text+"l"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_m:
                    text=text+"m"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_n:
                    text=text+"n"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_o:
                    text=text+"o"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_p:
                    text=text+"p"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_q:
                    text=text+"q"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_r:
                    text=text+"r"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_s:
                    text=text+"s"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_t:
                    text=text+"t"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_u:
                    text=text+"u"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_v:
                    text=text+"v"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_w:
                    text=text+"w"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_x:
                    text=text+"x"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_y:
                    text=text+"y"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_z:
                    text=text+"z"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_SPACE:
                    text=text+" "
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_BACKSPACE:
                    text=text[0:-1]
                    window_.blit(boite,(328.5,20))
                    pygame.display.flip()
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_RETURN:
                    for i in range(50):
                        if text == liste_[i][0]:
                            if liste_[i][3]==False:
                                noms = cooper_font.render(liste_[i][2], True , NOIR)
                                window_.blit(noms,liste_[i][1])
                                window_.blit(blanc,(0,0))
                                pygame.display.flip()
                                compteur+=1
                                liste_[i][3]=True
                    compte = cooper_font.render(str(compteur) + "/50", True , NOIR)
                    window_.blit(compte,(5,3))
                    window_.blit(boite,(328.5,20))
                    pygame.display.flip()
                    text=""
                    click=True
                    jouer=True

                if click==False and jouer ==True:
                    text_ = cooper_font.render(text, True , NOIR)
                    window_.blit(text_,(330,22))
                    pygame.display.flip()
                    jouer=False

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if 976<event.pos[0]<1024 and 0<event.pos[1]<25:
                        game1=False
                        menu = True



    if game2:
        compteur=0
        compte = cooper_font.render(str(compteur) + "/50", True , NOIR)
        window_.blit(back,(0,0))
        window_.blit(boite,(328.5,20))
        window_.blit(compte,(5,3))
        window_.blit(skip,(928,0))
        pygame.display.flip()
        for i in range(50):
            liste_[i][3]=False
        for i in range(50):
            numbers = cooper_font.render(str(liste_[i][4]), True , NOIR)
            window_.blit(numbers,liste_[i][1])
            pygame.display.flip()

        i=randint(0,49)
        states = cooper_font.render(str(liste_[i][0]), True , NOIR)
        window_.blit(states,(680,80))
        pygame.display.flip()

        while game2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game2 = False
                    close = True

                click=False

                if event.type == KEYDOWN and event.key == K_0:
                    text=text+"0"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_1:
                    text=text+"1"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_2:
                    text=text+"2"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_3:
                    text=text+"3"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_4:
                    text=text+"4"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_5:
                    text=text+"5"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_6:
                    text=text+"6"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_7:
                    text=text+"7"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_8:
                    text=text+"8"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_9:
                    text=text+"9"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_KP0:
                    text=text+"0"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_KP1:
                    text=text+"1"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_KP2:
                    text=text+"2"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_KP3:
                    text=text+"3"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_KP4:
                    text=text+"4"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_KP5:
                    text=text+"5"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_KP6:
                    text=text+"6"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_KP7:
                    text=text+"7"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_KP8:
                    text=text+"8"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_KP9:
                    text=text+"9"
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_BACKSPACE:
                    text=text[0:-1]
                    window_.blit(boite,(328.5,20))
                    pygame.display.flip()
                    click=True
                    jouer=True
                if event.type == KEYDOWN and event.key == K_RETURN:
                    if text == str(liste_[i][4]):
                        compteur+=1
                        liste_[i][3]=True
                        while liste_[i][3]==True:
                            i=randint(0,49)
                        window_.blit(blanc2,(680,80))
                        states = cooper_font.render(str(liste_[i][0]), True , NOIR)
                        window_.blit(states,(680,80))
                        window_.blit(blanc,(0,0))
                        pygame.display.flip()


                    compte = cooper_font.render(str(compteur) + "/50", True , NOIR)
                    window_.blit(compte,(5,3))
                    window_.blit(boite,(328.5,20))
                    pygame.display.flip()
                    text=""
                    click=True
                    jouer=True

                if click==False and jouer ==True:
                    text_ = cooper_font.render(text, True , NOIR)
                    window_.blit(text_,(330,22))
                    pygame.display.flip()
                    jouer=False

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if 976<event.pos[0]<1024 and 0<event.pos[1]<25:
                        game2=False
                        menu = True
                    if 928<event.pos[0]<976 and 0<event.pos[1]<25:
                        i=randint(0,49)
                        while liste_[i][3]==True:
                            i=randint(0,49)
                        window_.blit(blanc2,(680,80))
                        states = cooper_font.render(str(liste_[i][0]), True , NOIR)
                        window_.blit(states,(680,80))
                        pygame.display.flip()


    if close:
        ok = False
        pygame.quit()

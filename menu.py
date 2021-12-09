import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1280, 632))
pygame.display.set_caption("Trash Can Game")
screen.fill((255,255,255))
#Define as cores 
AMARELO  = (234, 196, 58)
BRANCO = (255, 255, 255)

#Definindo Fonte e Renderizando frase
import pygame.freetype
pygame.freetype.init()
fonteTexto = pygame.freetype.Font("Fontes/upheavtt.ttf", 45)

def get_pygame_events():
  pygame_events = pygame.event.get()
  return pygame_events

#Teclas
keys_pressed = get_pygame_events()

#Declarando Sons
musica_inicio = pygame.mixer.Sound("Sons/inicio.wav")
musica_inicio_abafado = pygame.mixer.Sound("Sons/inicio_abafado.wav")
musica_jogo = pygame.mixer.Sound("Sons/jogo.wav")
click = pygame.mixer.Sound("Sons/click.wav")
start_som = pygame.mixer.Sound("Sons/start.wav")
gameover_som = pygame.mixer.Sound("Sons/gameover.wav")
gameover_musica = pygame.mixer.Sound("Sons/gameover_musica.wav")
p_bem_vindo = pygame.mixer.Sound("Sons/bem-vindo.wav")
p_500 = pygame.mixer.Sound("Sons/500.wav")
p_1000 = pygame.mixer.Sound("Sons/1000.wav")
p_gameover = pygame.mixer.Sound("Sons/gameover_som.wav")
acerto_lixeira = pygame.mixer.Sound("Sons/acerto_lixeira.wav")
som_500 = pygame.mixer.Sound("Sons/som_500.wav")
som_1000 = pygame.mixer.Sound("Sons/som_1000.wav")
som_2000 = pygame.mixer.Sound("Sons/som_2000.wav")


fundo_inicio_img = [pygame.image.load("Inicio/1.jpg"),pygame.image.load("Inicio/2.jpg"),pygame.image.load("Inicio/3.jpg"),pygame.image.load("Inicio/4.jpg"),pygame.image.load("Inicio/5.jpg"),
                    pygame.image.load("Inicio/6.jpg"),pygame.image.load("Inicio/7.jpg")]

fundo_jogo_img = [pygame.image.load("Fundo/1.gif"),pygame.image.load("Fundo/2.gif"),pygame.image.load("Fundo/3.gif"),pygame.image.load("Fundo/4.gif"),pygame.image.load("Fundo/5.gif"),
                  pygame.image.load("Fundo/6.gif"),pygame.image.load("Fundo/7.gif"),pygame.image.load("Fundo/8.gif"),pygame.image.load("Fundo/9.gif"),pygame.image.load("Fundo/10.gif"),
                  pygame.image.load("Fundo/11.gif"),pygame.image.load("Fundo/12.gif"),pygame.image.load("Fundo/13.gif"),pygame.image.load("Fundo/14.gif"),pygame.image.load("Fundo/15.gif"),
                  pygame.image.load("Fundo/16.gif"),pygame.image.load("Fundo/17.gif"),pygame.image.load("Fundo/18.gif"),pygame.image.load("Fundo/19.gif"),pygame.image.load("Fundo/20.gif"),
                  pygame.image.load("Fundo/21.gif"),pygame.image.load("Fundo/22.gif"),pygame.image.load("Fundo/23.gif"),pygame.image.load("Fundo/24.gif"),pygame.image.load("Fundo/25.gif"),
                  pygame.image.load("Fundo/26.gif"),pygame.image.load("Fundo/27.gif"),pygame.image.load("Fundo/28.gif"),pygame.image.load("Fundo/29.gif"),pygame.image.load("Fundo/30.gif"),
                  pygame.image.load("Fundo/31.gif"),pygame.image.load("Fundo/32.gif"),pygame.image.load("Fundo/33.gif"),pygame.image.load("Fundo/34.gif"),pygame.image.load("Fundo/35.gif"),
                  pygame.image.load("Fundo/36.gif"),pygame.image.load("Fundo/37.gif"),pygame.image.load("Fundo/38.gif"),pygame.image.load("Fundo/39.gif"),pygame.image.load("Fundo/40.gif"),
                  pygame.image.load("Fundo/41.gif"),pygame.image.load("Fundo/42.gif"),pygame.image.load("Fundo/43.gif")]

p_bem_vindo.play()
#tela_inicial_menu
def fundo_inicio():
    gameover_musica.stop()
    musica_inicio_abafado.stop()
    musica_inicio.play(-1)
    musica_jogo.stop()
    sair = False 
    while not sair:      
        i = 0
        while i < 7:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    print("Mouse Movendo X:", x)
                    print("Mouse Movendo Y:", y)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #area_botao_jogo
                    if x > 446 and x < 813:
                        if y > 342 and y < 407:
                            click.play()
                            fundo_jogo()

                    #area_botao_sair
                    if x > 639 and x < 815:
                        if y > 428 and y < 474:
                            click.play()
                            botao_sair()

                    #area_botao_ajuda
                    if x > 449 and x < 624:
                        if y > 428 and y < 476:
                            click.play()
                            botao_ajuda()

                    #area_botao_creditos
                    if x > 1066 and x < 1246:
                        if y > 504 and y < 545:
                            click.play()
                            botao_creditos()

                    #area_botao_ligar_som
                    if x > 1176 and x < 1204:
                        if y > 572 and y < 595:
                            click.play()
                            musica_inicio.stop()
                            musica_inicio.play(-1)

                    #area_botao_desligar_som
                    if x > 1219 and x < 1246:
                        if y > 573 and y < 599:
                            click.play()
                            musica_inicio.stop()

                if event.type == pygame.QUIT:
                    print("sair")
                    pygame.quit()
            
            screen.blit(fundo_inicio_img[i],(0, 0))
            #botao-jogar
            jogar = pygame.image.load('Props/botao-jogar.png')
            screen.blit(jogar,(0,0))

            #botao-ajuda
            ajuda = pygame.image.load('Props/botao-ajuda.png')
            screen.blit(ajuda,(0,0))

            #botao-fechar
            fechar = pygame.image.load('Props/botao-sair.png')
            screen.blit(fechar,(0,0))

            #botao-creditos
            creditos = pygame.image.load('Props/botao-creditos.png')
            screen.blit(creditos,(0,0))

            #botao-som
            som = pygame.image.load('Props/botao-som.png')
            screen.blit(som,(0,0))
            
            pygame.time.delay(10)
            pygame.display.update()
            i += 1

#tela_jogo_jogar
def fundo_jogo():
    gameover_musica.stop()
    musica_inicio.stop()
    musica_jogo.stop()
    start_som.play()
    musica_jogo.play(-1)
    pontuacao = 0

    #Props 
    organico = pygame.image.load('Props/item-organico.png')
    plastico = pygame.image.load('Props/item-plastico.png')
    papel = pygame.image.load('Props/item-papel.png')
    vidro = pygame.image.load('Props/item-vidro.png')
    metal = pygame.image.load('Props/item-metal.png')    

    clock = pygame.time.Clock()
    
    sair = False
    i = 0
    while not sair:
        while i < 43:
            screen.blit(fundo_jogo_img[i],(0, 0))

            for event in pygame.event.get():
              #Caso saia
              if event.type == pygame.QUIT:
                  print("sair")
                  pygame.quit()

              #MOUSEMOTION PARA CAPTURA DE POSIÇÕES
              if event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                print("Mouse Movendo X:", x)
                print("Mouse Movendo Y:", y)
              
            #DEFINIÇÃO DE VARIÁVEIS
            #lixeiras
            lixeiras = pygame.image.load('Props/lixeiras.png')
            #placar
            placar = pygame.image.load('Props/placar.png')
            

            #MOVIMENTAÇÃO OBJETO            
            #posições tela
            posX = 610
            posY = 20

            #Objeto aleatório
            numero = random.randint(1,5)
            if numero == 1:
              objeto = plastico
              print('plástico')         
              
            elif numero == 2:
              objeto = papel
              print('papel')

            elif numero == 3:
              objeto = metal                
              print('metal')

            elif numero == 4:
              objeto = vidro
              print('vidro')
                                        
            elif numero == 5:
              objeto = organico     
              print('organico')


            while posY < 460:             
              #Fica blitando o fundo animado (?)
              print(i)
              if i > 41:
                i = 0
                screen.blit(fundo_jogo_img[i],(0, 0))
                print("if")
                
              else: 
                i += 1
                screen.blit(fundo_jogo_img[i],(0, 0))
                print("else")
              
              #Blita as lixeiras e o placar                  
              screen.blit(lixeiras,(0,0))
              screen.blit(placar,(0,0))

              #Blita pontuacao
              fonteTexto.render_to(screen, (50, 50), str(pontuacao), AMARELO) 
            
              #Lógica do aumento da dificuldade
              if (pontuacao == 0 or pontuacao < 100):      
                posY += 5

              elif pontuacao <500:
                posY += 6

              elif pontuacao <1000:
                posY += 8

              elif pontuacao < 1500:
                posY += 10

              elif pontuacao < 2000:
                posY += 12

              else:
                posY += 15

              # Movimentação do X e aceleração do Y
              for event in pygame.event.get():
                print("teste")
                
              comandos = pygame.key.get_pressed()
              if comandos[pygame.K_LEFT]:
                posX -= 15
              if comandos[pygame.K_RIGHT]:
                posX += 15
              if comandos[pygame.K_DOWN]:
                posY += 8


              #Vai blitando o objeto aleatório de acordo com a posição
              screen.blit(objeto, (posX,posY))
              pygame.display.update()

            #COLISÕES
            #Colisão lixeira plastico 
            if objeto == plastico:
              if(posX > 180 and posX < 305):
                acerto_lixeira.play()
                pontuacao += 50

              if(posX < 180 or posX >305):
                gameover(pontuacao)

            #Colisão lixeira papel
            if objeto == papel:
              if(posX > 370 and posX < 505):
                acerto_lixeira.play()
                pontuacao += 50

              if(posX < 370 or posX > 505):
                gameover(pontuacao)

            #Colisão lixeira metal
            if objeto == metal:
              if(posX > 560 and posX < 700):
                acerto_lixeira.play()
                pontuacao += 50

              if(posX < 560 or posX > 700):
                gameover(pontuacao)

            #Colisão lixeira vidro
            if objeto == vidro:
              if(posX > 750 and posX < 895):
                acerto_lixeira.play()
                pontuacao += 50

              if(posX < 750 or posX > 895):
                gameover(pontuacao)

            #Colisão lixeira organico
            if objeto == organico:
              if(posX > 950 and posX < 1090):
                acerto_lixeira.play()
                pontuacao += 50

              if(posX < 950 or posX > 1090):
                gameover(pontuacao)

              
            if pontuacao == 500:
                som_500.play()
                pygame.time.delay(200)
                p_500.play()
                
            if pontuacao == 1000:
                som_1000.play()
                pygame.time.delay(200)
                p_1000.play()

            if pontuacao == 2000:
                som_2000.play()
              
            clock.tick(60)
  
#botao_sair
def botao_sair():
    pygame.quit()

def botao_ajuda():
    musica_inicio.stop()
    musica_inicio_abafado.play(-1)
    sair = False 
    while not sair:      
        i = 0
        while i < 7:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    print("Mouse Movendo X:", x)
                    print("Mouse Movendo Y:", y)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x > 30 and x < 78:
                        if y > 30 and y < 73:
                            click.play()
                            fundo_inicio()

                if event.type == pygame.QUIT:
                    print("sair")
                    pygame.quit()
            
            screen.blit(fundo_inicio_img[i],(0, 0))
            #botao-voltar
            voltar = pygame.image.load('Props/botao-voltar.png')
            screen.blit(voltar,(0,0))

            #botao-voltar
            como_jogar = pygame.image.load('Props/como_jogar.png')
            screen.blit(como_jogar,(0,0))
            
            pygame.time.delay(120)
            pygame.display.update()
            i += 1

def botao_creditos():
    musica_inicio.stop()
    musica_inicio_abafado.play(-1)
    sair = False 
    while not sair:      
        i = 0
        while i < 7:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    print("Mouse Movendo X:", x)
                    print("Mouse Movendo Y:", y)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x > 30 and x < 78:
                        if y > 30 and y < 73:
                            click.play()
                            fundo_inicio()

                if event.type == pygame.QUIT:
                    print("sair")
                    pygame.quit()
            
            screen.blit(fundo_inicio_img[i],(0, 0))
            #botao-voltar
            voltar = pygame.image.load('Props/botao-voltar.png')
            screen.blit(voltar,(0,0))

            #desenvolvedores
            desenvolvedores = pygame.image.load('Props/desenvolvedores.png')
            screen.blit(desenvolvedores,(0,0))
            
            pygame.time.delay(120)
            pygame.display.update()
            i += 1

def gameover(pontuacao):
    musica_jogo.stop()
    gameover_som.play()
    p_gameover.play()
    gameover_musica.play(-1)
    sair = False 
    while not sair:      
        i = 0
        while i < 7:
            for event in pygame.event.get():
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if event.type == pygame.MOUSEMOTION:
                    print("Mouse Movendo X:", x)
                    print("Mouse Movendo Y:", y)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x > 376 and x < 683:
                        if y > 485 and y < 528:
                            click.play()
                            fundo_jogo()

                    if x > 726 and x < 905:
                        if y > 483 and y < 525:
                            click.play()
                            fundo_inicio()

                if event.type == pygame.QUIT:
                    print("sair")
                    pygame.quit()
            
            screen.blit(fundo_inicio_img[i],(0, 0))
            #gameover_menu
            gameover = pygame.image.load('Props/gameover.png')
            fonteTexto.render_to(screen, (377, 418), str(pontuacao), BRANCO)
            screen.blit(gameover,(0,0))
            
            pygame.time.delay(120)
            pygame.display.update()
            i += 1

def main():
    fundo_inicio()
main()

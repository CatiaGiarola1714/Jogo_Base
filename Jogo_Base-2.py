import pygame
import random

# Inicializa o PyGame
pygame.init()
# Inicializar  a fonte de texto
fonte = pygame.font.Font(None,36)#None = fonte padrao e 36 é o tamanho

# 1o Elementos dos 3 necessários: Janela
LARG_JANELA = 800 #Largura da Janela
ALT_JANELA = 600 # Altura da Janela

# Elementos da Janela
janela = pygame.display.set_mode((LARG_JANELA,ALT_JANELA))# Cria a Janela
pygame.display.set_caption('Joguinho_V0') # Nome da janela
# Elementos do Jogo
# Cores    R   G   B
BRANCO = (255,255,255)
PRETO = (0,0,0)

FPS = 60 # Quadros Por Segundos
clock = pygame.time.Clock() # Inicializar o Clock do Jogo

# Carregar as imagens dos Jogadores
F1_IMG = pygame.image.load('FormigaM.png')
F1 = pygame.transform.scale(F1_IMG,(40,50))
F1 = pygame.transform.rotate(F1,270)

F2_IMG = pygame.image.load('FormigaY.png')
F2 = pygame.transform.scale(F2_IMG,(40,50))
F2 = pygame.transform.rotate(F2,270)

FRUTA_IMG = pygame.image.load('morango.png')

GRAMADO = pygame.image.load('gramado.jpg')
GRAMADO = pygame.transform.scale(GRAMADO,(LARG_JANELA,ALT_JANELA))

# Cria o retangulo das Formigas
F1_RE = pygame.Rect(60,30,40,50)
F2_RE = pygame.Rect(60,80,40,50)
# Coloca a fruta no tamanho certo
FRUT = pygame.transform.scale(FRUTA_IMG,(50,50))

##FRUTAS = [pygame.Rect(200,140,50,50),
##         pygame.Rect(450,140,50,50),
##         pygame.Rect(670,140,50,50),
##         pygame.Rect(200,450,50,50),
##         pygame.Rect(450,450,50,50),
##         pygame.Rect(670,450,50,50)]

N_FRUTAS = 150
FRUTAS = []
for i in range(N_FRUTAS):
    xi = random.randint(60,740)
    yi = random.randint(60,540)
    FRUTAS.append(pygame.Rect(xi,yi,50,50))

# Velocidade de movimentação
vel = 5
# 2o Elemento dos 3 necessários: Ciclo repetitivo
Pontos_F1 = 0 # pontuação da formiga 1
Pontos_F2 = 0
roda = True
while roda:
    clock.tick(FPS) # reduzir o processamento para a frequencia de FPS
    # 3o Elemento dos 3 necessários: Verificação de eventos
    #janela.fill(BRANCO) # A cada iteração criar uma nova janela preta
    janela.blit(GRAMADO,(0,0)) # Coloca o gramado na imagem
    janela.blit(F1,(F1_RE.x,F1_RE.y))
    janela.blit(F2,(F2_RE.x,F2_RE.y))

    for fruta in FRUTAS:
        janela.blit(FRUT,(fruta.x,fruta.y))

    for fruta in FRUTAS:
        if F1_RE.colliderect(fruta): # Olha se teve colisao
            FRUTAS.remove(fruta) # Se SIM remove a fruta
            Pontos_F1 += 1# soma 1 ponto para a formiga
        if F2_RE.colliderect(fruta): # Olha se teve colisao
            FRUTAS.remove(fruta) # Se SIM remove a fruta
            Pontos_F2 += 1# soma 1 ponto para a formiga
    pontos_texto = fonte.render(f'Formiga 1: {Pontos_F1}  x  Formiga 2 : {Pontos_F2}',
                                True,(255,255,255))
                            
    pontos_RE = pontos_texto.get_rect()
    pontos_RE.topleft= (10,10)
    janela.blit(pontos_texto,pontos_RE)
    

    tecla = pygame.key.get_pressed()# Verifica se alguma tecla foi pressionada

    if tecla[pygame.K_a]==True and (F1_RE.x) > 0: # Se a tecla for o "a"
        F1_RE.x -= vel # Move 1 pixel para a esquerda
    elif tecla[pygame.K_d]==True and (F1_RE.x + 40)<= LARG_JANELA: # Se a tecla for o "d"
        F1_RE.x += vel # Move 1 pixel para a direita
    elif tecla[pygame.K_w]==True and (F1_RE.y) > 0: # Se a tecla for o "w"
        F1_RE.y -= vel # Move 1 pixel para cima
    elif tecla[pygame.K_s]==True and (F1_RE.y + 50)<= ALT_JANELA: # Se a tecla for o "s"
        F1_RE.y += vel # Move 1 pixel para baixo

    if tecla[pygame.K_LEFT]==True and (F2_RE.x) > 0: # Se a tecla for o "seta esquerda"
        F2_RE.x -= vel # Move 1 pixel para a esquerda
    elif tecla[pygame.K_RIGHT]==True and (F2_RE.x + 40)<= LARG_JANELA: # Se a tecla for o "seta direita"
        F2_RE.x += vel # Move 1 pixel para a direita
    elif tecla[pygame.K_UP]==True and (F2_RE.y) > 0: # Se a tecla for o "seta p/ cima"
        F2_RE.y -= vel # Move 1 pixel para cima
    elif tecla[pygame.K_DOWN]==True and (F2_RE.y + 50)<= ALT_JANELA: # Se a tecla for o "seta p/ baixo"
        F2_RE.y += vel # Move 1 pixel para baixo 
    for evento in pygame.event.get(): # Verifica se teve algum evento
        if evento.type == pygame.QUIT: # Verifica se evento foi apertar X
            roda = False # Finaliza o While

    if len(FRUTAS)==0: # Se não tem mais frutas então
        roda = False   # fecha o programa
    
    pygame.display.update() # Atualizar a janela com as modificações feitas

pygame.quit()

import pygame
import random

# Inicializa o PyGame
pygame.init()

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

FRUTA_IMG = pygame.image.load('morango.png')

GRAMADO = pygame.image.load('gramado.jpg')
GRAMADO = pygame.transform.scale(GRAMADO,(LARG_JANELA,ALT_JANELA))

# Cria o retangulo das Formigas
F1_RE = pygame.Rect(0,0,40,50)
# Coloca a fruta no tamanho certo
FRUT = pygame.transform.scale(FRUTA_IMG,(50,50))

# Velocidade de movimentação
vel = 3
# 2o Elemento dos 3 necessários: Ciclo repetitivo
roda = True
while roda:
    clock.tick(FPS) # reduzir o processamento para a frequencia de FPS
    # 3o Elemento dos 3 necessários: Verificação de eventos
    janela.fill(BRANCO) # A cada iteração criar uma nova janela preta
    janela.blit(F1,(F1_RE.x,F1_RE.y))

    tecla = pygame.key.get_pressed()# Verifica se alguma tecla foi pressionada

    if tecla[pygame.K_a]==True and (F1_RE.x) > 0: # Se a tecla for o "a"
        F1_RE.x -= vel # Move 1 pixel para a esquerda
    elif tecla[pygame.K_d]==True and (F1_RE.x + 40)<= LARG_JANELA: # Se a tecla for o "d"
        F1_RE.x += vel # Move 1 pixel para a direita
    elif tecla[pygame.K_w]==True and (F1_RE.y) > 0: # Se a tecla for o "w"
        F1_RE.y -= vel # Move 1 pixel para cima
    elif tecla[pygame.K_s]==True and (F1_RE.y + 50)<= ALT_JANELA: # Se a tecla for o "s"
        F1_RE.y += vel # Move 1 pixel para baixo

        
    for evento in pygame.event.get(): # Verifica se teve algum evento
        if evento.type == pygame.QUIT: # Verifica se evento foi apertar X
            roda = False # Finaliza o While
    
    pygame.display.update() # Atualizar a janela com as modificações feitas

pygame.quit()

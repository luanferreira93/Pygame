import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

pygame.init()
pygame.mixer.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

LARGURA = 640
ALTURA = 480
BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Dino Game')
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'dinoSpritesheet.png')).convert_alpha()

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #som de pulo
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons,'jump_sound.wav'))
        self.imagens_dinossauro = []
        #Pegando as sprites do Dino
        for i in range(3):
            img = sprite_sheet.subsurface((i*32,0), (32,32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro.append(img)
        
        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100, ALTURA - 64)
        self.pulo = False
        self.posicao_y_inicial = (ALTURA - 64 - 96 // 2)
        # Mascara de Colisão
        self.mask = pygame.mask.from_surface(self.image)
        self.som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons,'death_sound.wav'))

    def pular(self):
        self.pulo = True   
        self.som_pulo.play()
        pass

    def update(self):
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.index_lista)]
        
        # lógica de pulo do dino
        #Caso tenha apertado a tecla espaço
        if self.pulo:
            self.rect.y -=30
            if self.rect.y <= 100:
                self.pulo = False
        else:
            if self.rect.y < self.posicao_y_inicial:
                self.rect.y += 20
            else:
                self.rect.y = self.posicao_y_inicial
    
    def colisao(self):
        self.som_colisao.play()
    

class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32,0),(32,32))
        self.image = pygame.transform.scale(self.image,(32*3,32*3))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50,200,50)#50 inicio 200 final | (de 50 em 50)
        self.rect.x = LARGURA - randrange(30,300,90)
    
    def update(self):
        #Posição do campo superior direito do retângulo da sprite
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(50,200,50)
        self.rect.x -= 5

class Chao(pygame.sprite.Sprite):
    def __init__(self,pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32,0),(32,32))
        self.image = pygame.transform.scale(self.image,(32*2,32*2))
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 64 
        self.rect.x = pos_x * 64
    
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -= 5 
        

class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32,0),(32,32))
        self.image = pygame.transform.scale(self.image,(32*2,32*2))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.center = (LARGURA, ALTURA - 64)
        # Mascara de Colisão
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):

        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -= 10


todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)

for i in range(4):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)

for i in range(LARGURA//64+2):
    chao = Chao(i)
    todas_as_sprites.add(chao)

cacto = Cacto()
todas_as_sprites.add(cacto)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(cacto)



#Trocando o ícone da janela do jogo
game_icon = dino.imagens_dinossauro[0]
pygame.display.set_icon(game_icon)

relogio = pygame.time.Clock()

colidiu = False

while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #Caso o dino ainda esta no ar
                if dino.rect.y != dino.posicao_y_inicial:
                    #O pass significa não faça nada
                    pass
                else:
                    dino.pular()
    colisoes = pygame.sprite.spritecollide(dino,grupo_obstaculos,False,pygame.sprite.collide_mask)
    
    todas_as_sprites.draw(tela)

    #Pausando o jogo caso ocorra uma colisão
    if colisoes and colidiu == False:
        dino.colisao()
        colidiu = True
    if colidiu:
        pass
    else:
        todas_as_sprites.update()

    pygame.display.flip()
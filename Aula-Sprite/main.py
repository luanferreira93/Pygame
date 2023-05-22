import pygame,sys
from pygame.locals import *


pygame.init()

largura = 640

altura = 480

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Sprites')

# Esta herdando os métodos e atributos da classe Sprite do pygame
class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        # inicializando a classe herdada
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('assets/img/sprite-frog/attack_1.png'))
        self.sprites.append(pygame.image.load('assets/img/sprite-frog/attack_2.png'))
        self.sprites.append(pygame.image.load('assets/img/sprite-frog/attack_3.png'))
        self.sprites.append(pygame.image.load('assets/img/sprite-frog/attack_4.png'))
        self.sprites.append(pygame.image.load('assets/img/sprite-frog/attack_5.png'))
        self.sprites.append(pygame.image.load('assets/img/sprite-frog/attack_6.png'))
        self.sprites.append(pygame.image.load('assets/img/sprite-frog/attack_7.png'))
        self.sprites.append(pygame.image.load('assets/img/sprite-frog/attack_8.png'))
        self.sprites.append(pygame.image.load('assets/img/sprite-frog/attack_9.png'))
        self.sprites.append(pygame.image.load('assets/img/sprite-frog/attack_10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(128*3,64*3))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100,100
        self.animar = False
    
    def update(self):
        if self.animar:
            self.atual = self.atual + 0.15
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image,(128*3,64*3))
    
    def atacar(self):
        self.animar = True

todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)

relogio = pygame.time.Clock()


while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sapo.atacar()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    #usar flip ao invés do update
    pygame.display.flip()
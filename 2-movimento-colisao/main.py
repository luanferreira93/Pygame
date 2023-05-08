import sys , pygame, random

pygame.init()

largura = 640

altura = 480

x = largura/2 - 32

y = altura/2 - 32

fonte = pygame.font.SysFont('ariel',40,True,True)

pontos = 0

random_x = random.randint(50,600)
random_y = random.randint(50,400)

tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption('Joguinho')

relogio = pygame.time.Clock()


while True:
    relogio.tick(60)
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem,True,(255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pygame.key.get_pressed()[pygame.K_d]:
        x += 6
    if pygame.key.get_pressed()[pygame.K_a]:
        x -= 6
    if pygame.key.get_pressed()[pygame.K_w]:
        y -= 6
    if pygame.key.get_pressed()[pygame.K_s]:
        y += 6

  
    tela.fill((0,0,0))

    quadrado_branco = pygame.draw.rect(tela,(255,0,0),(random_x,random_y,40,40))
    quadrado_vermelho = pygame.draw.rect(tela,(0,0,255),(x,y,40,40))
    
    if quadrado_vermelho.colliderect(quadrado_branco):
        random_x = random.randint(50,600)
        random_y = random.randint(50,400)
        pontos = pontos + 1

    tela.blit(texto_formatado,(480,20))
    pygame.display.update()
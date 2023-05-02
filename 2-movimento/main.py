import sys , pygame

pygame.init()

largura = 640

altura = 480

x = largura/2 - 32

y = altura/2 - 32

tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption('Joguinho')

relogio = pygame.time.Clock()


while True:
    relogio.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_d:
        #         x += 6
        #     if event.key == pygame.K_a:
        #         x -= 6
        #     if event.key == pygame.K_w:
        #         y -= 6
        #     if event.key == pygame.K_s:
        #         y += 6
            

    if pygame.key.get_pressed()[pygame.K_d]:
        x += 6
    if pygame.key.get_pressed()[pygame.K_a]:
        x -= 6
    if pygame.key.get_pressed()[pygame.K_w]:
        y -= 6
    if pygame.key.get_pressed()[pygame.K_s]:
        y += 6

  
    tela.fill((0,0,0))

    pygame.draw.rect(tela,(255,255,255),(100,100,40,40))
    pygame.draw.rect(tela,(255,0,0),(x,y,40,40))
    pygame.display.update()
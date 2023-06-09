import sys , pygame, random

pygame.init()

largura = 640
altura = 480

x_cobra = int(largura/2 - 32)
y_cobra = int(altura/2 - 32)

x_moeda = random.randint(50,600)
y_moeda = random.randint(50,400)

velocidade_cobra = 6

X_controle = velocidade_cobra
y_controle = 0


tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption('Snake Game')

relogio = pygame.time.Clock()

lista_cobra = []

comprimento_inicial = 0

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        x = XeY[0]
        y = XeY[1]
        pygame.draw.rect(tela,(0,255,0),(x,y,25,25))
        


while True:
    relogio.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                X_controle = velocidade_cobra
                y_controle = 0
            if event.key == pygame.K_a:
                X_controle = -velocidade_cobra
                y_controle = 0
            if event.key == pygame.K_w:
                y_controle = -velocidade_cobra
                X_controle = 0
            if event.key == pygame.K_s:
                y_controle = velocidade_cobra
                X_controle = 0

                
    x_cobra = x_cobra + X_controle
    y_cobra = y_cobra + y_controle

  
    tela.fill((0,0,0))

    moeda = pygame.draw.circle(tela,(255,215,0),(x_moeda,y_moeda),8)
    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,25,25))

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)


    if moeda.colliderect(cobra):
        x_moeda = random.randint(50,600)
        y_moeda = random.randint(50,400)

        comprimento_inicial = comprimento_inicial + 1


    

    
    pygame.display.update()
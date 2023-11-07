# Esimerkki pygame pelin pääsilmukasta
import pygame

# pygame alustus
pygame.init()

# luodaan taustaikkuna, canvas
tausta = pygame.display.set_mode((1280, 720))

# kirjoitetaan otsikkopalkkiin
pygame.display.set_caption("Hoplaa!") 

# 3. ladataan kuvatiedosto
# kuva = pygame.image.load("joku_kuva.png") 

# 3. asetetaan kuvalle piirtopaikka
# yla_oikea = (0,0)

# 2. annetaan neliölle väri 
# nelio_vari = (255,0,0)

# asetetaan pääsilmukan ehtomuuttuja todeksi, että pysytään pelissä
running = True

while running:
    # odotetaan eventtejä
    # pygame.QUIT eventti tulee, kun käyttäjä klikkaa ikkunan oikean yläkulman X 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # peitetään edellisten ruutujen pikselit värillä
    tausta.fill("purple")

    # 3. blit() metodilla kuva näytölle haluttuun paikkaan
    # tausta.blit(kuva, dest = yla_oikea) 

    # 2. piirretään neliö omalla värillään
    # pygame.draw.rect(tausta, nelio_vari, pygame.Rect(30,30,60,60)) 

    # päivitetään muutokset näytölle
    pygame.display.update() 

    # lisää pelilogiikka tähän

pygame.quit()
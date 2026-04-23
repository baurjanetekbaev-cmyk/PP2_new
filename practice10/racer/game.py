import pygame, random, sys

pygame.init()

windowWidth = 400
windowHeight = 600
screen = pygame.display.set_mode((windowWidth, windowHeight))

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

enemySpeed = 3
playerSpeed = 4

enemyCounter = 0
coinCounter = 0

backgroundImage = pygame.image.load("images/street.png")

bigFont = pygame.font.SysFont("Arial", 50)
smallFont = pygame.font.SysFont("Arial", 20)

gameOverText = bigFont.render("GAME OVER", True, red)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/image.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= playerSpeed
        if keys[pygame.K_RIGHT] and self.rect.right < windowWidth:
            self.rect.x += playerSpeed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= playerSpeed
        if keys[pygame.K_DOWN] and self.rect.bottom < windowHeight:
            self.rect.y += playerSpeed


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/image copy.png")
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(40, windowWidth - 40), random.randint(-300, -50))

    def update(self):
        global enemyCounter

        self.rect.y += enemySpeed

        if self.rect.top > windowHeight:
            enemyCounter += 1
            self.respawn()


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("images/images.png"), (30, 30)
        )
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(40, windowWidth - 40), random.randint(-300, -50))

    def update(self):
        self.rect.y += enemySpeed

        if self.rect.top > windowHeight:
            self.respawn()


player = Player()
enemy = Enemy()
coin = Coin()

sprites = pygame.sprite.Group()
sprites.add(player, enemy, coin)

enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(backgroundImage, (0, 0))

    sprites.update()
    sprites.draw(screen)

    # coin collision
    if pygame.sprite.spritecollide(player, coins, True):
        coinCounter += 1
        new_coin = Coin()
        coins.add(new_coin)
        sprites.add(new_coin)

    # enemy collision
    if pygame.sprite.spritecollide(player, enemies, False):
        screen.fill(white)
        screen.blit(gameOverText, (80, 250))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    # UI
    coinText = smallFont.render(f"Coins: {coinCounter}", True, blue)
    enemyText = smallFont.render(f"Cars: {enemyCounter}", True, blue)

    screen.blit(coinText, (250, 10))
    screen.blit(enemyText, (250, 30))

    pygame.display.update()

pygame.quit()
sys.exit()
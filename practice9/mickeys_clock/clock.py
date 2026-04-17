import pygame
import datetime

pygame.init()
isDone = True
white = (255, 255, 255)

screen = pygame.display.set_mode((650, 650))
screen.fill(white)

clock = pygame.image.load("images/mickey.png")
leftArmIMAGE = pygame.image.load("images/image.png")
rightArmIMAGE = pygame.image.load("images/image copy.png")

pygame.display.update()

leftArmAngle = 0
rightArmAngle = 0

rightArmHourImage = pygame.transform.scale(
    rightArmIMAGE, (35, rightArmIMAGE.get_height() // 2 )
)

leftArmSecondImage = pygame.transform.scale(
    leftArmIMAGE,
    (leftArmIMAGE.get_width() // 3, leftArmIMAGE.get_height() // 3)
)

print(datetime.datetime.now())

while isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
            pygame.quit()

    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second

    clock1 = pygame.transform.scale(
        clock, (clock.get_width() // 3, clock.get_height() // 3)
    )
    screen.blit(clock1, (0, 0))

    left = pygame.transform.rotate(leftArmSecondImage, leftArmAngle)
    leftIMAGE = left.get_rect(center=(400, 170))

    right = pygame.transform.rotate(rightArmHourImage, rightArmAngle)
    rightIMAGE = right.get_rect(center=(339, 310))

    screen.blit(left, leftIMAGE.topleft)
    screen.blit(right, rightIMAGE.topleft)

    leftArmAngle = second * (-6)
    rightArmAngle = minute * (-6)

    pygame.display.update()
    pygame.display.flip()
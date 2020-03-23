import os, sys, math, random, pygame
#Mixer handles music implementation into games
from pygame import mixer

def mainGame(shipType):
    # Create game screen(width,height)
    screen = pygame.display.set_mode((800, 600))
    # Background music
    mixer.music.load("GATTACA, OST - Michael Nyman (1997).wav")
    # This plays the music on loop
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("GATTACA, OST - Michael Nyman (1997).wav"))
    #mixer.music.play(-1)
    bg = pygame.image.load("Space_Background.png")
    # Title and icon
    pygame.display.set_caption("Space Gladiators")
    icon = pygame.image.load("Game Icon.png")
    pygame.display.set_icon(icon)
    # These represent the player coordinates
    playerX = 370
    playerY = 480
    playerX_change = 0

    # Enemy
    Enemy1X = []
    Enemy1Y = []
    Enemy1X_change = []
    Enemy1Y_change = []
    num_of_enemies = 10
    Enemy1Img = pygame.image.load("Enemy_1.png")
    Enemy1Img = pygame.transform.scale(Enemy1Img, (64, 64))
    Enemy2Img = pygame.image.load("Enemy_2.png")
    Enemy2Img = pygame.transform.scale(Enemy2Img, (64, 64))
    Enemy3Img = pygame.image.load("Enemy_3.png")
    Enemy3Img = pygame.transform.scale(Enemy3Img, (64, 64))
    Enemy4Img = pygame.image.load("Enemy_4.png")
    Enemy4Img = pygame.transform.scale(Enemy4Img, (64, 64))
    Enemy5Img = pygame.image.load("Enemy_5.png")
    Enemy5Img = pygame.transform.scale(Enemy5Img, (64, 64))
    Enemy6Img = pygame.image.load("Enemy_6.png")
    Enemy7Img = pygame.image.load("Enemy_7.png")
    Enemy8Img = pygame.image.load("Enemy_8.png")
    Enemy9Img = pygame.image.load("Enemy_9.png")
    EnemyImgList1 = [Enemy1Img, Enemy2Img, Enemy3Img, Enemy4Img, Enemy5Img, Enemy6Img, Enemy7Img, Enemy8Img, Enemy9Img]
    EnemyImgList2 = []
    for x in range(num_of_enemies):
        EnemyImgList2.append(random.choice(EnemyImgList1))

    for i in range(num_of_enemies):
        # These represent the enemy coordinates
        EnemyImg = EnemyImgList2[i]
        Enemy1X.append(random.randint(0, 735))
        Enemy1Y.append(random.randint(50, 200))
        Enemy1X_change.append(1.2)
        Enemy1Y_change.append(26)

    #General bullet Type based on the chosen ship
    global bulletImg
    global bulletChange
    # Small Bullet
    small_bulletImg = pygame.image.load("Small bullet.png")
    small_bulletImg = pygame.transform.scale(small_bulletImg, (20, 21))
    small_bullet_change = 3
    # Medium Bullet
    medium_bulletImg = pygame.image.load("Medium bullet.png")
    medium_bulletImg = pygame.transform.scale(medium_bulletImg, (30, 30))
    medium_bullet_change = 2
    # Large Bullet
    large_bulletImg = pygame.image.load("Large bullet.png")
    large_bulletImg = pygame.transform.scale(large_bulletImg, (30, 30))
    large_bullet_change = 1
    bulletX = 0
    bulletY = 480
    # Ready - can't see bullet on the screen
    # Fire - bullet is moving
    bullet_state = "ready"

    #Bullet selection
    if shipType == 1:
        bulletImg = small_bulletImg
        bulletChange = small_bullet_change
    elif shipType == 2:
        bulletImg = medium_bulletImg
        bulletChange = medium_bullet_change
    elif shipType == 3:
        bulletImg = large_bulletImg
        bulletChange = large_bullet_change

    # Player
    if shipType == 1:
        playerImg = pygame.image.load("player_store3.png")
        playerImg = pygame.transform.scale(playerImg, (64, 64))
    elif shipType == 2:
        playerImg = pygame.image.load("player_spacecraft.png")
        playerImg = pygame.transform.scale(playerImg, (64, 64))
    elif shipType == 3:
        playerImg = pygame.image.load("player_store1.png")
        playerImg = pygame.transform.scale(playerImg, (64, 64))

    # Player score
    score_value = 0
    font = pygame.font.Font("freesansbold.ttf", 33)
    textY = 10
    textX = 10


    def showScore(x, y):
        # First we have to render the score text
        score = font.render("Score: " + str(score_value), True, (255, 255, 255))
        # Then we have to blit the score object onto the game screen
        screen.blit(score, (x, y))


    def player(x, y):
        screen.blit(playerImg, (x, y))


    def enemy1(x, y, i):
        screen.blit(EnemyImg, (x, y))


    def bulletFire(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 17, y - 10))

    def isCollision(enemy1X, enemy1Y, BulletX, BulletY):
        distance = math.sqrt(((BulletX - enemy1X) ** 2) + (BulletY - enemy1Y) ** 2)
        if (distance < 35) and bullet_state == "fire":
            return True
        else:
            return False

    def gameOver():
        # Game over text
        for j in range(num_of_enemies):
            Enemy1Y[j] = 2000
        font2 = pygame.font.Font("freesansbold.ttf", 33)
        textY2 = 250
        textX2 = 100
        gameover = font2.render("GAME OVER! Your final score was: " + str(score_value), True, (255, 255, 255))
        screen.blit(gameover, (textX2, textY2))

    # Game Loop
    running = True
    while running:
        # RGB color for the background
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Check if a keystroke is being pressed at all
            if event.type == pygame.KEYDOWN:
                # Checks to see if the keystroke is right or left
                if event.key == pygame.K_LEFT:
                    if shipType == 1:
                        playerX_change = -3
                    elif shipType == 2:
                        playerX_change = -2
                    elif shipType == 3:
                        playerX_change = -1
                if event.key == pygame.K_RIGHT:
                    if shipType == 1:
                        playerX_change = 3
                    elif shipType == 2:
                        playerX_change = 2
                    elif shipType == 3:
                        playerX_change = 1
                # Ensuring that both the space bar is clicked and the state is ready. Only then can a new bullet be fired at
                # a time
                if (event.key == pygame.K_SPACE) and bullet_state == "ready":
                    # Gunshot music
                    if (bullet_state == "ready"):
                        mixer.music.load("Gunshot.mp3")
                        mixer.music.play()
                    bullet_state = "fire"
                    # This saves the bulletX position at the moment in time where the player position was at the time of
                    # firing the bullet. This makes sure the bullet stays in one x position when travelling upwards instead
                    # of following the player when it moves after shooting
                    bulletX = playerX
                    bulletFire(bulletX, bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change
        # Setting boundaries so that the spaceship does not leave the map
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy version
        for i in range(num_of_enemies):
            Enemy1X[i] += Enemy1X_change[i]
            # Setting boundaries so that the spaceship does not leave the map
            if Enemy1X[i] <= 0:
                Enemy1X_change[i] = 1.2
                Enemy1Y[i] += Enemy1Y_change[i]
            elif Enemy1X[i] >= 736:
                Enemy1X_change[i] = -1.2
                Enemy1Y[i] += Enemy1Y_change[i]
            #GAMEOVER CONDITION
            if Enemy1Y[i] >= 410:
                gameOver()
            # Bullet collision with enemy
            collision = isCollision(Enemy1X[i], Enemy1Y[i], bulletX, bulletY)
            if collision:
                bullet_state = "ready"
                bulletY = 480
                score_value += 1
                Enemy1X[i] = random.randint(1, 735)
                Enemy1Y[i] = random.randint(50, 200)
            enemy1(Enemy1X[i], Enemy1Y[i], i)

        # Bullet movement
        if bulletY <= 0:
            #Resets the bullet to original position if it hits the top of the screen
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            bulletFire(bulletX, bulletY)
            # This is so that the bullet actually moves upward by the amount we specified (The vertical axis value decreases
            # As the bullet goes upward so we subtract the change from the original position)
            bulletY -= bulletChange

        # We call the player method after the fill method so that the player sprite gets drawn onto the screen and not under
        # it
        player(playerX, playerY)
        ##This is also vital as it allows the background to stay the color that we set it
        showScore(textX, textY)
        pygame.display.update()






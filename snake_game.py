import pygame,sys
import time
import random

pygame.init()

cyan = (0,255,255)
pinkish = (242, 7, 109)
gold = (235, 171, 52)
window_width = 1000
window_height = 700
score=0

gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Slither')

'''in-built function for clock to keep track of time'''
clock = pygame.time.Clock()
FPS = 10#refresh rate
blockSize = 20
noPixel = 0

def myQuit():
    '''handling event especially quitting'''
    pygame.quit()
    sys.exit(0)	

font = pygame.font.SysFont(None, 25, italic=True)

def drawGrid():
	sizeGrd = window_width // blockSize
	
def snake(blockSize, snakelist):
    #x = 250 - (segment_width + segment_margin) * i
    for size in snakelist:
        pygame.draw.rect(gameDisplay,pinkish,[size[0]+5,size[1],blockSize,blockSize],4)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width/4, window_height/5])    

def message_to_screen1(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width/4, window_height/4])    

def gameLoop():
    global score
    gameExit = False #has another life to quit or not
    gameOver = False #press q and quit

    lead_x = window_width/2
    lead_y = window_height/2

    change_pixels_of_x = 0
    change_pixels_of_y = 0

    snakelist = []
    snakeLength = 1

    randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
    randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0

    '''gameloop begins'''
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(cyan)
            message_to_screen("Your score is "+str(score),gold)
            message_to_screen1(":( GAMEOVER  press c-->Play Again or Q-->quit",gold)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:#quit
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:#continue
                        gameLoop()

        '''logic 1-->handling events setting or checking the values of x and y''' 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myQuit()
                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN
                if leftArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel
                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel
                elif upArrow:
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = noPixel
                elif downArrow:
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = noPixel

            '''logic 2-->check for the boundary exit'''
            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True
        
        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y
        gameDisplay.fill(cyan)
        AppleThickness = 20

        '''logic 3-->Apple creation at random position'''
        print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
        pygame.draw.rect(gameDisplay, gold, [randomAppleX,randomAppleY,AppleThickness,AppleThickness])

        allspriteslist = []
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)
        
        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist [:-1]:
            if eachSegment == allspriteslist:
                gameOver = True

        '''logic 4-->drawing snake after eating and updating'''        
        snake(blockSize, snakelist)
        pygame.display.update()

        '''logic 5-->snake hitting apple'''
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
                randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0
                snakeLength += 1
                score+=1
        clock.tick(FPS)      
    quit()
gameLoop()


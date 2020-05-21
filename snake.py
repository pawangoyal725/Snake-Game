import pygame
import random
import os
pygame.init()


#------------Background Music
pygame.mixer.init()

#------------Colours--(red,green,blue)
white= (255,255,255)
red= (255,0,0)
green= (0,190,0)
darkgreen= (0,101,51)
black= (0,0,0)
darkred= (161,4,4)
#------------Creating Window
screen_width= 800
screen_height= 500
game_window= pygame.display.set_mode((screen_width,screen_height))

#------------Background Image's
bgimg= pygame.image.load("Snake_welcome.jpg")
bgimg= pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
#------------
gameimg= pygame.image.load("Background.jpg")
gameimg= pygame.transform.scale(gameimg,(screen_width,screen_height)).convert_alpha()
#------------
gameoverimg= pygame.image.load("Game_over.jpg")
gameoverimg= pygame.transform.scale(gameoverimg,(screen_width,screen_height)).convert_alpha()

#-------------Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()

#------Creating Snake Function
def plot_snake(game_window, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window, color, (x, y, snake_size, snake_size))

#--------SCORE Board
font= pygame.font.SysFont(None, 50)
def text_screen(text,color,x,y):
    screen_text= font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

clock= pygame.time.Clock()
fps= 30

#----------Welcome Screen
def welcome():
    exit_game= False
    while not exit_game:
        game_window.fill(white)
        game_window.blit(bgimg,(0,0))
        text_screen("------------Welcome To Snakes World------------",darkred,50,100)
        text_screen("Press Space-Bar To Play",darkred,200,340)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("Back.mp3")
                    pygame.mixer.music.play(-1)
                    game_loop()
                    
        pygame.display.update()
        clock.tick(fps)

#--------------Game Loop
def game_loop():
    #-------------Game Variable
    exit_game= False
    game_over= False
    snake_x= 55
    snake_y= 55
    snake_size= 15
    velocity_x= 0   #------Speed variable for x
    velocity_y= 0   #------Speed variable for y
    food_x= random.randint(10,screen_width/2)    #-------Snake Food Position
    food_y= random.randint(10,screen_height/2)   #-------Snake Food Position
    score= 0

    snk_list= []
    snk_length= 1

    if (not os.path.exists("Hi-score.txt")):
        with open("Hi-score.txt","w") as f:
            f.write("0")
    with open("Hi-score.txt","r") as f:
        Hi_score= f.read()

    while not exit_game:
        if game_over:
            with open("Hi-score.txt","w") as f:
                f.write(str(Hi_score))

            game_window.fill(white)
            game_window.blit(gameoverimg,(0,0))
            text_screen("Your Hi-Score is "+ Hi_score ,darkred,250,100)
            text_screen("Press Enter To Continue!",green,200,300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game= True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game= True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 7
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - 7
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - 7
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 7
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score = score + 10


            snake_x= snake_x + velocity_x
            snake_y= snake_y + velocity_y
            
            if abs(snake_x-food_x) < 7 and abs(snake_y-food_y) < 7 :
                score += 10
                food_x= random.randint(10,screen_width/2)
                food_y= random.randint(10,screen_height/2)
                snk_length += 2

                if score>int(Hi_score):
                    Hi_score = score

            head= []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]


            game_window.fill(white)
            game_window.blit(gameimg,(0,0))
            text_screen("SCORE:- "+ str(score) +"  Hi-Score:- " + str(Hi_score),darkred,5,5)          #--------Score Board Function Calling
            pygame.draw.rect(game_window, red, (food_x, food_y, snake_size, snake_size))  #------Creating Snake Food

            if head in snk_list[:-1]:
                game_over= True
                pygame.mixer.music.load("End.mp3")
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("End.mp3")
                pygame.mixer.music.play()


            plot_snake(game_window, darkgreen, snk_list, snake_size)        #------Creating Snake using function calling
        pygame.display.update()
        clock.tick(fps)
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    pygame.quit()
    quit()
#-------------------------------------------------------------------------------------------------------------------------------------
welcome()
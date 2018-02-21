import pygame
import time
import random

pygame.init()
x=0
snake = []
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
global direction
gamedisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('smack')
img = pygame.image.load('snake.png')
##img='right'
##if img == 'right' :
##   pygame.transform.rotate(img,270)
direction = "up"

font = pygame.font.SysFont(None,25)
def snake(block_size,snakelist):
    if direction == "up":
        head = pygame.transform.rotate(img,0)
    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "down":
        head = pygame.transform.rotate(img,180)
    if direction == "left":
        head = pygame.transform.rotate(img,90)
    gamedisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))

    for XnY in snakelist[:-1]:
        pygame.draw.rect(gamedisplay, green, [XnY[0],XnY[1],block_size,block_size])
def text_objects(text,color):
    textsurface = font.render(text, true, color)
    return textsurface, textsurface.get_rect()

def score(x):
    text = font.render("score:"+str(x),True ,green)
    gamedisplay.blit(text,[0,0])



def msg_to_screen(msg,color):
##    screen_text = font.render(msg, True, color)
##    gamedisplay.blit(screen_text, [300,300])
      textsurf, textrect = text_object(msg,color)
      textrect.center = (400,300)
      gamedisplay.blit(textsurf, textrect)
def msg_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gamedisplay.blit(screen_text, [random.randrange(100,500),random.randrange(100,500)])    

lead_x=300
lead_y=300
snakelist = []
snakelength = 1
lead_x_change = 0
lead_y_change = 0
blocksize = 10
block_size = 10
block_size_x = 10
gameExit = False
randappleX = round(random.randrange(0,800-blocksize)/10.0)*10.0
randappleY = round(random.randrange(0,600-blocksize)/10.0)*10.0
while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               direction = "left"
               lead_x_change = -10
               lead_y_change = 0 
            elif event.key == pygame.K_RIGHT:
               direction = "right"
               lead_x_change = 10
               lead_y_change = 0 
            elif event.key == pygame.K_UP:
               direction = "up"
               lead_y_change = -10
               lead_x_change = 0 
            elif event.key == pygame.K_DOWN:
               direction = "down"
               lead_y_change = 10
               lead_x_change = 0
            
        if lead_x<0 or lead_y<0 or lead_x>=800 or lead_y>=600:
            gameExit = True
    lead_x += lead_x_change
    lead_y += lead_y_change
    gamedisplay.fill(white)
    pygame.draw.rect(gamedisplay,red ,[randappleX,randappleY,blocksize,blocksize])

    score(snakelength)
    
    snakehead = []
    snakehead.append(lead_x)
    snakehead.append(lead_y)
    snakelist.append(snakehead)
    if len(snakelist) > snakelength:
       del snakelist[0]
    for eachsegment in snakelist[:-1]:
        if eachsegment == snakehead:
            gameExit = True
    snake(block_size,snakelist)

    snake(block_size,snakelist)  
    if lead_x == randappleX and lead_y == randappleY:          
       randappleX = round(random.randrange(0,800-blocksize)/10.0)*10.0
       randappleY = round(random.randrange(0,600-blocksize)/10.0)*10.0
       snakelength += 10
       x=x+1
    pygame.display.update()
    clock.tick(30)

msg_to_screen("you lose, go home piece of shit", black)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()


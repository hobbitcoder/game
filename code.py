import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500,400))
clock = pygame.time.Clock()
random_pos_y = [random.randint(25,200),random.randint(210,400),random.randint(0,400)]
random_pos_x = [random.randint(410,450)]
game_state = "game over"
level = "level 1"
score = 0
game_over_message = "start"

#book
book_surf = pygame.surface.Surface((25,60)).convert_alpha()
book_surf.fill((200,0,0))
book_rect = book_surf.get_rect(midtop = (30,70))
book_gravity = 10
speedy = 4  
#font
def display_score(scor):
  font = pygame.font.Font('rawline.ttf',25)
  score_surf = font.render(str(score),True,(255,255,0))
  score_rect = score_surf.get_rect(midbottom = (250,25))
  screen.blit(score_surf,score_rect)

#backround
backround = pygame.surface.Surface((500,400)).convert()     

#arrows
class arrow:
  def __init__(self,pos_y,pos_x):
    self.speed = 4
    self.surf = pygame.surface.Surface((75,25))
    self.surf.fill(("Green"))
    self.rect = self.surf.get_rect(bottomleft = (pos_x,pos_y))
    pygame.draw.rect(screen,(255,215,0),self.rect,5)
    
  def get_arrow_number(self):
    if self.rect.y >= 25 and self.rect.y <= 200:
      self.arrow_number = 0
    
    elif self.rect.y >= 210 and self.rect.y <= 400:
      self.arrow_number = 1
    else:
      self.arrow_number = 2
    return self.arrow_number
    
  def reset_pos(self,arrow_number):
    if arrow_number == 0:
      self.rect.bottomleft = (random.randint(410,450),random.randint(30,200))
    elif arrow_number ==1:
      self.rect.bottomleft = (random.randint(410,450),random.randint(210,400))
    elif arrow_number == 2: 
      self.rect.bottomleft = (random.randint(410,450),random.randint(30,400))


arrow1 = arrow(random_pos_y[0],random_pos_x[0])
arrow1_arrow_num = arrow1.get_arrow_number()

arrow2 = arrow(random_pos_y[1],random_pos_x[0])
arrow2_arrownum = arrow2.get_arrow_number()

arrow3 = arrow(random_pos_y[2],random_pos_x[0])
arrow3_arrownum = arrow3.get_arrow_number()

def game_over(score,message):
  
  backround = pygame.image.load("waterfall.png")
  score_font = pygame.font.Font("rawline.ttf",35)
  restart = pygame.font.Font("rawline.ttf",17)
  
  if message == "restart":
    restart = restart.render("press enter to restart",True,(0,255,0))
    message = "restart"
  elif message == "start":
    
    restart = restart.render("press enter to start",True,(0,255,0))
  restart_rect = restart.get_rect(midbottom = (250,200))
  
  score_surf = score_font.render("score = " + str(score),True,(0,255,0))
  score_rect = score_surf.get_rect(midbottom = (250,140))
  
  screen.blit(backround,(0,0))
  pygame.draw.rect(screen,(0,0,0),(120,80,250,250),0,50)
  screen.blit(score_surf,score_rect)
  screen.blit(restart,restart_rect)
while  True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if game_state == "game running":    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
          book_gravity = -10
    if game_state == "game over":
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          book_rect.midtop = (30,70)
          arrow1.reset_pos(0)
          arrow2.reset_pos(1)
          arrow3.reset_pos(2)
          score = 0  
          level = "level 1"
          game_state = "game running"
        
  if game_state == "game running":
    
    score =+ score
    
    book_rect.y += book_gravity
    arrow1.rect.x -= arrow1.speed
    arrow2.rect.x -= arrow2.speed
    book_gravity += 1 
    screen.blit(backround,(0,0))
    
    if level == "level 2" :
      screen.blit(arrow3.surf,arrow3.rect)
      arrow3.rect.x -= arrow3.speed
      
    screen.blit(arrow1.surf,arrow1.rect)
    screen.blit(arrow2.surf,arrow2.rect)
    display_score(score)
    pygame.draw.rect(screen,(255,0,0),book_rect,0,7)
    # resets the arrows pos
    if arrow1.rect.right <= 0 :
      score += 1
      arrow1.reset_pos(arrow1_arrow_num)
    
    if arrow2.rect.right <= 0 :
      score += 1
      arrow2.reset_pos(arrow2_arrownum)
    
    if level == "level 2" and arrow3.rect.right <= 0 :
      score += 1
      arrow3.reset_pos(arrow3_arrownum)
    # makes book bounce  
    if book_gravity >= 10:
      book_gravity = 10
    #stops the book from going of the screeen
    if book_rect.bottom >= 390:
      book_rect.bottom = 390
    if book_rect.top <= 7:
      book_rect.top = 7 
    # changes level
    if score >= 20:
      level = "level 2"
    # checks if the arrows collide with the book
    if  book_rect.colliderect(arrow1.rect) or book_rect.colliderect(arrow2.rect):
      game_state = "game over"
    if level == "level 2":
      if book_rect.colliderect(arrow3.rect):
        game_state = "game over"
    # keeps the game_over_message at "restart" when the game is running
    game_over_message = "restart"
  #game over state
  if game_state == "game over":
    game_over(score,game_over_message)
  
  pygame.display.update()
  clock.tick(60)  

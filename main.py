import pygame
import os
import math
import random

pygame.init()
WIDTH,HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("WELCOME TO HANGMAN")

Radius = 20
Gap = 15
letters=[]
start_x= round((WIDTH - (Radius * 2 + Gap) * 13) / 2)
start_y= 400
A = 65

for i in range(26):
  x = start_x + Gap * 2 + ((Radius * 2 + Gap) * (i % 13))
  y = start_y + ((i//13) * (Gap + Radius * 2))
  letters.append([x,y, chr(A + i), True])
  

Letter_Font = pygame.font.SysFont('timesnewroman',25)
Word_Font = pygame.font.SysFont('timesnewroman',40)
Title_Font = pygame.font.SysFont('timesnewroman',45)
Trophy = pygame.image.load("Trophy.png")
Cry = pygame.image.load("Cry.png")
images=[]
for i in range (7): 
  image=pygame.image.load("Hangman "+str(i)+".png")
  images.append(image)

hangman_status = 0
words = ["DEVELOPER","HANGMAN","MALDIVES","STUDENT","CODING"]
word = random.choice(words)
guessed = []

WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
  win.fill(WHITE)
  text = Title_Font.render("HANGMAN GAME",1,BLACK)
  win.blit(text, (WIDTH/2 - text.get_width()/2,20))
  
  display_word = ""
  for letter in word:
    if letter in guessed:
      display_word += letter + " "
    else:
      display_word += "_ "
  text = Word_Font.render(display_word, 1, BLACK)
  win.blit(text,(400, 200))
      
  for letter in letters:
    x,y, ltr,visible=letter
    if visible:
     pygame.draw.circle(win, BLACK,(x,y), Radius, 2)
     text = Letter_Font.render(ltr,1,BLACK)
     win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
  win.blit(images[hangman_status],(150,100))
  pygame.display.update()

def display_message(message):
  pygame.time.delay(900)
  win.fill(WHITE)
  win.blit(Trophy,(300,260))
  text = Word_Font.render(message, 1, BLACK)
  win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 -text.get_height()/2))
  pygame.display.update()
  pygame.time.delay(2500)

def display_messagelost(message):
  pygame.time.delay(900)
  win.fill(WHITE)
  win.blit(Cry,(300,270))
  text = Word_Font.render(message, 1, BLACK)
  win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 -text.get_height()/2))
  pygame.display.update()
  pygame.time.delay(2500)


  

while run:
  clock.tick(FPS)
  
  draw()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      m_x,m_y = pygame.mouse.get_pos()
      for letter in letters:
        x,y,ltr,visible = letter
        if visible:
         dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
         if dis < Radius:
          letter[3] = False
          guessed.append(ltr)
          if ltr not in word:
            hangman_status += 1
  draw()
  won = True
  for letter in word:
    if letter not in guessed:
      won = False
      break

  if won:
    display_message("Congratulations, you WON!")
    pygame.display.update()
    break
  if hangman_status == 6:
    display_messagelost("Sorry, you LOST!")
    display_messagelost("The correct word was " + word)
    break
pygame.quit()

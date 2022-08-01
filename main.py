
import pygame as pg
import time, math



# Pygame Initialization
pg.init()
pg.font.init()

screen = pg.display.set_mode([500,500])
clock = pg.time.Clock()

my_font = pg.font.SysFont('Comic Sans MS', 30)
pg.display.set_caption('Bitches Locator 3000')

# Variables
angle = 270
leng = 150
x = leng * math.sin(math.radians(angle))
y = leng * math.sin(math.radians(90 - angle))

def pos():
    global x, y
    x = leng * math.sin(math.radians(angle))    
    y = leng * math.sin(math.radians(90 - angle))

    # print(f"""X sine: {x}\nY sine: {y} \n""")
    
def tick():
    global angle
    angle += 0.50
    if (angle > 360.00):
        angle = angle - 360
    pos()

paused = False
running = True
while running:

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_b:
                print("Pause begun.")
                time.sleep(5)
                print("Pause ended.")

                
    screen.fill(("gray"))
   

    # Program info
    text_surface = my_font.render('Locating Bitches', False, (0, 0, 0))
    screen.blit(text_surface, (140,50))

    # Radar itself
    pg.draw.circle(screen, (0,153,5), (250,250), 150)
    pg.draw.line(screen, 'black',(100,250), (400,250),2)
    pg.draw.line(screen, 'black',(250,100), (250,400),2)
    pg.draw.circle(screen, "Black", (250,250), 150, 2)
    pg.draw.circle(screen, "Black", (250,250), 100, 2)
    pg.draw.circle(screen, "Black", (250,250), 50, 2)
    pg.draw.circle(screen, "Black", (250,250), 20, 2)

    # Debug mode keep commented out
    pg.draw.circle(screen, 'Green',(250, x + 250), 10 )
    pg.draw.circle(screen, 'Green',(y + 250, 250), 10)
    pg.draw.circle(screen, 'Green',(y + 250, x + 250), 10)
    
    # Radar hand
    pg.draw.line(screen, 'Green',(250, 250), (y + 250, x + 250),5)
    tick()

    # Flip the display
    pg.display.flip()
    clock.tick(90)

import pygame as pg
import time, math


#######################################################
# PyGame Initialization
#######################################################
pg.init()
# module for fonts
pg.font.init()
# module for loading and playing sounds & music
pg.mixer.init()
screen = pg.display.set_mode([500,500])
clock = pg.time.Clock()


# Variables
angle = 270
leng = 150
x = leng * math.sin(math.radians(angle))
y = leng * math.sin(math.radians(90 - angle))

def pos():
    global x, y
    x = leng * math.sin(math.radians(angle))    
    y = leng * math.sin(math.radians(90 - angle))
    print(f"""X sine: {x}\n Y sine: {y} \n""")
    
def tick():
    global angle
    angle += 0.06
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
                time.sleep(5)
                print("KOKOT")

                
    screen.fill((255, 255, 255))
    

    pg.draw.circle(screen, 'Green',(150, x + 150), 10 )
    pg.draw.circle(screen, 'Green',(y + 150, 150), 10)
    pg.draw.circle(screen, 'Green',(y + 150, x + 150), 10)
    pg.draw.line(screen, 'Green',(150, 150), (y + 150, x + 150))
    tick()

    # Flip the display
    pg.display.flip()
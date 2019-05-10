#Dean Church
#asteroids
#rev
#add ship to screen
#rev
#add thrust and screenwrapping
#sound does not work



#get the asteroids moving on screen




#imports
from superwires import games
import random
import math

games.init(screen_width = 640, screen_height = 480, fps = 60)

#global variables





#classes

class Asteroid(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("sprites/asteroid3.png"),
              MEDIUM : games.load_image("sprites/asteroid2.png"),
              LARGE : games.load_image("sprites/asteroid1.png")}
    
    SPEED = 2

    def __init__(self,x,y,size):
        super(Asteroid, self).__init__(
            image = Asteroid.images[size],
            x=x,
            y=y,
            dx = random.choice([1, -1])*Asteroid.SPEED*random.random()/size,
            dy = random.choice([1, -1])*Asteroid.SPEED*random.random()/size)
        self.size = size

    def update(self):
        if self.left > games.screen.width:
            self.right = 0
            
        if self.right < 0:
            self.left = games.screen.width
            
        if self.top > games.screen.height:
            self.bottom = 0
            
        if self.bottom < 0:
            self.top = games.screen.height
            


class Ship(games.Sprite):
    image = games.load_image("sprites/spaceship.png")
    #sound = games.load_sound("sounds/soundfx/thrust.bfxrsound")
    
    ROTATION_STEP = 8
    VELOCITY_STEP = .03
    
    def update(self):
        #key setup
        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
            
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle -= Ship.ROTATION_STEP

        #apply thrust
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            #Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
        #Wrapping screen
        if self.left > games.screen.width:
            self.right = 0
            
        if self.right < 0:
            self.left = games.screen.width
            
        if self.top > games.screen.height:
            self.bottom = 0
            
        if self.bottom < 0:
            self.top = games.screen.height

class Missile(games.Sprite):
    pass

class Explosion(games.Sprite):
    pass







#main
def main():
    #loading data
    bg_img = games.load_image("sprites/background.png", transparent = False)




    #create objects
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x=x, y=y, size=size)
        games.screen.add(new_asteroid)

    player = Ship(image = Ship.image,
                  x = games.screen.width/2,
                  y = games.screen.height/2)

    #draw to screen
    games.screen.background = bg_img
    games.screen.add(player)





    #set up game






    #start mainloop
    games.screen.mainloop()





main()













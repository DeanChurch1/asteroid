#Dean Church
#asteroids
#rev
#add ship to screen
#rev
#add thrust and screenwrapping
#rev
#add laser and laser sound


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
    sound = games.load_sound("sounds/soundfx/explosion.wav")
    
    ROTATION_STEP = 8
    VELOCITY_STEP = .03
    
    def update(self):
        #key setup
        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
            
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP

        if games.keyboard.is_pressed(games.K_t):
            Ship.sound.play()
        
        #apply thrust
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
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

        #fire missile
        if games.keyboard.is_pressed(games.K_SPACE):
            Missile.sound.play()
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)

class Missile(games.Sprite):
    image = games.load_image("sprites/projectile.png")
    sound = games.load_sound("sounds/soundfx/laser.wav")
    BUFFER = 5
    VELOCITY_FACTOR = 7
    LIFETIME = 40
    def __init__(self, ship_x, ship_y, ship_angle):
        Missile.sound.play()
        angle = ship_angle * math.pi/180
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * math.sin(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y

        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        super(Missile, self).__init__(image = Missile.image,
                                      x = x, y = y,
                                      dx = dx, dy = dy)
        self.lifetime = Missile.LIFETIME
    def update(self):
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

        #wrap laser
        if self.left > games.screen.width:
            self.right = 0
            
        if self.right < 0:
            self.left = games.screen.width
            
        if self.top > games.screen.height:
            self.bottom = 0
            
        if self.bottom < 0:
            self.top = games.screen.height
    

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

    shot = Missile(200,200,0)

    #draw to screen
    games.screen.background = bg_img
    games.screen.add(player)
    games.screen.add(shot)




    #set up game






    #start mainloop
    games.screen.mainloop()





main()













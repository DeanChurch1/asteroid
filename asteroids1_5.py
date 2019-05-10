#Dean Church
#asteroids
#rev
#add ship to screen
#rev
#add thrust and screenwrapping
#rev
#add laser and laser sound
#rev
#fixing fire rate
#rev
#adding collision detection
#rev
#adding explosions



#get the asteroids moving on screen




#imports
from superwires import games
import random
import math

games.init(screen_width = 640, screen_height = 480, fps = 60)

#global variables





#classes

class Wrapper(games.Sprite):
    def update(self):
        """Wrap around screen"""
        if self.left > games.screen.width:
            self.right = 0
                
        if self.right < 0:
            self.left = games.screen.width
                
        if self.top > games.screen.height:
                self.bottom = 0
                
        if self.bottom < 0:
            self.top = games.screen.height

        def die(self):
            """Destroy the missile"""
            self.destroy()

class Collider(Wrapper):
    def update(self):
        super(Collider, self).update()
        #Check if overlapping 
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()
            
    def die(self):
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy() 




class Asteroid(Wrapper):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    SPAWN = 2
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


            
    def die(self):
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(x = self.x, y = self.y, size = self.size - 1)
                games.screen.add(new_asteroid)
        super(Asteroid, self)
        


class Ship(Collider):
    image = games.load_image("sprites/spaceship3.png")
    sound = games.load_sound("sounds/soundfx/thrust.wav")
    
    ROTATION_STEP = 6
    VELOCITY_STEP = .03
    MISSILE_DELAY = 20

    def __init__(self, x, y):
        super(Ship, self).__init__(image = Ship.image, x=x, y=y)
        self.missile_wait = 0
    
    def update(self):
        super(Ship, self).update()
        #Missile counter
        if self.missile_wait > 0:
            self.missile_wait -= 1

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
        

        #fire missile
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait <= 0:
            Missile.sound.play()
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

       

class Missile(Collider):
    image = games.load_image("sprites/projectile.png")
    sound = games.load_sound("sounds/soundfx/laser.wav")
    BUFFER = 200
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
        super(Missile, self).update()
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

             

class Explosion(games.Animation):
    sound = games.load_sound("sounds/soundfx/explosion.wav")
    images = ["sprites/explosion1.png",
              "sprites/explosion2.png",
              "sprites/explosion3.png",
              "sprites/explosion4.png",
              "sprites/explosion5.png",
              "sprites/explosion6.png",
              "sprites/explosion7.png",
              "sprites/explosion8.png",
              "sprites/explosion9.png"]
    def __init__(self,x,y):
        super(Explosion,self).__init__(images = Explosion.images,
                                       x = x, y = y,
                                       repeat_interval = 4, n_repeats = 1,
                                       is_collideable = False)
        Explosion.sound.play()
              


#main
def main():
    #loading data
    bg_img = games.load_image("sprites/background.png", transparent = False)




    #create objects
    for i in range(1):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x=x, y=y, size=size)
        games.screen.add(new_asteroid)

    player = Ship(x = games.screen.width/2, y = games.screen.height/2)


    #draw to screen
    games.screen.background = bg_img
    games.screen.add(player)





    #set up game

    #start mainloop
    games.screen.mainloop()

main()

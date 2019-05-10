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
#rev notes
#Major overhaul
#final rev



#get the asteroids moving on screen


#imports
from superwires import games, color
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
    POINTS = 30
    images = {SMALL : games.load_image("sprites/asteroid3.png"),
              MEDIUM : games.load_image("sprites/asteroid2.png"),
              LARGE : games.load_image("sprites/asteroid1.png")}
    
    SPEED = 2

    total = 0

    def __init__(self,game,x,y,size):
        Asteroid.total += 1
        super(Asteroid, self).__init__(
            image = Asteroid.images[size],
            x=x,
            y=y,
            dx = random.choice([1, -1])*Asteroid.SPEED*random.random()/size,
            dy = random.choice([1, -1])*Asteroid.SPEED*random.random()/size)
        self.size = size
        self.game = game 


            
    def die(self):
        Asteroid.total -= 1
        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10

        
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game = self.game,
                                        x = self.x
                                        , y = self.y,
                                        size = self.size - 1)
                games.screen.add(new_asteroid)
        #advance
        if Asteroid.total == 0:
            self.game.advance()
            
        super(Asteroid, self).die()
        


class Ship(Collider):
    image = games.load_image("sprites/spaceship3.png")
    sound = games.load_sound("sounds/soundfx/thrust.wav")
    
    ROTATION_STEP = 6
    VELOCITY_STEP = .03
    MISSILE_DELAY = 20
    VELOCITY_MAX = 3

    def __init__(self,game, x, y):
        super(Ship, self).__init__(image = Ship.image, x=x, y=y)
        self.missile_wait = 0
        self.game = game

    def die():
        self.game.end()
        super(Ship, self).die()
    
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

            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)

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
              




class Game(object):
    def __init__(self):
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        
        games.screen.add(self.score)
        
        self.sound = games.load_sound("sounds/soundfx/levelup1.wav")
        
        self.level = 0
        
        self.create_ship()


    def create_ship(self):
        self.player = Ship(self,
                           x = games.screen.width/2,
                           y = games.screen.height/2)
        games.screen.add(self.player)
        
    def play(self):
        games.music.load("sounds/theams/Orbit Beat 130.wav")
        games.music.play(-1)
        #bg
        bg_img = games.load_image("sprites/background.png")
        games.screen.background = bg_img
        #advance
        self.advance()

        #start game
        games.screen.mainloop()
    
    def advance(self):
        self.level += 1
        BUFFER = 150
        
        for i in range(self.level):
            #calculate new y and y
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min
            #choose distance
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)
            #calculate distance
            x = self.player.x + x_distance
            y = self.player.y + y_distance
            #wrap screen
            x %= games.screen.width
            y %= games.screen.height
            #create asteroid
            new_asteroid = Asteroid(game = self, x=x, y=y, size=Asteroid.LARGE)
            games.screen.add(new_asteroid)
            #display lvl number
            level_message = games.Message(value = "Level" + str(self.level),
                                          size = 40,
                                          color = color.yellow,
                                          x = games.screen.width/2,
                                          y = games.screen.width/10,
                                          lifetime = 3*games.screen.fps,
                                          is_collideable = False)
            games.screen.add(level_message)
            #play new level sound
            if self.level > 1:
                self.sound.play()




    def end(self):
        """End the game"""
        end_message = games.Message(value = "Game Over",
                                          size = 90,
                                          color = color.blue,
                                          x = games.screen.width/2,
                                          y = games.screen.width/2,
                                          lifetime = 5*games.screen.fps,
                                          after_death = games.screen.quit,
                                          is_collideable = False)
        games.screen.add(end_message)

            


#main
def main():
    astrocrash = Game()
    astrocrash.play()
main()


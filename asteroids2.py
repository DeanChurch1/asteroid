#Dean Church
#asteroids




#get the asteroids moving on screen




#imports
from superwires import games
import random

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
    pass

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

    #draw to screen
    games.screen.background = bg_img






    #set up game






    #start mainloop
    games.screen.mainloop()





main()













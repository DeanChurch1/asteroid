from superwires import games

games.init(screen_width = 640, screen_height = 480, fps = 60)

class Ship(games.Sprite):
    ship_img = games.load_image("sprites/spaceship.png", transparent = True)
    def __init__(self,):
        super(Ship,self).__init__(image = Ship.ship_img,
                                  x = games.screen.width/2,
                                  y = games.screen.height/2)
    def update(self):
        """ Move ship with keys"""
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            self.y -= 10

        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 10
            
        if games.keyboard.is_pressed(games.K_s) or games.keyboard.is_pressed(games.K_DOWN):
            self.y += 10
            
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 10
            
        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270
                                
                                
                 
def main():

    #load data
    bg_img = games.load_image("sprites/background.png", transparent = False)
    explosion_files = ["sprites/explosion1.png",
                       "sprites/explosion2.png",
                       "sprites/explosion3.png",
                       "sprites/explosion4.png",
                       "sprites/explosion5.png",
                       "sprites/explosion6.png",
                       "sprites/explosion7.png"]


    #asteroid = games.load_image("sprites/asteroid1.png", transparent = False)                   
    


    #create objects
    player = Ship()
    explosion = games.Animation(images = explosion_files,
                                x = games.screen.width/2,
                                y = games.screen.height/2,
                                n_repeats = 0,
                                repeat_interval = 10,)
                                #transparent = True)

    #draw to screen
    games.screen.background = bg_img
    games.screen.add(player)
    games.screen.add(explosion)
    #games.screen.add(asteroid)


    #game setup



    



    games.screen.mainloop()




main()

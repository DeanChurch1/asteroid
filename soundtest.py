#sound and music
#Demonstrate music

from superwires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)


#load sound fx
shoot = games.load_sound("sounds/soundfx/laser.bxfrsound")
#thrust = games.load_sound("sounds/soundfx/thrust.wav")
#explosion = games.load_sound("sounds/soundfx/meteorexp.wav")
#levelup = games.load_sound("sounds/soundfx/


#load theams

games.music.load("sounds/theams/Orbit Beat 130.wav")


#create menu
choice = None
while choice != "0":
    print(
    """
    Sound and music
    0-quit
    1-play laser
    2-loop laser sound
    3-stop laser sound
    4-play theme music
    5-loop theme music
    6-stop theme music
    """
    )

    choice = input("choice: ")
    print()

    # exit
    if choice == "0":
        print("Goodbye")
    elif choice == "1":
        shoot.play()
        print("Playing missile sound.")
    elif choice == "2":
        loop = int(input("Loop how many extra times? (-1 = forever): "))
        thrust.play(loop)
        print("Looping thrust")
##        while True:
##            shoot.play()
##            choice2 = input("Do you want to quit")
##            if choice2 == "q":
##                break
    elif choice == "3":
        thrust.stop()
        print("stop looping thrust")
    elif choice == "4":
        games.music.play()
        print("Playing theme music.")
    elif choice == "5":
        loop = int(input("loop how many extra times?"))
        games.music.play(loop)
    elif choice == "6":
        games.music.stop()





        
    

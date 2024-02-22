# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kaoru")
define pName = Character("Bunkai")

# The game starts here.

label start:
    play music "audio/Hikari_afurete.mp3"

    # Show a background and character sprites
    scene bg room   
    
#python:

#    $ pName = renpy.input("Write your name and press enter to start the game.", length=10) or "Bunkai"
    $ config.disable_input
    
    # Back to Dialogue
label welcoming:
    scene bg room 
    show eileen happy

    # Dialogue
    
    k "Excuse me! You're [pName], right?"
    
    pName "Hm? Yes, that's me."
    
    k "Welcome to Hokkaido!" 

    k "I am [k], and I'll be your guide around here." 
    
    pName "Pleased to meet you [k]! Thanks for the help." 
    
    k "Happy to do it, he-he." 

    k "We'll make a wonderful story, full of pictures and music." 

    k "By the way, you can share this with the whole world, \nI'm sure they'll like it!" 

# The menu statement lets presents a choice to the player:
menu:

    "Keep going.":
        jump nextPage

    "Finish the trip.":
        jump endGame

label nextPage:
    scene bg room
    show eileen happy at right

    k "Since we are in Location, the first thing we should do is ..."
    
    k "Let's go!"

label endGame:
    scene bg room
    show eileen happy at right
    
    k "Sadly, our trip ends here. I hope you've enjoyed it!"    
    
    # Ends the game.
    return


define player = Character("You")
define bryan = Character("Bryan")
define jade = Character("Jade")

image bg start = im.Scale("start_bg.png", 1920, 1080)
image bg forest = im.Scale("forest_bg.png", 1920, 1080)
image bg ice = im.Scale("ice_bg.png", 1920, 1080)
image bg fire = im.Scale("fire_bg.png", 1920, 1080)

image player = "player.png"
image bryan = "bryan.png"
image jade = "jade.png"

image maze_map = im.Scale("map.jpg", 1420, 700)

image door 1 = im.Scale("1_door.jpg", 1920, 1080)
image door 2 = im.Scale("2_doors.jpg", 1920, 1080)

# The game starts here.

label start:

    scene bg start

    show player with dissolve

    player """
    Where am i?

    I am in the forest?

    What I am doing here?

    Wait!!!!!

    What is this!!!!!

    A HOLE!!!!

    WHAAAAAAAA I AM FALLING HELPPPPP!!!!!!!!!!

    Ouch that's really hurt
    
    What is this?

    A trap game?
    """
    hide player

    scene bg forest with dissolve

    show bryan

    bryan """
    Welcome to It's a Trap game
    
    Here you be given a change to pick which entrance you would like to enter

    Your destiny will decide what will happen to you

    """

    hide bryan

    show player

    player """
    What is that.....

    Hey where are you show yourself again

    He suddenly vanish!!

    Where did that man go

    Who's commingg??

    There's people comming!!!!!

    Thanks god!!

    Hey!!!!!
    """

    hide player

    show jade

    jade """
    Hey!!!
    
    Are you trap tooo???
    """

    hide jade 

    show player

    player """
    Whattttt!!!!!!!!!

    Where both trap???

    Wait suit your self up

    Let's look around

    What is this a map?
    """

    hide player

    show maze_map at truecenter

    jade "Problably that is a map way out"

    player """
    Hmmmmm!!!!!!
    
    Oh there is an entrance here!!!
    """

    hide maze_map

    jump first_level

    return

label first_level:

    hide player
    show door 2

    player """
    But there is two where do I go

    A trap and Not a trap
    """

    jade "I will go to Not a Trap cause it's says it's not a trap"

    player "What if it is really a trap and just tricking you"

    jade "What so ever I will go not Its not a Tap now... BYE"

    player "Hmmmmm....Where do i go?"

    menu:
        "Trap":
            hide door
            show player
            player "Wait what another entrace"
            jump second_level
        "Not a Trap":
            scene bg fire
            player """
            Wait its so hot in here

            the door close WAIT!!!!!

            I told you it's just a trap

            HELP!!!!!!
            """
            "Player died"
            jump end

label second_level:
    hide player
    show door 2
    player "A trap and Not a trap again"
    menu:
        "Trap":
            scene bg ice
            player """
            Wait!!!! What is this?
            
            It's so cold

            Help!!!!!

            HELP!!!!!
            """
            "Player died"
            jump end
        "Not a Trap":
            hide door
            show player
            player "Again!!!!!!!!"
            jump third_level

label third_level:
    hide player
    show door 2
    player "wait theres another entrance behind"
    show door 1
    player "It's says safe, Probably this is the right one to choose"
    menu:
        "Trap":
            scene bg ice
            player """
            Wait!!!! What is this?
            
            It's so cold

            Help!!!!!

            HELP!!!!!
            """
            "Player died"
            jump end
        "Not a Trap":
            hide door
            player "Pew, Thanks good I am now outside"
            jump end
        "Safe":
            scene bg fire
            player """
            Wait its so hot in here

            the door close WAIT!!!!!

            I told you it's just a trap

            HELP!!!!!!
            """
            "Player died"
            jump end

label end:
    "Thank you for playing the game"
    jump start
    

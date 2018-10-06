import random

def ChooseMove():
    global z
    rockpopularity = int((open("/Users/timothy/Documents/rock.txt","r")).read())
    scissorspopularity = int((open("/Users/timothy/Documents/scissors.txt","r")).read())
    paperpopularity = int((open("/Users/timothy/Documents/paper.txt","r")).read())

    if rockpopularity > scissorspopularity:
        if rockpopularity > paperpopularity:
            return 1
        elif rockpopularity == paperpopularity:
            return random.choice([1,2])
        elif paperpopularity > scissorspopularity:
            return 2
    elif scissorspopularity > rockpopularity:
        if scissorspopularity > paperpopularity:
            return 0 
        elif paperpopularity > scissorspopularity:
            return 2
        else:
            return random.choice([0,1])
    else:
        if paperpopularity == rockpopularity:
            return random.randint(0,1)
        else:
            return random.choice([0,1])

while True:
    move = ["rock", "paper", "scissors"]
    movenumber = 0
    computermove = ChooseMove()
    go = 1
    while go == 1:
        playermove = move.index(input("What move do you want to choose:   "))
        popularity = str(int(open("/Users/timothy/Documents/" + move[playermove] + ".txt","r").read()) + 1)
        (open("/Users/timothy/Documents/" + move[playermove] + ".txt","w")).write(popularity)
        go = 2
    print ()
    print ("The computer picked " + move[computermove])
    print ()
    if playermove - computermove == 1:
        print ("Player won")
    elif playermove - computermove == 2:
        print ("Player lost")
    elif playermove - computermove == -1:
        print ("Player lost")
    elif playermove - computermove == -2:
        print ("Player won")
    else:
        print ("It's a draw")
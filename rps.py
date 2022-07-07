f = open("ldb.txt","a+")
f.write("n 0 \n")
f.close()

def ldb(name):
    global d
    d = {}
    l2 = []
    f = open("ldb.txt","r+")
    l = f.readlines()
    for i in l:
        l2 = i.split()
        d[l2[0]] = int(l2[1])

    f.close()

    if name == "n":
        pass
    elif name in d.keys():  
        d[name] = d.get(name)+ 1

        f = open("ldb.txt","w+")
        for i in d:
            f.write(f"{i} {d.get(i)} \n")

        f.close()
    else:
        f = open("ldb.txt","a")
        f.write(f"{name} 1 \n")
        f.close()

    val = list(d.values())
    key = list(d.keys())
    highscore = max(d.values())
    pos = val.index(highscore)
    
    return(f'''HIGH-SCORE: {highscore} 
    By: {key[pos]}''')

ldb("n")
key = list(d.keys())

def hasspace(string):
    for i in string:
        if i == " ":
            return(True)
        else:
            return(False)

def rps():
    print('''
    WELCOME TO 
    ROCK, PAPER, SCISSORS ''')

    while True:
        player_name = input("Enter your name(>= 3 letters and no spaces): ")
        if player_name in key:
            res = input("""This name exists...
            if you want to continue with it type "yes" else type "no" to choose someother name.""")
            if res == "yes":
                break
            elif res == "no":
                pass
        elif len(player_name) < 3 or hasspace(player_name):
            pass
        else:
            break
            

    player_score = 0
    cpu_score = 0
    draw = 0

    while True:
        if player_score == 3 or cpu_score == 3:
            break
        import random
        cpu_list = ['r','p','s']
        player = input("Your Turn (r for rock,p for paper, s for scissors): ")
        cpu = random.choice(cpu_list)
        print(f"Computer: {cpu}")
    
        
        if (player.lower() == 'r' and cpu == 's') or (player.lower() == 'p' and cpu == 'r') or (player.lower() == 's' and cpu == 'p'):
            player_score += 1
            print("Round won")
        elif (cpu == 'r' and player.lower() == 's') or (cpu == 'p' and player.lower() == 'r') or (cpu == 's' and player.lower() == 'p'):
            cpu_score += 1
            print("Round lost")
        else:
            draw += 1
            print("It's a draw")

    if player_score == 3 :
        print(f"{player_name} Wins!!! \nComputer = {cpu_score} \nYou = {player_score} \nDraw = {draw}")
        print(ldb(player_name))
    elif cpu_score == 3:
        print(f"The Computer Wins!!! \nComputer = {cpu_score} \nYou = {player_score} \nDraw = {draw}")

rps()

print("Thank you for playing the game \nHope you had fun!!!")

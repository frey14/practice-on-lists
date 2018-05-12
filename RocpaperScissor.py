'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock'''

a=input("make your choice person1")
b=input("make your choice person2")
a=str(a)
b=str(b)
score1=score2=0
if a=="Rock":
    if b=="Scissor":
        score1=score1+1
    elif b=="paper":
        score2=score2+1
    elif b=="Rock":
        score1=score1
        score2=score2

elif a=="Scissor":
    if b=="Rock":
        score2=score2+1
    elif b=="paper":
        score1=scor1+1
    elif b=="Scissor":
        score1=score1
        score2=score2
elif a=="paper":
    if b=="Rock":
        score1=score1+1
    elif b=="Scissor":
        score2=score2+1
    elif b=="paper":
        score1=score1
        score2=score2
if score1>score2:
    print("person1 is winner")
elif score1<score2:
    print("person2 is winner")
else:
    print("this is a tie")
        

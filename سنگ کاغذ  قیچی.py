import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    chois = int(input('Enter a valid choice please ☺: '))
    
    if chois == 1:
        chois_name = 'rock'
    elif chois == 2:
        chois_name = 'paper'
    elif chois == 3:
        chois_name = 'scissors'

    print('user chois', chois_name)
    print('now copeuter...')
    chois_compeuter = random.randint(1, 3)
    if chois_compeuter == 1:
        chois_compeuter_name = 'rock'
    elif chois_compeuter == 2:
        chois_compeuter_name = 'paper'
    elif chois_compeuter == 3:
        chois_compeuter_name = 'scisors'

    print('comp chois: ', chois_compeuter_name)
    print(chois_name, "vs", chois_compeuter_name)
    if chois_compeuter==chois:
        result= 'DRAW'
    elif (chois==1 and chois_compeuter==2) or(chois==2 and chois_compeuter==1):
        result=('paper')
    elif(chois==1 and chois_compeuter==2) or(chois==2 and chois_compeuter==3):
        result=('rock')
    elif(chois==2 and chois_compeuter==2) or(chois==2 and chois_compeuter==3):
        ('scisors')
    if result=='DRAW':
        print("<== It's a tie! ==>")
    elif result==chois_name:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")
        print("Do you want to play again? (Y/N)")
        ans=input('y / n ? ' )
        if ans=='n':
          break
        
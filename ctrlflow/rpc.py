import random, sys

print('ROCK', 'PAPER', 'SCISSORS');

#performance tracking variables

wins = 0;
losses = 0;
ties = 0;

#main game loop

while True:
    print('%s wins, %s losses, %s ties' %(wins, losses, ties));
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit');
        playermove = input()
        if playermove == "q":
            sys.exit()  
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break #break player input loop
        print('type one of r, p, s, or q.')

    #display what the player chose
    if playermove == 'r':
        print('Rock versus..')
    elif playermove == 'p':
        print('paper')
    elif playermove == 's':
        print('scissors')
    
    #display computer choice

    computerChoice = random.randint(1, 3)
    if computerChoice == 1:
        computerMove = 'r'
        print('Rock')
    elif computerChoice == 2:
        computerMove = 'p'
        print('paper')
    elif computerChoice == 3:
        computerMove = 's'
        print('scissors')

    #display & record wins ties and losses
    if playermove == computerMove:
        print('its a tie!')
        ties = ties +1
    elif playermove == 'r' and computerMove == 's':
        print('you win!')
        wins = wins +1
    elif playermove == 'p' and computerMove == 'r':
        print('you win')
        wins = wins +1
    elif playermove == 's' and computerMove == 'p':
        print('you win')
        wins = wins +1 
    elif playermove == 'r' and computerMove == 'p':
        print('you loose')
        losses = losses+1
    elif playermove == 'p' and computerMove == 's':
        print('you loose')
        losses = losses +1
    elif playermove == 's' and computerMove == 'r':
        print('you loose')
        losses = losses +1 
    



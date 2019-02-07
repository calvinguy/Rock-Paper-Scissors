from random import randint


class computer():
#randomizes a choice of rock, paper, or scissors for computer
    def randomizer(self):
        choicelist = ['rock', 'paper', 'scissors']

        choice = choicelist[randint(0, len(choicelist) - 1)]

        return choice

class player():
#prompts input from player to choose rock, paper, or scissors.
    def playerinput(self):
        cinput = False

        while cinput == False:
            choice = input("Let's play Rock, Paper, Scissors! Which one will you choose? \n >>").lower()

            if choice == 'rock' or choice == 'paper' or choice =='scissors':
                cinput = True
            else:
                print("You didn't select a valid answer, try again.")

        return choice

class RPS():
#compares choice between computer and player and determines winner.
    def play(self):

        Tie = "Tie game"
        Win = "You win!"
        Lose ="You lose :("

        results = {
                'P_rock C_rock':Tie,
                'P_rock C_scissors':Win,
                'P_rock C_paper':Lose,
                'P_scissors C_scissors':Tie,
                'P_scissors C_rock':Lose,
                'P_scissors C_paper':Win,
                'P_paper C_paper':Tie,
                'P_paper C_rock':Win,
                'P_paper C_scissors':Lose,
                }

        CompChoice = computer.randomizer()
        PlayerChoice = player.playerinput()

        print(f"The computer chose {CompChoice}:")
        print(results.get(f"P_{PlayerChoice} C_{CompChoice}"))

#create object
computer = computer()
player = player()
RPS = RPS()


RPS.play()

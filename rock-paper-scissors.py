from random import choice
class Game():
    def intro(self):
        print('--- Rock Paper Scissors Game ---')
        self.rounds = int(input('How many rounds would you like to play? '))

    def play(self):
        for _ in range(self.rounds):
            self.choice = input('Rock, paper, or scissors [r/p/s]? ')
            computer_choice = ComputerChoice().generate_choice()
            print(f'You: {self.choice}   |  Computer: {computer_choice}')
            result = Result(self.choice, computer_choice)
            print(result.result())

class ComputerChoice():
    def generate_choice(self):
        return str(choice('rps'))

class Result():
    def __init__(self, user_choice, computer_choice):
        self.user_choice = user_choice
        self.computer_choice = computer_choice
    
    def result(self):
        if self.user_choice == 'r':
            return Rock().rock_outcomes(self.computer_choice)
        if self.user_choice == 'p':
            return Paper().paper_outcomes(self.computer_choice)
        if self.user_choice == 's':
            return Scissors().scissors_outcomes(self.computer_choice)


class Rock(Game):
    def rock_outcomes(self, computer_choice):
        if computer_choice == 'r':
            return 'It was a tie.'
        if computer_choice == 'p':
            return 'Computer won.'
        if computer_choice == 's':
            return 'You won.'

class Paper(Game):
    def paper_outcomes(self, computer_choice):
        if computer_choice == 'r':
            return 'You won.'
        if computer_choice == 'p':
            return 'It was a tie.'
        if computer_choice == 's':
            return 'Computer won.'

class Scissors(Game):
    def scissors_outcomes(self, computer_choice):
        if computer_choice == 'r':
            return 'Computer won.'
        if computer_choice == 'p':
            return 'You won.'
        if computer_choice == 's':
            return 'It was a tie.'
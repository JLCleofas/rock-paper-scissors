from random import choice

class Game:
    def __init__(self):
        self.rounds = 0
    
    def start(self):
        while True:
            try:
                print('--- Rock Paper Scissors Game ---')
                self.rounds = int(input('How many rounds would you like to play? '))
                break
            except ValueError:
                print('Please enter a number.')
    
    def play(self):
        for _ in range(self.rounds):
            self.user_choice = input('Rock, paper, or scissors [r/p/s]? ').strip().lower()
            self.computer_choice = choice('rps')
            print(f'You: {self.user_choice}   |  Computer: {self.computer_choice}')
            result = self.decision(self.user_choice, self.computer_choice)
            print(result)
    
    def decision(self, user, computer):
        if user == computer:
            return 'It was a tie.'
        user_vs_computer = (user, computer)
        wins = [('r', 's'), ('p', 'r'), ('s', 'p')]
        return 'You won.' if user_vs_computer in wins else 'Computer won.'

    def run(self):
        self.start()
        self.play()

game = Game()
game.run()
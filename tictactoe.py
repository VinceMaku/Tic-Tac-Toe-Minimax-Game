from __future__ import print_function

class Board(object):
        def __init__(self, inner=None):
                self.inner = inner or [None for x in range(9)]
        def play(self, position, player):
                assert(0 <= position < len(self.inner))
                if self.inner[position]:
                        return False
                self.inner[position] = player
                return True
        def get(self, position):
                assert(0 <= position < len(self.inner))
                return self.inner[position]
        def winner(self):
                return self.hwinner() or self.vwinner() or self.dwinner()
        def hwinner(self):
                table = self.inner
                for index in range(0,9,3):
                        if table[index] and table[index] == table[index+1] and table[index] == table[index+2]:
                                return table[index]
        def vwinner(self):
                table = self.inner
                for index in range(3):
                        if table[index] and table[index] == table[index+3] and table[index] == table[index+6]:
                                return table[index]
        def dwinner(self):
                table = self.inner
                if table[0] and table[0] == table[4] and table[0] == table[8]:
                        return table[0]
                if table[2] and table[2] == table[4] and table[2] == table[6]:
                        return table[2]
        def full(self):
                return all(self.inner)
        def __str__(self):
                display = []
                for index, column in enumerate(self.inner):
                        if display:
                                display.append(index%3 and ' ' or '\n')
                        display.append(str(column or index+1))
                return ''.join(display)
        def copy(self):
                return Board(self.inner[:])

class Player(object):
        def __init__(self, color, name):
                self.color = color
                self.name = name
        def __str__(self):
                return self.color
        def play(self, board):
                raise NotImplementedError

class Human(Player):
        def play(self, board):
                print(board)
                value = 0
                while value < 1 or value > 9 or board.get(value - 1):
                        value = raw_input(self.name + ": ")
                        value = value.isdigit() and int(value) or 0
                board.play(value - 1, self)

class Computer(Player):
        other = Player(None, None)
        def play(self, board):
                if not self.other.name:
                        for value in range(9):
                                index = board.get(value)
                                if index and index != self:
                                        self.other = index
                                        break
                for index in range(1, -3, -1):
                        for indices in range(9):
                                if not board.get(indices):
                                        table = board.copy()
                                        table.play(indices, self)
                                        if self.minimax(table, min) > index:
                                                board.play(indices, self)
                                                return
        def minimax(self, board, less):
                if board.winner():
                        return board.winner() == self and 1 or -1
                if board.full():
                        return 0
                more = less == min and 1 or -1
                for p in range(9):
                        if not board.get(p):
                                table = board.copy()
                                table.play(p, less == min and self.other or self)
                                more = less(more, self.minimax(table, less == min and max or min))
                                if more == (less == min and -1 or 1):
                                        return more
                return more

class Heuristic(Computer):
        def play(self, board):
                if not self.other.name:
                        for move in range(9):
                                omove = board.get(move)
                                if omove and omove != self:
                                        self.other = omove
                                        break
                board.play(self.findmove(board), self)
        def findmove(self, board):
                if not any(board.inner): #empty board
                        return 0

                for index in range(1, -3, -1): #default to minimax
                        for indices in range(9):
                                if not board.get(indices):
                                        table = board.copy()
                                        table.play(indices, self)
                                        if self.minimax(table, min) > index:
                                                return indices

class Game(object):
        def __init__(self, *players):
                self.players = list(players)
                self.board = Board()
        def play(self):
                while not self.board.winner() and not self.board.full():
                        delete = self.players.pop(0)
                        delete.play(self.board)
                        self.players.append(delete)
                print(self.board)
                if self.board.winner():
                        print(self.board.winner().name, "wins!")                        
                else:
                        print("The game is draw.")
                play_again_decision()
def nomination():
        decision = str(raw_input("Do you want to go first [Y]/[N]? "))
        decision = decision.upper()
        if decision in ["Y","YES"]:
                return Game(Human('X', "Player"), Heuristic('O', "Computer")).play()
        elif decision in ["N","NO"]:
                return Game(Heuristic('X', "Computer"), Human('O', "Human")).play()
        else:
                print("The following input is not correct pls try again !")
                nomination()
def play_again_decision():
        play_again = str(raw_input("Do you want to play again [Y]/[N]? " ))
        play_again = play_again.upper()
        if play_again in ["Y","YES"]:
                nomination()
        elif play_again in ["N","NO"]:
                print("Thank you for playing the game")
        else:
                print("Error please try again! ")
                play_again_decision()


if __name__ == '__main__':
         nomination()

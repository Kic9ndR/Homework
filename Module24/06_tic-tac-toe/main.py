from dataclasses import dataclass

@dataclass
class Cell:
    status: bool
    map: Board.maps
    player: Player
    
    def step_map(self):
        if isinstance(self.map[ind], str):
            print('Данная клетка уже занята')
        else:
            ind = self.map.index(self.player.steps)
            self.map[ind] = self.player.symbol

class Board:

    def print_map(self):
        maps = []
        for n in range(1, 9):
            for _ in range(3):
                print(n, end='')
                self.maps.append(n)
            print('\n')
        return self.maps

@dataclass
class Player:
    name: str
    symbol: str

    def moves(self):
        steps = []
        while False:
            step = input('Ваш ход: ')
            steps.append(step)
        return steps

@dataclass
class Game:
    players1: Player
    players2: Player
    field: Board
    cell: Cell

    game_over = False

    def status_game(self):
        win = ''
    
        for i in victories:
            if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
                win = "X"
            elif maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
                win = "O"
            else:
                print('Идет жаркая борьба!')
        return f'{win} победил!'
 
    def method_1(self):
        while self.game_over == False:

            if win != "": 
                game_over = True
            else:
                game_over = False

            first_map = self.field.print_map
            first_map
            print(f'{self.players.name} Вам необходимо выбрать первый ход.')
            self.players.moves

            if win != "":
                game_over = True
            else:
                game_over = False

            second_map = self.field.print_map
            second_map
            print(f'{self.players.name} Вам необходимо выбрать второй ход.')
            self.players.moves

            self.status_game(self)
        return f'Победа досталась {self.status_game.win}'

    def method_2(self):
        maps = self.field.print_map

        while self.game_over == False:
            maps
            self.players1.moves
            maps
            self.players2.moves

            if win != "": 
                game_over = True
            else:
                game_over = False

            self.status_game(self)
        return

    def method_3(self):
        score = 0
        start_game = int(input('Начинаем игру?(1 - да, 2 - нет) '))

        while start_game == 1:
            



victories = [[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]]

board = Board
print(board.print_map)
name1 = input('Ваше имя: ')
name2 = input('Ваше имя: ')

p1 = Player(name1, 'X')
p2 = Player(name2, 'O')
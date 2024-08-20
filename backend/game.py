import random
from backend import algorithm
from backend.playfield import playfield
import numpy as np

class game:

    def __init__(self):
        self.playfield = playfield()

    def move(self,sign,place_number):
        return self.playfield.move(sign,place_number)
    
    def ai_move(self,ai_sign, player_sign):
        return algorithm.minimax(self.playfield,True,ai_sign,player_sign)
    
    def get_board(self):
        return np.array(self.playfield.array).flatten()
    
    def get_board_2d(self):
        return self.playfield.array
    

    def play():
        player_sign = "O"
        ai_sign = "X"
        board = playfield()
        active_player = game.player_start()

        while playfield.check_for_end != 10:
            succesful = False
            if active_player:
                while not succesful:
                    space = input("Enter space")
                    succesful = board.move(player_sign,space)
                    if succesful:
                        #move tonen in javascript
                        print("")
            else:
                board.move(ai_sign, algorithm.minimax(board,True,ai_sign,player_sign))
                #move tonen in javascript
            
            #board.print_field()



    def player_start():
        random_value = random.random()
        if random_value > 0.5:
            return True
        else:
            return False
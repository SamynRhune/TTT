from playfield import playfield
from algorithm import minimax

playfield = playfield()

print("Welcome to tic tac toe")

while playfield.check_for_end("O") == 10:
    place_number = input("Give a place number: ")
    print("PLAYER")
    playfield.move("O", int(place_number))
    playfield.print_field()
    if playfield.check_for_end("O") != 10:
        break
    print("AI")
    playfield.move("X",minimax(playfield,True,"X","O"))
    playfield.print_field()

""" print(minimax(playfield,True,"X","O"))
playfield.print_field() """
"""playfield.move("O",7)
playfield.print_field()
print(minimax(playfield,True,"X","O"))
playfield.print_field()
playfield.move("O",2)
playfield.print_field()
print(minimax(playfield,True,"X","O"))
playfield.print_field() """
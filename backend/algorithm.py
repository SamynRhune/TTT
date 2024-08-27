from backend.playfield import playfield
import copy
import numpy as np

def minimax(board, isMaximizing, ai_sign, player_sign, depth=0):
    available_array = board.check_available_field()
    calculating_array = []
    
    row_count = len(board.array)
    col_count = len(board.array[0])

    for i in range(row_count):
        for j in range(col_count):
        #only if there is available space
            if available_array[i][j] == True:
                temp_board = copy.deepcopy(board)
            
            #board updaten
                if isMaximizing:
                    temp_board.array[i][j] = ai_sign  
                else:
                    temp_board.array[i][j] = player_sign
                    
            #check_for_end or go deeper in algorithm
                if temp_board.check_for_end(ai_sign) != 10:
                    if depth != 0:
                        return temp_board.check_for_end(ai_sign)
                    else:
                        calculating_array.append(temp_board.check_for_end(ai_sign))
                else:
                    return_arrays = (minimax(temp_board, not isMaximizing, ai_sign,player_sign,depth+1))
                    calculating_array.append(return_arrays)
            #if space not empty it cant be chosen
            elif depth == 0:
                calculating_array.append(-10)

    if isMaximizing:
        if depth == 0:
            return calculating_array.index(max(calculating_array))
        else:
            return max(calculating_array)
    else:
        return min(calculating_array)

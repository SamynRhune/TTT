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
            #als er een leeg vakje is
            if available_array[i][j] == True:
                temp_board = copy.deepcopy(board)

                #solution_array[i][j] = minimax(temp_board, isMaximizing, ai_sign, player_sign,i,j)
            
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

            elif depth == 0:
                calculating_array.append(-10)


    #print(sum(solution_array)/len(solution_array))
    if isMaximizing:
        if depth == 0:
            return calculating_array.index(max(calculating_array))
        else:
            return max(calculating_array)
    else:
        return min(calculating_array)

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list) or isinstance(item, np.ndarray):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

def get_place(min_array,avg_array):
    if max(min_array) == -1:
        max_value = max(avg_array)
        return avg_array.index(max_value)
        
    else:
        max_value = max(min_array)
        return min_array.index(max_value)
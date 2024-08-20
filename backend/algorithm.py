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
            
            #AI aan zet
                if isMaximizing:
                    temp_board.array[i][j] = ai_sign
                    if temp_board.check_for_end(ai_sign) != 10:
                        return temp_board.check_for_end(ai_sign)
                    else:
                        return_arrays = (minimax(temp_board, not isMaximizing, ai_sign,player_sign,depth+1))
                        calculating_array.append(return_arrays)
                        """ if depth == 0 :
                            avg_array.append(sum(np.array(return_arrays).flatten())/len(np.array(return_arrays).flatten())) """
                #PERSOON aan zet
                else:
                    temp_board.array[i][j] = player_sign
                    if temp_board.check_for_end(ai_sign) != 10:
                        return temp_board.check_for_end(ai_sign)
                    else:
                        return_arrays = (minimax(temp_board, not isMaximizing, ai_sign,player_sign,depth+1))
                        calculating_array.append(return_arrays)
                        """ if depth == 0 :
                            avg_array.append(sum(np.array(return_arrays.flatten())/len(np.array(return_arrays).flatten()))) """
            

    #print(sum(solution_array)/len(solution_array))
    if depth == 0:
        avg_array = []
        min_array = []
        """ print("SOLUTION ARRAY")
        print(solution_array)
        print("LEN")
        print(len(solution_array)) """
        current_index = 0
        solution_array = []
        for i in range(len(np.array(board.array).flatten())):
            field = flatten(board.array)
            
            if field[i] == 0:
                if isinstance(calculating_array[current_index],list) :
                    part_array = flatten(calculating_array[current_index])
                    avg_array.append(sum(part_array)/len(part_array))
                    min_array.append(min(part_array))
                    current_index = current_index + 1
                elif calculating_array[current_index] == -1:
                    current_index = current_index + 1
                    avg_array.append(-1)
                    min_array.append(-100)
                elif calculating_array[current_index] == 1:
                    current_index = current_index + 1
                    avg_array.append(1)
                    min_array.append(1)
                elif calculating_array[current_index] == 0:
                    current_index = current_index + 1
                    avg_array.append(0)
                    min_array.append(0)
            else:
                avg_array.append(-1)
                min_array.append(-100)
         
        """ print(avg_array)
        print(min_array) """
        return get_place(min_array,avg_array)
    else:
        return (calculating_array)
                

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

class playfield:
    def __init__(self, board=None):
        if board == None:
            self.array = [[0,0,0]
                         ,[0,0,0]
                         ,[0,0,0]]
        else:
            self.array = board
    
    def reset(self):
        self.array = [[0,0,0]
                      ,[0,0,0]
                      ,[0,0,0]]
        return True
    
    def copy(self):
        return playfield(self.array)

    def print_field(self):
        row_count = len(self.array)
        for i in range(row_count):
            print(self.array[i])
    
    def place_number_to_coordinates(self,place_number):
        if(place_number >= len(self.array)*len(self.array[0])):
            print("number is to big")
        else:
            col_count = len(self.array[0])
            target_row = int(place_number/col_count)
            target_col = place_number % col_count
            return target_col, target_row

    def move(self, player_sign, place_number):
        col, row = self.place_number_to_coordinates(place_number)

        if self.array[row][col] == 0:
            self.array[row][col] = player_sign
            #succesvol
            return True
        else:
            print("Space is not empty")
            #no succes
            return False
    

    def check_for_end(self, current_player):
        if self.check_row_win(current_player) != 0:
            return self.check_row_win(current_player)
        
        if self.check_col_win(current_player) != 0:
            return self.check_col_win(current_player)       
        
        if self.check_cross_win(current_player) != 0:
            return self.check_cross_win(current_player)
        
        if self.check_draw() == False:
            return 10
        return 0
    
    def check_row_win(self, current_player):
        row_count = len(self.array)
        col_count = len(self.array[0])
        
        for i in range(row_count):
            current_col = 0
            win_potential = True
            current_sign = "N"

            #als kolom niet buiten array valt en er is nog win potentieel 
            while ((current_col+1) < col_count) and win_potential:

                current_sign = self.array[i][current_col]
                #not(als deze kolom en volgende kolom zelfde zijn en niet 0)
                if not((self.array[i][current_col] == self.array[i][current_col+1]) and self.array[i][current_col] != 0):
                    win_potential = False

                current_col = current_col+1

            if win_potential:
                if current_sign == current_player:
                    return 1
                else:
                    return -1
            
                

        return 0


    def check_col_win(self, current_player):
            row_count = len(self.array)
            col_count = len(self.array[0])
            
            for i in range(col_count):
                current_row = 0
                win_potential = True
                current_sign = "N"

                #a 
                while ((current_row+1) < row_count) and win_potential:
                    #not()
                    current_sign = self.array[current_row][i]

                    if not((self.array[current_row][i] == self.array[current_row+1][i]) and self.array[current_row][i] != 0):
                        win_potential = False
                    
                    current_row = current_row +1

                if win_potential:
                    if current_sign == current_player:
                        return 1
                    else:
                        return -1
            
            return 0

    def check_cross_win(self, current_player):
        row_count = len(self.array)
        current_sign = "N"

        i = 0 
        win_potential = True
        while ((i+1) < row_count) and win_potential:
            current_sign = self.array[i][i]
            if not(self.array[i][i] == self.array[i+1][i+1] and self.array[i][i] != 0):
                win_potential = False

            i = i+1
        
        if win_potential:
            #print("lb-ro")
            if current_sign == current_player:
                return 1
            else:
                return -1
        
        win_potential = True
        i = 0
        while ((i+1) < row_count) and win_potential:
            current_sign = self.array[i][row_count-(i+1)]
            if not(self.array[i][row_count-(i+1)] == self.array[i+1][row_count-(i+2)] and self.array[i][row_count-(i+1)] != 0):
                win_potential = False
            
            i = i+1
        
        if win_potential:
                if current_sign == current_player:
                    return 1
                else:
                    return -1
        return 0
    
    def check_draw(self):
        current_block = "X"
        current_row = 0 
        
        row_count = len(self.array)
        col_count = len(self.array[0])
        
        while current_block != 0 and current_row < row_count:
            current_col = 0
            while current_block != 0 and current_col < col_count:
                current_block = self.array[current_row][current_col]
                
                current_col = current_col +1
            current_row = current_row + 1
        
        return current_block != 0
    
    def check_available_field(self):
        row_count = len(self.array)
        col_count = len(self.array[0])
        available_array = [[None for _ in range(3)] for _ in range(3)]
    
        for i in range(row_count):
            for j in range(col_count):
                if self.array[i][j] == 0:
                    available_array[i][j] = True
                else:
                    available_array[i][j] = False
        return available_array


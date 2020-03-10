from .constraint import Constraint
from utils import MatrixUtil
from tetris.tetrominos import TetrominoUtil

from tetris.tetrominos import Tetromino #TEMPORARY

class TetrominoPuzzleConstraint(Constraint):
  
  def __init__(self, grid):
    super().__init__()
    self._grid = MatrixUtil.copy(grid)

    # Helpful Functions:
    # MatrixUtil.copy(matrix) --> returns a copy of the matrix
    # MatrixUtil.valid_position(matrix, row, col) --> returns True iff (row, col) is a valid position within the matrix
    
    # TetrominoUtil.copy(tetromino) --> returns a copy of the tetromino
    # Tetromino.get_pruned_grid() --> returns a condensed version of the block grid representing a tetromino piece.
    #                                 Use this over Tetromino.get_original_grid()!
    # Tetromino.get_pruned_dimensions() --> returns row_count, col_count of the tetromino piece
    # Tetromino.rotate(rotation_amount) --> rotates the tetromino piece rotation_amount times
    
  def check(self, variables, assignments):
    
    # Question 2, your check solution goes here.

    # This method returns True iff the given variables and their assignments satisfy the Tetromino Puzzle
    # Constraint. Recall this constraint is that all tetromino pieces are placed onto the grid without
    # colliding with any present pieces on the grid or any other pieces to be placed.

    # As you will be manipulating Tetromino pieces here you should be manipulating _copies_ of the pieces
    # instead of the original. Same goes with the grid being worked with (self._grid).

    #pruned dimensions returns row count col count so variable J would be (2, 3) i.e 2 rows occupied and 3 columns
    #pruned grid lets you know how many spaces are occupied in each row
 
    for var in variables: #check to make sure no variable overlaps another or goes off the grid
      if assignments[var] != None:
         #checking position of assignmetn with matrix
        var_copy = TetrominoUtil.copy(var)
          
        var_row = assignments[var][0][0]
        var_col = assignments[var][0][1]
          
        var_copy.rotate(assignments[var][1]) #rotate cyop by rotation count 
        var_x = var_copy.get_pruned_dimensions()[0]
        var_y = var_copy.get_pruned_dimensions()[1]
        #print(var_x)
        #print(var_y)
        var_grid = var_copy.get_pruned_grid()
        
        if MatrixUtil.valid_position(self._grid, assignments[var][0][0] + var_x-1, assignments[var][0][1] + var_y-1): #beta 
        #if MatrixUtil.valid_position(self._grid, assignments[var][0][0], assignments[var][0][1]):
          #now check if it doesnt collide with any other variables, need to use matrices
          for var2 in variables:
            if var != var2 and assignments[var2] != None:
              var2_copy = TetrominoUtil.copy(var2)
             
              var2_row = assignments[var2][0][0]
              var2_col = assignments[var2][0][1]
              

              var2_copy.rotate(assignments[var2][1]) #rotate copy by rotation count
              var2_x = var2_copy.get_pruned_dimensions()[0]
              var2_y = var2_copy.get_pruned_dimensions()[1]
              var2_grid = var2_copy.get_pruned_grid()
              
              for i in range(len(var_grid)):
                for j in range(len(var2_grid)):
                  if (var_row + i) == (var2_row + j):
                    #print("checking")
                    if ((var_col + len(var_grid[i])) <= var2_col) or (var_col >= var2_col + len(var2_grid[j])):
                      continue
                    else:
                      return False
        else:
          return False
    
    
    return True
            
            
      
          
        
      
      
      
      #if MatrixUtil.valid_position(matrix, 
                                   
    #print(var.get_pruned_grid())
    
    #print(MatrixUtil.valid_position(matrix, 2, 5))
    

    

  def has_future(self, csp, var, val):
    # Question 5, your has future implementation goes here.

    # Recall this method will return True iff the given variable : value combination exists within
    # a possible satisfying assignment. This means you will have to check all possible assignments
    # which have this variable : value combination to see if any such assignments satisfy the
    # Tetromino Puzzle constraint.
    
    raise NotImplementedError("Has Future method for TetrominoPuzzleConstraint is not implemented")

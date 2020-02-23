from state import *

# Here you will implement evaluation functions. Recall that weighing components of your
# evaluation differently can have positive effects on performance. For example, you could
# have your evaluation prioritize running away from opposing agents instead of activiating
# switches. Also remember that for values such as minimum distance to have a positive effect
# you should inverse the value as _larger_ evaluation values are better than smaller ones.

# Helpful Functions:
# You may define any helper functions you want in this file.
# GameState.get_enemies() --> returns a list of opposing agent positions.
# GameState.get_boxes() --> returns a list of (row, col) positions representing where the boxes are on the map
# GameState.get_switches() --> returns a dictionary where the keys are the locations of the switches as (row, col) and the value
#                              being True if the switch is on and False if off.
# GameState.get_player_position() --> returns the current position of the player in the form (row, col)
# GameState.get_remaining_points() --> returns a list of the positions of the remaining armory points of the map in the form (row, col) 
  
class EvaluationFunctions:

  @staticmethod
  def manhattan_heuristic(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

  @staticmethod
  def euclidean_heuristic(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5  

  @staticmethod
  def score_evaluation(state):
    return state.get_score()
  
  @staticmethod
  def box_evaluation(state):
    #Question 4, your box evaluation solution goes here
    #Returns a numeric value evaluating the given state where the larger the better
    #return 0
    raise NotImplementedError("Box Evaluation not implemented")

  @staticmethod
  def points_evaluation(state):
    #Question 5, your points evaluation solution goes here
    #Returns a numeric value evaluating the given state where the larger the better
    for pos in state.get_switches():
      #only one switch so simply set it to switch_pos
      switch_pos = pos
    player_pos = state.get_player_position()
    if state.get_obtained_points() >= 5: 
      #Case of only need to hit switch compare switch and player position
      return 1/EvaluationFunctions.euclidean_heuristic(player_pos, switch_pos)
    distances = []
    total_dis = 0
    point_to_switch = 0
    player_to_point = 0
    player_pos = state.get_player_position()
    temp_remain = state.get_remaining_points()[:] #copy remaining points so we can delete from copy
    
    for k in range(5 - state.get_obtained_points(), 0, -1):
      if k == 1: #IF ONLY ONE POINT IS LEFT TO OBTAIN
        for i in range(0, len(temp_remain)):
          point_pos = temp_remain[i]
          player_to_point = EvaluationFunctions.euclidean_heuristic(player_pos, point_pos) * 1.5 
          #Points evaluate smaller here because we do inverse later making them bigger (need point before we get to switch)
          point_to_switch = EvaluationFunctions.euclidean_heuristic(point_pos, switch_pos) * 3 
          #want combined distance between player and point, point and switch
          sum_both = ((player_to_point) + (point_to_switch))
          distances.append(sum_both)
        for enemy in state.get_enemies():
          total_dis += EvaluationFunctions.euclidean_heuristic(player_pos, enemy)
        #Apparently you have to check this because sometimes there aren't enough points on the board 
        #to obtain the boots so you could have an empty distances and the check loops through the 5 points
        #For example the first test case in Q5 has only 3 points and 0 obtained so it just ignores the fact
        #that you need 5 points and says best state is when there is no points left and you're at the switch
        #even though you don't have 5 points
        if distances != []:
          distances.sort() 
          total_dis += 1/distances[0] #smallest distance is most optimal do inverse because bigger better
          #reset distances
          distances = []
      else:
        for i in range(0, len(temp_remain)):
          point_pos = temp_remain[i]
          player_to_point = (EvaluationFunctions.euclidean_heuristic(player_pos, point_pos), point_pos)
          distances.append(player_to_point)
        #find and add the shortest distance between points and player
        for enemy in state.get_enemies():
          total_dis += EvaluationFunctions.euclidean_heuristic(player_pos, enemy)
        if distances != []:
          distances.sort()
          temp_remain.remove(distances[0][1]) #remove point because we theoretically got the point
          player_pos = distances[0][1] #update player_pos because we theoretically moved them
          #need to do the inverse because smaller is better here but overall want bigger to be better
          #multiply by 1.5 because points are more important than enemies
          total_dis += 1/(distances[0][0] * 1.5)
          #reset distances
          distances = []
    return total_dis    
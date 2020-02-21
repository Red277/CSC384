from state import *
import math
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
  #returns the SMALLEST distance between a box in boxes and a given switch
  def get_min_box_distance(switch_loc, boxes, state):
    distance = math.inf
    for box in boxes:
      temp = EvaluationFunctions.manhattan_heuristic(switch_loc, box)
      temp2 = EvaluationFunctions.manhattan_heuristic(box, state.get_player_position())
      x = temp + temp2
      print(temp2)
      print(temp)
      if x < distance:
        distance = x
    
    return distance

  @staticmethod
  def safe_div(n, d):
    return n / d if d else 0  
  
  @staticmethod
  def score_evaluation(state):
    return state.get_score()
  
  @staticmethod
  def box_evaluation(state):
    #Question 4, your box evaluation solution goes here
    #Returns a numeric value evaluating the given state where the larger the better
    
    eval_sum = 0
    player_pos = state.get_player_position()
    
    box_to_switch_sum = 0
    switches = state.get_switches()
    boxes = state.get_boxes()
    for switch_loc in switches:
      a = EvaluationFunctions.get_min_box_distance(switch_loc, boxes, state)
      #print(a)
      box_to_switch_sum += a
    
    player_to_enemy_sum = 0
    enemies = state.get_enemies()
    for enemy in enemies:
      player_to_enemy_sum += EvaluationFunctions.manhattan_heuristic(enemy, player_pos)
      
    #inverse sum before mutiplying with weight
    #10 and 5 are just randomly chosen so box distance is prioritized over enemy distance
    eval_sum += EvaluationFunctions.safe_div(1, box_to_switch_sum) * 10  #+  EvaluationFunctions.safe_div(1, player_to_enemy_sum) * 15
    print(eval_sum)
    #print(box_to_switch_sum)
    return eval_sum    

  @staticmethod
  def points_evaluation(state):
    #Question 5, your points evaluation solution goes here
    #Returns a numeric value evaluating the given state where the larger the better
    return 0
    #raise NotImplementedError("Points Evaluation not implemented")

from state import *
from utils import *

import math

class GameTreeSearching:
  # You will also find that the GameStateHandler class (already imported) will help perform needed operations on the
  # the game states. To declare a GameStateHandler simply wrap it around a GameState like such,
  # handler = GameStateHandler(GameState) where GameState will be an instance of GameState.
  
  # Below is a list of helpful functions:
  # GameStateHandler.get_successors() --> returns successors of the handled state
  # GameStateHandler.get_agents() --> returns a list of the positions of the agents on the map
  # GameStateHandler.get_agent_count() --> returns the number of agents on the map
  # GameStateHandler.get_agent_actions(agent_pos) --> returns a list of the possible actions the given agent can take
  # GameStateHandler.get_successor(agent_pos, action) --> returns the successor state if the given agent took the given action 
  # GameState.get_player_position() --> returns the players position in that game state as (row, col)
  # GameState.copy() --> returns a copy
  # GameState.is_win() --> returns True if the game state is a winning state
  # GameState.is_loss() --> returns True if the game state is a losing state

  # Hint:
  # To avoid unwanted issues with recursion and state manipulation you should work with a _copy_ of the state
  # instead of the original.



  @staticmethod
  def minimax_search(state, eval_fn, depth = 2):
    # Question 1, your minimax search solution goes here
    # Returns a SINGLE action based off the results of the search
    moves = depth * 2
    return GameTreeSearching.minimax_helper(state, eval_fn, depth, moves)[0]
    
    
  @staticmethod
  def minimax_helper(state, eval_fn, depth, moves):
    state_copy = state.copy()
    best_action = None
    
    handler = GameStateHandler(state_copy)
    agents = handler.get_agents()
    
    player = moves % 2
    
    if moves == 0:                             #depth end
      return best_action, eval_fn(state_copy)    
    elif player == 1 and state_copy.is_loss():  #if MIN and lossed
      return best_action, eval_fn(state_copy)
    elif player == 0 and state_copy.is_win(): #if MAX and won
      return best_action, eval_fn(state_copy)
    
    
    if player == 1: #MIN SO OPPONENT
      value = math.inf
      agents = agents[1:]
    else:
      value = -math.inf
      agents = agents[:1]
      
    for agent in agents:
      for action in handler.get_agent_actions(agent):  #succesor is a tuple [direction, new_state]
        next_pos = handler.get_successor(agent, action)
        next_move, next_val = GameTreeSearching.minimax_helper(next_pos, eval_fn, depth-1, moves-1)

        if player == 0 and value < next_val:  #MAX
          value, best_action = next_val, action
        if player == 1 and value > next_val:  #MIN
          value, best_action = next_val, action      
    
    return best_action, value
    
    

  @staticmethod
  def alpha_beta_search(state, eval_fn, depth):
    # Question 2, your alpha beta pruning search solution goes here
    # Returns a SINGLE action based off the results of the search
    moves = depth * 2
    return GameTreeSearching.alpha_beta_helper(state, eval_fn, depth, -math.inf, math.inf, moves)[0]
  
  @staticmethod
  def alpha_beta_helper(state, eval_fn, depth, alpha, beta, moves):
    state_copy = state.copy()
    best_action = None

    player = moves % 2

    handler = GameStateHandler(state_copy)
    agents = handler.get_agents()

    if moves == 0:                             #depth end
      return best_action, eval_fn(state_copy)    
    elif player == 1 and state_copy.is_loss():  #if MIN and lossed
      return best_action, eval_fn(state_copy)
    elif player == 0 and state_copy.is_win(): #if MAX and won
      return best_action, eval_fn(state_copy)

    if player == 1: #MIN SO OPPONENT
      value = math.inf
      agents = agents[1:]
    else:
      value = -math.inf
      agents = agents[:1]

    for agent in agents:
      for action in handler.get_agent_actions(agent):  #succesor is a tuple [direction, new_state]
        next_pos = handler.get_successor(agent, action)
        next_move, next_val = GameTreeSearching.alpha_beta_helper(next_pos, eval_fn, depth-1, alpha, beta, moves-1)

        if player == 0: #PLAYER MAX CHECK DIFF
          if value < next_val:
            value, best_action = next_val, action
          if value >= beta:
            return best_action, value
          alpha = max(alpha, value)
        if player == 1: #PLAYER MIN 
          if value > next_val:
            value, best_action = next_val, action
          if value <= alpha:
            return best_action, value
          beta = min(beta, value)
    return best_action, value  
  
  @staticmethod
  def expectimax_search(state, eval_fn, depth):
    # Question 3, your expectimax search solution goes here
    # Returns a SINGLE action based off the results of the search
    moves = depth * 2
    return GameTreeSearching.expectimax_helper(state, eval_fn, depth, moves)[0]
  
  def expectimax_helper(state, eval_fn, depth, moves):
    state_copy = state.copy()
    best_action = None
    
    handler = GameStateHandler(state_copy)
    agents = handler.get_agents()
    
    player = moves % 2
    
    if moves == 0:                             #depth end
      return best_action, eval_fn(state_copy)    
    elif player == 1 and state_copy.is_loss():  #if MIN and lossed
      return best_action, eval_fn(state_copy)
    elif player == 0 and state_copy.is_win(): #if MAX and won
      return best_action, eval_fn(state_copy)
    
    if player == 1: #CHANCE SO OPPONENT
      value = 0
      agents = agents[1:]
    else:               #MAX
      value = -math.inf
      agents = agents[:1]
      
    for agent in agents:
      for action in handler.get_agent_actions(agent):  #succesor is a tuple [direction, new_state]
        next_pos = handler.get_successor(agent, action)
        next_move, next_val = GameTreeSearching.expectimax_helper(next_pos, eval_fn, depth-1, moves-1)

        if player == 0 and value < next_val:   #MAX
          value, best_action = next_val, action
        if player == 1:   #CHANCE
          value = value + 1/len(handler.get_agent_actions(agent)) * next_val #uniform chance for each action to be chosen
          
    
    return best_action, value
    #no best action for CHANCE players
    
  
  

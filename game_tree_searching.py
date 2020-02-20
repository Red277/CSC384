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
    state_copy = state.copy()
    best_action = None

    if state_copy.is_win() or depth == -2:
      return best_action
    if abs(depth) == 1: #MIN SO OPPONENT
      value = math.inf
      handler = GameStateHandler(state_copy)
      agents = handler.get_agents()[1:]
      for agent in agents:
        for action in handler.get_agent_actions(agent):  #succesor is a tuple [direction, new_state]
          #for move in handler.get_successor(agent, action):
          next_pos = handler.get_successor(agent, action)
          next_val = eval_fn(next_pos)    #equiv to DFMiniMax(nxt_pos)?
          next_move = GameTreeSearching.minimax_search(next_pos, eval_fn, depth-1)   
          if abs(depth) != 1 and value < next_val:
            value, best_action = next_val, action
          if abs(depth) == 1 and value > next_val:
            value, best_action = next_val, action      
      return best_action
    else:               #MAX SO PLAYER
      value = -math.inf
      handler = GameStateHandler(state_copy)
      succ = handler.get_successors()
      for move in handler.get_successors():  #succesor is a tuple [direction, new_state]
        next_pos = move[1]   #move is a tuple
        next_val = eval_fn(next_pos)    #equiv to DFMiniMax(nxt_pos)?
        next_move = GameTreeSearching.minimax_search(next_pos, eval_fn, depth-1)             
        if abs(depth) != 1 and value < next_val:
          value, best_action = next_val, move[0]
        if abs(depth) == 1 and value > next_val:
          value, best_action = next_val, move[0]
    
      return best_action

  @staticmethod
  def alpha_beta_search(state, eval_fn, depth):
    # Question 2, your alpha beta pruning search solution goes here
    # Returns a SINGLE action based off the results of the search
    
    raise NotImplementedError("Alpha Beta Pruning search not implemented")

  @staticmethod
  def expectimax_search(state, eval_fn, depth):
    # Question 3, your expectimax search solution goes here
    # Returns a SINGLE action based off the results of the search
    raise NotImplementedError("Expectimax search not implemented")

from .probability_agent import ProbabilityAgent
from utils import vector_to_direction
from probability import EchoGrid, DistributionModel
from state import *
from collections import Counter

class MarkovAgent(ProbabilityAgent):
  
  def __init__(self, valid_positions):
    super().__init__(valid_positions)
    self._echo_grid = EchoGrid()

  # Helpful Hints and Functions:
  # EchoGrid.get_echo_distribution() --> returns a distribution over all legal positions on the map as a dictionary
  #                                      where the key is a position and value is the probability of a mouse being there.
  # ProbabilityAgent.reset_thoughts() --> resets self._thoughts to be uniform (i.e. agent thinks all positions may have a mouse)
  # DistributionModel.normalize(distribution) --> normalizes the given distribution
  # DistributionModel.get_movement_distribution(state, agent_pos) --> returns a movement distribution for the given agent through it's position. 
  # GameState.copy() --> returns a copy
  # GameStateHandler.move_mouse(old_pos, new_pos) --> moves the mouse from the old position to the new position on the map
  
  # Instead of using a regular dictionary we recommend you use a Counter object to avoid needing to check for keys before using
  # them. Counters default any unseen key to the value of 0.

  # Remember to normalize brefore updating the agents thoughts and to look over only valid positions (use self._valid_positions).
  
  def listen(self, state):
    # Question 1, your MarkovAgent listen solution goes here.
    # For this method there is a special case to consider which happens when the distribution given by the EchoGrid
    # has only information which has NOT been seen before. In this case you must reset your current thought distribution
    # before continuing.
    raise NotImplementedError("MarkovAgent's Predict not implemented")    
    # Uncomment this when you start implementing
    self._echo_grid.update(state) # Do Not Remove, it is required to have the EchoGrid give accurate information
    
    # Write your code here
    flag = True
    thoughts = Counter(self._thoughts)
    echo_distribution = self._echo_grid.get_echo_distribution()
    for pos in self._valid_positions:
      if pos in thoughts:
        flag = False
        break
      
    if(flag):
      self.reset_thoughts()
      return
    for pos in self._valid_positions:
      if echo_distribution[pos] > 0:
        #can normalize
        #if thoughts[pos] == 0:
          #thoughts[pos] = echo_distribution[pos]
        #DistributionModel.normalize(thoughts)
        thoughts[pos] = self._thoughts[pos] * echo_distribution[pos]
      #else:
      #  thoughts[pos] = 0
    DistributionModel.normalize(thoughts)
    self._thoughts = thoughts
    return
    #reset thoughts nothing in common    
    
    
  # Implement the Time Lapse for HMM (Question 3)
  def predict(self, state):
    # Question 2, your MarkovAgent predict solution goes here.
    # Recall for the predict method we want to track one mouse down at a time by "predicting their moves". This should
    # be done through moving the mouse into positions on the map using this distribution to update your thoughts.
    # To avoid annoyances of state manipulation you should use a copy of the given state when you pretend to move the mouse
    # so that it does not effect the actual state.
    raise NotImplementedError("MarkovAgent's Predict not implemented")
    # Uncomment this when you start implementing
    self._echo_grid.update(state) # Do Not Remove, it is required to have the EchoGrid give accurate information

    # Write your code here
    
    copy_state = state.copy()
    for mouse in state._mice:
      return
    
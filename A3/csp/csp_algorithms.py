from .csp import CSP
from .csp_util import CSPUtil
from .variable import Variable

class CSPAlgorithms:

  # Here you will implement all the Constraint Solving Algorithms. Below are functions we think
  # will be helpful in your implementations. Please read the handout for specific instructions
  # for each algorithm.
  
  # Helpful Functions:
  # CSP.unassigned_variables() --> returns a list of the unassigned variables left in the CSP 
  # CSP.assignments() --> returns a dictionary which holds variable : value pairs
  # CSP.extract_unassigned() --> returns the next unassigned variable in line
  # CSP.assign(variable, value) --> assigns the given value to the given variable
  # CSP.unassign(variable) --> unassigns the given variable (value = None) 
  # CSP.constraints() --> returns a list of constraints for the CSP
  # CSP.num_unassigned() --> returns the number of unassigned variables
  # Variable.domain() --> returns the domain of the variable instance
  # Constraint.check(variables, assignments) --> returns True iff the given variables and their assignments
  #                                              satisfy the constraint instance
  
  @staticmethod
  def backtracking(csp):
    # Question 3, your backtracking algorithm goes here.

    # Returns an assignment of values to the variables such that the constraints are satisfied. None
    # if no assignment is found.
    
    if csp.num_unassigned() == 0:
      #print("wtf")
      return csp.assignments()
      #terminate after one solution found
          
    var = csp.extract_unassigned() #select next variable to assign
    for val in var.domain():
      csp.assign(var, val) #addes key:value pair into assignments for you
      constraintOK = True
      
      for constraint in csp.constraints():
        if not constraint.check(csp.variables(), csp.assignments()):
          constraintOK = False
          break 
      if constraintOK == True:
        return CSPAlgorithms.backtracking(csp) #recursion
    
    csp.unassign(var)                  #unassings var AND appends it to unassigned for u

    return
  
  #@staticmethod
  #def backtracking_helper(unassignedVars, constraints, assignments, csp):
    ##unassignedVars = csp.unassigned_variables()
    #if len(unassignedVars) == 0:
      ##for var in variables:
        ##print var.name(), " =", var.getValue()
        
      ##if allSolutions: #boolean, was set to true to print all sol
      ##  return # continue search to print all solutions
      ##else:
      #return assignments
      ##terminate after one solution found
          
    #var = csp.extract_unassigned() #unassignedVars.extract() #select next variable to assign
    #for val in var.domain():
      #csp.assign(var, val) #addes key:value pair into assignments for you
      #constraintOK = True
      
      #for constraint in constraints: #?
        ##if constraint.numUnassigned() == 0: #?
        #var_list = []
        #for key in assignments:
          #var_list.append(key)
        #if not constraint.check(var_list, assignments):         #?
          #constraintsOK = False
          #break 
      
      #if constraintOK:
        #backtracking(unassignedVars, constraints, assignments, csp) #recursion
    
    #csp.assign(var, None)                   #var.setValue(None) #undo assignemnt to vared vars
    #unassignedVars.append(var)   #unassignedvars.insert(var) restore var to unassigned
    
    #return None
    
  #@staticmethod
  #def constraintsOf(var, listOfConstraints):
    #temp = []
    #for constraint in listOfConstraints:
      #if var in constraint.
      
    
  @staticmethod
  def forward_checking(csp):
    # Question 4, your foward checking algorithm goes here.

    # Returns an assignment of values to the variables such that the constraints are satisfied. None
    # if no assignment is found.

    # Helpful Functions:
    # CSPUtil.forward_check(csp, constraint, var) --> returns True iff there is no DWO when performing
    #                                                 a forward check on the given constraint and variable.
    # CSPUtil.undo_pruning_for(var) --> undoes all pruning that was caused by forward checking the given variable.

    if csp.num_unassigned() == 0:
      return csp.assignments()
    var = csp.extract_unassigned() #select next variable to assign
    for val in var.active_domain(): #cuttent domain?
      csp.assign(var, val) #addes key:value pair into assignments for you
      noDWO = True
  
      for constraint in csp.constraints():  
        #if not constraint.check(var_list, csp.assignments()):
        if csp.num_unassigned() >= 1:
          if not (CSPUtil.forward_check(csp, constraint, var)):
            noDWO = False
            break
      if noDWO:
        return CSPAlgorithms.forward_checking(csp)
      CSPUtil.undo_pruning_for(var)
    csp.unassign(var)                  #unassings var AND appends it to unassigned for u
    return
      
  @staticmethod
  def gac(csp):
    # Question 6, your gac algorithm goes here.

    # Returns an assignment of values to the variables such that the constraints are satisfied. None
    # if no assignment is found.

    # Helpful Functions:
    # CSPUtil.gac_enfore(csp, var) --> returns True iff there is no DWO when attempting to enforce consistency
    #                                  on the constraints of the csp for the given variable.
    # CSPUtil.undo_pruning_for(var) --> undoes all pruning that was caused by forward checking the given variable.

    if csp.num_unassigned() == 0:
      print("wtf")
      return csp.assignments() #terminate after one solution found
          
    var = csp.extract_unassigned() #select next variable to assign
    for val in var.domain():
      csp.assign(var, val) #addes key:value pair into assignments for you
      noDWO = True
      if not CSPUtil.gac_enforce(csp, var):
        noDWO = False
      if noDWO:
        return CSPAlgorithms.gac(csp)
      CSPUtil.undo_pruning_for(var)
    
    csp.unassign(var)                  #unassings var AND appends it to unassigned for u

    return    

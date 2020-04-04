from collections import Counter
from .distribution_model import DistributionModel

class ParticleGrid:

  def __init__(self, valid_positions, particle_count=400):
    self._particle_count = particle_count
    self._valid_positions = valid_positions
    self.reset()

  def reset(self):
    # Question 3, your reset implementation goes here.
    # Recall this method resets the particle distribution to be a uniform distribution.
    # Make sure to have the particle distribution be a _Counter_ not a regular dictionary!
    
    self._particle_distribution = Counter()
    pos_len = len(self._valid_positions)
    for i in range(len(self._valid_positions)):
      pos = self._valid_positions[i]
      div = self._particle_count // pos_len
      for num in range(div):
        self._particle_distribution[pos] += 1 / self._particle_count
    
    
  def reweight_particles(self, distribution):
    # Qustion 4, your reweight particles implementation goes here.
    # This method focuses on updating the particle distribution by sampling the given distribution.
    # Remember to normalize the distribution!

    # For sampling use DistributionModel.sample_distribution(distribution, sample_amount) which will
    # return a list of legal positions got by sampling the given distribution.
    self._particle_distribution = Counter()
    if self._particle_count == 0:
      self.reset()
    else:
      samples = DistributionModel.sample_distribution(distribution, self._particle_count)
      iterator = samples
      for sample in range(len(samples)):
        appear = samples[sample]
        num_appear = 0
        counter = 0
        while(counter < len(samples)):
          if(iterator[counter] == appear):
            num_appear += 1
          counter += 1     

        self._particle_distribution[appear] = num_appear
    for leftover in distribution:
      if not leftover in self._particle_distribution:
        self._particle_distribution[leftover] = 0.0
    DistributionModel.normalize(self._particle_distribution)
      
  def get_particle_distribution(self):
    return self._particle_distribution

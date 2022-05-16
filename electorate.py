import numpy as np
from matplotlib import pyplot as plt
import random
from pprint import pprint

class Population:
    def __init__(self, blocs, num_issues):
        self.blocs = blocs
        self.num_issues = num_issues
        self.spectrum = []
        for bloc in blocs:
            for voter in bloc.voters:
                self.spectrum.append(voter.right_left_score)

class Bloc:
    def __init__(self, mean=0.0, sd=1.0, quantity=100):
        self.voters = []
        for i in range(quantity):
            self.voters.append(Voter(right_left_score=np.random.normal(mean, sd)))

class Voter:
    def __init__(self, right_left_score=0.0):
        self.right_left_score = right_left_score

    
if __name__=='__main__':
    republicans = Bloc(mean=1.0, sd=0.3, quantity=1000)
    democrats = Bloc(mean = -1.0, sd=0.3, quantity=5000)
    nonpartisans = Bloc(mean = 0.0, sd=1.0, quantity=500)
    smc_electorate = Population(blocs=(republicans, democrats, nonpartisans), num_issues=1)
    pprint(vars(smc_electorate))
    pprint(vars(republicans))
    pprint(vars(democrats))
    pprint(vars(nonpartisans))
    plt.hist(smc_electorate.spectrum, bins=50)
    plt.savefig('Electorage.png')

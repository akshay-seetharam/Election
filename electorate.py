import numpy as np
from matplotlib import pyplot as plt
import random
from pprint import pprint

class Electorate:
    def __init__(self, blocs, num_issues):
        self.blocs = blocs
        self.num_issues = num_issues
        self.spectrum = []
        for bloc in blocs:
            self.spectrum.append([])
            for voter in bloc.voters:
                self.spectrum[-1].append(voter.right_left_score)

    def plot(self):
        plt.hist(self.spectrum, stacked=True, density=True, bins=70, label=self.blocs)
        plt.legend()
        plt.title('Left-Right Spectrum of Electorate\n')
        plt.show()


class Bloc:
    def __init__(self, mean=0.0, sd=1.0, quantity=100, name=None):
        self.mean = mean
        self.sd = sd
        self.quantity = quantity
        self.name = name
        self.voters = []
        for i in range(quantity):
            self.voters.append(Voter(right_left_score=np.random.normal(mean, sd)))
            
    def __str__(self):
        return f'{self.name}: mean {self.mean}, sd {self.sd}, quantity {self.quantity}'

class Voter:
    def __init__(self, right_left_score=0.0):
        self.right_left_score = right_left_score

    
if __name__=='__main__':
    republicans = Bloc(mean=1.0, sd=0.3, quantity=1000, name="Republicans")
    democrats = Bloc(mean = -1.0, sd=0.3, quantity=5000, name="Democrats")
    independents = Bloc(mean = 0.0, sd=1.0, quantity=500, name="Independents")
    libs = Bloc(mean=1.3, sd=0.2, quantity=200, name="Libertarians")
    smc_electorate = Electorate(blocs=(republicans, democrats, independents, libs), num_issues=1)
    pprint(vars(smc_electorate))
    pprint(vars(republicans))
    pprint(vars(democrats))
    pprint(vars(independents))

    smc_electorate.plot()

import numpy as np
import matplotlib.pyplot as plt
import random
from pprint import pprint
import math

class Electorate:
    def __init__(self, blocs, issues={}, name=None):
        self.blocs = blocs
        self.issues = issues
        self.spectrum = []
        self.name = name
        for bloc in blocs:
            self.spectrum.append([])
            for voter in bloc.voters:
                self.spectrum[-1].append(voter.right_left_score)

        for issue in self.issues:
            for count, bloc in enumerate(self.blocs):
                bloc.add_issue(issue, mean=issues[issue][count][0], sd=issues[issue][count][1])

    def __str__(self):
        return f'{self.name}: Electorate comprising {str(self.blocs)}'
                
    def plot(self):
        plt.hist(self.spectrum, stacked=True, density=True, bins=70, label=self.blocs)
        plt.legend()
        plt.title('Left-Right Spectrum of Electorate\n')
        plt.savefig('imgs/spectrum.png')
        plt.figure()
        fig, axs = plt.subplots(2) # HARD CODE TODO
        for count, issue in enumerate(self.issues):
            axs[count].hist(self.issue_spectrum(issue), stacked=True, density=True, bins=70, label=[str(i)[:str(i).rindex(':')] for i in self.blocs])
            axs[count].set_title(f'{issue} Belief Distribution')
            axs[count].legend()
        plt.savefig('imgs/issues.png')
            
    def issue_spectrum(self, issue):
        spec = []
        for bloc in self.blocs:
            spec.append([])
            for voter in bloc.voters:
                spec[-1].append(voter.issues[issue])
        return spec


class Bloc:
    def __init__(self, mean=0.0, sd=1.0, quantity=100, name=None):
        self.mean = mean
        self.sd = sd
        self.quantity = quantity
        self.name = name
        self.voters = []
        for i in range(quantity):
            self.voters.append(Voter(right_left_score=np.random.normal(mean, sd), bloc=self))
            
    def __str__(self):
        return f'{self.name}: mean {self.mean}, sd {self.sd}, quantity {self.quantity}'

    def add_issue(self, issue, mean=0, sd=1):
        for voter in self.voters:
            voter.add_issue(issue, mean, sd)

class Voter:
    def __init__(self, right_left_score=0.0, tribalism=0.25, bloc):
        self.right_left_score = right_left_score
        self.tribalism = tribalism
        self.issues = {}
        self.bloc = bloc

    def __str__(self):
        return f'Voter with right/left score {self.right_left_score} and tribalism {self.tribalism}'

    def add_issue(self, issue, mean=0, sd=1): # TODO: Add weight
        self.issues[issue] = np.random.normal(mean, sd), np.random.random() # position, weight

    def rank(self, candidates):
        """
        given a list of candidates and their positions on issues, return a ranked list based on the voter's positions
        :param candidates:
        :return:
        """
        return 'sam to write'
    
if __name__=='__main__':
    republicans = Bloc(mean=1.0, sd=0.3, quantity=1000, name="Republicans")
    democrats = Bloc(mean = -1.0, sd=0.3, quantity=5000, name="Democrats")
    independents = Bloc(mean = 0.0, sd=1.0, quantity=500, name="Independents")
    libs = Bloc(mean=1.3, sd=0.2, quantity=200, name="Libertarians")
    greens = Bloc(mean=-1.2, sd=0.2, quantity=350, name="Greens")
    smc_electorate = Electorate(blocs=(republicans, democrats, independents, libs, greens), issues={'Abortion': [[-0.9, 0.1], [0.8, 0.2], [0.6, 0.4], [0.9, 0.1], [0.95, 0.09]], 'Gun Rights': [[0.95, 0.1], [-0.8, 0.3], [0.0, 0.5], [0.99, 0.05], [-0.7, 0.4]]})
    # pprint(vars(smc_electorate))
    # pprint(vars(republicans))
    # pprint(vars(democrats))
    # pprint(vars(independents))

    smc_electorate.plot()

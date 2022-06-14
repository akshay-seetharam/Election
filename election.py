from electorate import *
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

class Candidate:
    def __init__(self, name, right_left_score, issues, popularity):
        self.name = name
        self.right_left_score = right_left_score
        self.issues = issues
        self.popularity = popularity

    def __str__(self):
        return f'{self.name} is a candidate whose right/left score is {self.right_left_score}'


if __name__=='__main__':

    fileList = glob.glob('imgs/*.png')
    for file in fileList:
        try:
            os.remove(file)
        except Exception as e:
            print(e)
    print('imgs cleared of pngs') if glob.glob('imgs/*.png') == [] else print('img clearing failed')
    
    republicans = Bloc(mean=1.0, sd=0.3, quantity=1000, name="Republicans")
    democrats = Bloc(mean = -1.0, sd=0.3, quantity=5000, name="Democrats")
    independents = Bloc(mean = 0.0, sd=1.0, quantity=500, name="Independents")
    libs = Bloc(mean=1.3, sd=0.2, quantity=200, name="Libertarians")
    greens = Bloc(mean=-1.2, sd=0.2, quantity=350, name="Greens")

    blocs = [republicans, democrats, independents, libs, greens]

    issues = {'Abortion': [[-0.9, 0.1], [0.8, 0.2], [0.6, 0.4], [0.9, 0.1], [0.95, 0.09]], 'Gun Rights': [[0.95, 0.1], [-0.8, 0.3], [0.0, 0.5], [0.99, 0.05], [-0.7, 0.4]]}
    # dict = {key1:val1, key2:val2, ... }
    
    smc_electorate = Electorate(blocs=blocs, issues=issues)
    smc_electorate.plot()

    asterix = Candidate('asterix', 0.1, zip(issues.keys(), [0.5, 0.7])) # asterix is generally pro-choice and loves guns
    obelix = Candidate('obelix', 0.3, zip(issues.keys(), [-0.8, -0.4])) # obelix is a prude and is jealous of people who don't need the potion to be powerful
    getafix = Candidate('getafix', 0.4, zip(issues.keys(), [0.95, 0.88])) # getafix invented the pill and gunpowder (by accident)

    candidates = [asterix, obelix, getafix]
    for i in candidates:
        print(i)

    pprint('Rank for first Republican voter')
    pprint(republicans.voters[0].rank(candidates)) # return voter's preference for candidates
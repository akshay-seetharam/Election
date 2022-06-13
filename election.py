from electorate import *
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

class Candidate:
    pass


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

    asterix = Candidate('asterix', issues.keys())
    obelix = Candidate('obelix', issues.keys())
    getafix = Candidate('getafix', issues.keys())

    candidates = [asterix, obelix, getafix]

    pprint('Rank for first Republican voter')
    pprint(republicans.voters[0].rank(candidates)) # return voter's preference for candidates


    spectrum = smc_electorate.spectrum
    abortion = smc_electorate.issue_spectrum('Abortion')
    guns = smc_electorate.issue_spectrum('Gun Rights')

    plottables = [spectrum, abortion, guns]

    plt.clf()
    
    fig, axs = plt.subplots(ncols=plottables)

    pprint(spectrum)
    
    axs[0].plot(spectrum, label=str(blocs))
    plt.show()
    
    plt.savefig('imgs/3d.png')

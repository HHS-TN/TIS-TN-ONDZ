import numpy as np


def readArray(filename):
    '''
    lees een door saveArray opgeslagen array weer uit

    arugmenten:
        filename: filenaam waar de data staat
    '''

    data = np.loadtxt(filename, unpack=False, delimiter=',')
    return data


if __name__ == '__main__':
    # module wordt uitgevoerd
    
    import matplotlib.pyplot as plt
    
    # data opgeslagen met meerdere sensors tegelijk uitgelezen.
    data = readArray('meting_test1_1581080207.txt')
    time = data[:,0]
    gem = data[:,1:].mean(axis=1)
    std = data[:,1:].std(axis=1)
    print(std)
    dt = time[1:]-time[:-1]
    plt.errorbar(time,gem, yerr=100*std)
    plt.show()

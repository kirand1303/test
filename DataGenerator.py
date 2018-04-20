import numpy as np
import matplotlib.pylab as plt

class DataGenerator:

    def linear_fn_increase( self ):
        x = np.arange(100)
        delta = np.random.uniform(-10,10,size=(100,))
        y = .4 * x + 3 + delta
        print(y)
        plt.plot(x,y)
        plt.show()

    def linear_fn_decrease( self ):
        x = np.arange(100)
        delta = np.random.uniform(-10,10,size=(100,))
        y = .4 * x - 3 + delta
        print(y)
        plt.plot(x,y)
        plt.show()


d = DataGenerator()
#d.linear_fn_increase()
d.linear_fn_decrease()


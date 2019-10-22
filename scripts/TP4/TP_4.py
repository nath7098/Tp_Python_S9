import matplotlib.pyplot as plt
import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

if __name__ == '__main__':
    list_alea1 = random.sample(range(0, 100), 10)
    list_alea2 = random.sample(range(0, 100), 10)
    list_alea3 = random.sample(range(0, 100), 10)

    plt.subplot(221)
    plt.plot(list_alea1)
    plt.ylabel('Label 1')
    plt.xlabel('Test 1')

    plt.subplot(223)
    plt.plot(list_alea1,[1,2,6,5,4,8,56,78,82,94],"r--", linewidth=5)
    plt.plot(list_alea2,[1,2,6,5,4,8,56,78,82,94],"b", linewidth=3)
    plt.plot(list_alea3,[1,2,6,5,4,8,56,78,82,94],"g", linewidth=2,marker="*", label="EntrepriseBis")
    plt.ylabel('Temps')
    plt.xlabel('Argent')

    plt.legend()
    plt.annotate('Crash', xy=(60, 60), xytext=(160, 5.5),arrowprops={'facecolor':'black', 'shrink':0.02} )

    #Histogram
    plt.subplot(222)
    n, bins, patches = plt.hist(list_alea1, 50, density=1, facecolor='b', alpha=0.5)

    plt.xlabel('Mise')
    plt.ylabel(u'Probabilité')
    plt.axis([0, 100, 0,0.2])
    plt.grid(True)

    #Camember
    plt.subplot(224)
    name = ['-18', '18-25', '25-50', '50-60',"60","80","10-12", "1-8","100+","80-100"]
    data = list_alea1

    explode = (0, 0.15, 0, 0,0,0,0,0,0.15,0.65)
    plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    plt.show()

    #2D
    delta = 0.025
    x = np.arange(-3.0, 3.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
    Z = (Z1 - Z2) * 2

    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, Z)
    ax.clabel(CS, inline=1, fontsize=10)
    ax.set_title('Simplest default with labels')

    plt.show()

    #3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-2, 2)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=10, aspect=5)

    plt.show()
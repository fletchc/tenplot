import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button


inputs = ["1", "2"]

plt.ion()

while 1:
    print("Enter an option:\n \
1) Plot a constraint tensor.\n \
2) Quit.")

    option = input()
    if option not in inputs:
        print("Please select a valid option.")
        continue;

    if option == "2":
        print("Quitting...")
        break;

    print("Enter the size of the tensor:")
    n = int(input())

    # i, j, k, l = np.indices((n, n, n, n))
    i, j, k = np.indices((n, n, n))

    # indices are zero indexed which makes our calculations off by one
    # fixed by adding one to everything
    i = i + 1
    j = j + 1
    k = k + 1
    # l = l + 1
    lindex = 0
    print("Enter a constraint expression:")
    express = input()

    print("Generating plot...")

    # voxels = j > i + (n - k)
    voxels = eval(express)

    colors = np.empty(voxels.shape, dtype=object)
    colors[voxels] = 'blue'

    plt.subplots_adjust(bottom=0.25)

    axdim = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor="blue")
    dim_slider = Slider(
        ax=axdim,
        label='l index',
        valmin=1,
        valmax=n,
        valinit=1,
    )


    ax = plt.figure().add_subplot(projection='3d')
    ax.voxels(voxels, facecolors=colors, edgecolor='k')

    def update(val):
        lindex = round(val) - 1
        voxels = eval(express)
        colors = np.empty(voxels.shape, dtype=object)
        # print(voxels)
        colors[voxels] = 'blue'
        ax.voxels(voxels, facecolors=colors, edgecolor='k')
        plt.draw()

    dim_slider.on_changed(update)
    plt.show()

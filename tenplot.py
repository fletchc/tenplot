import matplotlib.pyplot as plt
import numpy as np


inputs = ["1", "2"]

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

    i, j, k = np.indices((n, n, n))

    # indices are zero indexed which makes our calculations off by one
    # fixed by adding one to everything
    i = i + 1
    j = j + 1
    k = k + 1
    print("Enter a constraint expression:")
    express = input()

    print("Generating plot...")

    # voxels = j > i + (n - k)
    voxels = eval(express)

    colors = np.empty(voxels.shape, dtype=object)
    colors[voxels] = 'blue'

    ax = plt.figure().add_subplot(projection='3d')
    ax.voxels(voxels, facecolors=colors, edgecolor='k')

    plt.show()

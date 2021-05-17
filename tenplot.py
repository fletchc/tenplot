import matplotlib.pyplot as plt
import numpy as np

n = 8
i, j, k = np.indices((n, n, n))

# indices are zero indexed which makes our calculations off by one
# fixed by adding one to everything
i = i + 1
j = j + 1
k = k + 1

# voxels = j > i + (n - k)
voxels = (i < j) & (j <= k)

colors = np.empty(voxels.shape, dtype=object)
colors[voxels] = 'blue'

ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolor='k')

plt.show()

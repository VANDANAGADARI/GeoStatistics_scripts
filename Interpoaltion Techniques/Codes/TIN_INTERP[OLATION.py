import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import LinearNDInterpolator

# --- Same input data ---
data_3x3 = np.array([
    [10, 20, 15],
    [25, 30, 20],
    [10, 15, 10]
])

# Known coordinates
x_orig, y_orig = np.meshgrid(np.arange(3), np.arange(3))
known_coords = np.stack([x_orig.ravel(), y_orig.ravel()], axis=-1)
known_values = data_3x3.ravel()

# Target grid (9x9)
grid_x, grid_y = np.meshgrid(np.linspace(0, 2, 9), np.linspace(0, 2, 9))

# --- TIN Interpolation ---
tin_interp = LinearNDInterpolator(known_coords, known_values)

data_9x9 = tin_interp(grid_x, grid_y)

# --- Plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.imshow(data_3x3, origin='lower', extent=[0, 2, 0, 2])
ax1.set_title("Original 3x3 Grid")

ax2.imshow(data_9x9, origin='lower', extent=[0, 2, 0, 2])
ax2.set_title("TIN Interpolated (Linear)")

plt.show()

print(np.round(data_9x9, 2))
import numpy as np
import matplotlib.pyplot as plt
from pykrige.ok import OrdinaryKriging

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

# Target grid axes (PyKrige expects 1D grid vectors)
grid_x_1d = np.linspace(0, 2, 9)
grid_y_1d = np.linspace(0, 2, 9)

# --- Ordinary Kriging ---
OK = OrdinaryKriging(
    known_coords[:, 0],
    known_coords[:, 1],
    known_values,
    variogram_model='linear',   # try: 'linear', 'power', 'gaussian', 'spherical', 'exponential'
    verbose=False,
    enable_plotting=False
)

Z_krig, variance = OK.execute('grid', grid_x_1d, grid_y_1d)

# --- Plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.imshow(data_3x3, origin='lower', extent=[0, 2, 0, 2])
ax1.set_title("Original 3x3 Grid")

ax2.imshow(Z_krig, origin='lower', extent=[0, 2, 0, 2])
ax2.set_title("Ordinary Kriging")

plt.show()

print("Kriging 9x9:\n", np.round(Z_krig, 2))
print("Kriging variance (uncertainty):\n", np.round(variance, 4))
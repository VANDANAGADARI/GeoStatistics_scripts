import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import SmoothBivariateSpline

# --- Input data (3x3 grid) ---
data_3x3 = np.array([
    [10, 20, 15],
    [25, 30, 20],
    [10, 15, 10]
])

# --- Generate known coordinates ---
x_orig, y_orig = np.meshgrid(np.arange(3), np.arange(3))

x = x_orig.ravel()
y = y_orig.ravel()
z = data_3x3.ravel()

# --- Target grid (9x9) ---
grid_x, grid_y = np.meshgrid(
    np.linspace(0, 2, 9),
    np.linspace(0, 2, 9)
)

# --- Spline Interpolation ---
# kx=2, ky=2 required because we only have 9 points
spline = SmoothBivariateSpline(x, y, z, kx=2, ky=2, s=0)

# Evaluate spline on grid
Z_spline = spline.ev(grid_x.ravel(), grid_y.ravel()).reshape(9, 9)

# --- Plotting ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Original data
ax1.imshow(data_3x3, origin='lower', extent=[0, 2, 0, 2])
ax1.set_title("Original 3x3 Grid")

# Interpolated result
ax2.imshow(Z_spline, origin='lower', extent=[0, 2, 0, 2])
ax2.set_title("Spline Interpolated (9x9)")

plt.tight_layout()
plt.show()

# --- Output ---
print("Spline Interpolated 9x9 Grid:\n")
print(np.round(Z_spline, 2))
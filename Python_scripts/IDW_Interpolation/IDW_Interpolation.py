import numpy as np
import matplotlib.pyplot as plt

# 1. Create the initial 3x3 matrix (Known data points)
data_3x3 = np.array([
    [10, 20, 15],
    [25, 30, 20],
    [10, 15, 10]
])

# Define coordinates for the 3x3 points (0, 1, 2)
x_orig, y_orig = np.meshgrid(np.arange(3), np.arange(3))
known_coords = np.stack([x_orig.ravel(), y_orig.ravel()], axis=-1)
known_values = data_3x3.ravel()

# 2. Define the 9x9 target grid (Interpolation points)
# We use linspace to get 9 points evenly spaced between 0 and 2
grid_x, grid_y = np.meshgrid(np.linspace(0, 2, 9), np.linspace(0, 2, 9))
target_coords = np.stack([grid_x.ravel(), grid_y.ravel()], axis=-1)

def idw_interpolate(source_coords, source_values, target_coords, p=2):
    """
    p: Power parameter. Higher values make the influence of 
       distant points move toward zero faster.
    """
    # Calculate distance between every target point and every source point
    # Resulting shape: (81 target points, 9 source points)
    dists = np.linalg.norm(target_coords[:, np.newaxis] - source_coords, axis=2)
    
    # Avoid division by zero at exact point locations
    dists = np.maximum(dists, 1e-9)
    
    # Calculate weights (1 / d^p)
    weights = 1 / (dists ** p)
    
    # Normalize weights so they sum to 1
    weights /= weights.sum(axis=1, keepdims=True)
    
    # Calculate the weighted average of the known values
    return np.dot(weights, source_values)

# 3. Run interpolation and reshape to 9x9
interpolated_flat = idw_interpolate(known_coords, known_values, target_coords)
data_9x9 = interpolated_flat.reshape(9, 9)

# --- Visualization ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.imshow(data_3x3, origin='lower', extent=[0, 2, 0, 2])
ax1.set_title("Original 3x3 Grid")

ax2.imshow(data_9x9, origin='lower', extent=[0, 2, 0, 2])
ax2.set_title("IDW Interpolated 9x9 Grid")

plt.show()

print("Final 9x9 Matrix:")
print(np.round(data_9x9, 2))
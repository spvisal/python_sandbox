#import numpy package 
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create numpy are of baseball
np_height_in = np.array(baseball)

# print out height in np_height_in
print(np_height_in)

# Convert np_height_in to np_height_m
np_height_m = np_height_in * 0.0254

# print the final result
print(np_height_m)

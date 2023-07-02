
import cv2
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# read and preproces the "galaxy.tif" image
image = cv2.imread('galaxy.tif')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 255

# set the number of iteration
t = 100

# Repeat the preprocessedd image t times along the third axis
imageT = np.repeat(image[:, :, np.newaxis], t, axis=2)

# Generate random samples from a Poisson distribution based on the repeated image
samples = stats.poisson.rvs(imageT)

# generate a binary image where each pixel is 1 
binaryImage = (samples >= 1).astype(float)

# estimate the parameter lambda using the MLE formula
lambdaHat = -np.log(1 - np.mean(binaryImage, axis=2))

# Display the estimted parameter lambda as a grayscale image
plt.imshow(lambdaHat, cmap='gray')
plt.show()


plt.savefig('./my_images/brain_398.png')

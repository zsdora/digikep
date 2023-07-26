import cv2
import numpy as np

# bemeneti kép beolvasása
img = cv2.imread("FCards_02_rs.jpg")

# csatornákra bontás
b, g, r = cv2.split(img)

# vörös területek meghat.
red_mask = (r > 120) & (g < 85) & (b < 200)

# fehér területek meghat.
white_mask = (r > 50) & (g > 50) & (b > 50) & (np.max(img, 2) - np.min(img, 2) <= 50)

# fekete területek meghat.
black_mask = (r < 120) & (g < 120) & (b < 120) & (np.max(img, 2) - np.min(img, 2) <= 25)

# eredménykép létrehoz.
result = np.zeros_like(img)
result[white_mask] = [255, 255, 255]
result[red_mask] = [0, 0, 255]
result[black_mask] = [0, 0, 0]
result[~(white_mask | red_mask | black_mask)] = [0, 255, 255]

# eredménykép és bemeneti kép megjel.
cv2.imshow("Vegeredmeny", result)
cv2.imwrite("vegeredmeny.jpg", result) # kep lementese fajlba
cv2.imshow("Bemeneti kep", img)

# SPACE lenyomására ablakok bezárása
cv2.waitKey(0)

cv2.destroyAllWindows()

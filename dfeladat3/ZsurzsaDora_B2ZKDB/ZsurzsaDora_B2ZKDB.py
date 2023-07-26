import cv2
import numpy as np

# 7x7 méretű, téglalap alakú strukturáló elem
structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

# Dilatáció, erózió, erózió, dilatáció lépéssorozat
img = cv2.imread("car_numberplate_rs.jpg", cv2.IMREAD_COLOR)
dilated = cv2.dilate(img, structuring_element, iterations=1)
eroded = cv2.erode(dilated, structuring_element, iterations=2)
final_dilated = cv2.dilate(eroded, structuring_element, iterations=1)

# Gauss simítás a képen 5x5 méretben, 4-es szórással
gauss_smoothed = cv2.GaussianBlur(final_dilated, (5, 5), sigmaX=4.0, sigmaY=4.0)

# Bontsa fel a képet különálló csatornákra,
# zöld és a kék csatornák maximum értékeit tartalm.
blue, green, red = cv2.split(gauss_smoothed)
max_bg = cv2.max(blue, green)

# Vonja ki a vörös csatorna képből az előző zöld-kék maximum eredményt
diff = cv2.subtract(red, max_bg)

# Küszöbölje a különbség képet 50 értéknél
thresh_value = 50
_, thresholded_img = cv2.threshold(diff, thresh_value, 255, cv2.THRESH_BINARY)

# Detektáljon összefüggő komponenseket és szűrje azokat
edges = cv2.Canny(thresholded_img, 100, 200)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
gray_img[edges > 0] = [0, 0, 255]

cv2.imwrite("ZsurzsaDora_B2ZKDB.png", gray_img)
cv2.imshow("Eredmeny", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

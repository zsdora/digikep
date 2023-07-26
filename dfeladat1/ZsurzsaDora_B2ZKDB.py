# Modul definíciók importálása
import cv2
import numpy as np

# 480x640x3 méretű Numpy tömb létrehozása RGB színes képnek
img = np.ndarray((480, 640, 3), np.uint8)
# Feltöltés fehér színnel
img.fill(255)

# készítő nevének kiiratása bal alsó sarokban (kep, 'Szoveg', (bazis_x, bazis_y),font,betumeret, (b, g, r), vastagsag)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'Zsurzsa Dora', [0, 470], font, 1, (255, 0, 0), 2)

# Kör rajzolása az (300, 150) középponttal, 40 sugárral, vörös színnel, kitöltve
cv2.circle(img, (300, 150), 40, (0, 0, 192), -1)

# test
cv2.line(img, (300, 190), (300, 300), (0, 0, 0), 5)

# jobb kar
cv2.line(img, (350, 190), (300, 250), (0, 0, 0), 3)

# bal kar
cv2.line(img, (300, 250), (240, 190), (0, 0, 0), 3)

# jobb láb
cv2.line(img, (300, 300), (350, 350), (0, 0, 0), 3)

# bal láb
cv2.line(img, (300, 300), (240, 350), (0, 0, 0), 3)

# Kép megjelenítése ablakban
cv2.imshow('img', img)

print('Billentyűzet-figyelő ciklus')
print('L: forgatás 90 fokkal balra')
print('R: forgatás 90 fokkal jobbra')
print('B: 1 képpontos külső keret rajzolása az aktuális képhez fekete színnel ')
print('E: 1 képpontnyi külső keret levágása ')
print('S: Képmátrix mentése')
print('Q: Kilépés')

while True:
    key = cv2.waitKey(1)
    cv2.imshow('img', img)

    # Kép forgatása 90 fokkal balra
    if key == ord('L'):
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Kép forgatása 90 fokkal jobbra
    elif key == ord('R'):
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Külső keret rajzolása az aktuális képhez fekete színnel
    elif key == ord('B'):
        img = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        print(img.shape)

    # Külső keret levágása
    elif key == ord('E'):
        img = img[1:-1, 1:-1]
        print(img.shape)

    # Képmátrix mentése
    elif key == ord('S'):
        cv2.imwrite("ZsurzsaDora_B2ZKDB.png", img)

    # Kilépés a végtelen ciklusból
    elif key == ord('Q'):
        break


# Kép mentése fájlba
cv2.imwrite('ZsurzsaDora_B2ZKDB.png', img)

# Összes ablak bezárása
cv2.destroyAllWindows()

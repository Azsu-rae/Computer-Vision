import cv2

img = cv2.imread("Images/compteur.jpeg")

height, width, channels = img.shape

print(img[0][0][0])
print(height)
print(width)
print(channels)

for i in range(0, width-2):
    for j in range(0, height-2):
        if img[j][i][0] < 97:
            img[j][i] = [0, 0, 0]
        else:
            img[j][i] = [255, 255, 255]


cv2.imshow('Image', img)
cv2.waitKey(0)

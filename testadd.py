import cv2
import numpy as np
import itertools
import time

def combine(bg, fg):
    for y, x in itertools.product(range(fg.shape[0]), range(fg.shape[1])):
        if np.sum(fg[y, x]):
            bg[y, x] = fg[y, x]
    return bg

start = time.time()

img1 = cv2.imread("images/small_test.png")
img2 = cv2.imread("images/small_test2.png")
img3 = cv2.imread("images/small_test3.png")

layers = [img1,img2,img3]
canvas = np.zeros(layers[0].shape, dtype='uint8')

bg = canvas
for layer in layers:
    bg = combine(bg,layer)

end = time.time()
print(end-start)
cv2.imshow("resultat",bg)
cv2.waitKey(0)


# --------------------

my_image1 = "./images/processed/lesouvriersdesde01sociuoft_0039-mask-zone-en-tête.png"
my_image2 = "./images/processed/lesouvriersdesde01sociuoft_0039-mask-zone-liste.png"
my_image3 = "./images/processed/lesouvriersdesde01sociuoft_0039-mask-zone-séparateur.png"
my_image4 = "./images/processed/lesouvriersdesde01sociuoft_0039-mask-zone-texte.png"

fg = cv2.imread(my_image2)
bg = cv2.imread(my_image4)

print(bg.shape)
print(fg.shape)

counter = 0
for y,x in itertools.product(range(fg.shape[0]), range(fg.shape[1])):
    if np.sum(fg[y,x]):
        bg[y,x] = fg[y,x]
        counter += 1

print("changed {} pixels".format(counter))
end = time.time()
print(end-start)
get_glimpse(bg)
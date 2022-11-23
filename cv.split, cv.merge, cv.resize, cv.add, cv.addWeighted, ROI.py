import cv2

img = cv2.imread('Messi.jpg')
img2 = cv2.imread('Pomegranate.jpg')


print(img.shape)
print(img.size)
print(img2.size)

print (img.dtype)

b,g,r = cv2.split(img)

img = cv2.merge((b,g,r))

#ROI : region of interest
# ball = img[280:340  , 330:390  ] #y2,y1   & x2,x1
# img[273:333 , 100:160 ] = ball


#resize 
img = cv2.resize(img , (512,512))
img2 = cv2.resize(img2 , (512,512))

#Photo merging
#dst = cv2.add(img,img2)
dst = cv2.addWeighted(img, .8 , img2 , .2 , 10)


cv2.imshow('frame', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
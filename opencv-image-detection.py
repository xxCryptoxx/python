import cv2

# set up
cv2.namedWindow('detection', cv2.WINDOW_NORMAL)

# input
img = cv2.imread('img1.jpg')
 
# classifiers
car_classifier = 'cars.xml'
ped_classifier = 'pedestrians.xml'

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

car_tracker = cv2.CascadeClassifier(car_classifier)
ped_tracker = cv2.CascadeClassifier(ped_classifier)

# apply to image
cars = car_tracker.detectMultiScale(gray_img)
peds = ped_tracker.detectMultiScale(gray_img)

# process with opencv
print(cars)
print(peds)

# box them, knock them out
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
    cv2.putText(img, 'car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

for (x, y, w, h) in peds:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
    cv2.putText(img, 'person', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# display results
cv2.imshow('detection', img)
cv2.waitKey()
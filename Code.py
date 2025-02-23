import cv2
import numpy
Circles = cv2.imread("Circles.jpg")
Ghost = cv2.imread("Ghost.png")
greyGhost = cv2.cvtColor(Ghost, cv2.COLOR_BGR2GRAY)
Parameters = cv2.SimpleBlobDetector_Params()
Parameters.filterByCircularity = True
Parameters.minCircularity = 0.5
Parameters.filterByInertia = True
Parameters.minInertiaRatio = 0.1
Detector = cv2.SimpleBlobDetector_create(Parameters)
Points = Detector.detect(Circles)
print(Points)
blobs = cv2.drawKeypoints(Circles, Points, numpy.zeros((1,1)), (200, 75, 5), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("window", blobs)
cv2.waitKey(0)
"""
detection = cv2.HoughCircles(greyGhost, cv2.HOUGH_GRADIENT, 1, 10, param1 = 100, param2 = 50, minRadius = 20, maxRadius = 100)
print(detection)
detection = numpy.uint16(numpy.around(detection))
print(detection)
for i in detection[0,:]:
    print(i)
    x = i[0]
    y = i[1]
    r = i[2]
    circle = cv2.circle(Ghost, (x, y), r, (0, 255, 0), 5)
    cv2.imshow("window", circle)
cv2.waitKey(0)
greyCircles = cv2.cvtColor(Circles, cv2.COLOR_BGR2GRAY)
circleDetection = cv2.HoughCircles(greyCircles, cv2.HOUGH_GRADIENT, 1, 1, param1 = 100, param2 = 50, minRadius = 1, maxRadius = 200)
print(circleDetection)
circleDetection = numpy.uint16(numpy.around(circleDetection))
print(circleDetection)
for i in circleDetection[0,:]:
    print(i)
    x = i[0]
    y = i[1]
    r = i[2]
    circle2 = cv2.circle(Circles, (x, y), r, (0, 255, 0), 5)
    cv2.imshow("window", circle2)
cv2.waitKey(0)
"""
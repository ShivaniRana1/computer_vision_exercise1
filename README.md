# computer_vision_exercise1

In task 1: 
I have contoured each object present in Image and find out the line contour which is contours[6],contours[7],contours[1],contours[0] and which this extract 
height of each line which is provided by minAreaRect. After that I have stored each line's height in a list and compare individual line's height with list
and give number according to line's height. The final picture is saved as numbering_image.png

In task 2:
I contoured each rectangle and find it's center(k), width and height, angle of rotation(theta) using minAreaRect. After that , I have used warpAffine function to rotate
image about theta angle with center of rotation as k. Now we can seperately get individual aligned image in separate image file i.e. straight_image1.png

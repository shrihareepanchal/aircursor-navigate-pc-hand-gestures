import math

def get_landmark_position(handLms,shape):
    h,w,_ = shape  # shape of the image frame(height,width,channel(optional))
    landmarks = [] # empty list of landmarks to store x,y cordinates
    for lm in handLms.landmark:
        landmarks.append((int(lm.x * w), int(lm.y * h)))
    return landmarks

def get_finger_distance(p1, p2): # calculating the Ecludian distance between two fingertips
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def smooth_coords(curr,prev_x,prev_y,factor): # curr-> current position, prev_x,prev_y -> last position of cursor
    x = prev_x + (curr[0] - prev_x) / factor  # moves cursor from previous to current target
    y = prev_y + (curr[1] - prev_y) / factor
    return int(x), int(y)




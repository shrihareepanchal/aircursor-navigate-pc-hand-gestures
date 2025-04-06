from utils import get_finger_distance

def detect_click(landmarks, threshold=30): # max distance bet finger to register a tip
    index_tip = landmarks[8] # tip of index finger
    thumb_tip = landmarks[4] # tip of thumb
    dist = get_finger_distance(index_tip,thumb_tip)
    return dist < threshold # if dist bet two finger is small than threshold then click


    


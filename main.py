import cv2
import pyautogui
import mediapipe as mp
from utils import get_landmark_position, get_finger_distance, smooth_coords
from gestures import detect_click
from config import SMOOTHING

pyautogui.FAILSAFE = False # execution stops if mouse is moved to the top-left corner

# Camera and Screen diamentions
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size() # getting screen width and height for hand position

# Setup Mediapipe hand tracking
mp_hands = mp.solutions.hands 
hands = mp_hands.Hands(max_num_hands=1) # tracks only one hand
mp_draw = mp.solutions.drawing_utils # darw landmarks and connections on the video frame

prev_x, prev_y = 0, 0 # stores previous cordinates

# loop for Real time detection
while True:
    success, frame = cap.read()
    if not success or frame is None:
        print("Frame capture failed.")
        continue

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    # Show and handle quit
    try:
        cv2.imshow("AirCursor", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print("Error displaying frame:", e)
        break


    # detecting hands
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            
            #Landmark Extraction & Mouse Mapping
            lm_list = get_landmark_position(handLms, frame.shape)
            if lm_list:
                index_x, index_y = smooth_coords(lm_list[8], prev_x, prev_y, SMOOTHING)
                prev_x, prev_y = index_x, index_y
                
                #Move Cursor & Detect Click
                screen_x = int(index_x * screen_w / frame.shape[1])
                screen_y = int(index_y * screen_h / frame.shape[0])
                pyautogui.moveTo(screen_x, screen_y)

                if detect_click(lm_list):
                    pyautogui.click()
            
            #Draw Hand Landmarks on Frame
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    #Display the Frame
    cv2.imshow("AirCursor", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

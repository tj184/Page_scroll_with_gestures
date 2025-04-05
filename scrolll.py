import cv2
import mediapipe as mp
import pyautogui
import time
import webbrowser

webpage_url = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\RUN rmd.py\\Page scrol\\test_page.html"
webbrowser.open_new_tab(webpage_url)

print("Opening test page... Please wait 5 seconds.")
time.sleep(5)

pyautogui.click(x=500, y=500)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            
            if index_finger_tip.y < wrist.y:
                print("Scroll Down")
                pyautogui.scroll(-500)
            elif index_finger_tip.y > wrist.y:
                print("Scroll Up")
                pyautogui.scroll(500)
    
    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

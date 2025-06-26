import pyautogui
import keyboard
import time

def reactionTest():
    pyautogui.moveTo(930, 420, duration=0.1)
    pyautogui.leftClick()
    while True:
        if pyautogui.pixel(930,420) == (75, 219, 106):
            print('green')
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.2
            pyautogui.leftClick()
        else:
            print('waiting')
            time.sleep(1)
        
        if keyboard.is_pressed('esc'):
            break

        if pyautogui.pixel(1087, 589) == (149, 195, 232):
            pyautogui.moveTo(1087, 589, duration=0.2)
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.4
            pyautogui.leftClick()

def cursor():
    while True:
        if keyboard.is_pressed('p'):
            pos = pyautogui.position()
            colour = pyautogui.pixel(1087, 589)
            print('Position ', pos)
            print('Colour ', colour)
            break

def sequence():
    search_region = (768, 281, 362, 359) 
    scan_area = [
        (827, 340), (950, 340), (1080, 340),
        (810, 465), (950, 465), (1080, 465),
        (810, 590), (950, 590), (1080, 590)
    ]
    target_colour = (37, 115, 193)

    print("Starting color scan. Press ESC to exit.")
    while True:
        for pos in scan_area:
            pixel_colour = pyautogui.pixel(pos[0], pos[1])
            if pixel_colour == target_colour:
                print(f"Found target colour at {pos}! Clicking.")
                pyautogui.moveTo(pos[0], pos[1])

        if keyboard.is_pressed('esc'):
            print("ESC pressed, exiting.")
            break
        
        time.sleep(0.1)

reactionTest()
cursor()
sequence()
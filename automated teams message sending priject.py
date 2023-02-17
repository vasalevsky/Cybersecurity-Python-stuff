import time
import pyautogui

def send_message():
    # open Microsoft Teams
    pyautogui.hotkey('win')
    pyautogui.typewrite('teams (work or school)')
    time.sleep(3)
    pyautogui.press('enter')
    print("Opened Microsoft Teams")
    time.sleep(3)
    # wait for Teams to load
    image1 = r"C:\Users\kholo\OneDrive\Documents\PSEO\Pyton\chat icon ss.png"
    image2 = r"C:\Users\kholo\OneDrive\Documents\PSEO\Pyton\chat icon ss1.png"
    chat_icon = pyautogui.locateCenterOnScreen(image1, confidence=0.8) or pyautogui.locateCenterOnScreen(image2,
                                                                                                         confidence=0.8)

    if chat_icon:
        pyautogui.click(chat_icon)
        print("Clicked on the chat button")
        time.sleep(4)
    else:
        print("Could not find the chat button on the screen")

    try:
        person_icon = pyautogui.locateOnScreen(r"C:\Users\kholo\OneDrive\Documents\PSEO\Pyton\thelma ss.png", confidence=0.9)
        pyautogui.click(person_icon)
        print("i clicked on person")
        time.sleep(3)
    except Exception as e:
        print("Error while trying to locate and click on the person icon: ", e)
        return



    pyautogui.typewrite("hey how's your day going")
    print("Typed the message")
    time.sleep(3)
    pyautogui.press('enter')
    print("Sent the message")

send_message()

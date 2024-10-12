import pyautogui
import time


# Function to wait for an image to appear and click or double-click it
def wait_and_click(image_path, confidence=0.7, wait_time=0.5, action_delay=0.25, click_delay=5, move_duration=0.5, double_click=False):
    print(f"Waiting for image: {image_path}")
    while True:
        try:
            result = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if result is not None:
                center = pyautogui.center(result)
                center_x = int(center.x)
                center_y = int(center.y)
                
                print(f"Found image at ({center_x}, {center_y}). {'Double-clicking' if double_click else 'Clicking'} now.")
                pyautogui.moveTo(center_x, center_y, move_duration, pyautogui.easeOutQuad)
                
                # Wait for a short time before clicking
                time.sleep(action_delay)
                
                # Perform either a click or double-click
                if double_click:
                    pyautogui.doubleClick()
                else:
                    pyautogui.click()
                
                # Optionally wait after clicking
                time.sleep(click_delay)
                break
            else:
                # If image not found, print message and wait before trying again
                print("Image not found. Retrying in 0.5 seconds...")
                time.sleep(wait_time)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying in 0.5 seconds...")
            time.sleep(wait_time)

# Main script to locate and interact with buttons in sequence

# 1. Wait and double-click Jagex Launcher icon
wait_and_click(r'mouseMoverImages\RSicon.png', confidence=0.7, click_delay=0.5, double_click=True)

# 2. Wait and click the PLAY button
wait_and_click(r'mouseMoverImages\play.png', confidence=0.7, click_delay=10)

# 3. Wait and click the click-to-switch button
wait_and_click(r'mouseMoverImages\clicktoswitch.png', confidence=0.6, click_delay=0.5)

# 4. Wait and click the world number button (world 433)
wait_and_click(r'mouseMoverImages\world433.png', confidence=0.7, click_delay=0.5)

# 5. Wait and click the play now button
wait_and_click(r'mouseMoverImages\playnow.png', confidence=0.7, click_delay=0.5)

# 6. Wait and click the click-to-play button
wait_and_click(r'mouseMoverImages\clicktoplay.png', confidence=0.7, click_delay=5)

# 7. Starts fishing for shrimps 
wait_and_click(r'mouseMoverImages\shrimps.png', confidence=0.7)

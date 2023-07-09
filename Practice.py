import pyautogui
import time

# Move the cursor to a specific coordinate (x, y) with a duration
def move_cursor(x, y, duration=0.5):
    pyautogui.moveTo(x, y, duration=duration)

# Move the cursor relative to its current position with a duration
def move_cursor_relative(dx, dy, duration=0.5):
    pyautogui.move(dx, dy, duration=duration)

# Click the mouse at the current cursor position
def click():
    pyautogui.click()

# Double-click the mouse at the current cursor position
def double_click():
    pyautogui.doubleClick()

# Example usage
move_cursor(500, 500)  # Move cursor to (500, 500)
time.sleep(1)  # Pause for 1 second
move_cursor_relative(100, -50)  # Move cursor 100 pixels right and 50 pixels up from the current position
time.sleep(1)  # Pause for 1 second
click()  # Click the mouse at the current cursor position
time.sleep(1)  # Pause for 1 second
double_click()  # Double-click the mouse at the current cursor position

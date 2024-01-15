import cv2
import pyautogui
import numpy as np

# 设置截取屏幕的左上角坐标和宽高
x, y, width, height = 0, 0, 800, 600

while True:
    # 使用 pyautogui 截取屏幕指定区域
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    frame = np.array(screenshot)

    # 将截取的屏幕转为 BGR 格式
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # 显示截取的画面
    cv2.imshow('Screen Capture', frame)

    # 检测按键，按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

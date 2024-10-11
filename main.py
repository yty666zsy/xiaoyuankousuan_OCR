import pytesseract
from PIL import ImageGrab
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

# 配置 tesseract 的可执行文件路径
pytesseract.pytesseract.tesseract_cmd = r'E:\tools\software\tesseract\tesseract.exe'

# OCR 识别数字并保存截图
def recognize_digits(area_coords, screenshot_name):
    # 截取数字区域
    screenshot = ImageGrab.grab(bbox=(area_coords[0][0], area_coords[0][1], area_coords[1][0], area_coords[1][1]))

    # 保存截图
    screenshot.save(screenshot_name)  # 保存截图为指定文件名

    # 第一套配置
    custom_oem_psm_config = '--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
    result = pytesseract.image_to_string(screenshot, config=custom_oem_psm_config).strip()

    # 过滤只包含数字的部分
    result = ''.join(filter(str.isdigit, result))

    # 尝试将识别结果转换为整数
    if result:
        try:
            return int(result)
        except ValueError:
            print(f"无法将识别结果 '{result}' 转换为整数")
            return None
    else:
        print("未识别到数字，尝试使用备用配置进行识别")

        # 第二套配置：使用稍微不同的模式
        digits = pytesseract.image_to_string(screenshot, config='--psm 6 --oem 3').strip()
        digits = ''.join(filter(str.isdigit, digits))

        if digits:
            try:
                return int(digits)
            except ValueError:
                print(f"备用方案识别结果 '{digits}' 仍无法转换为整数")
                return None
        else:
            print("仍未识别到数字，尝试使用第三套方案")

            # 第三套配置：改变识别模式为更宽松的模式
            third_config = '--psm 11 --oem 3 -c tessedit_char_whitelist=0123456789'
            third_attempt = pytesseract.image_to_string(screenshot, config=third_config).strip()
            third_attempt = ''.join(filter(str.isdigit, third_attempt))

            if third_attempt:
                try:
                    return int(third_attempt)
                except ValueError:
                    print(f"第三套方案识别结果 '{third_attempt}' 无法转换为整数")
                    return None
            else:
                print("第三套方案也未能识别到数字")
                return None


# 比较两个数字大小
def compare_digits(digit1, digit2):
    try:
        num1 = int(digit1)
        num2 = int(digit2)

        if num1 > num2:
            return "大于"
        elif num1 < num2:
            return "小于"
        else:
            return "等于"
    except ValueError:
        return "识别的数字格式有误，无法进行比较。"

# 在绘图区域内模拟鼠标绘制符号
def draw_symbol(symbol, draw_area):
    # 获取绘图区域的起始坐标
    start_x, start_y = draw_area[0]

    # 将鼠标移动到绘图区域的起始位置
    pyautogui.moveTo(start_x, start_y)

    # 模拟鼠标点击
    pyautogui.mouseDown()  # 按下鼠标左键

    if symbol == "<":
        # 绘制 "<" 字符
        pyautogui.moveRel(-60, 60)  # 左下移动
        pyautogui.moveRel(60, 0)  # 向右移动
    else:
        # 绘制符号“>”的代码，右下向左
        pyautogui.moveRel(60, 60)  # 右下移动
        pyautogui.moveRel(-60, 0)  # 向左移动

    pyautogui.mouseUp()  # 松开鼠标左键

def process_questions(num_questions):
    # 假设 selector.coordinates 是你从鼠标区域选择器中得到的数字区域坐标
    selector = {
        'coordinates': [(1133, 473), (1286, 632), (1475, 495), (1608, 640)]  # 示例坐标，用你实际选择的坐标替换
    }

    # 添加延时 2 秒
    time.sleep(2)

    for i in range(num_questions):
        # 假设你有两个数字区域
        digit_area_1_coords = selector['coordinates'][:2]
        digit_area_2_coords = selector['coordinates'][2:]

        # 识别两个区域的数字，并保存对应的截图
        digit1 = recognize_digits(digit_area_1_coords, f"./img/digit_area_1_{i}.png")
        digit2 = recognize_digits(digit_area_2_coords, f"./img/digit_area_2_{i}.png")

        print(f"识别出的第一个数字: {digit1}")
        print(f"识别出的第二个数字: {digit2}")

        # 对比两个数字的大小
        result = compare_digits(digit1, digit2)
        print(result)

        # 根据比较结果绘制相应的符号
        symbol = "<" if result == "小于" else ">"

        # 绘制符号在指定的绘图区域内
        draw_area_coords = [(1200, 1120), (1565, 1341)]  # 示例绘图区域坐标
        print(f"在绘图区域绘制符号: {symbol}")
        draw_symbol(symbol, draw_area_coords)

        # 在每次循环之间添加0.5秒的延时
        time.sleep(0.5)

    messagebox.showinfo("完成", "所有题目已处理完毕。")

# GUI 界面
def start_processing():
    try:
        num_questions = int(entry.get())
        process_questions(num_questions)
    except ValueError:
        messagebox.showerror("错误", "请输入一个有效的数字。")

# 创建主窗口
root = tk.Tk()
root.title("OCR 数字比较")
root.geometry("300x150")

# 创建标签和输入框
label = tk.Label(root, text="请输入题目个数:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

# 创建开始按钮
start_button = tk.Button(root, text="开始处理", command=start_processing)
start_button.pack(pady=20)

# 启动主循环
root.mainloop()

import pyautogui
import tkinter as tk

def show_mouse_position():
    root = tk.Tk()
    root.title("鼠标位置监视")
    root.geometry("300x100")

    position_label = tk.Label(root, text="鼠标位置: x=0, y=0", font=("Arial", 16))
    position_label.pack(pady=20)

    def update_position():
        # 打印调试信息，确保该函数被调用
        print("Updating position...")
        x, y = pyautogui.position()
        print(f"当前鼠标位置: x={x}, y={y}")
        position_label.config(text=f"鼠标位置: x={x}, y={y}")
        # 通过 root.after 设置定时调用
        root.after(100, update_position)

    # 启动第一次位置更新
    update_position()
    root.mainloop()

# 调用函数以启动GUI和鼠标位置监控
show_mouse_position()
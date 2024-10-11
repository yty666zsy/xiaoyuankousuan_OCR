# xiaoyuankousuan_OCR
# 基于OCR识别的小猿口算



- **编译器版本**: Python 3.12

## 项目结构

```
.
├── README.md                             # 使用说明文档
├── get_xy_mouse.py                       # 获取鼠标坐标的库
├── main.py                               # 主程序
├── img                                   # 文件夹，用于保存特定区域识别的图片
│   └── ...                               # 分割保存的图片
```

## 使用方法

### 一、环境安装

```bash
git clone https://github.com/yty666zsy/xiaoyuankousuan_OCR.git
cd xiaoyuankousuan_OCR
conda create --name xiaoyuankousuan python=3.12
conda activate xiaoyuankousuan
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyautogui opencv-python pillow pytesseract numpy
```

### 二、win的Tesseract 配置

- 下载地址: [Tesseract 官方下载](https://github.com/UB-Mannheim/tesseract/wiki)
- 配置环境路径path
- **配置 Tesseract 的可执行文件路径**:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

#### 验证 Tesseract 安装

在**命令行**(Windows)中输入以下命令，验证是否正确安装:

```bash
tesseract -v
```

如果成功显示版本信息，则安装成功。

### 三、使用流程

1. **运行get_xy_mouse.py**:
   在命令行中运行 `main.py`,获取鼠标位置，记录下来，需要记录四个位置（左上1，右下1；左上2，右下3），分别是识别区域的两个位置的数字，接下来继续记录绘制区域的坐标，同上（左上3，右下3）.

   ```bash
   python get_xy_mouse.py
   ```

   

2. **修改main函数**:
   在 `main.py` 中，根据实际需要调整以下参数：

   （1）上述的识别区域的位置

   ![image-20241011102214659](C:\Users\yuzai\AppData\Roaming\Typora\typora-user-images\image-20241011102214659.png)

   （2）绘图坐标区域

   ![image-20241011102335593](C:\Users\yuzai\AppData\Roaming\Typora\typora-user-images\image-20241011102335593.png)

   **3.运行main函数**

   ```
   python main.py
   ```

   4.输入需要作答的题目个数开始，本项目使用OCR仍旧有bug，有些数字识别不出来，正在优化

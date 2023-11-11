#เรียกใช้ ไลบารี่หลายตัวเพื่อสร้างหน้าต่าง เปลี่ยน resolution ต่างๆ 
import tkinter as tk
import win32api
import win32con
import win32gui
from PIL import Image, ImageTk
import urllib.request, io

#สร้างฟังชั่น เพื่อให้ปุ่มเรียกใช้ full hd
def change_resolution_full_hd():
    # ตั้งค่า full hd
    devmode = win32api.EnumDisplaySettings(None, 0)
    devmode.PelsWidth, devmode.PelsHeight = 1920, 1080
    devmode.DisplayFrequency = 144
    win32api.ChangeDisplaySettings(devmode, 0)

#สร้างฟังชั่น เพื่อให้ปุ่มเรียกใช้ แต่เป็นขนาด 1280*720
def change_resolution_hd():
    # ตั้งค่า hd 120hz
    devmode = win32api.EnumDisplaySettings(None, 0)
    devmode.PelsWidth, devmode.PelsHeight = 1280, 720
    devmode.DisplayFrequency = 120
    win32api.ChangeDisplaySettings(devmode, 0)

# สร้างหน้าต่าง tkinter
root = tk.Tk()
root.resizable(width=False, height=False)
root.title("Change Resolution") # กำหนดชื่อหน้าต่าง tkinter

import url
#ผมสร้างตัวแปร  url ให้รับ ภาพมาจาก url 
url = url.url
image_bytes = urllib.request.urlopen(url).read()
image = Image.open(io.BytesIO(image_bytes))

# สร้างปุ่มในหน้าต่าง ชื่อ full hd
btn_full_hd = tk.Button(root, text="Full HD", command=change_resolution_full_hd)
btn_full_hd.pack()

# สร้างปุ่ม hd 120hz
btn_hd_120hz = tk.Button(root, text="HD 120Hz", command=change_resolution_hd)
btn_hd_120hz.pack()

# เพื่อให้หน้าต่างมีขนาดเท่ากับรูปภาพครับ
window_width, window_height = image.size
root.geometry("{}x{}".format(window_width, window_height))

# สร้าง image label
tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=tk_image)
image_label.pack()
label = tk.Label(root, image=tk_image)
label.pack()
root.mainloop()

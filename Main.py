import customtkinter
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import os
# 设置主题
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# 创建主窗口
root = customtkinter.CTk()
root.geometry("400x300")
root.title("TXT OpenER")

# 创建密码输入框
entry_password = customtkinter.CTkEntry(master=root, placeholder_text="请输入密码")
entry_password.pack(pady=12, padx=10)

# 创建下载按钮
download_button = customtkinter.CTkButton(master=root, text="See Now", command=lambda: download_and_display(entry_password.get()))
download_button.pack(pady=12, padx=10)

# 创建进度条
progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=12, padx=10)

# 创建文本框显示下载内容
text_box = customtkinter.CTkTextbox(master=root)
text_box.pack(fill="both", expand=True)

def download_and_display(password):
    if password == "111012":  # 这里应该替换为更安全的密码验证方式
        file_path = "https://down.aoo.ink/ac.txt"  # 替换为你的文件路径
        try:
            response = requests.get(file_path, stream=True)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))
            progress_bar['maximum'] = total_size

            with open('temp.txt', 'wb') as f:  # 创建临时文件，用于显示进度
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        progress_bar['value'] += len(chunk)
                        root.update_idletasks()

            # 将临时文件内容读取到内存并显示在文本框中
            with open('temp.txt', 'r', encoding='utf-8') as f:  # 这里假设文件编码为 UTF-8
                text = f.read()
                text_box.delete('1.0', tk.END)
                text_box.insert('1.0', text)

            # 删除临时文件
            os.remove('temp.txt')

            messagebox.showinfo("提示", "文件内容已显示在文本框中")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("错误", f"下载失败：{e}")
    else:
        messagebox.showerror("错误", "密码错误！")

root.mainloop()

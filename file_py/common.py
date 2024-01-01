from tkinter import filedialog


class Variable:
    user_df = None  # 保存所有用户的信息
    user_zd = None  # 保存当前登录用户的信息
    ip = None  # 保存服务器ip
    prodDate_df = None  # 保存生产日期ate

def select_file(prompt_message):  # 选择文件 prompt_message 提示信息
    return filedialog.askopenfilename(filetypes=[(prompt_message, '*.xlsx')])

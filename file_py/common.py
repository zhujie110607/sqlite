from tkinter import filedialog

def select_file(prompt_message): # 选择文件 prompt_message 提示信息
    return filedialog.askopenfilename(filetypes=[(prompt_message, '*.xlsx')])



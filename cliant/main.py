import tkinter as tk

root = tk.Tk()
tk.Label(master=root, text="文字").pack()
tk.Label(master=root, bitmap='warning').pack()

if __name__ == '__main__':
    root.mainloop()

import tkinter as tk


def test_func():
    print("this is test func")


class TopMenus(tk.Menu):

    def add_setting_menus(self):
        setting_menu = tk.Menu(master=self, tearoff=0)
        self.add_cascade(label="设置", menu=setting_menu)
        setting_menu.add_command(label="屏幕广播模式", command=test_func)
        setting_menu.add_command(label="简单录屏模式", command=test_func)

    def show(self):
        self.add_setting_menus()
        self.master.config(menu=self)

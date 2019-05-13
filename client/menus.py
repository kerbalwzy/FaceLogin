from tkinter import Menu
from videoFrame import VideoFrame
from utils import single_instance


def test_func():
    print("this is test func")


@single_instance
class TopMenus(Menu):

    def __start_preview(self):
        self.master.video_frame.start_preview()
        self.setting_menu.entryconfig("开启预览", state="disable")
        self.setting_menu.entryconfig("关闭预览", state="normal")

    def __stop_preview(self):
        self.master.video_frame.stop_preview()
        self.setting_menu.entryconfig("开启预览", state="normal")
        self.setting_menu.entryconfig("关闭预览", state="disable")

    def add_setting_menus(self):
        setting_menu = Menu(master=self, tearoff=0)
        self.add_cascade(label="功能", menu=setting_menu)

        setting_menu.add_command(label="开启预览",
                                 command=lambda: self.__start_preview())

        setting_menu.add_command(label="关闭预览",
                                 command=lambda: self.__stop_preview(),
                                 state="disable")

        setting_menu.add_separator()
        setting_menu.add_command(label="开启传输",
                                 command=test_func)

        setting_menu.add_command(label="关闭传输",
                                 command=test_func,
                                 state="disable")

        self.setting_menu = setting_menu

    def add_user_menus(self):
        user_menu = Menu(master=self, tearoff=0)
        self.add_cascade(label='用户', menu=user_menu)
        user_menu.add_command(label="注册", command=test_func)
        user_menu.add_command(label="登录", command=test_func)
        user_menu.add_command(label="退出登录", command=test_func, state='disable')

    def show(self):
        self.add_user_menus()
        self.add_setting_menus()
        self.master.config(menu=self)

from tkinter import Tk
from menus import TopMenus
from videoFrame import VideoFrame

from utils import single_instance


# from sys import platform
# # change default 'python' menu
# # Check if we're on OS X, first.
# if platform == 'darwin':
#     from Foundation import NSBundle
#
#     bundle = NSBundle.mainBundle()
#     print(bundle)
#     if bundle:
#         info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
#         info['CFBundleName'] = "ScreenMonitorClient"

@single_instance
class ClientRootWindow(Tk):

    def show(self):
        self.create_window()
        self.update()
        VideoFrame(master=self, bg="black").show()
        TopMenus(master=self).show()

    def create_window(self):
        # create the root window and make it center
        self.wm_title("ScreenMonitorClient")

        self.screen_w, self.screen_h = self.maxsize()
        w = int(self.screen_w * 0.618)
        h = int(self.screen_h * 0.618)
        m_w = int((self.screen_w - w) / 2)
        m_h = int((self.screen_h - h) / 2)
        self.geometry("{}x{}+{}+{}".format(w, h, m_w, m_h))
        self.resizable(width=False, height=False)  # 禁止调整窗口大小


if __name__ == '__main__':
    client = ClientRootWindow()
    # client.mainloop()
    client.show()
    client.mainloop()

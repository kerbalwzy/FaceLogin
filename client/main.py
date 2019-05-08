import tkinter as tk
from menus import TopMenus


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


class ClientRootWindow(tk.Tk):

    def mainloop(self, n=0):
        self.create_window()
        TopMenus(master=self).show()

        super().mainloop()

    def create_window(self):
        # create the root window and make it center
        self.wm_title("ScreenMonitorClient")

        screen_w, screen_h = self.maxsize()
        w = int(screen_w * 0.618)
        h = int(screen_h * 0.618)
        m_w = int((screen_w - w) / 2)
        m_h = int((screen_h - h) / 2)
        self.geometry("{}x{}+{}+{}".format(w, h, m_w, m_h))
        # self.resizable(width=False, height=False) # 禁止调整窗口大小



if __name__ == '__main__':
    client = ClientRootWindow()
    client.mainloop()

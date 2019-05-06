import tkinter as tk


class ClientRootWindow(tk.Tk):

    def create_window(self):
        self.title = "ScreenMonitorClient"
        screen_w, screen_h = self.maxsize()
        w = int(screen_w*0.618)
        h = int(screen_h*0.618)
        self.geometry("{}x{}".format(w, h))


if __name__ == '__main__':
    client = ClientRootWindow()
    client.create_window()
    client.mainloop()

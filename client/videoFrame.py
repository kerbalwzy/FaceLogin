import time

from tkinter import Frame, Label, TOP, YES, BOTH
from PIL import Image, ImageTk

from config import VIDEO_COVER_PATH
from utils import single_instance

import threading
from mss import mss


@single_instance
class VideoFrame(Frame):

    def show(self):
        cover_image = self.init_video_cover()
        self.panel = Label(self, image=cover_image)
        self.panel.image = cover_image
        self.panel.pack()
        self.pack(side=TOP, expand=YES, fill=BOTH)

        t = threading.Thread(target=self.open_preview)
        t.daemon = True
        t.start()

    def resize_img(self, image):
        # 对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例

        img_w, img_h = image.size
        box_w, box_h = self.master.winfo_width(), self.master.winfo_height()

        f1 = 1.0 * box_w / img_w  # 1.0 forces float division in Python2
        f2 = 1.0 * box_h / img_w
        factor = max([f1, f2])
        # use best down-sizing filter
        self.VFwidth = int(img_w * factor)
        self.VFheight = int(img_h * factor)
        return image.resize((self.VFwidth, self.VFheight), Image.ANTIALIAS)

    def init_video_cover(self):
        # 获取窗口的封面图片
        image = Image.open(VIDEO_COVER_PATH)
        image = self.resize_img(image)
        cover_image = ImageTk.PhotoImage(image)
        return cover_image

    def open_preview(self):
        # TODO， this have BUG
        """
        if I did not move the mouse actively,
        It would not take a screenshot, which seemed to cause a blockage.
        """
        with mss() as sct:
            while True:
                s = time.time()
                monitor = {"top": 0, "left": 0,
                           "width": self.master.screen_w,
                           "height": self.master.screen_h}
                sct_img = sct.grab(monitor)
                screen_img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
                e = time.time()
                print(e - s)
                screen_img = self.resize_img(screen_img)
                img = ImageTk.PhotoImage(screen_img)
                self.panel.config(image=img)
                self.panel.image = img

import time

from tkinter import Frame, Label, TOP, YES, BOTH
from PIL import Image, ImageTk

from config import VIDEO_COVER_PATH
from utils import single_instance

from mss import mss


@single_instance
class VideoFrame(Frame):
    _after_id = None
    _is_preview = False
    _first_resize = True

    def show(self):
        self.__load_cover_img()
        self.panel = Label(master=self, image=self.__cover_img)
        self.__set_cover_img()

        self.panel.pack()
        self.pack(side=TOP, expand=YES, fill=BOTH)

        self.sct = mss()
        self.monitor = {"top": 0, "left": 0,
                        "width": self.master.screen_w,
                        "height": self.master.screen_h}

    def resize_img(self, image):
        # 对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
        if self._first_resize:
            img_w, img_h = image.size
            box_w, box_h = self.master.winfo_width(), self.master.winfo_height()

            f1 = 1.0 * box_w / img_w
            f2 = 1.0 * box_h / img_w
            factor = max([f1, f2])
            # use best down-sizing filter
            self.VFwidth = int(img_w * factor)
            self.VFheight = int(img_h * factor)

        return image.resize((self.VFwidth, self.VFheight), Image.ANTIALIAS)

    def __load_cover_img(self):
        # 从本地读取预览封面图片
        if not hasattr(self, "__cover_img"):
            image = Image.open(VIDEO_COVER_PATH)
            image = self.resize_img(image)
            self.__cover_img = ImageTk.PhotoImage(image)

    def __set_cover_img(self):
        self.panel.config(image=self.__cover_img)
        self.panel.image = self.__cover_img

    def start_preview(self):
        self.after(500, self.preview)
        self._is_preview = True

    def stop_preview(self):
        self._is_preview = False
        self.after(500, self.__set_cover_img)

    def _screen_shot(self):
        sct_img = self.sct.grab(self.monitor)
        screen_img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
        return screen_img

    def preview(self):
        screen_img = self._screen_shot()
        screen_img = self.resize_img(screen_img)
        img = ImageTk.PhotoImage(screen_img)
        self.panel.config(image=img)
        self.panel.image = img

        if self._is_preview:
            self._after_id = self.after(100, self.preview)

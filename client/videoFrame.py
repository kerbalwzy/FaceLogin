from tkinter import Frame, Label, TOP, YES, BOTH
from PIL import Image, ImageTk

from config import VIDEO_COVER_PATH


class VideoFrame(Frame):

    def show(self):
        cover_image = self.init_video_cover()
        self.panel = Label(self, image=cover_image)
        self.panel.image = cover_image
        self.panel.pack(side=TOP, expand=YES, fill=BOTH)
        self.pack(side=TOP, expand=YES, fill=BOTH)

    def resize_img(self, image):
        '''
        对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
        '''
        img_w, img_h = image.size
        box_w, box_h = self.master.winfo_width(), self.master.winfo_height()

        f1 = 1.0 * box_w / img_w  # 1.0 forces float division in Python2
        f2 = 1.0 * box_h / img_w
        factor = min([f1, f2])
        # use best down-sizing filter
        width = int(img_w * factor)
        height = int(img_h * factor)
        return image.resize((width, height), Image.ANTIALIAS)

    def init_video_cover(self):
        image = Image.open(VIDEO_COVER_PATH)
        image = self.resize_img(image)
        cover_image = ImageTk.PhotoImage(image)
        return cover_image

    def load_video(self):
        pass

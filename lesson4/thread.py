import time
import tkinter
import tkinter.messagebox
from threading import Thread


def download():
    time.sleep(2)
    tkinter.messagebox.showinfo('提示', '下载完成!')


def thread():
    t = Thread(target=download)
    t.daemon = True
    t.start()


def show_about():
    tkinter.messagebox.showinfo('关于', 'test')


def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=thread)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()

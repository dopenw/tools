from tkinter import *
import pyperclip
import webbrowser
from googletrans import Translator


def center(main_window):
    main_window.update_idletasks()
    #获取屏幕的高度和宽度
    w = main_window.winfo_screenwidth()
    h = main_window.winfo_screenheight()
    size = tuple(int(_) for _ in main_window.geometry().split('+')[0].split('x'))
    x = w/2  + size[0]/2
    print(x)
    y =  size[1]/2
    print(y)
    print("size:",size)
    #resize
    size=(50,50)
    main_window.geometry("%dx%d+%d+%d" % (size + (x, y)))



def show_image():
    def key(event):
        print ("pressed", repr(event.char))

    def callback(event):
        print ("clicked at", event.x, event.y)
        webbrowser.open('https://translate.google.com/?hl=en&tab=wT#auto/'+'zh-CN/'+unicode(pyperclip.paste()))
        #problem:
        # 1. 对于使用浏览器访问有‘/’字符时需要转义 :slove: '/' --> '%2F'
        # 2. 使用api时有代理问题
        # translator = Translator()
        # translator.translate(pyperclip.paste(),dest='zh-CN')


    def dragwin(event):
        x = root.winfo_pointerx() - root._offsetx
        y = root.winfo_pointery() - root._offsety
        root.geometry('+{x}+{y}'.format(x=x,y=y))

    def clickwin(event):
        root._offsetx = event.x
        root._offsety = event.y

    root = Tk()
    #hide窗口标题栏
    root.overrideredirect(1)
    center(root)
    canvas= Canvas(root, width=50, height=50)
    # mouse 左键
    canvas.bind("<Button-1>", callback)
    # mouse 中键，移动窗口
    canvas.bind('<Button-3>',clickwin)
    canvas.bind('<B3-Motion>',dragwin)


    photo = PhotoImage(file = './test1.png')
    canvas.create_image(25,25,image=photo)
    canvas.pack()

    root.after(3000,lambda:root.destroy())

    root.mainloop()


if __name__=="__main__":
    pyperclip_source_value=''
    while True:
        pyperclip_current_value=pyperclip.paste()
        if pyperclip_current_value!=pyperclip_source_value:
            show_image()
            pyperclip_source_value=pyperclip_current_value
        # else:
        #     print("no value");

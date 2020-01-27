from tkinter import *
import sys
import os
import re

# make taglist
taglist = []
paths = sys.argv[0].split("\\")
paths.pop()
paths.append("taglist.txt")
path = '/'
path=path.join(paths)
tagfile = open(path, 'r')
taglist = []
for line in tagfile:
    tagline = re.split("[,;，；]", line.strip())
    taglist = taglist + tagline
# 文本框初始化
win = Tk()
win.configure(background='#262A32')
win.title("Please input your tags")
sw = win.winfo_screenwidth()
sh = win.winfo_screenheight()
x = sw
y = sh / 2
win.geometry("+%d+%d" % (100, y))
win.wm_attributes('-topmost', 1)
Label(win, text=" Tags:", font=("","15", "bold"), bg='#262A32', fg="#FFFFFF").grid(row=0,sticky=W)
Label(win, bg='#1D7BC6', width=81, height=1).place(x=10, y=37)
tagVar = StringVar()
# 指定文件
if len(sys.argv) > 1:
    os.chdir(sys.argv[1])
# 显示已有标记
if os.path.isfile("desktop.ini"):
    fd = open("desktop.ini", mode="r")
    fd.readline()
    tagline = fd.readline()
    tags = tagline.split(",")
    tagVar.set(tags[1])
    fd.close()
# 生成输入框
E1 = Entry(win, textvariable=tagVar, font=("", "16", ""), width=52, relief=FLAT,
           bg="#262A32", fg="#FFFFFF", insertbackground="#FFFFFF")
E1.focus()
E1.grid(row=1, columnspan=5, pady=6, padx=10)

def maktag(event):  # 生成标记文件
    tagline = tagVar.get()
    tagline = tagline.strip()
    tagl = re.split("[,;，；]", tagline)
    tags = set(tagl)
    if '' in tags:
        tags.remove('')
    tagl=list(tags)
    tagl.sort()
    tag = ";"
    tag = tag.join(tagl)
    fd = open("desktop.ini", mode="w")
    fd.write("[{F29F85E0-4FF9-1068-AB91-08002B27B3D9}] \n")
    fd.write("Prop5=31,"+tag)
    fd.close()
    win.quit()


def addtag(i):  # 通过按钮添加标记
    if len(tagVar.get()) == 0:
        tagVar.set(taglist[i])
    else:
        tagVar.set(taglist[i]+';'+tagVar.get())
    # buttonlist[i].configure(state=DISABLED)


def cleartag():
    tagVar.set('')


def edit():
    os.system(path)
    return

# 生成按钮表
buttonlist = []
for atag in taglist:
    buttonlist.append(Button(win, text=atag, width=8, height=1, font=("楷体", "16", "bold"),
                             relief=FLAT, bg="#333742", foreground="#FFFFFF", activebackground="#666971",
                             activeforeground="#FFFFFF"))
for i in range(len(buttonlist)):
    buttonlist[i].configure(command=lambda arg=i: addtag(arg))
    buttonlist[i].grid(row=i//5+3, column=i%5, ipady=10, pady=6)

win.bind('<Return>', maktag)  # 回车确定
enbu = Button(win, text="OK", font=("楷体", "16", "bold"), relief=FLAT, bg="#219788",
              foreground="#FFFFFF", activebackground="#6DBAB1", activeforeground="#FFFFFF",
              width=8, height=2)
enbu.bind('<Button-1>', maktag)
clbu = Button(win, text="Clear", command=cleartag, font=("楷体", "16", "bold"),
              relief=FLAT, bg="#D74037", foreground="#FFFFFF", activebackground="#E5817B",
              activeforeground="#FFFFFF", width=8, height=2)
edbu = Button(win, text="Edit", command=edit, font=("楷体", "16", "bold"),
              relief=FLAT, bg="#2794E9", foreground="#FFFFFF", activebackground="#71B8F1",
              activeforeground="#FFFFFF", width=8, height=2,)
enbu.grid(row=len(buttonlist)//5+4, column=1)
clbu.grid(row=len(buttonlist)//5+4, column=2)
edbu.grid(row=len(buttonlist)//5+4, column=3)
win.mainloop()

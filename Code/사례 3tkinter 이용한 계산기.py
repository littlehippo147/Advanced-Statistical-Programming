## 洹몃┝��

from tkinter import *

##### 蹂��� �ㅼ젙:
canvas_height = 400
canvas_width = 600
canvas_colour = "black"

p1_x = canvas_width / 2
p1_y = canvas_height
p1_colour = "green"
line_width = 5
line_length = 5


##### Functions:

# �ъ슜�� 肄섑듃濡�
def p1_move_N(event):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, (p1_y - line_length), width=line_width, fill=p1_colour)
    p1_y = p1_y - line_length


def p1_move_S(event):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, p1_y + line_length, width=line_width, fill=p1_colour)
    p1_y = p1_y + line_length


def p1_move_E(event):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x + line_length, p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x + line_length


def p1_move_W(event):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x - line_length, p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x - line_length


def erase_all(event):
    canvas.delete(ALL)


##### 硫붿씤:
window = Tk()
window.title("MyEtchaSketch")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

# �ㅻ� �뚮��� �� ��吏곸엫
window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Left>", p1_move_W)
window.bind("<Right>", p1_move_E)
window.bind("u", erase_all)

window.mainloop()

## 怨꾩궛湲�
## version 1

# myCalculator_expt1.py

from tkinter import *
from decimal import *

##### 硫붿씤:
window = Tk()
window.title("MyCalculator")

# �댁슜 �섏젙�� 媛��ν븳 �뷀듃由� �꾩젽�� �ъ슜�� 寃곌낵 �붿뒪�뚮젅�� �ъ슜
display = Entry(window, width=45, bg="light green")
display.grid()


# �レ옄 踰꾪듉 �앹꽦:
def click1():
    display.insert(END, "1")


Button(window, text="1", width=5, command=click1).grid(row=1, column=0)

##### 硫붿씤 諛섎났臾� �ㅽ뻾
window.mainloop()

## version 2
from tkinter import *
from decimal import *


# �� �낅젰 �⑥닔:
def click(key):
    display.insert(END, key)


##### 硫붿씤:
window = Tk()
window.title("MyCalculator")

# top_row �꾨젅�� �앹꽦
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# �섏젙 媛��ν븳 �뷀듃由� �꾩젽
display = Entry(top_row, width=45, bg="light green")
display.grid()

# �レ옄 踰꾪듉 �꾨젅�� �앹꽦
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

# �レ옄 踰꾪듉�� �쒓났�� �レ옄:
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=']

# 諛섎났臾몄쑝濡� �レ옄 踰꾪듉 �앹꽦
r = 0  # �� 移댁슫��
c = 0  # �� 移댁슫��

for btn_text in num_pad_list:
    Button(num_pad, text=btn_text, width=5, command=click).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1

##### 硫붿씤 諛섎났臾� �ㅽ뻾
window.mainloop()

## version 3
from tkinter import *
from decimal import *


# �� �낅젰 �⑥닔:
def click(key):
    display.insert(END, key)


##### 硫붿씤:
window = Tk()
window.title("MyCalculator")

# top_row �꾨젅�� �앹꽦
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# �섏젙 媛��ν븳 �뷀듃由� �꾩젽
display = Entry(top_row, width=45, bg="light green")
display.grid()

# �レ옄 踰꾪듉 �꾨젅�� �앹꽦
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=']

# 諛섎났臾몄쑝濡� �レ옄 踰꾪듉 �앹꽦
r = 0
c = 0
for btn_text in num_pad_list:
    # �� 遺�遺꾩� �섏쨷�� �닿껐�� 寃껋엯�덈떎:
    Button(num_pad, text=btn_text, width=5, command=click).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1

# �곗궛�� �꾨젅�� �앹꽦
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C']

# 諛섎났臾몄쑝濡� �곗궛�� 踰꾪듉 �앹꽦
r = 0
c = 0
for btn_text in operator_list:
    Button(operator, text=btn_text, width=5, command=click).grid(row=r, column=c)
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1

##### 硫붿씤 諛섎났臾� �ㅽ뻾
window.mainloop()

## �묐룞�섎뒗 version 1
from tkinter import *


# �� �낅젰 �⑥닔:
def click(key):
    display.insert(END, key)


##### 硫붿씤:
window = Tk()
window.title("MyCalculator")

# top_row �꾨젅�� �앹꽦
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# �섏젙 媛��ν븳 �뷀듃由� �꾩젽
display = Entry(top_row, width=45, bg="light green")
display.grid()

# �レ옄 踰꾪듉 �꾨젅�� �앹꽦
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=']

# 諛섎났臾몄쑝濡� �レ옄 踰꾪듉 �앹꽦
r = 0
c = 0
for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)


    Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1

# �곗궛�� �꾨젅�� �앹꽦
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C']

# 諛섎났臾몄쑝濡� �곗궛�� 踰꾪듉 �앹꽦
r = 0
c = 0
for btn_text in operator_list:
    Button(operator, text=btn_text, width=5, command=click).grid(row=r, column=c)
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1

##### 硫붿씤 諛섎났臾� �ㅽ뻾
window.mainloop()

## �묐룞�섎뒗 version 2
from tkinter import *


# �� �낅젰 �⑥닔:
def click(key):
    # = 踰꾪듉�� �뚮졇�� �� 怨꾩궛 �섑뻾:
    if key == '=':
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END, " --> Error!")

    # C 踰꾪듉�� �뚮젮議뚯쓣 �� display �뷀듃由� �꾩젽 �댁슜 鍮꾩�:
    elif key == "C":
        display.delete(0, END)

    # 洹� �� �ㅻⅨ �ㅻ� �뚮��� �� �ㅽ뻾�� 湲곕낯 �숈옉:
    else:
        display.insert(END, key)


##### 硫붿씤:
window = Tk()
window.title("MyCalculator")

# top_row �꾨젅�� �앹꽦
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# �섏젙 媛��ν븳 �뷀듃由� �꾩젽
display = Entry(top_row, width=45, bg="light green")
display.grid()

# �レ옄 踰꾪듉 �꾨젅�� �앹꽦
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=']

# 諛섎났臾몄쑝濡� �レ옄 踰꾪듉 �앹꽦
r = 0
c = 0
for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)


    Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1

# �곗궛�� �꾨젅�� �앹꽦
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C']

# 諛섎났臾몄쑝濡� �곗궛�� 踰꾪듉 �앹꽦
r = 0
c = 0
for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)


    Button(operator, text=btn_text, width=5, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1

##### 硫붿씤 諛섎났臾� �ㅽ뻾
window.mainloop()

## 醫��� 蹂듭옟�� 怨꾩궛湲�
from tkinter import *


# �⑺넗由ъ뼹 �⑥닔:
def factorial(n):
    return "factorial (!)"


# 10吏꾩닔瑜� 2吏꾩닔濡� 蹂��섑븯�� �⑥닔:
def to_binary(n):
    return "-> binary"


# 2吏꾩닔瑜� 10吏꾩닔濡� 蹂��섑븯�� �⑥닔:
def from_binary(n):
    return "binary -> 10"


# �� �낅젰 �⑥닔:
def click(key):
    # = 踰꾪듉�� �뚮졇�� �� 怨꾩궛 �섑뻾:
    if key == "=":
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END, " --> Error!")

    # C 踰꾪듉�� �뚮젮議뚯쓣 �� display �뷀듃由� �꾩젽 �댁슜 鍮꾩�:
    elif key == "C":
        display.delete(0, END)

    # �곸닔 踰꾪듉�� ���� �묒뾽:
    elif key == constants_list[0]:
        display.insert(END, "3.141592654")

    # �⑥닔 踰꾪듉�� ���� �묒뾽:
    elif key == functions_list[0]:
        n = display.get()  # �꾩옱 display �뷀듃由� �꾩젽 媛� �섏쭛
        display.delete(0, END)  # �꾩옱 display �뷀듃由� �꾩젽 �댁슜 鍮꾩�
        display.insert(END, factorial(n))

    elif key == functions_list[2]:
        n = display.get()  # �꾩옱 display �뷀듃由� �꾩젽 媛� �섏쭛
        display.delete(0, END)  # display �뷀듃由� �꾩젽 �댁슜 鍮꾩�
        display.insert(END, to_binary(n))

    elif key == functions_list[3]:
        n = display.get()  # �꾩옱 display �뷀듃由� �꾩젽 媛� �섏쭛
        display.delete(0, END)  # display �뷀듃由� �꾩젽 �댁슜 鍮꾩�
        display.insert(END, from_binary(n))

    # 洹� �� �ㅻⅨ �ㅻ� �뚮��� �� �ㅽ뻾�� 湲곕낯 �숈옉:
    else:
        display.insert(END, key)


##### 硫붿씤:
window = Tk()
window.title("MyCalculator")

# top_row �꾨젅�� �앹꽦
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# �섏젙 媛��ν븳 �뷀듃由� �꾩젽
display = Entry(top_row, width=45, bg="light green")
display.grid()

# �レ옄 踰꾪듉 �꾨젅�� �앹꽦
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=']

# 諛섎났臾몄쑝濡� �レ옄 踰꾪듉 �앹꽦
r = 0
c = 0
for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)


    Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1

# �곗궛�� �꾨젅�� �앹꽦
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C']

# 諛섎났臾몄쑝濡� �곗궛�� 踰꾪듉 �앹꽦
r = 0
c = 0
for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)


    Button(operator, text=btn_text, width=5, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1

# �곸닔 �꾨젅�� �앹꽦
constants = Frame(window)
constants.grid(row=3, column=0, sticky=W)

constants_list = ['pi']

# 諛섎났臾몄쑝濡� �곸닔 踰꾪듉 �앹꽦
r = 0
c = 0
for btn_text in constants_list:
    def cmd(x=btn_text):
        click(x)


    Button(constants, text=btn_text, width=22, command=cmd).grid(row=r, column=c)
    r = r + 1

# �⑥닔 �꾨젅�� �앹꽦
functions = Frame(window)
functions.grid(row=3, column=1, sticky=E)

functions_list = [
    'factorial (!)',
    '10-> binary',
    'binary -> 10']

# 諛섎났臾몄쑝濡� �⑥닔 踰꾪듉 �앹꽦
r = 0
c = 0
for btn_text in functions_list:
    def cmd(x=btn_text):
        click(x)


    Button(functions, text=btn_text, width=13, command=cmd).grid(row=r, column=c)
    r = r + 1

##### 硫붿씤 諛섎났臾� �ㅽ뻾
window.mainloop()

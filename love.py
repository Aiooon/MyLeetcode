

# 关闭窗口提示
from tkinter import messagebox, Button


def close_window():
    messagebox.showinfo(title="╭(╯^╰)╮", message="不选好不许走嘛！")

love.title("（づ￣3￣）づ╭❤～爱你么么哒~")
btn = Button(love, text="在一起！", width=10, height=2, command=close_all_window)
btn.place(x=100, y=30)
love.protocol("WM_DELETE_WINDOW", no_close)

window = Tk()
window.title("hei(,,･∀･)ﾉ゛hello，小姐姐")  # 窗口标题
window.geometry("360x640+550+50")  # 窗口大小
window.protocol("WM_DELETE_WINDOW", close_window)  # 窗口关闭
label = Label(window, text="关注你很久了(*^▽^*)", font=("微软雅黑", 18))
label.place(x=60, y=50)
label = Label(window, text="做我女朋友好不好？(*^▽^*)", font=("微软雅黑", 20))
label.place(x=10, y=100)
btn1 = Button(window, text="好", width=15, height=2, command=Love)
btn1.place(x=110, y=200)
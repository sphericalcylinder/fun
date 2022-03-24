import tkinter
import tkinter.ttk

root = tkinter.Tk()

img = tkinter.PhotoImage(file='compitition/assets/poop.png')


def poop():
    root.update_idletasks()
    window = tkinter.Toplevel(root, width=163, height=311)
    canvas = tkinter.Canvas(
        window, height=162, width=310, background='#ffffff')
    canvas.create_image((155, 81), image=img)
    canvas.pack()


def superpoop():
    root.withdraw()
    for i in range(50):
        poop()


button = tkinter.ttk.Button(root, text="Activate poop", command=superpoop)
button.grid(padx=30, pady=30)

tkinter.mainloop()

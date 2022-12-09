

import tkinter as tk

root = tk.Tk()


label = tk.Label(root, text='Text on the screen',
                 font=('Times New Roman','80'), fg='black', bg='white')
label.pack()

root.overrideredirect(True)
root.geometry("+250+250")
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white") # -- фон_белый

root.mainloop()


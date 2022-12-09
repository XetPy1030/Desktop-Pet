import tkinter as tk

# select a color as the transparent color
TRNAS_COLOR = '#ffffff'

root = tk.Tk()
root.config(bg='')

root.overrideredirect(1)
# root.attributes('-zoomed', True, '-alpha', True, '-topmost', False)
# root.attributes('-transparentcolor', 'white')

image = tk.PhotoImage(file='da.png')
tk.Label(root, image=image).pack()


root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white") # -- фон_белый


# support dragging window

def start_drag(event):
    global dx, dy
    dx, dy = event.x, event.y

def drag_window(event):
    print(1)
    root.geometry(f'+{event.x_root-dx}+{event.y_root-dy}')

root.bind('v', start_drag)
root.bind('c', drag_window)

root.mainloop()
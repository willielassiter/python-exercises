import tkinter as tk

main_window = main_window = tk.Tk ()

textLabel = tk.Label (main_window, text="this is a label.")

textLabel.pack ()

def f (event):
    print (event.x, event.y)

def on_click (event):
    print ("clicked at", event.x, event.y)
    print (event)

frame = tk.Frame (main_window, width=100, height=100, bg="blue")

frame.bind ("<Button-1>", on_click)
frame.bind ("<Button-2>", on_click)
frame.bind ("<Button-3>", on_click)
frame.pack ()


# main_window.bind ("<Motion>", f)

main_window.mainloop ()

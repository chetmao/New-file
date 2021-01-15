import tkinter as tk
# Create empty window
root = tk.Tk()
# window size
root.geometry("600x600")
# Frame
frame = tk.Frame()
# Set title
frame.master.title("Hello PNC")
#.....all your code for window
canvas = tk.Canvas(frame)
canvas.create_rectangle(10, 10, 500, 500,fill="#2e3366")
canvas.create_rectangle(10, 10, 300, 300,fill="#ff0000")
canvas.create_rectangle(10, 10, 200, 200,fill="#0000ff")
canvas.create_rectangle(10, 10, 100, 100,fill="#2e3366")
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
# Display all
root.mainloop()
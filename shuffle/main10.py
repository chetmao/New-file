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
canvas.create_rectangle(80, 80, 200, 200,fill="#2e3366")
canvas.create_rectangle(210, 80, 330, 200,fill="red")
canvas.create_rectangle(340, 80, 460, 200,fill="red")

canvas.create_rectangle(100, 230, 200, 320,fill="#2e3366")
canvas.create_rectangle(210, 80, 330, 200,fill="red")
canvas.create_rectangle(340, 80, 460, 200,fill="red")
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
# Display all
root.mainloop()
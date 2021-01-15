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
canvas.create_oval(0, 0, 50, 50,fill="#2e3366")
canvas.create_oval(10, 10, 50, 50,fill="#2e3366")
canvas.create_oval(20, 20, 50, 50,fill="#2e3366")
canvas.create_oval(30, 30, 50, 50,fill="#2e3366")
canvas.create_oval(40, 40, 50, 50,fill="#2e3366")
canvas.create_text(400,500, text="HELLO! CLASS C", font=('Arial', 30))


canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
# Display all
root.mainloop()
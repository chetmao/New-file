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
for i in range(10):
    canvas.create_oval(10*i, 10*i, 100*i, 100*i,fill="#2e3366")
canvas.create_text(400,500, text="HELLO! CLASS C", font=('Arial', 30))


canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
# Display all
root.mainloop()
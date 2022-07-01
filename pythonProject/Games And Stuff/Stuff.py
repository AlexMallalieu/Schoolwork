import tkinter as tk
letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'delete', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'x', 'b', 'n', 'm', 'return']
x_coord = 0.1
y_coord = 0.7
height = 0.05
width = 0.07
button = []
guess = []

root = tk.Tk()

def attempt():
    label_h = 0.09
    label_w = 0.09
    label_x = 0.2
    label_y = 0.1
    for x in entry.get():
        guess.append(x)
    for x in guess:
        label = tk.Label(frame, bg="gray", text=x)
        label.place(relx=label_x, rely=label_y, relheight=label_h, relwidth=label_w)
        label_x = label_x + 0.13





canvas = tk.Canvas(root, height=800, width=800)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=1, relheight=1)

entry = tk.Entry(frame, bg='white', fg='black', font='40')
entry.place(relx=0.4, rely=0.5)

return_button = tk.Button(frame, bg='gray', font='40', text='enter', command=attempt)
return_button.place(relx=0.475, rely=0.55)

# let = tk.Button(frame, text=x)
#     ind = letters.index(x)
#     button.append(ind)
#     let.place(relx=x_coord, rely=y_coord, relheight=height, relwidth=width)
#     x_coord = x_coord + 0.07
#     if x == 'p':
#         width = width + 0.1
#     if x == 'delete':
#         y_coord = y_coord + 0.06
#         x_coord = 0.12
#     else:
#         width = 0.07
#     if x == 'l':
#         y_coord = y_coord + 0.06
#         x_coord = 0.14



root.mainloop()
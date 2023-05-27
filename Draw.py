import tkinter as tk
from tkinter import ttk


def draw_huffman_tree_gui(root):
    def traverse(node, x, y, dx):
        nonlocal canvas_width

        if node is None:
            return

        node_x = x + dx / 2

        canvas.create_oval(node_x - 10, y - 10, node_x + 10, y + 10, fill='white')
        canvas.create_text(node_x, y, text=f"{node.key}:{node.freq}")

        if node.left is not None:
            left_x = x - dx / 2
            left_y = y + 50
            canvas.create_line(node_x, y + 10, left_x, left_y - 10, fill='black')
            traverse(node.left, left_x, left_y, dx / 2)

        if node.right is not None:
            right_x = x + dx + dx / 2
            right_y = y + 50
            canvas.create_line(node_x, y + 10, right_x, right_y - 10, fill='black')
            traverse(node.right, right_x, right_y, dx / 2)

        if x + dx > canvas_width:
            canvas_width = x + dx

    canvas_width = 0

    root_window = tk.Tk()
    root_window.title("Huffman Tree Visualization")
    canvas = tk.Canvas(root_window, width=800, height=600)
    canvas.pack()

    traverse(root, 400, 50, 300)

    root_window.mainloop()


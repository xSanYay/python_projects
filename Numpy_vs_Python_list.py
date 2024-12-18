import tkinter as tk
from tkinter import ttk
import numpy as np
import time
import seaborn as sns  
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def compare_timings_and_plot():
    size = int(size_slider.get())
    python_list = list(range(size))
    numpy_array = np.arange(size)

    start_time = time.time()
    [x * 2 for x in python_list]
    python_time = time.time() - start_time

    start_time = time.time()
    numpy_array * 2
    numpy_time = time.time() - start_time

    data = {
        "Operation": ["Python List", "NumPy Array"],
        "Time (seconds)": [python_time, numpy_time]
    }

    ax.clear()  
    sns.barplot(x="Operation", y="Time (seconds)", data=data, ax=ax, palette="pastel")  
    ax.set_title(f"Performance Comparison (Size={size})")
    ax.set_ylabel("Time (seconds)")
    ax.set_xlabel("Data Type")
    canvas.draw() 

root = tk.Tk()
root.title("NumPy vs Python List Timing Comparison")

control_frame = tk.Frame(root)
control_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

tk.Label(control_frame, text="Array Size:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
size_slider = ttk.Scale(control_frame, from_=10**3, to=10**6, orient="horizontal", length=300)
size_slider.set(10**5)
size_slider.pack(side=tk.LEFT, padx=10)

plot_button = tk.Button(control_frame, text="Compare and Plot", command=compare_timings_and_plot, font=("Arial", 12))
plot_button.pack(side=tk.LEFT, padx=10)

fig, ax = plt.subplots(figsize=(6, 4))  
canvas = FigureCanvasTkAgg(fig, master=root)  
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

root.geometry("700x500")
root.mainloop()

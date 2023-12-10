import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Global list to store data points
data_points = []

def click_event(event):
  """
  Handles click events on the canvas.
  """
  # Get click coordinates relative to the canvas
  x_coord = event.xdata
  y_coord = event.ydata

  # Add data point to the list
  data_points.append((x_coord, y_coord))

  # Update plot with new data point
  ax.plot(x_coord, y_coord, marker="o", color="blue", linestyle="")
  canvas.draw()


def print_data():
  """
  Prints all the data points to the console.
  """
  print("Data points:")
  for point in data_points:
    print(f"\t({point[0]}, {point[1]})")
  
def linear_model():
  global data_points
  df = np.array(data_points)
  lr = LinearRegression().fit(np.atleast_2d(df[:, 0]).reshape(-1, 1), np.atleast_2d(df[:, 1]).reshape(-1, 1))
  y = lr.predict(np.atleast_2d((-10, 10)).reshape(-1, 1))
  ax.cla()
  ax.set_xlim((-10, 10))
  ax.set_ylim((-10, 10))
  ax.set_xlabel("X1")
  ax.set_ylabel("X2")
  ax.grid(True)
  ax.plot(df[:,0], df[:, 1], marker="o", color="blue", linestyle="")
  ax.plot((-10, 10), y, c = 'r')
  canvas.draw()

# Initialize the main window
root = tk.Tk()
root.title("Data Point Collector")

# Create the matplotlib figure
fig = Figure(figsize=(6, 6))
ax = fig.add_subplot(111)
ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))
# Create the canvas for matplotlib
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, columnspan=2)

# Bind click event to the canvas
canvas.mpl_connect("button_press_event", click_event)

# Create the "Print Data" button
button = tk.Button(root, text="Print Data", command=print_data, width=20)
button.grid(row=1, column=0)

button2 = tk.Button(root, text="Linear Regression", command=linear_model, width=20)
button2.grid(row=1, column=1)

name = tk.Label(root, height=2, font=('Arial', 14), text="ML engine")
name.grid(row=2, columnspan=2)
# Set initial plot
ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.grid(True)

# Start the main loop
root.mainloop()

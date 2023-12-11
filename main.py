import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Global list to store data points
data_points = pd.DataFrame(columns=["X1", "X2", "label"])
def reset_axes(axes):
  axes.cla()
  axes.set_xlim((-10, 10))
  axes.set_ylim((-10, 10))
  axes.set_xlabel("X1")
  axes.set_ylabel("X2")
  axes.grid(True)
def plot_datapoints():
  ax.plot(data_points["X1"], data_points["X2"], marker="o", color="blue", linestyle="")

def click_event(event):
  # Get click coordinates relative to the canvas
  # Add data point to the list
  data_points.loc[len(data_points)] = [event.xdata, event.ydata, ""]
  # Update plot with new data point
  ax.plot(event.xdata, event.ydata, marker="o", color="blue", linestyle="")
  canvas.draw()
def print_data():
  print("Data points:")
  print(data_points)
def linear_model():
  if len(data_points) > 1:
    lr = LinearRegression().fit(data_points["X1"].values.reshape(-1, 1), data_points["X2"].values.reshape(-1, 1))
    y = lr.predict(np.atleast_2d((-10, 10)).reshape(-1, 1))
    reset_axes(ax)
    plot_datapoints()
    ax.plot((-10, 10), y, c = 'r')
    canvas.draw()
def undo(): 
  if len(data_points) > 0:
    data_points.drop(data_points.tail(1).index,inplace=True)
    reset_axes(ax)
    plot_datapoints()
    canvas.draw()

# Initialize the main window
root = tk.Tk()
root.title("Data Point Collector")

# Create the matplotlib figure
fig = Figure(figsize=(6, 6))
ax = fig.add_subplot(111)
reset_axes(ax)
# Create the canvas for matplotlib
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, columnspan=3)

# Bind click event to the canvas
canvas.mpl_connect("button_press_event", click_event)

# Create the "Print Data" button
printBtn = tk.Button(root, text="Print Data", command=print_data, width=20)
printBtn.grid(row=1, column=0)

linearRegBtn = tk.Button(root, text="Linear Regression", command=linear_model, width=20)
linearRegBtn.grid(row=1, column=1)

undoBtn = tk.Button(root, text="Undo", command=undo, width=20)
undoBtn.grid(row=1, column=2)

name = tk.Label(root, height=2, font=('Arial', 14), text="ML engine")
name.grid(row=2, columnspan=3)

# Start the main loop
root.mainloop()

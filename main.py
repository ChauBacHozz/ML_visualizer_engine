import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Global list to store data points
data_points = pd.DataFrame(columns=["X1", "X2", "label", "marker"])
label_dict = {}
def reset_axes(axes):
  axes.cla()
  axes.set_xlim((-10, 10))
  axes.set_ylim((-10, 10))
  axes.set_xlabel("X1")
  axes.set_ylabel("X2")
  axes.grid(True)
def plot_datapoints():
  for index, data_point in data_points.iterrows():
    ax.plot(data_point["X1"], data_point["X2"], marker= data_point['marker'], color="blue", linestyle="")

def click_event(event):
  if marker_style not in label_dict:
    label_dict[marker_style] = len(label_dict)
  data_points.loc[len(data_points)] = [event.xdata, event.ydata, label_dict[marker_style], marker_style]
  ax.plot(event.xdata, event.ydata, marker=marker_style, color="blue", linestyle="")
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
def change_marker(style):
  global marker_style
  marker_style = markerOptions[style]
# Initialize the main window
root = tk.Tk()
root.title("Data Point Collector")

# Create the matplotlib figure
fig = Figure(figsize=(6, 6))
ax = fig.add_subplot(111)
reset_axes(ax)
# Create the canvas for matplotlib
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, columnspan=4)

# Bind click event to the canvas
canvas.mpl_connect("button_press_event", click_event)

markerOptions = {
  'Circle': 'o',
  'Filled X': 'X',
  'Triangle': '^',
  'Square': 's'
}
marker_style = markerOptions['Circle']
clicked = tk.StringVar()
clicked.set(markerOptions['Circle'])
markerDM = tk.OptionMenu(root, clicked, *markerOptions.keys(), command=change_marker)
markerDM.config(width=12)
markerDM.grid(row=1, column=0)

# Create the "Print Data" button
printBtn = tk.Button(root, text="Print Data", command=print_data, width=20)
printBtn.grid(row=1, column=1)

linearRegBtn = tk.Button(root, text="Linear Regression", command=linear_model, width=20)
linearRegBtn.grid(row=1, column=2)

undoBtn = tk.Button(root, text="Undo", command=undo, width=20)
undoBtn.grid(row=1, column=3)

name = tk.Label(root, height=2, font=('Arial', 14), text="ML engine")
name.grid(row=2, columnspan=4)

# Start the main loop
root.mainloop()

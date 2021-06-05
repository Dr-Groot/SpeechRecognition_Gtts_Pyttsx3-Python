# install matplotlib library using 'pip install matplotlib'
import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [3, 5, 7, 9, 11]

# syntax for using matlplotlib.pyplot.plot(x axis, y axis, 'LineSpecification').
# LineSpecificaiton conntains Colour-PointStyle-LineStyle, etc in any order (Check Guide for more)
# Line 9 will produce red colour, circle point with dashed line style.
plt.plot(x, y, 'ro--')

# for labelling x and y axis
plt.ylabel('y Label')
plt.xlabel('x Label')

plt.draw()
# draw() will display the current figure that you are working on

plt.show()
# show() will re-draw the figure. This allows you to work in interactive mode and, 
# should you have changed your data or formatting, allow the graph itself to change.

# --------------------Guide--------------------
# Line Specification: 
# Colour: b (blue: default), g (green), r (red), c (cyan), m (magenta), y (yellow), k (black), w (white)
# PointStyle: . (Point: default), o (circle), * (star), + (plus), x (X), v ^ < > (Down Up Left Right triangles)
# LineStyle: - (solid line: default), -- (Dashed Line), : (Dotted Line), -. (Dash-Dot line)
# Other Plots: 
# 1.Line Plot: plt.plot(x,y) (replace with line 10)
# 2.Bar Plot: plt.bar(x,y) (replace with line 10)
# 3.Histogram: plt.hist(x) (replace with line 10)
# 4.Scatter Plot: plt.scatter(x,y) (replace with line 10)

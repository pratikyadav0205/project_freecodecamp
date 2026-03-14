from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Line plot
fig1 = draw_line_plot()
fig1.savefig("line_plot.png")
print("Saved line_plot.png")

# Bar plot
fig2 = draw_bar_plot()
fig2.savefig("bar_plot.png")
print("Saved bar_plot.png")

# Box plot
fig3 = draw_box_plot()
fig3.savefig("box_plot.png")
print("Saved box_plot.png")
from motion import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool,ColumnDataSource

df["Start_String"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_String"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

f=figure(x_axis_type='datetime',height=100, width=500, sizing_mode='scale_width',title="Motion Graph")
f.yaxis.minor_tick_line_color=None
f.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start","@Start_String"),("End","@End_String")])
f.add_tools(hover)

f.quad(left="Start", right="End", bottom=0, top=1, color="lightgreen",source=cds)

output_file("Plot.html")

show(f)

'''
Author: Jake Bradford
Licence: GNU General Public License v3.0

Boilerplate code for generating multi-axes figures (plots with multiple panels)

Reminder of matplotlib terminology:
    - Figure: the "surface" to draw on (it manages Axes)
    - Axes: a panel/plot of the Figure
    - Axis: a number-line-like object

Read below to see configuration options.
'''

# Import necessary libraries
import random
random.seed(2021)

import matplotlib.pyplot as plt

# Plot settings
LEGEND_LOC = 'lower right' # (upper|lower) (left|right)
LINE_WIDTH = 0.75
MARKER = 'o'
MARKER_SIZE = 2
NUM_PANELS_COLS = 1
NUM_PANELS_ROWS = 3
OUTPUT_FILE = __file__
OUTPUT_FORMATS = ['png'] # png, pdf, svg, eps
PANEL_SIZE_X = 3
PANEL_SIZE_Y = 9
PLOT_OUTPUT_DPI = 300

# Create the figure
fig, ax = plt.subplots(
    nrows = NUM_PANELS_ROWS, 
    ncols = NUM_PANELS_COLS, 
    figsize = (
        NUM_PANELS_ROWS * PANEL_SIZE_X,
        NUM_PANELS_COLS * PANEL_SIZE_Y
    )
)


'''
Start drawing on the Axes

There are many approaches to drawing on multiple Axes.
Below, I provide sample code for iterating through the Axes, and drawing
on each progressively. Also, I provide an example where I draw on the last
Axes using indexing. 
'''
for axes in ax[:-1]:
    axes.set_title('Title')
    axes.set_xlabel('x label')
    axes.set_ylabel('y label')

    import random
    x = list(range(0,100))
    y = random.sample(range(0, 1000), 100)
    
    axes.plot(
        x, 
        y, 
        linewidth=LINE_WIDTH, 
        marker=MARKER, 
        markersize=MARKER_SIZE,
        label="Line"
    )
    
    axes.legend(loc=LEGEND_LOC) 
    
ax[-1].set_title('Setting the title via indexing')
ax[-1].set_xlabel('x label')
ax[-1].set_ylabel('y label')
ax[-1].plot(
    x, 
    y, 
    linewidth=LINE_WIDTH, 
    marker=MARKER, 
    markersize=MARKER_SIZE,
    label="Another line"
)
ax[-1].set_yscale("log")
ax[-1].legend(loc=LEGEND_LOC) 
        
plt.tight_layout()
outFig = fig.get_figure()
for OUTPUT_FORMAT in OUTPUT_FORMATS:
    fp = f"{OUTPUT_FILE}.{OUTPUT_FORMAT}"
    outFig.savefig(
        fp, 
        format=OUTPUT_FORMAT, 
        dpi=PLOT_OUTPUT_DPI
    )
    print(f'Wrote to: {fp}')
    
plt.clf()

# Done
print('Goodbye.')

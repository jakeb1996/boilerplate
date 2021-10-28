'''
Author: Jake Bradford
Licence: GNU General Public License v3.0

Provide this script a list of methods to execute, in return for input size vs. 
run time plot. You specify input dataset sizes and the number of repeat tests.

The functions that you wish to test should accept only one argument, which is
the test dataset. You should complete the method `generateTestData(n)`.

Read below to see configuration options.
'''

# Import your code here
# import MyFile

FUNCTIONS_TO_TEST = [
    # For example...
    # MyFile.InsertionSort,
    # MyFile.SelectionSort,
    # MyFile.BubbleSort
]

# Import necessary libraries
import random
random.seed(2021)

import matplotlib.pyplot as plt

from time import time

# Input sizes (start and stop are inclusive)
START = 10_000
STOP = 100_000
STEP = 500

# Number of repeat tests
REPEATS = 5

# Plot settings
OUTPUT_FILE = __file__
OUTPUT_FORMATS = ['png'] # png, pdf, svg, eps
PLOT_OUTPUT_DPI = 300
IS_Y_LOG = False
LINE_WIDTH = 0.75
MARKER = 'o'
MARKER_SIZE = 2
LEGEND_LOC = 'lower right' # (upper|lower) (left|right)

# Create the figure
fig = plt.figure(figsize=(5, 5))
fig = fig.add_subplot(111)
fig.set_title('Empirical Analysis of Algorithms')
fig.set_xlabel('Input size')
fig.set_ylabel('Time (seconds)')

# A function to generate test data with `n` items
def generateTestData(n):
    testData = []
    testData = random.sample(
        range(0, 1000000), 
        n
    )
    return testData

# A function to run the tests
# Returns:
#   - x, input sizes used
#   - y, average of individual repeat tests
def runTests(start, stop, step, repeats, fn):
    x = []
    y = []

    for s in range(start, stop+step, step):
        _y = []
        for r in range(repeats):
            start = time()
            p = fn(
                generateTestData(s)
            )
            
            _y.append(time() - start)
            
        x.append(s)
        y.append(float(sum(_y) / len(_y)))
        
    return (x, y)

# Start running the tests
for FUNCTION_TO_TEST in FUNCTIONS_TO_TEST:
    x, y = runTests(START, STOP, STEP, REPEATS, FUNCTION_TO_TEST)

    fig.plot(
        x, 
        y, 
        linewidth=LINE_WIDTH, 
        marker=MARKER, 
        markersize=MARKER_SIZE,
        label=f"{FUNCTION_TO_TEST.__name__}"
    )

# Draw the plot
if IS_Y_LOG:
    fig.set_yscale("log")

fig.legend(loc=LEGEND_LOC)         
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

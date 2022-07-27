# ~~ ---
# ~~ title: "Python Template"
# ~~ author: "Yingqi Jing"
# ~~ date: 08.06.2022
# ~~ header-includes:
# ~~     - \usepackage{textcomp}
# ~~     - \renewcommand{\thefigure}{S\arabic{figure}}
# ~~     - \renewcommand{\thetable}{S\arabic{table}}
# ~~     - \renewcommand{\thesection}{S\arabic{section}}
# ~~     - \renewcommand{\thesubsection}{S\arabic{section}.\arabic{subsection}}
# ~~     - \usepackage{tocloft}
# ~~     - \settowidth{\cftsecnumwidth}{S10x}
# ~~ output:
# ~~     pdf_document:
# ~~         fig_crop: true
# ~~         fig_caption: true
# ~~         latex_engine: xelatex
# ~~         toc: true
# ~~         toc_depth: 4
# ~~         number_section: true
# ~~         pandoc_args: ["--variable=lof", "--variable=lot",
# ~~                       "--bibliography=/Users/jakejing/switchdrive/bib/references.bib",
# ~~                       "--csl=/Users/jakejing/switchdrive/bib/unified-style-linguistics.csl"]
# ~~ ---
# ~~ \clearpage


# %% name = "setup", echo = False, include=False
import os
import sys
sys.path.append(os.getcwd())
# Note: user-defined module should come after the line of setting current wd
from inspect import getsource as trace
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
# %%


# ~~ # Introduction


# ~~ Here I am using a special character (# ~~ ) as indicator for yaml header and markdown inline code format. You also write inline comments directly, though it may cause some warnings for the spelling of code. To compile this script into pdf, I have written a funtion that can automatically delete the specaial indicator, and render the file into pdf via `pweave` function.


# %% name = "check source code via inspect getsource function"
def add_two(A, B):
    return A + B

print("===========")
print(trace(add_two))

# print("=========")
# print(trace(np.mean))
# %%


# ~~ # Data and Methods


# %% name = "for loop"
for i in range(10):
    print(i)
# %%

# ~~ # Results

# ~~ # Discussions

# ~~ # References



# vscode-python-config

This repos. includes the step-by-step configuration of python in **VS code**. I am trying to make the configuration as similar as the one I have for `Rmarkdown` notebook. Thus, most shortcuts and outlook would would be more or less the same as my rmarkdown notebook in VS code.

Here are the necessary extensions I have installed:

```
1. python
2. pylance
3. Jupyter 
4. Jupyter Keymap
5. Docs View # another way to look at func doc
6. Kite AutoComplete # func docs
7. multi-command # useful for defining a sequence of commands
```

### 1. Hide the "run cell" and "debug cell" icon at the top of cell

You need to search for "code lens" in settings, and uncheck **Jupyter:Enable Cell Code Lens**


### 2. Change the keybinding for running commands and moving around, and run the selected line

```
cmd + enter: run the current line
shift + cmd + enter: run the current chunk
shift + cmd + N: run the next chunk
ctrl + b: go to previous chunk
ctrl + n: go to next chunk
ctrl + a: go to the beginning of the chunk
ctrl + e: go to the end of the chunk
```

Here I am also attaching my multicmds inside my **settings.json** file. 

```json
     {
            "command": "multicmd.py.run.next.chunk.center",
            "sequence": [
                "jupyter.gotoNextCellInFile",
                "jupyter.runcurrentcell",
                "cursorDown",
                "center-editor-window.center",
                "interactive.scrollToBottom"
            ]
        },
        {
            "command": "multicmd.py.go.next.chunk.center",
            "sequence": [
                "jupyter.gotoNextCellInFile",
                "cursorDown",
                "center-editor-window.center"
            ]
        },
        {
            "command": "multicmd.py.go.previous.chunk.center",
            "sequence": [
                "jupyter.gotoPrevCellInFile",
                "cursorDown",
                "center-editor-window.center"
            ]
        },
        {
            "command": "multicmd.py.run.current.chunk.center",
            "sequence": [
                "jupyter.runcurrentcell",
                "center-editor-window.center",
                "interactive.scrollToBottom"
            ]
        },
        {
            "command": "multicmd.py.run.current.line.move.down",
            "sequence": [
                "jupyter.execSelectionInteractive",
                "cursorDown",
                "interactive.scrollToBottom"
            ]
        },
        {
            "command": "multicmd.py.go.beginning.cell",
            "sequence": [
                "jupyter.gotoPrevCellInFile",
                "jupyter.gotoNextCellInFile",
                "cursorDown",
                "center-editor-window.center"
            ]
        },
        {
            "command": "multicmd.py.go.end.cell",
            "sequence": [
                "jupyter.gotoNextCellInFile",
                "cursorUp",
                "cursorUp",
                "center-editor-window.center"
            ]
        }
```



### 3. Always show the lates running cell in interactive terminal

You can search for "scroll" in settings, and tick the option for **Enable/disable smart scroll** and tick **jupyter: always scroll on new cell**.

### 4. Always expand all cells in the interavtive window

To set it as default to expand cells, you can search for "collapse cell" in settings, and choose "never" in the notebook for **interactive window: collapse cell input code**.

### 5. Quickly check function docs by using kite plugin

Here I am binding the key, **F1**, to open the kite doc for functions at the cursor. This is quite convenient since I am more used to the function documention and help in R. Of course, you can search inside the modules or [python documentations](https://docs.python.org/3/).

### 6. Other useful tricks

(1) Useful shortcuts (show and hide the terminal via **shift + tab**)

(2) Suggestion: better not to append comment (#) after the script line, since it may cause problem for look for help function

e.g., print? # search for help would cause error.

(3) Install "Doc View" extension so that you can see the function documentation, which is somehow similar to the kite copilot function. You can find it insider the sidebar of vs code or go to terminal (**shift + tab**) in vs code-click the symbol for documentation.

Check this link for an overview: https://www.youtube.com/watch?v=I525eE-hsNc

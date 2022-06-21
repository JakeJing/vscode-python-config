# vscode-python-config

This repos. includes the step-by-step configuration of python in **VS code**. I am trying to make the configuration as similar as the one I have for `Rmarkdown` notebook. Thus, most shortcuts and outlook would would be more or less the same as my rmarkdown notebook in VS code.

Here are some important .json files for customize your settings.

```json
1. settings.json
2. keybinding.json
3. snippets - python.json
4. snippets - r.json
5. snippets - rmd.json
```

Here are the necessary extensions I have installed:

```json
1. python
2. pylance
3. Jupyter 
4. Jupyter Keymap
5. Docs View # another way to look at func doc
6. Kite AutoComplete # func docs
7. multi-command # useful for defining a sequence of commands
8. language-weave # funcs like weave.jl and pweave
9. terminal-command-keys # binding key to run cmds in terminal
10. Better comments # supports * ? ! // and TODO comments highlighting
11. indent-rainbow # color the indentations (not needed)
12. vscode-icons # for file icon theme in Explore
13. Rainbow CSV # colorize the csv cols
14. Rainbow Brackets # match colors of brackets
15. select-by # useful for customized movement by regexp
```

### 1. Hide the "run cell" and "debug cell" icon at the top of cell

You need to search for "code lens" in settings, and uncheck **Jupyter:Enable Cell Code Lens**

### 2. Change the keybinding for running commands and moving around, and run the selected line

It is quite important for me to move between and winthin cells. Since I have defined my own cell marker (**# %% name**), it is necessary to set you own rule to navigate between cells. Here I am using `select-by` extension, which allows me to match cells via predefined regular expressions and move around. It also allows us to run multiple commands in a row. This make it quite suitable for me (see the [extension documentation](https://github.com/rioj7/select-by#an-example) for details).

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
// cell navigation by using moveby.regex from select-by extension
{
    "key": "ctrl+b", // moveby to previous chunk and center
    "when": "editorTextFocus && jupyter.hascodecells && !jupyter.webExtension && !notebookEditorFocused && editorLangId == 'python'",
    "command": "extension.multiCommand.execute",
    "args": {
      "sequence": [
        {
          "command": "cursorUp"
        },
        {
          "command": "moveby.regex",
          "args": {
            "regex": "# %% name", // define cell chunk marker
            "properties": [
              "moveby", // index1: moveby
              "prev", // index2: previous
              "start" // index3: cursor move to the start 
            ],
            "label": "move to previous chunk",
          }
        },
        {
          "command": "cursorDown"
        },
        {
          "command": "center-editor-window.center"
        }
      ]
    }
  },
  {
    "key": "ctrl+n", // moveby to next chunk and center
    "when": "editorTextFocus && jupyter.hascodecells && !jupyter.webExtension && !notebookEditorFocused && editorLangId == 'python'",
    "command": "extension.multiCommand.execute",
    "args": {
      "sequence": [
        {
          "command": "moveby.regex",
          "args": {
            "regex": "# %% name",
            "properties": [
              "moveby", // index1: moveby
              "next", // index2: previous
              "start" // index3: cursor move to the start 
            ],
            "label": "move to next chunk",
          }
        },
        {
          "command": "cursorDown"
        },
        {
          "command": "center-editor-window.center"
        }
      ]
    }
  },
  {
    "key": "shift+cmd+n", // run next chunk and center
    "when": "editorTextFocus && jupyter.hascodecells && !jupyter.webExtension && !notebookEditorFocused && editorLangId == 'python'",
    "command": "extension.multiCommand.execute",
    "args": {
      "sequence": [
        {
          "command": "moveby.regex",
          "args": {
            "regex": "# %% name",
            "properties": [
              "moveby", // index1: moveby
              "next", // index2: previous
              "start" // index3: cursor move to the start 
            ],
            "label": "move to next chunk",
          }
        },
        {
          "command": "cursorDown"
        },
        {
          "command": "jupyter.runcurrentcell",
        },
        {
          "command": "center-editor-window.center"
        },
        {
          "command": "interactive.scrollToBottom"
        }
      ]
    }
  },

// other commands rely on vs-code jupyter cmds
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



### 3. Always show the latest running cell in interactive terminal

You can search for "scroll" in settings, and tick the option for **Enable/disable smart scroll** and tick **jupyter: always scroll on new cell**.

**Note:** it seems that there is no good solution to this issue at this moment, you just need to run a cell several times until the interactive window gets fixed at the last line (see this [issue](https://github.com/microsoft/vscode/issues/145353)). My currect solution is to use multi commands to always scroll the interactive window to the bottom in your **settings.json**, and set a keybinding in **keybindings.json**.

```json
        {
            "command": "multicmd.py.run.current.chunk.center",
            "sequence": [
                "jupyter.runcurrentcell",
                "center-editor-window.center",
                "interactive.scrollToBottom"
            ]
        },
```

```json
  {
    "key": "shift+cmd+enter",
    "command": "multicmd.py.run.current.chunk.center",
    "when": "editorTextFocus && editorLangId == 'python' && jupyter.hascodecells && !jupyter.webExtension && !notebookEditorFocused"
  },
```



### 4. Always expand all cells in the interavtive window

To set it as default to expand cells, you can search for "collapse cell" in settings, and choose "never" in the notebook for **interactive window: collapse cell input code**.

### 5. Quickly check function docs by using kite plugin

Here I am binding the key, **F1**, to open the kite doc for functions at the cursor. This is quite convenient since I am more used to the function documention and help in R. Of course, you can search inside the modules or [python documentations](https://docs.python.org/3/).

### 6. Inlne title bar

You need to rely on the extension of "Customize UI" to set the title bar of VS code to be inline. Searching "customize" and set **customize UI: Title Bar** as inline. You need to restart to see the effect.

### 7. Set notebook output font size

To save the space for the notebook output, I set "**Notebook:Output font size**" at 15.

### 8. Python autoformating

You can make use of auto formating to clean you code. Here I am using "autopep8", and you can also choose "black" in  "**Python:Formating:Provider**"

### 9. Automatically compile .py file into pdf


I am using `pandoc` and `pweave` to first convert the currect python script into python markdown format (**.pmd**), and then compile it into pdf. Here I have a fish function to do these automatically. 

Note that to avoid the annoying warnings, I am using some specific character (`# ~~` ) as an indicator for yaml header and markdown inline code format. You also write inline comments directly, though it may cause some warnings for the spelling of code. To compile this script into pdf, I have written a funtion that can automatically delete the specaial indicator, and render the file into pdf via `pweave` function. 

```bash
# set the current date
set DT (date +"%d.%m.%Y")

# replace the indicator chars and chunk names
sed  's/^# ~~ //' $filename | sed 's/^# %% /```python,/' | sed 's/^# %%$/```/' | sed "s/^date.*/date: $DT/" > "$rootname".pmd

# compile pmd into md
pweave -f pandoc "$rootname".pmd

# pandoc render md into tex
/usr/local/bin/pandoc +RTS -K512m -RTS "$rootname".md --to latex --from markdown+autolink_bare_uris+tex_math_single_backslash --output "$rootname".tex --self-contained --table-of-contents --toc-depth 4 --number-sections --highlight-style tango --variable graphics --wrap preserve --include-in-header /var/folders/lw/_wcbs1pd6437lkq86pnljf7r0000gq/T//RtmpuTh6pD/rmarkdown-strb0d135922d1.html --variable 'geometry:margin=1in' --variable tables=yes --standalone -Mhas-frontmatter=false

# compile tex into pdf 2 times to get the content page
xelatex "$rootname".tex
xelatex "$rootname".tex

# remove temp files
rm "$rootname".md "$rootname".tex "$rootname".aux "$rootname".lo* "$rootname".out "$rootname".toc

# open the rendered pdf via Preview
open -a Preview "$rootname".pdf
```

This give you the basic tools to run `autoweave template.py` in your terminal and see whether it works properly.

```bash
autoweave template.py
```

To directly run the command in VS code, I am using an extension of **terminal-command-keys** to map the key of **cmd+shift+k** to render the python script by adding the following chunk inside your **keybindings.json**. 

```json
  {
    "description": "render a python file into pdf",
    "key": "cmd+shift+k",
    "command": "terminalCommandKeys.run",
    "when": "editorTextFocus && editorLangId == 'python'",
    "args": {
      "cmd": "autoweave ${file}"
    }
  },
```

### 10. disable scroll beyond the last line

You can search  "**scrollBeyondLastLine**" in setings and uncheck **Editor:scroll beyond last line**.

### 11. change the regular expression for jupyter cells

You can search for "jupyter cell" in the settings, and change the following options.

```json
jupyter.codeRegularExpression: ^(#\s*%%\s*name|#\s*\<codecell\>|#\s*In\[\d*?\]|#\s*In\[ \])

jupyter.defaultCellMarker: # %% name

jupyter.markdownRegularExpression: ^(#\s*%%\s*\[markdown\]|#\s*\<markdowncell\>)|^(#\s*%%(\s.*?)\s#\s*%%\s*name)
```



### 13. Other useful tricks

(1) hover around the dataset or function, you will be able to have a preview of the data and function doc.

(2) Useful shortcuts (show and hide the terminal via **shift + tab**)

(3) Suggestion: better not to append comment (#) after the script line, since it may cause problem for look for help function

e.g., print? # search for help would cause error.

(4) Install "Doc View" extension so that you can see the function documentation, which is somehow similar to the kite copilot function. You can find it insider the sidebar of vs code or go to terminal (**shift + tab**) in vs code-click the symbol for documentation.

Check this link for an overview: https://www.youtube.com/watch?v=I525eE-hsNc

(5) use `object.__dir__()` to check all applicable functions associated to the object type. Pls don't forget the bracket at the end. Or you can directly use `dir(object)` to get the applicable funds. 

(6) block select in vs code (**select via mouse** & holding **alt + shift** keys)

(7) trim trailing whitespace (seach in the comd template and search "trim trailing whitespace")

(8) indent line (**cmd + [**) and outdent line (**cmd + ]**)

(9) **toggle column selection** mode in command template (enable/disable column selection)

(10) Inspect an object in python

- **Cmd + p:** print(dir(obj))

- list(obj)

- vars(obj)

- **cmd + r:** It will make use of `objbrowser` module.

  **Attributes**: are shown in black in the interactive window;

  **Functions/Methods**: are shown in blue

  ```python
  from objbrowser import browse
  
  # replace $0$ with object name, and run the cmd
  browse({'obj': $0$}, *show_callable_attributes* = True,*show_special_attributes* = False, *reset* = True)
  ```

  

  








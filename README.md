# vscode-python-config

This repos. includes the step-by-step configuration of python in **VS code**. I am trying to make the configuration as similar as the one I have for `Rmarkdown` notebook. Thus, most shortcuts and outlook would would be more or less the same as my rmarkdown notebook in VS code.

Here are the necessary extensions I have installed:

```
1. python
2. pylance
3. Jupyter 
4. Jupyter Keymap
5. Docs View
```

1. Hide the "run cell" and "debug cell" icon at the top of cell

You need to search for "code lens" in settings, and uncheck **Jupyter:Enable Cell Code Lens**


2. Change the keybinding for running commands and moving around, and run the selected line

```
cmd + enter: run the current line
shift + cmd + enter: run the current chunk
shift + cmd + N: run the next chunk
ctrl + b: go to previous chunk
ctrl + n: go to next chunk
ctrl + a: go to the beginning of the chunk
ctrl + e: go to the end of the chunk
```


3. Setting -> search "output scroll" (1) check the option for "Enable/disable smart scroll"; (2) check the option for "always scroll on new cell".

4. Setting it as default to expand cells and set Keybinding for expand all the cells in interactive window

Settings -> collapse cell -> notebooks -> set "never" for collapse cell input code

5. bind the key, **F1**, to open the kite doc for functions at the cursor



(1) Useful shortcuts (show and hide the terminal via shift + tab)

(2) Suggestion: better not to append comment (#) after the script line, since it may cause problem for look for help function

e.g., print? # search for help would cause error.

(3) Install "Doc View" extension so that you can see the function documentation, which is somehow similar to the kite copilot function

Check this link for an overview: https://www.youtube.com/watch?v=I525eE-hsNc

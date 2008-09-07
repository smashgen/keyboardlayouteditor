This is the Keyboard Layout Editor, a pygtk program that helps create or edit XKB keyboard layouts.

This is the version that has been submitted to the GSoC xorg project; you can find the latest version
at 
http://code.google.com/p/keyboardlayouteditor/

You are strongly encouraged to use the version that is found at the above URL, 
as it includes several bug fixes.

The project was developed using Eclipse (Ganymede), with the Python (PyDev) and Antlr (AntlrIDE) add-ons.
If you also have SVN support in Eclipse, you can grab the latest source from within Eclipse.
There is also integration with Mylene so that you can get the list of issues/bugs/todo items 
automatically.

To run the application, you need the python binding packages for 
* Cairo
* Pango
* GObject
* lxml

and the Antlr 3.1 Runtime environment for Python. You grab that at 
http://antlr.org/download/Python/
Choose the appropriate *.egg file for the 3.1 version, then type

sudo easy_install antlr_python_runtime-3.1-py2.5.egg

This should to the installation for you.

You run this program with 

./KeyboardLayoutEditor.py

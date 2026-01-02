# src/build.py
import FreeCAD as App
from parts.block import make_block

doc = App.newDocument("FCMD")
make_block(10, 20, 5)
App.ActiveDocument.recompute()

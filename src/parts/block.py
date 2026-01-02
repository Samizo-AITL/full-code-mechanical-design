# src/parts/block.py
import FreeCAD as App
import Part

def make_block(w=10, d=20, h=5):
    box = Part.makeBox(w, d, h)
    obj = App.ActiveDocument.addObject("Part::Feature", "Block")
    obj.Shape = box
    return obj

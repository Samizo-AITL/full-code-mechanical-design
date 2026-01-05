# src/parts/block.py
import FreeCAD as App
import Part

def make_block(
    width: float,
    depth: float,
    height: float,
    name: str = "Block",
    origin=(0, 0, 0),
):
    """
    Generate a rectangular block.

    Parameters
    ----------
    width  : X direction size
    depth  : Y direction size
    height : Z direction size
    origin : (x, y, z) reference point
    """

    box = Part.makeBox(width, depth, height)

    obj = App.ActiveDocument.addObject("Part::Feature", name)
    obj.Shape = box
    obj.Placement.Base = App.Vector(*origin)

    return obj

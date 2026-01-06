# parts/base_plate.py
import FreeCAD as App
import Part

def make_base_plate(
    name="BasePlate",
    L=120.0,   # length [mm]
    W=80.0,    # width  [mm]
    T=6.0,     # thickness [mm]
    corner_r=6.0,
    hole_d=5.5,
    hole_edge=12.0
):
    """
    Base plate with rounded corners + 4 through holes.
    Returns (doc_object, shape)
    """
    doc = App.ActiveDocument

    # Base solid
    plate = Part.makeBox(L, W, T)

    # Rounded corners (fillet vertical edges only)
    # Find edges that are vertical (parallel to Z) and at outer perimeter.
    fillet_edges = []
    for e in plate.Edges:
        # edge is a line: check direction approx along Z
        try:
            c = e.Curve
            if hasattr(c, "Direction"):
                d = c.Direction
                if abs(d.x) < 1e-6 and abs(d.y) < 1e-6 and abs(abs(d.z) - 1.0) < 1e-6:
                    # vertical line edge
                    fillet_edges.append(e)
        except Exception:
            pass

    if fillet_edges and corner_r > 0:
        plate = plate.makeFillet(corner_r, fillet_edges)

    # 4 holes
    # Hole centers: offset from edges by hole_edge
    xs = [hole_edge, L - hole_edge]
    ys = [hole_edge, W - hole_edge]

    for x in xs:
        for y in ys:
            cyl = Part.makeCylinder(hole_d / 2.0, T * 3.0, App.Vector(x, y, -T))  # longer than thickness
            plate = plate.cut(cyl)

    obj = doc.addObject("Part::Feature", name)
    obj.Shape = plate
    obj.Label = name
    return obj, plate

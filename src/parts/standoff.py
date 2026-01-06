# parts/standoff.py
import FreeCAD as App
import Part

def make_standoff(
    name="Standoff",
    outer_d=12.0,
    inner_d=5.5,
    H=25.0,
    chamfer=0.8
):
    """
    Simple standoff: outer cylinder with through hole + optional chamfer on top/bottom.
    Returns (doc_object, shape)
    """
    doc = App.ActiveDocument

    outer = Part.makeCylinder(outer_d/2.0, H)
    hole  = Part.makeCylinder(inner_d/2.0, H * 3.0, App.Vector(0, 0, -H))
    solid = outer.cut(hole)

    # Small chamfer: apply to circular edges (top & bottom outer edges)
    if chamfer > 0:
        chamfer_edges = []
        for e in solid.Edges:
            # pick outer rim circles by radius proximity
            try:
                c = e.Curve
                if c.__class__.__name__ == "Circle":
                    if abs(c.Radius - outer_d/2.0) < 1e-3:
                        chamfer_edges.append(e)
            except Exception:
                pass
        if chamfer_edges:
            try:
                solid = solid.makeChamfer(chamfer, chamfer_edges)
            except Exception:
                # If chamfer fails, keep as-is.
                pass

    obj = doc.addObject("Part::Feature", name)
    obj.Shape = solid
    obj.Label = name
    return obj, solid

# assembly/demo_assembly.py
import FreeCAD as App

from parts.base_plate import make_base_plate
from parts.standoff import make_standoff

def build_demo_assembly(params=None):
    """
    Create base plate + 4 standoffs at hole positions.
    """
    if params is None:
        params = {}

    L = float(params.get("L", 120.0))
    W = float(params.get("W", 80.0))
    T = float(params.get("T", 6.0))
    hole_edge = float(params.get("hole_edge", 12.0))
    hole_d = float(params.get("hole_d", 5.5))

    st_outer_d = float(params.get("st_outer_d", 12.0))
    st_inner_d = float(params.get("st_inner_d", hole_d))
    st_H = float(params.get("st_H", 25.0))

    doc = App.ActiveDocument

    base_obj, _ = make_base_plate(
        name="BasePlate",
        L=L, W=W, T=T,
        corner_r=float(params.get("corner_r", 6.0)),
        hole_d=hole_d,
        hole_edge=hole_edge
    )

    # Hole centers match base_plate logic
    xs = [hole_edge, L - hole_edge]
    ys = [hole_edge, W - hole_edge]

    standoffs = []
    idx = 1
    for x in xs:
        for y in ys:
            st_obj, _ = make_standoff(
                name=f"Standoff{idx}",
                outer_d=st_outer_d,
                inner_d=st_inner_d,
                H=st_H,
                chamfer=float(params.get("st_chamfer", 0.8))
            )
            # Place on top of the plate, centered at hole
            st_obj.Placement.Base = App.Vector(x, y, T)
            standoffs.append(st_obj)
            idx += 1

    doc.recompute()
    return base_obj, standoffs

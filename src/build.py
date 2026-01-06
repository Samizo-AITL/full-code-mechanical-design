# build.py

import sys
import os

PROJECT_ROOT = r"C:\Users\Lenovo\GitHub\full-code-mechanical-design-sample"
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

import FreeCAD as App
import Part

from assembly.demo_assembly import build_demo_assembly

def export_step(objects, out_path):
    # STEP export: Part.export expects document objects list
    Part.export(objects, out_path)

def export_stl(objects, out_path):
    import Mesh
    Mesh.export(objects, out_path)

def main():
    # Create document
    doc = App.newDocument("FCMD_Demo")

    params = {
        "L": 120.0,
        "W": 80.0,
        "T": 6.0,
        "corner_r": 6.0,
        "hole_d": 5.5,
        "hole_edge": 12.0,
        "st_outer_d": 12.0,
        "st_inner_d": 5.5,
        "st_H": 25.0,
        "st_chamfer": 0.8,
    }

    base, standoffs = build_demo_assembly(params=params)

    # Output directory
    out_dir = os.path.join(os.path.dirname(__file__), "out")
    os.makedirs(out_dir, exist_ok=True)

    # Export assembly as STEP/STL
    asm_objects = [base] + standoffs
    export_step(asm_objects, os.path.join(out_dir, "demo_assembly.step"))
    export_stl(asm_objects, os.path.join(out_dir, "demo_assembly.stl"))

    # Also save FreeCAD file
    doc.saveAs(os.path.join(out_dir, "demo_assembly.FCStd"))
    App.Console.PrintMessage(f"Exported to: {out_dir}\n")

if __name__ == "__main__":
    main()

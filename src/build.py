# src/build.py
import FreeCAD as App
import os

from parts.block import make_block

# Create document
doc = App.newDocument("FCMD")

# === Design parameters (design intent) ===
WIDTH  = 10
DEPTH  = 20
HEIGHT = 5

# Generate part
block = make_block(WIDTH, DEPTH, HEIGHT)

# Recompute model
doc.recompute()

# Save result
output_path = os.path.abspath("output.FCStd")
doc.saveAs(output_path)

print(f"Model generated: {output_path}")

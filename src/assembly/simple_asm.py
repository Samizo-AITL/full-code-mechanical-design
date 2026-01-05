# src/assembly/simple_asm.py
import FreeCAD as App

from parts.block import make_block


def build_simple_assembly():
    """
    Minimal example of a placement-based assembly.

    No constraints.
    No solver.
    Explicit placement only.
    """

    # === Base block ===
    base = make_block(
        width=10,
        depth=20,
        height=5,
        name="BaseBlock",
        origin=(0, 0, 0),
    )

    # === Upper block ===
    upper = make_block(
        width=6,
        depth=10,
        height=3,
        name="UpperBlock",
        origin=(2, 5, 5),  # placed explicitly on top of base
    )

    return [base, upper]


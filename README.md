# Full Code Mechanical Design

**A code-driven approach to mechanical design without relying on GUI-based CAD workflows.**

This repository explores a methodology for designing mechanical parts and assemblies
entirely through Python code using FreeCAD, focusing on reproducibility, clarity of design intent,
and automation.

---

## Concept

Traditional CAD workflows are heavily dependent on GUI operations, feature histories,
and constraint-based assemblies.
This project intentionally avoids those assumptions and adopts the following principles:

- Dimensions are **variables**
- Geometry is defined by **functions**
- Parts are treated as **modules**
- Assemblies are defined by **placements**, not constraints
- The GUI is used only as a **viewer**

The goal is to preserve design intent and reproducibility directly in code.

---

## Why Code-Driven Mechanical Design?

- High reproducibility (identical results on every execution)
- Easy generation of design variants and parametric families
- Design intent is explicit and version-controlled
- Strong compatibility with automation (CSV, optimization, FEM, CAM)
- Suitable for complex systems and equipment-level design

This approach can be summarized as:

**Mechanical Design as Code**

---

## Design Policy

- Do not rely on FreeCAD GUI operations
- Prefer direct OCCT-based geometry (Part module)
- Use Sketch / PartDesign only when strictly necessary
- Define clear reference origins and orientations for all parts
- Define assemblies using explicit coordinate placements

---

## Repository Structure

```
├─ parts/ # Individual part generators (functions/modules)
├─ assembly/ # Assembly and layout definitions
├─ build.py # Entry point to generate the complete model
└─ README.md
```

---


---

## Status

- Experimental
- Actively evolving
- Focused on establishing a robust, GUI-independent design workflow

---

## Philosophy

> CAD is not a drawing tool.  
> It is an engine for executing design logic.

---

## License

MIT (planned)


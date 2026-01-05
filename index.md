---
title: "full-code-mechanical-design"
description: "A code-driven approach to mechanical design using Python and FreeCAD"
---

# Full Code Mechanical Design

**A code-driven approach to mechanical design without relying on GUI-based CAD workflows.**

This repository explores a methodology for designing mechanical parts and assemblies
entirely through Python code using FreeCAD, focusing on reproducibility, clarity of design intent,
and automation.

---

## 🔗 Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/full-code-mechanical-design/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/full-code-mechanical-design/tree/main) |

[![Back to Samizo-AITL Portal](https://img.shields.io/badge/Back%20to%20Samizo--AITL%20Portal-brightgreen)](https://samizo-aitl.github.io)

---

This repository explores a methodology for designing mechanical parts and assemblies
entirely through Python code using FreeCAD, focusing on reproducibility,
clarity of design intent, and automation.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18134920.svg)](https://doi.org/10.5281/zenodo.18134920)

---

## Citation & Prior Art

This work is published with a DOI via Zenodo (10.5281/zenodo.18134920)
and constitutes prior art for code-driven mechanical design methodologies.

---

## Why Full Code Mechanical Design Wins

Mechanical design should not be treated as a static artifact (CAD data or drawings),
but as a reproducible, evolvable set of rules.

**Full Code Mechanical Design** shifts the core of mechanical design from
manual GUI operations to explicit, executable code.

In this approach:

- Geometry is defined by code, not by mouse operations
- Dimensions are variables, not fixed values
- Design intent is explicit and reviewable
- Verification and design live in the same environment
- Mechanical design becomes reusable intellectual property (IP)

This is not an efficiency improvement.  
It is a structural transformation of mechanical design itself.

Once design logic is expressed as code,
there is no reason to return to GUI-driven workflows.

---

## Concept

Traditional CAD workflows are heavily dependent on GUI operations,
feature histories, and constraint-based assemblies.

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
├─ src/
│  ├─ parts/        # Individual part generators (functions/modules)
│  ├─ assembly/     # Assembly and layout definitions
│  └─ build.py      # Entry point to generate the complete model
├─ README.md
└─ LICENSE
```

---

## ▶ Quick Start (Minimal Reproducible Example)

This repository includes a **minimal working example** that generates
a simple 3D mechanical model using **FreeCAD in headless (non-GUI) mode**.

### Requirements

- FreeCAD 0.21 or later
- Python bundled with FreeCAD

⚠️ **Important**  
Do **NOT** use system Python.  
You must use the Python interpreter bundled with FreeCAD.

---

### Execution (Windows example)

```powershell
cd src
"C:\Program Files\FreeCAD 0.21\bin\FreeCADCmd.exe" build.py
```

This will:

- Generate a simple part defined in `parts/`
- Assemble it using placement logic in `assembly/`
- Create a FreeCAD document (`.FCStd`) as output

The FreeCAD GUI is **not required** for model generation.  
It may be used only to inspect the generated result.

---

### Execution (Linux example)

```bash
cd src
freecadcmd build.py
```

---

### Purpose of This Example

This example is intentionally minimal.

Its purpose is **not** to demonstrate complex geometry,
but to prove that:

- Mechanical geometry can be generated entirely by code
- Design intent lives in Python, not in GUI operations
- CAD is an execution engine, not an authoring environment

More advanced examples will be added incrementally.

---

## Status

This repository currently focuses on defining the **conceptual and architectural
principles** of Full Code Mechanical Design.

Python / FreeCAD implementation examples will be added incrementally,
starting from minimal reproducible geometry definitions.

---

## Philosophy

> CAD is not a drawing tool.  
> It is an engine for executing design logic.

---

## Example Output

The following model was generated by running the provided Python code in FreeCAD
without any GUI-based modeling operations.

![example](docs/example.png)

---

## Analogy to SoC Design

This approach is directly analogous to modern SoC design workflows.

In semiconductor design, manual wiring and layout-centric design
ended decades ago. Today, engineers describe intent using RTL
(Verilog/VHDL), while placement and routing are handled by tools.

Mechanical design is currently at a similar turning point.

Traditional mechanical CAD workflows rely heavily on manual GUI
operations, much like hand-routing in early chip design.

In contrast, this project treats:

- Geometry generation as layout
- OCCT as the geometry engine
- Python code as RTL
- Assemblies as floorplanning
- CAD tools as execution environments

In this sense, **Full Code Mechanical Design is to mechanical engineering
what RTL is to SoC design**.

---

## Beyond CAD: Mechanical Design as IP

By expressing geometry, constraints, and design decisions
entirely in code, mechanical design itself becomes
a reusable and evolvable intellectual property (IP).

The generated CAD model is only a byproduct.  
The true asset is the executable design knowledge,
similar to RTL or IP blocks in SoC design.

---

## Intellectual Property Notice

This repository represents a reference implementation of
code-driven mechanical design methodology.

The core value of this project lies not in generated CAD files,
but in the design logic encoded as software.

Forking is permitted under the license.
However, claims of originality or ownership over the methodology itself are not.

---

## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **Expertise** | Semiconductor devices (logic, memory, high-voltage mixed-signal)<br>Thin-film piezo actuators for inkjet systems<br>PrecisionCore printhead productization, BOM management, ISO training |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

---

## 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/full-code-mechanical-design//#-license)

| Item | License | Description |
|------|---------|-------------|
| **Source Code** | Apache License 2.0 | Free to use, modify, redistribute, with patent protection |
| **Text Materials** | CC BY 4.0 | Attribution required |
| **Figures & Diagrams** | CC BY-NC 4.0 | Non-commercial use only |
| **Generated CAD Outputs** | Same as source code | Derived from licensed code |
| **External References** | Original license applies | Cite properly |

### Methodology Notice

This repository discloses a code-driven mechanical design methodology.
The methodology itself is provided as prior art and may not be claimed
as exclusive intellectual property by third parties.

### Prior Art Notice

This repository and its associated Zenodo record
(DOI: 10.5281/zenodo.18134920)
constitute a public disclosure of the
Full Code Mechanical Design methodology.

---

## 💬 Feedback

> Suggestions, improvements, and discussions are welcome via GitHub Discussions.

[GitHub Discussions](https://github.com/Samizo-AITL/full-code-mechanical-design/discussions)

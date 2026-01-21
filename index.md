---
title: "full-code-mechanical-design"
description: "A code-driven approach to mechanical design using Python and FreeCAD"
---

# 🧩 Full Code Mechanical Design

**A code-driven approach to mechanical design without relying on GUI-based CAD workflows.**

[![Back to Portal (EN)](https://img.shields.io/badge/Back%20to%20Portal-0B5FFF?style=for-the-badge&logo=homeassistant&logoColor=white)](https://samizo-aitl.github.io/portal/en/)

This repository explores a methodology for designing mechanical parts and assemblies  
**entirely through Python code using FreeCAD**, focusing on:

- ♻️ reproducibility  
- 🧠 clarity of design intent  
- 🤖 automation  

---

## 🔗 Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/full-code-mechanical-design/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/full-code-mechanical-design/tree/main) |

---

This repository explores a methodology for designing mechanical parts and assemblies  
entirely through Python code using FreeCAD, focusing on reproducibility,  
clarity of design intent, and automation.

📌 **Persistent Identifier (DOI)**  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18134920.svg)](https://doi.org/10.5281/zenodo.18134920)

---

## 📚 Citation & Prior Art

This work is published with a DOI via **Zenodo** (10.5281/zenodo.18134920)  
and constitutes **prior art** for code-driven mechanical design methodologies.

---

## 🕰 Historical Context

Prototype fabrication → machining → dimensional measurement → drawing.  
Three-dimensional objects are projected onto two-dimensional drawings  
using orthographic projection, and conversely, three-dimensional form  
is reconstructed mentally from two-dimensional drawings.

This bidirectional translation constituted a **core skill**  
for traditional mechanical designers.

From this perspective, it is understandable that  
**generative design or code-driven approaches**—where the designer  
does not directly manipulate geometry—can feel intuitively  
difficult to accept.

However, semiconductor layout design followed a **similar trajectory**.

There was a time when routing was performed manually,  
with designers carefully accounting for process-specific behavior  
based on experience and tacit knowledge.

As design rules were formalized and incorporated into **PDKs**,  
the center of design activity shifted  
from manual layout to logical description using **Verilog**.

Viewed in the context of technological history,  
it may be unavoidable that mechanical design  
will follow a comparable path.

---

## 🏆 Why Full Code Mechanical Design Wins

Mechanical design should not be treated as a static artifact  
(CAD data or drawings),  
but as a **reproducible, evolvable set of rules**.

**Full Code Mechanical Design** shifts the core of mechanical design from  
manual GUI operations to **explicit, executable code**.

In this approach:

- 🧮 Geometry is defined by code, not by mouse operations  
- 📐 Dimensions are variables, not fixed values  
- 🧠 Design intent is explicit and reviewable  
- 🧪 Verification and design live in the same environment  
- 🧱 Mechanical design becomes reusable intellectual property (IP)  

This is **not an efficiency improvement**.  
It is a **structural transformation** of mechanical design itself.

Once design logic is expressed as code,  
there is no reason to return to GUI-driven workflows.

---

## 🧠 Concept

Traditional CAD workflows are heavily dependent on GUI operations,  
feature histories, and constraint-based assemblies.

This project intentionally avoids those assumptions and adopts the following principles:

- 🔢 Dimensions are **variables**  
- 🧩 Geometry is defined by **functions**  
- 📦 Parts are treated as **modules**  
- 📐 Assemblies are defined by **placements**, not constraints  
- 👁 The GUI is used only as a **viewer**  

The goal is to preserve **design intent and reproducibility** directly in code.

---

## ❓ Why Code-Driven Mechanical Design?

- ♻️ High reproducibility (identical results on every execution)  
- 🔁 Easy generation of design variants and parametric families  
- 🧠 Design intent is explicit and version-controlled  
- 🤖 Strong compatibility with automation (CSV, optimization, FEM, CAM)  
- 🏗 Suitable for complex systems and equipment-level design  

This approach can be summarized as:

> **Mechanical Design as Code**

---

## 📐 Design Policy

- ❌ Do not rely on FreeCAD GUI operations  
- ✅ Prefer direct OCCT-based geometry (Part module)  
- ⚠️ Use Sketch / PartDesign only when strictly necessary  
- 📍 Define clear reference origins and orientations for all parts  
- 🧭 Define assemblies using explicit coordinate placements  

---

## 🗂 Repository Structure

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

### 🔧 Requirements

- FreeCAD 0.21 or later  
- Python bundled with FreeCAD  

⚠️ **Important**  
Do **NOT** use system Python.  
You must use the Python interpreter bundled with FreeCAD.

---

### ▶ Execution (Windows example)

```powershell
cd src
"C:\Program Files\FreeCAD 0.21\bin\FreeCADCmd.exe" build.py
```

This will:

- 🧩 Generate a simple part defined in `parts/`  
- 🧭 Assemble it using placement logic in `assembly/`  
- 📄 Create a FreeCAD document (`.FCStd`) as output  

The FreeCAD GUI is **not required** for model generation.  
It may be used only to inspect the generated result.

---

### ▶ Execution (Linux example)

```bash
cd src
freecadcmd build.py
```

---

### 🎯 Purpose of This Example

This example is intentionally **minimal**.

Its purpose is **not** to demonstrate complex geometry,  
but to prove that:

- Geometry can be generated **entirely by code**  
- Design intent lives in **Python**, not GUI operations  
- CAD is an **execution engine**, not an authoring environment  

---

## 🚧 Status

This repository currently focuses on defining the  
**conceptual and architectural principles**  
of Full Code Mechanical Design.

Python / FreeCAD implementation examples  
will be added incrementally.

---

## 🧭 Philosophy

> CAD is not a drawing tool.  
> It is an engine for executing design logic.

---

## 🧱 Example Output

The following model was generated by running the provided Python code in FreeCAD  
without any GUI-based modeling operations.

<a href="http://samizo-aitl.github.io/full-code-mechanical-design/fig/01_demo_assembly_generated.png" target="_blank">
  <img src="http://samizo-aitl.github.io/full-code-mechanical-design/fig/01_demo_assembly_generated.png"
       alt="Code-generated mechanical assembly (FreeCAD + Python)"
       style="width:80%;">
</a>

*Figure 1. Mechanical assembly generated purely by Python code using FreeCAD as a geometry engine.*

---

## 📐 Geometric Core Example (Function-Defined Geometry)

The following model demonstrates a **purely geometric solid**  
generated from a continuous mathematical function,  
without sketches, constraints, or GUI-based modeling steps.

<a href="http://samizo-aitl.github.io/full-code-mechanical-design/fig/02_geometric_function_loft.png" target="_blank">
  <img src="http://samizo-aitl.github.io/full-code-mechanical-design/fig/02_geometric_function_loft.png"
       alt="Function-defined geometric solid generated purely by code"
       style="width:80%;">
</a>

*Figure 2. A geometric solid generated from an explicit radius function  
$r = f(z)$ using Python code and FreeCAD as a geometry engine.*

---

## 🔌 Analogy to SoC Design

This approach is directly analogous to modern **SoC design workflows**.

- Geometry generation → layout  
- OCCT → geometry engine  
- Python → RTL  
- Assemblies → floorplanning  
- CAD → execution environment  

In this sense:

> **Full Code Mechanical Design is to mechanical engineering  
> what RTL is to SoC design.**

---

## 💎 Beyond CAD: Mechanical Design as IP

By expressing geometry, constraints, and design decisions  
entirely in code, mechanical design itself becomes  
a **reusable and evolvable intellectual property (IP)**.

The generated CAD model is only a byproduct.  
The true asset is the **executable design knowledge**.

---

## 🔍 Practical Workflow Comparison  
### Conventional Mechanical Design vs Full Code Mechanical Design

| Aspect | Conventional Workflow | Full Code Mechanical Design |
|------|----------------------|-----------------------------|
| Design authoring | GUI-based CAD operations | Python code |
| Dimensions | Fixed | Variables |
| Design intent | Implicit | Explicit |
| Design change | Manual edits | Logic change |
| Reusability | Low | High |
| Review | Drawings | Code + model |
| Scalability | Limited | High |

---

## 👤 Author

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **Expertise** | Semiconductor devices (logic, memory, high-voltage mixed-signal)<br>Thin-film piezo actuators for inkjet systems<br>Printhead productization, BOM management, ISO training |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-black?logo=github)](https://github.com/Samizo-AITL) |

---

## 📄 License

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/full-code-mechanical-design/#---license)

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

## 💬　Feedback

> Suggestions, improvements, and discussions are welcome via GitHub Discussions.

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/full-code-mechanical-design/discussions)

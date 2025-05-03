# Cause and Fault in Development

Welcome to the repository for the paper **"Cause and Fault in Development"**. This repository contains the experiments, data, analyses, and figures that support the research.

---

## 📖 Table of Contents
- [Introduction](#-introduction)
- [Repository Structure](#-repository-structure)
- [About the Experiments](#-about-the-experiments)

---

## 💡 Introduction

Responsibility requires causation. This is part of philosophical orthodoxy, embodied in the law, and reflected in psychological theories of responsibility. Even models suggesting that blame and praise influence causal judgment presuppose that causation must be established before such biases can operate.

The connection between responsibility and causation is also reflected in children's judgments: They don't blame someone merely associated with an outcome; causal involvement is necessary. Young children prioritize the magnitude of the outcome that was caused, regardless of intent, while older children also consider intentions. This "outcome-to-intention shift" may stem from distinct processes: one focused on mental states for judging intentionality, the other on causation. While one of the central questions concerning this shift is how, and when, mental states become integrated, it is usually assumed that causation is established first. But there are different kinds of causes that children reason about, which may influence their developing understanding of responsibility.

<img src="figures/exp_overview.png" alt="Methodology" width="100%" align="center">

---

## 📂 Repository Structure

```plaintext
├── appendix
├── code
│   ├── R
│   ├── experiments
│   └── python
├── data
├── docs
└── figures
```

### 🔍 Detailed Breakdown
- **`appendix/`**: Contains additional information and analyses not included in the paper.
  - **`appendix.pdf`**: [The appendix document.](appendix/appendix.pdf)

- **`code/`**: All code for running experiments, analyzing data, and generating figures.
  - **`experiments/`**: Experiment-specific code, including pre-registrations available via the Open Science Framework:
    - **Experiment 1**  
      - Fault question first ordering ([pre-registration](https://osf.io/2u4fp/?view_only=405ad3e533ba4e85982c97b10c372257))  
      - Fault question last ordering ([pre-registration](https://osf.io/f4n6w/?view_only=c6898909be10454dad7075fd519a7afc))  
    - **Experiment 2** ([pre-registration](https://osf.io/sjakw/?view_only=1f1bc44ef0f24b869f6eef3a839440ad))
  - **`R/`**: Scripts for data analysis and figure generation. See a rendered file [here](https://davdrose.github.io/cause_fault_dev/).

- **`data/`**: Contains anonymized datasets for all experiments.

- **`docs/`**: Contains a visualization of the analysis script in `code/R/`.

- **`figures/`**: All figures used in the paper, generated using scripts in `code/R/`.

---
<!-- 
## 🚀 Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/cause-and-fault.git
   cd cause-and-fault
   ```
2. Install required dependencies for each language used in `code/`.

3. Navigate to `code/` for experiment execution or analysis scripts:
   - For data analysis:
     ```bash
     cd code/R
     Rscript analysis_script.R
     ```
   - For experiment execution:
     ```bash
     cd code/experiments
     python experiment1.py
     ```

--- -->

## 🔬 About the Experiments

- Experiments involving **children** were conducted using **Lookit**.  
- Pre-registrations for all experiments are accessible on the Open Science Framework (links provided in the [Repository Structure](#-repository-structure)).

---
<!-- 
## 🖼️ Figures

All figures in the paper can be found in the `figures/` directory, generated using the analysis scripts in `code/R/`.

--- -->

Feel free to suggest additional improvements or features via issues or pull requests!

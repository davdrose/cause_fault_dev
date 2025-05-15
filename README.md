# Cause and Fault in Development

Preprint: [https://osf.io/preprints/psyarxiv/e58br_v1](https://osf.io/preprints/psyarxiv/e58br_v1)

Welcome to the repository for the paper **"Cause and Fault in Development"**. This repository contains the experiments, data, analyses, and figures that support the research.

## 👥 Authors

- **David Rose**★†¹  
- **Cici Hou**★²  
- **Shaun Nichols**³  
- **Tobias Gerstenberg**¹  
- **Ellen M. Markman**¹  

¹ Department of Psychology, Stanford University  
² Department of Computer Science, Stanford University  
³ Department of Philosophy, Cornell University  

★ joint first authors  
† davdrose@stanford.edu

## 📖 Table of Contents
- [Introduction](#-introduction)
- [Repository Structure](#-repository-structure)
- [About the Experiments](#-about-the-experiments)
- [CRediT author statement](#-credit-author-statement)

## 💡 Introduction

Responsibility requires causation. But there are different kinds of causes. Some are connected to their effects; others are disconnected. We ask how children's developing ability to distinguish causes relates to their understanding of moral responsibility. We found in Experiment 1 that when Andy hits Suzy with his bike, she falls into a fence and it breaks, 3-year-old children treated "caused", "break" and "fault" as referring to the direct cause, Suzy. By 4, they differentiated causes: Andy "caused" the fence to break, it's his "fault", but Suzy "broke" it. We found in Experiment 2 that when the chain involved disconnection, 3-year-olds focused only on the direct cause. Around 5 they distinguished causes, saying that the disconnecting cause "caused" an object to break, it’s their "fault", but the direct cause "broke" it. Our findings relate to the outcome-to-intention shift in moral responsibility and suggest a more fundamental shift in children's understanding of causation.

<img src="figures/exp_overview.png" alt="Methodology" width="100%" align="center">

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
      - Fault question first ordering ([pre-registration](https://osf.io/2u4fp))  
      - Fault question last ordering ([pre-registration](https://osf.io/f4n6w))  
    - **Experiment 2** ([pre-registration](https://osf.io/sjakw))
  - **`R/`**: Scripts for data analysis and figure generation. See a rendered file [here](https://davdrose.github.io/cause_fault_dev/).

- **`data/`**: Contains anonymized datasets for all experiments.

- **`docs/`**: Contains a visualization of the analysis script in `code/R/`.

- **`figures/`**: All figures used in the paper, generated using scripts in `code/R/`.

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

## 🖋️ CRediT author statement

[What is a CRediT author statement?](https://www.elsevier.com/researcher/author/policies-and-guidelines/credit-author-statement)

| Term                       | David Rose | Cici Hou | Shaun Nichols | Tobias Gerstenberg | Ellen M. Markman |
| -------------------------- | ---------- | -------- | ------------- | ------------------ | ---------------- |
| Conceptualization          | X          | X        | X             | X                  | X                |
| Methodology                | X          | X        | X             |                    | X                |
| Software                   | X          | X        |               |                    |                  |
| Validation                 | X          | X        |               |                    |                  |
| Formal analysis            | X          | X        |               |                    |                  |
| Investigation              | X          | X        |               |                    |                  |
| Resources                  |            | X        |               |                    |                  |
| Data Curation              |            | X        |               |                    |                  |
| Writing – Original Draft   | X          | X        |               |                    |                  |
| Writing – Review & Editing | X          | X        | X             | X                  | X                |
| Visualization              | X          | X        |               |                    |                  |
| Supervision                | X          |          | X             | X                  | X                |
| Project administration     | X          |          | X             | X                  | X                |
| Funding acquisition        |            |          |               |                    | X                |


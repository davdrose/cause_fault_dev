# R Code for Data Analysis

This folder contains the R code and caches used for analyzing data. 

---

## Contents

### 1. R Script
The R script (`main.Rmd`) contains the following sections:
- **Title and Authors**: The title, authors, and date of analysis generation.
- **Packages**: Loading necessary R packages for data manipulation, statistical analysis, and plotting.
- **Settings**: Setting up themes, contrasts, and suppressing warnings for clean outputs.
- **Helper Functions**: Custom functions for color gradients and softmax calculations.
- **Experiment 1 (Chain Cases)**:
  - **Data**: Reading and processing data for chain case scenarios.
  - **Demographics**: Summarizing participant demographics.
  - **Statistical Analysis**: Running Bayesian models to analyze differences and interaction effects.
  - **Plots**: Visualizing results using `ggplot2`.
- **Experiment 2 (Absence Cases)**:
  - Structure similar to Experiment 1.
- **Appendix**:
  - **Preregistered Analyses**: Further Bayesian models (e.g., question-by-age interactions) and extended plots and tables not included in the main text.
- **Session Info**: Displaying the session details for reproducibility.

### 2. Cache Folder
The `cache/` directory contains pre-computed model fits generated during the analysis. These files speed up re-execution of the R script and ensure reproducibility of results.

---

## Output

- **Plots**: Graphical representation of the data and analysis results.
- **Statistical Results**: Bayesian model summaries and comparisons.
- **Demographics**: Participant information grouped by gender and language.

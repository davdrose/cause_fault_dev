# Python Code for Data Cleaning

This folder contains the Python script to clean and process CSV data for experiments involving scenarios and participant responses. The script provide functionality to assign scenario labels, clean response data, and handle missing or incomplete entries.

---

## Contents

1. **`get_scenario`**:
   - Assigns scenario labels to rows based on the `"scenario_order"` column.
   - Processes data in batches of 6 rows and assigns labels like `"fence"`, `"mirror"`, `"fan"`, and `"window"`.
   - Saves the updated DataFrame to a specified output file.

2. **`clean_data`**:
   - Cleans the data based on a specific column's values.
   - Handles special conditions like `"both"`, `"neither"`, and names like `"Sophia"`, `"Suzy"`, `"Bobby"`, and `"Andy"`.
   - Updates `proximal` and `distal` columns (or `direct` and `absent` for Experiment 2 files).
   - Saves the cleaned data to a new file.

3. **`check_response`**:
   - Identifies rows with missing `"response"` values (e.g., `"N_A"`) and prints the corresponding `"full_response"` content.

4. **`fill_data`**:
   - Fills empty cells in a specified column with a default value (e.g., `0`).
   - Useful for ensuring numerical consistency in the dataset.

5. **`remove_blank_data`**:
   - Removes rows with missing values in a specific column.
   - Outputs a cleaned file with only complete rows.

6. **`main`**:
   - Processes a dataset by:
     - Removing blank rows.
     - Assigning scenarios.
     - Cleaning response data.
     - Filling empty values in columns as needed.
   - Customizable for Experiment 1 (`proximal`/`distal`) or Experiment 2 (`direct`/`absent`).

---

## Usage

### Prerequisites
- Python 3.x
- `pandas` library installed (`pip install pandas`).

### Running the Script
1. Place your raw CSV file in the `data/` directory.
2. Update the `csv_file`, `column`, and `output_file` variables in the `__main__` block to match your input and output file paths.
3. Run the script:
   ```bash
   python script_name.py
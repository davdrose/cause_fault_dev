import pandas as pd

# Function to assign scenario labels based on "scenario_order" every six rows
def get_scenario(csv_file, column, output_file):
    df = pd.read_csv(csv_file)
    
    # Iterate through the DataFrame in steps of 6 rows
    for i in range(0, len(df), 6):
        scenario_order = df.loc[i, "scenario_order"]
        # Assign scenarios based on "scenario_order"
        if scenario_order == "fence_first":
            df.loc[i:i+2, "scenario"] = "fence"
            df.loc[i+3:i+5, "scenario"] = "mirror"
        elif scenario_order == "fence_second":
            df.loc[i:i+2, "scenario"] = "mirror"
            df.loc[i+3:i+5, "scenario"] = "fence"
        elif scenario_order == "wall_first":
            df.loc[i:i+2, "scenario"] = "fan"
            df.loc[i+3:i+5, "scenario"] = "window"
        elif scenario_order == "wall_second":
            df.loc[i:i+2, "scenario"] = "window"
            df.loc[i+3:i+5, "scenario"] = "fan"
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

# Function to clean data based on specific column values
def clean_data(csv_file, column, output_file):
    df = pd.read_csv(csv_file)
    
    # Iterate through rows and assign values to "proximal" and "distal" based on conditions
    for i in range(len(df)):
        response = df.loc[i, column].lower()
        
        if "both" in response:
            df.loc[i, "proximal"] = 1
            df.loc[i, "distal"] = 1
        elif "neither" in response or "nobody" in response or "no one" in response:
            df.loc[i, "proximal"] = 0
            df.loc[i, "distal"] = 0
        else:
            # Handle individual names and gender-based conditions
            if "sophia" in response or "suzy" in response:
                df.loc[i, "distal"] = 1 if df.loc[i, "gender_order"] == "girl" else 0
                df.loc[i, "proximal"] = 1 if df.loc[i, "gender_order"] != "girl" else 0
            if "bobby" in response or "andy" in response:
                df.loc[i, "distal"] = 1 if df.loc[i, "gender_order"] == "boy" else 0
                df.loc[i, "proximal"] = 1 if df.loc[i, "gender_order"] != "boy" else 0
            if "boy" in response:
                df.loc[i, "distal"] = 1 if df.loc[i, "gender_order"] == "boy" else 0
            if "girl" in response:
                df.loc[i, "distal"] = 1 if df.loc[i, "gender_order"] == "girl" else 0
    
    # Rename columns if the file is part of Experiment 2
    if "exp2" in csv_file:
        df.rename(columns={"distal": "absent", "proximal": "direct"}, inplace=True)
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

# Function to check rows missing "response" values
def check_response(csv_file):
    df = pd.read_csv(csv_file)
    missing_responses = df[df["response"] == "N_A"]
    for _, row in missing_responses.iterrows():
        print(f"Line {row.name}: {row['full_response']}")

# Function to fill empty cells in a column with a default value
def fill_data(csv_file, column, default_value=0):
    df = pd.read_csv(csv_file)
    df[column].fillna(default_value, inplace=True)
    df.to_csv(csv_file, index=False)

# Function to remove rows with missing values in a specific column
def remove_blank_data(csv_file, column):
    df = pd.read_csv(csv_file)
    df = df[df[column].notna()]
    df.to_csv(csv_file, index=False)

# Main script
if __name__ == "__main__":
    # File paths and column to process
    csv_file = "data/exp2_child.csv"
    column = "full_response"
    output_file = "data/exp2_child_clean.csv"
    
    # Clean and process data
    remove_blank_data(csv_file, column)
    get_scenario(csv_file, column, output_file)
    clean_data(output_file, column, output_file)
    
    # Optional checks and column filling
    # check_response(output_file)
    if "exp1" in csv_file:
        fill_data(output_file, "proximal")
        fill_data(output_file, "distal")
    else:
        fill_data(output_file, "absent")
        fill_data(output_file, "direct")
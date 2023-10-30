import os
import pandas as pd

# Define the folder path where your .csv files are located
folder_path = './data_files/each_following'

# Get a list of all .csv files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

following_dict = {}

# Loop through each .csv file
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)

    # Read the .csv file into a DataFrame
    df = pd.read_csv(file_path)

    # Access and visit non-empty rows in the first column
    for index, row in df.iterrows():
        if not pd.isna(row.iloc[0]):
            value = row.iloc[0]  # Access the value in the first column
            if value != "utfpr.curitiba" and value != "utfpr_":
                if value in following_dict:
                    following_dict[value] += 1
                    # print(f"{value} : {following_dict[value]}")
                else:
                    following_dict[value] = 1
                    # print(f"new account : {value}")
                # print(f'File: {csv_file}, Row {index + 1}, Value: {value}')
            
# Sort the dictionary by values in descending order and take the top 10
sorted_data = dict(sorted(following_dict.items(), key=lambda item: item[1], reverse=True)[:50])

top_profiles = []
# Print the top 10 values and their corresponding keys
for key, value in sorted_data.items():
    print(f'{key}: {value}')
    
    top_profiles.append(key)
    # Create a sample DataFrame (replace this with your actual DataFrame)
    data = {'top-profiles': top_profiles}

df = pd.DataFrame(data)
# Save the DataFrame as a .csv file
df.to_csv("top_profiles.csv", index=False)  # Use index=False to exclude row indices

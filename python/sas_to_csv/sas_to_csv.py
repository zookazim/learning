import pandas as pd
import csv

# Replace 'your_sas_file.sas7bdat' with the actual filename
sas_file = f"C:\\temp\\sas_files\\servicecontacts_2021.sas7bdat"
csv_file = f"C:\\temp\\sas_files\\Service Contacts - year4.csv"

try:
    # Read the SAS file into a pandas DataFrame
    df = pd.read_sas(sas_file, encoding='latin-1')
    
    # Write the DataFrame to a CSV file, excluding the index
    df.to_csv(csv_file, index=False, quoting=csv.QUOTE_NONNUMERIC)

    print(f"Successfully converted {sas_file} to {csv_file}")


except FileNotFoundError:
    print(f"Error: File not found: {sas_file}")
except Exception as e:
    print(f"An error occurred: {e}")
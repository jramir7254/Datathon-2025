from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


full_data = './Raw Data/Data for Hackathon.xlsx'

oper_units = ['UNITONBT', 'UNITONBA', 'HEATINBA', 'HEAT_QA', 'LOADMWBA', 'GFLOW_BA']

emissn_units = ['SO2TONS', 'NOXTONS', 'COTONS', 'NH3TONS']


def create_folders(num):
    # Define the folder paths
    plant_fldr = Path(f"Lake{num} Data")
    opper_units_fldr = Path(f"./Lake{num} Data/Operational Units")
    emissn_fldr = Path(f"./Lake{num} Data/Emission Units")

    # Create the folders
    plant_fldr.mkdir(parents=True, exist_ok=True)
    opper_units_fldr.mkdir(parents=True, exist_ok=True)
    emissn_fldr.mkdir(parents=True, exist_ok=True)

    print(f"Created folders for Plant-{num}.")


def write_data(lake_data, num):
    for unit in oper_units:
        lake_unit_data = lake_data[lake_data['Parameter'] == unit]
        lake_unit_data.to_excel(f"./Lake{num} Data/Operational Units/Lake{num}_{unit}_Data.xlsx", index=False)

    print(f"Wrote operational units for Plant-{num}.")

    for emissn in emissn_units:
        lake_unit_data = lake_data[lake_data['Parameter'] == emissn]
        lake_unit_data.to_excel(f"./Lake{num} Data/Emission Units/Lake{num}_{emissn}_Data.xlsx", index=False)

    print(f"Wrote emission units for Plant-{num}.")


def method():
    for i in range(1, 5):
        print(f"Started organizing process for Plant-{i}.")
        create_folders(i)

        # Read the data
        lake_data = pd.read_excel(full_data)

        # Filter data by source
        lake_data = lake_data[lake_data['Source'] == f'LAKE-{i}']

        # Re-arange data for simplicity
        lake_data = lake_data[['TimeStamp', 'Source', 'Parameter', 'Units', "Value"]]

        lake_data.to_excel(f"./Lake{i} Data/Lake{i}_Data.xlsx", index=False)
        print(f"Wrote full data for Plant-{i}.")

        write_data(lake_data, i)

        print(f"Finished writing data for Plant-{i}.\n\n")


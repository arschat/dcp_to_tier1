# DCP spreadsheet to Tier 1 metadata

This is a project to convert the metadata schema from Human Cell Atlas Data Platform (formelrly known as DCP, Data Coordination Platform) to Human Cell Atlas Tier 1.

## Usage

To convert metadata, run the two notebooks in this sequence:
* [get_flatten_per_cs_metadata_Amnon.ipynb](get_flatten_per_cs_metadata_Amnon.ipynb) to create a flatten csv version of the dcp_spreadsheet on the cell_suspension level
* [dcp_biomaterial_to_tier1.ipynb](dcp_biomaterial_to_tier1.ipynb) to convert the dcp field from the flatten csv file, to the Tier 1 metadata fields (based on the mapping of fields specified on [metadata_dict.py](metadata_dict.py)), and produce an excel file with the `_Tier1.xlsx` extension, and two csv files with the `_tier1_uns.csv` and `_tier1_obs.csv`

Please specify the `file_name` of the dcp_spreadsheet found in the dcp_spreadsheets folder, in both notebooks. In [get_flatten_per_cs_metadata_Amnon.ipynb](get_flatten_per_cs_metadata.ipynb) you also have to specify the file you will begin from.

## Requirements
The packages needed for these notebooks are listed in the requirements.txt file. To install via pip use:
```bash
pip install -r requirements.txt
```
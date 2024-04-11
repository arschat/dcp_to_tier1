# DCP spreadsheet to Tier 1 metadata

This is a project to convert the metadata schema from Human Cell Atlas Data Platform (formelrly known as DCP, Data Coordination Platform) to Human Cell Atlas Tier 1.

## Usage

To convert metadata, run the two notebooks in this sequence:
1. [flatten_dcp_metadata.ipynb](flatten_dcp_metadata.ipynb) to create a flatten csv version of the dcp_spreadsheet on the cell_suspension/ library level
2. [flat_dcp_to_tier1.ipynb](flat_dcp_to_tier1.ipynb) to convert the dcp field from the flatten csv file, to the Tier 1 metadata fields (based on the mapping of fields specified on [metadata_dict.py](metadata_dict.py)), and produce an excel file with the `_Tier1.xlsx` extension, and two csv files with the `_tier1_uns.csv` and `_tier1_obs.csv`

Please specify the `file_name` of the dcp_spreadsheet found in the dcp_spreadsheets folder, in both notebooks.

## Requirements
The packages needed for these notebooks are listed in the requirements.txt file. To install via pip use:
```bash
pip install -r requirements.txt
```

# Known limitations
- [flatten_dcp_metadata.ipynb](flatten_dcp_metadata.ipynb)
    - Tested only on simple experimental design (`Donor organism` -> `Specimen from organism`/ `Sample` -> `Cell suspension`/ `Library` -> `Analysis File` & `Sequence file`)
    - No support for "Spatial transcriptomics" data
- [flat_dcp_to_tier1.ipynb](flat_dcp_to_tier1.ipynb)
    - Will not populate Tier 1 fields at the cell level (cell type related fields)
    - Some DCP field values are not yet mapped to their Tier 1 
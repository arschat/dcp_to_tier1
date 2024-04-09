import os
import argparse
import pandas as pd
import requests


def fix_friendly_dcp_names(input_spreadsheet):
    """Fix the friendly names downloaded directly from HCA DP"""
    hca_template_url = 'https://github.com/ebi-ait/geo_to_hca/raw/master/template/hca_template.xlsx'
    hca_template_file = requests.get(hca_template_url, timeout=200).content
    dcp_template = pd.read_excel(hca_template_file, sheet_name=None, nrows=4, header=None)

    # create dict with tab: {programmatic_name: friendly_name}
    dcp_template = {
        tab_name: tab.iloc[[3,0]].transpose().set_index(3).to_dict()[0] \
            for tab_name, tab in dcp_template.items()
        }

    file_name = input_spreadsheet
    dcp_spreadsheet = pd.read_excel(file_name, sheet_name=None)

    for tab in dcp_spreadsheet.keys():
        if tab not in dcp_template.keys():
            continue
        dcp_spreadsheet[tab].columns = [dcp_template[tab].get(value[2], value[2].replace("_", " ")) \
            for _, value in dcp_spreadsheet[tab].items()]

    # overwrite file
    with pd.ExcelWriter(file_name, engine='openpyxl', mode='w') as writer:
        for tab in dcp_spreadsheet:
            dcp_spreadsheet[tab].to_excel(writer, sheet_name=tab, index=False, header=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process DCP spreadsheet using HCA template")
    parser.add_argument("--spreadsheet", type=str, help="Path to the spreadsheet file")
    args = parser.parse_args()
    if args.spreadsheet:
        fix_friendly_dcp_names(args.spreadsheet)
    else:
        print("Please provide the path to the spreadsheet file using --spreadsheet option.")

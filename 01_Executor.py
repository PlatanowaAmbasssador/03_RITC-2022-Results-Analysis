import papermill as pm
from pathlib import Path
import os
import shutil

# Directory Paths

BASE_DIR = Path.cwd() 

INPUTS_DIR = BASE_DIR / "inputs"

OUTPUTS_DIR = BASE_DIR / "outputs"

TEMPLATE_PATH = BASE_DIR / "templates" 

# Parameters

case_name = ['All_Cases', 'Electricty_Trading_Case', 'Algorithmic_Trading_Case', 'Matlab_Volatility_Trading_Case', 'Liquidity_Risk_Case']

file_name = f'{INPUTS_DIR}/Final_Resuts_from_RITC_2022' 

sheet_name_all = ['finalrank', 'ET', 'AT', 'MVT', 'LR'] 

subheats_list = [None, ["ET_1","ET_2","ET_3","ET_4"], ["AT-1","AT-2","AT-3","AT-4", "AT-5","AT-6","AT-7","AT-8","AT-9","AT-10"], ["MVT-1","MVT-2","MVT-3","MVT-4", "MVT-5"],  ["LR-1","LR-2","LR-3","LR-4","LR-5"]]

# Papermill Execution

for cn, sna, sl in zip(case_name, sheet_name_all, subheats_list):
    pm.execute_notebook(
                TEMPLATE_PATH / f"CASE_TEMPLATE_{sna}.ipynb",
                OUTPUTS_DIR / f"{cn}_Score_Analysis.ipynb",
                parameters={
                    "case_name": cn,
                    "file_name": file_name,
                    "sheet_name_all": sna,
                    "subheats_list": sl,
                },
            )

    command = f"! jupyter nbconvert --to html --no-input {OUTPUTS_DIR}/{cn}_Score_Analysis.ipynb"
    os.system(command)

    shutil.move(f"{OUTPUTS_DIR}/{cn}_Score_Analysis.html", f"{OUTPUTS_DIR}/html_outputs/{cn}_Score_Analysis.html")
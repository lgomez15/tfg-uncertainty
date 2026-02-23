import json

with open("notebooks/training/02_garch_x_modeling.ipynb", "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        src = "".join(cell["source"])
        if "DATA_PROCESSED = Path('../../data/processed')" in src:
            new_src = src.replace("DATA_PROCESSED = Path('../../data/processed')", 
                                  "DATA_PROCESSED = Path('../../data/processed')\nif not DATA_PROCESSED.exists():\n    DATA_PROCESSED = Path('data/processed')")
            cell["source"] = [line + ("\n" if not line.endswith("\n") else "") for line in new_src.split("\n") if line]

with open("notebooks/training/02_garch_x_modeling.ipynb", "w") as f:
    json.dump(nb, f, indent=1)


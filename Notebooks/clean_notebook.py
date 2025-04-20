import json

# Replace this path with the full path to your notebook if needed
notebook_path = "Visual_EEG_Pattern_Synthesis_and_Recognition_with_Deep_Learning.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = json.load(f)

if "widgets" in notebook.get("metadata", {}):
    del notebook["metadata"]["widgets"]

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Notebook metadata cleaned successfully.")

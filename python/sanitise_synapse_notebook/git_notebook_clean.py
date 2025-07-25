import json
import sys
import argparse

def clean_notebook(filepath, output_path=None, remove_all_outputs=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # Remove spark.autotune.trackingId if found
    for cell in notebook.get("cells", []):
        metadata = cell.get("metadata", {})
        if "spark.autotune.trackingId" in metadata:
            print(f"Removing spark.autotune.trackingId from a cell")
            metadata.pop("spark.autotune.trackingId")
        cell["metadata"] = metadata

        if remove_all_outputs:
            cell["execution_count"] = None

    # Also check notebook-level metadata
    nb_meta = notebook.get("metadata", {})
    if "spark.autotune.trackingId" in nb_meta:
        print("Removing spark.autotune.trackingId from notebook-level metadata")
        nb_meta.pop("spark.autotune.trackingId")
    notebook["metadata"] = nb_meta

    # Write cleaned notebook
    output_file = output_path if output_path else filepath
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2)
    print(f"Notebook cleaned and saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean spark.autotune.trackingId from Synapse/Jupyter notebooks")
    parser.add_argument("file", help="Path to the notebook JSON file")
    parser.add_argument("--out", help="Optional output file path")
    parser.add_argument("--strip-all", action="store_true", help="Also remove execution_count and outputs")

    args = parser.parse_args()
    clean_notebook(args.file, args.out, args.strip_all)

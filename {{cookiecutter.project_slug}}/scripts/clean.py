from pathlib import Path
import typer
import shutil
from paths import data_raw_dir, data_interim_dir, data_processed_dir, results_dir

app = typer.Typer()

def clean_directory(directory: Path):
    if directory.exists():
        for item in directory.iterdir():
            if item.is_file():
                item.unlink()  # delete file
            elif item.is_dir():
                shutil.rmtree(item)  # delete directory and its contents

@app.command()
def clean(data: bool = typer.Option(False, help="Clean data folders"),
          results: bool = typer.Option(False, help="Clean results folder")):
    if data:
        typer.echo("Cleaning data directories...")
        # delete the contents of raw, interim, and processed in the data folder, but retain the folder structure
        for dir_path in [data_raw_dir, data_interim_dir, data_processed_dir]:
            clean_directory(dir_path)
        # retain the external folder
        typer.echo("Data directories cleaned but structure retained.")
    
    if results:
        typer.echo("Cleaning results directory...")
        clean_directory(results_dir)
        typer.echo("Results directory cleaned.")

if __name__ == "__main__":
    app()

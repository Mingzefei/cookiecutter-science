# script/backup.py
import zipfile
import typer
from pathlib import Path
from datetime import datetime
from paths import backup_dir, config_dir, results_dir, data_dir, notebooks_dir, src_dir, scripts_dir

app = typer.Typer()

def compress_files(target_dir: Path, zip_name: str, paths_to_backup):
    backup_path = target_dir / f"{zip_name}.zip"
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for path in paths_to_backup:
            if path.exists():
                if path.is_dir():
                    for file in path.rglob("*"):
                        zipf.write(file, file.relative_to(path.parent))
                else:
                    zipf.write(path, path.name)
    print(f"Backup completed: {backup_path}")

@app.command()
def backup(all: bool = typer.Option(False, help="Perform full backup")):
    # obtain current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # default lightweight backup files
    config_file = typer.prompt("Please enter config file path", default=config_dir / "config.yaml")
    config_file = Path(config_file)
    
    # check if config file exists
    if not config_file.exists():
        typer.echo(f"Error: Config file '{str(config_file)}' not found!")
        raise typer.Exit(code=1)
    
    paths_to_backup = [results_dir, config_file]
    
    if all:
        paths_to_backup.extend([data_dir, notebooks_dir, src_dir, scripts_dir])
        zip_name = f"all_exp_{timestamp}"
    else:
        zip_name = f"exp_{timestamp}"
    
    # perform backup
    compress_files(backup_dir, zip_name, paths_to_backup)

if __name__ == "__main__":
    app()

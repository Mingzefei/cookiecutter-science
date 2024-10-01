# scripts/paths.py
from pathlib import Path


def find_project_root(current_path: Path = Path(__file__)) -> Path:
    """
    Find the root of the project by looking for a marker file.
    """
    for parent in current_path.resolve().parents:
        if (parent / "pyproject.toml").is_file() or (parent / "scripts").is_dir():
            return parent
    raise FileNotFoundError(
        "Project root not found. Make sure you have 'pyproject.toml' or 'scripts' in the project root."
    )


root_dir = find_project_root()

backup_dir = root_dir / "backup"

config_dir = root_dir / "config"

data_dir = root_dir / "data"
data_raw_dir = data_dir / "raw"
data_interim_dir = data_dir / "interim"
data_processed_dir = data_dir / "processed"
data_external_dir = data_dir / "external"

docs_dir = root_dir / "docs"

notebooks_dir = root_dir / "notebooks"

reports_dir = root_dir / "reports"

reports_figures_dir = reports_dir / "figures"

results_dir = root_dir / "results"

scripts_dir = root_dir / "scripts"

src_dir = root_dir / "src"

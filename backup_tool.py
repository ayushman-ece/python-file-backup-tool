import shutil
from datetime import datetime
from pathlib import Path


def backup_folder(source_path, backup_path):
    source = Path(source_path).expanduser().resolve()
    backup_root = Path(backup_path).expanduser().resolve()

    if not source.exists() or not source.is_dir():
        raise ValueError("Source folder does not exist.")

    if backup_root == source or source in backup_root.parents:
        raise ValueError("Backup folder cannot be inside the source folder.")

    files = [path for path in source.rglob("*") if path.is_file()]

    if not files:
        return None, 0

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination = backup_root / f"backup_{timestamp}"
    destination.mkdir(parents=True, exist_ok=False)

    copied = 0

    try:
        for file_path in files:
            relative_path = file_path.relative_to(source)
            target_path = destination / relative_path

            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file_path, target_path)
            copied += 1
    except OSError:
        shutil.rmtree(destination, ignore_errors=True)
        raise

    return destination, copied
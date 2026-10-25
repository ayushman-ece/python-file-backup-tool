# 📦 Python File Backup Tool

A simple, modular Python command-line application that creates timestamped backups of files and folders.

## ✨ Features

- 📁 Back up files from a selected source folder
- 🗂️ Preserve the original folder structure
- 🕒 Create timestamped backup folders
- 📋 Display the number of files copied
- 🛡️ Validate source paths and prevent backups inside the source folder
- ⚠️ Handle common file and folder errors
- 🧩 Separate backup logic from the command-line interface

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** `pathlib`, `shutil`, `datetime`
- **Storage:** Local filesystem

## 📂 Project Structure

```text
python-file-backup-tool/
├── main.py
├── backup_tool.py
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-file-backup-tool.git
```

### 2. Open the project directory

```bash
cd python-file-backup-tool
```

### 3. Run the application

```bash
python main.py
```

### 4. Enter the paths

Provide the source folder and the destination where backups should be stored.

## 💡 Example

```text
===== PYTHON FILE BACKUP TOOL =====
Enter source folder path: C:\MyFiles
Enter backup destination path: D:\Backups

Backup completed successfully!
Files copied: 5
Backup location: D:\Backups\backup_20261026_120000
```

*Example output; the timestamp, file count, and paths depend on your run.*

## 🧠 Concepts Learned

- Functions and modular programming
- File and directory handling
- `pathlib` for path manipulation
- `shutil.copy2()` for copying files and metadata
- Recursive directory traversal
- Date and time formatting
- Exception handling
- Input validation
- Git and GitHub project organization

## ⚠️ Limitations

- This is a learning project, not an enterprise backup solution.
- It does not provide encryption, cloud synchronization, or automatic scheduling.
- Keep important files backed up in more than one safe location.
- Verify backups before relying on them for recovery.

## 🔮 Future Improvements

- Add file filtering by extension
- Add backup verification
- Generate backup logs
- Support automatic scheduled backups
- Add a restore feature
- Add progress reporting for large folders

## 👨‍💻 Author

**Your Name**

Python learning and portfolio project.

---

*Built with Python, one project at a time. 🚀*

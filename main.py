from backup_tool import backup_folder


def main():
    print("\n===== PYTHON FILE BACKUP TOOL =====")

    source = input("Enter source folder path: ").strip().strip('"')
    backup = input("Enter backup destination path: ").strip().strip('"')

    try:
        destination, count = backup_folder(source, backup)

        if destination is None:
            print("No files found to back up.")
        else:
            print("\nBackup completed successfully!")
            print(f"Files copied: {count}")
            print(f"Backup location: {destination}")

    except (ValueError, OSError) as error:
        print(f"\nBackup failed: {error}")


if __name__ == "__main__":
    main()
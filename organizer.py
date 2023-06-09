import os
import shutil


def move_documents_to_folder():
    home_dir = os.path.expanduser("~")

    desktop_path = os.path.join(home_dir, "Desktop")
    downloads_path = os.path.join(home_dir, "Downloads")
    documents_path = os.path.join(home_dir, "Documents/ORGANIZER")

    document_files = []
    document_files.extend(get_document_files(desktop_path))
    document_files.extend(get_document_files(downloads_path))

    for file_path in document_files:
        file_extension = os.path.splitext(file_path)[1].lower()
        folder_name = f"{file_extension[1:].upper()} FOLDER"
        destination_folder = os.path.join(documents_path, folder_name)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        try:
            shutil.move(file_path, destination_folder)
        except shutil.Error:
            file_name = os.path.basename(file_path)
            new_file_name = add_duplicate_suffix(file_name)
            new_file_path = os.path.join(destination_folder, new_file_name)
            shutil.move(file_path, new_file_path)


def get_document_files(folder_path):
    document_extensions = [
        ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".pdf",
        ".txt", ".rtf", ".csv", ".odt", ".ods", ".odp", ".pages", ".numbers",
    ]

    document_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in document_extensions:
                document_files.append(os.path.join(root, file))

    return document_files


def add_duplicate_suffix(file_name):
    base_name, extension = os.path.splitext(file_name)
    new_file_name = f"{base_name}_duplicate{extension}"
    return new_file_name

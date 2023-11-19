import os
import time

def rename_files(folder_path):
    start_time = time.time()  # Record the start time
    files = os.listdir(folder_path)
    total_files = len(files)
    processed_files = 0

    for file_name in files:
        if file_name.startswith("y2mate.com - "):
            new_name = file_name[len("y2mate.com - "):]
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            processed_files += 1

            # Calculate and print progress percentage
            progress_percent = (processed_files / total_files) * 100
            print(f'Renaming: {file_name} -> {new_name} ({progress_percent:.2f}% complete)')

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    print(f'\nRenaming completed in {elapsed_time:.2f} seconds.')

# Specify the path to the folder containing the files
folder_path = "target"

# Call the function to rename files in the specified folder
rename_files(folder_path)

import os
import time
import re


def rename_files(folder_path):
    start_time = time.time()  # Record the start time
    files = os.listdir(folder_path)
    total_files = len(files)
    processed_files = 0

    # List of phrases to put in brackets
    phrases = [
        "Official Video",
        "Official Music Video",
        "Official Lyric Video",
        "Official Audio",
        "Audio",
        "Visualizer",
        "Music Visualizer"
    ]

    for file_name in files:
        new_name = file_name

        # Remove "y2mate.com - " prefix
        if new_name.startswith("y2mate.com - "):
            new_name = new_name[len("y2mate.com - "):]

        # Remove "_1080p" suffix (before the file extension)
        if "_1080p" in new_name:
            base, ext = os.path.splitext(new_name)
            if base.endswith("_1080p"):
                base = base[:-len("_1080p")]
                new_name = base + ext

        # Replace double spaces with a hyphen
        new_name = new_name.replace("  ", " - ")

        # Put brackets around specified phrases
        for phrase in phrases:
            new_name = re.sub(rf'\b{phrase}\b', rf'({phrase})', new_name)

        # Rename the file if any changes were made
        if new_name != file_name:
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            processed_files += 1

            # Calculate and print progress percentage
            progress_percent = (processed_files / total_files) * 100
            print(
                f'Renaming file: {processed_files} -> ({progress_percent:.2f}% complete)')

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    print(f'\nRenaming completed in {elapsed_time:.2f} seconds.')


# Specify the path to the folder containing the files
folder_path = "target"

# Call the function to rename files in the specified folder
rename_files(folder_path)

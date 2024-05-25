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



"""
This Python script is designed to automate the process of renaming files in a specified 
folder, performing several key modifications to clean and standardize the file names. 

The script performs the following tasks:

Prefix Removal:

The script identifies and removes the prefix "y2mate.com - " from any file name that 
starts with this string.

Suffix Removal:

It removes the suffix "_1080p" from the file names, ensuring this suffix is eliminated 
if it appears before the file extension.

Double Space Replacement:

The script scans the file names for any occurrences of double spaces (" ") and replaces 
them with a hyphen and a single space (" - ").

Bracket Phrases:

It identifies specific phrases within the file names, such as:

"Official Video", 
"Official 
Music Video",
"Official Lyric Video", 
"Official Audio", 
"Audio", 
"Visualizer",
"Music Visualizer". 

These phrases are then enclosed in brackets, transforming, for example, "Official 
Video" into "(Official Video)".

Progress Tracking:

Throughout the renaming process, the script tracks the number of files processed and 
calculates the progress percentage, printing this information to the console to keep the 
user informed of the script's progress.

Execution Time Measurement:

The script measures the total time taken to rename the files and prints this elapsed time 
upon completion.

Usage Instructions

Specify the Folder Path:

Modify the folder_path variable in the script to point to the directory containing the files 
you want to rename.

Run the Script:

Execute the script in your Python environment. The script will process all files in the 
specified folder according to the rules described above.

Example before Running the Script:

"y2mate.com - ARTIST  Song Title feat Another Artist and DJ G400 Official Video_1080p.mp4"

After Running the Script:

"ARTIST - Song Title feat Another Artist and DJ G400 (Official Video).mp4"

By using this script, you can automate the tedious task of manually renaming multiple files, 
ensuring consistent and clean file naming conventions in your folder.

"""

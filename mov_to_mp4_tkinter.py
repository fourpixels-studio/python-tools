import moviepy.editor as mp
import os
import tkinter as tk
from tkinter import filedialog
import sys


def convert_mov_to_mp4(input_file, output_file):
    try:
        video = mp.VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264')
        print(f'Successfully converted {input_file} to {output_file}')
    except Exception as e:
        print(f'An error occurred: {e}', file=sys.stderr)
        sys.exit(1)


def choose_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select a .mov file",
        filetypes=(("MOV files", "*.mov"), ("All files", "*.*"))
    )
    return file_path


if __name__ == "__main__":
    input_file = choose_file()
    if not input_file:
        print("No file selected. Exiting.")
        sys.exit(1)

    output_file = os.path.splitext(input_file)[0] + '.mp4'
    convert_mov_to_mp4(input_file, output_file)


"""
Requirements
==============================
certifi==2024.6.2
charset-normalizer==3.3.2
decorator==4.4.2
future==1.0.0
idna==3.7
imageio==2.34.1
imageio-ffmpeg==0.5.1
moviepy==1.0.3
numpy==2.0.0
pillow==10.3.0
proglog==0.1.10
requests==2.32.3
tqdm==4.66.4
urllib3==2.2.1
==============================
"""

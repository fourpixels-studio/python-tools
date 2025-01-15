from moviepy.editor import VideoFileClip


def convert_mov_to_mp4(input_file: str, output_file: str):
    """
    Converts a .mov file to .mp4 format.

    :param input_file: Path to the input .mov file.
    :param output_file: Path to the output .mp4 file.
    """
    try:
        # Load the .mov file
        clip = VideoFileClip(input_file)
        # Write the video to the output file in .mp4 format
        clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
        print(f"Conversion successful! MP4 saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Safely close the clip to release resources
        if 'clip' in locals():
            clip.close()


# Example usage
if __name__ == "__main__":
    # Replace with your input .mov file path
    input_mov = "/Users/user/Music/video.mov"
    # Replace with your desired output .mp4 file path
    output_mp4 = "/Users/user/Music/video.mp4"
    convert_mov_to_mp4(input_mov, output_mp4)

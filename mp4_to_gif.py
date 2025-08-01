from moviepy.editor import VideoFileClip

def video_to_gif(input_path, output_path, start_time=None, end_time=None, resize_width=None):
    """
    Converts a video file to a GIF.

    Args:
        input_path (str): Path to input video file.
        output_path (str): Path to save the output GIF.
        start_time (float): Start time in seconds (optional).
        end_time (float): End time in seconds (optional).
        resize_width (int): Resize width in pixels (optional).

    Returns:
        None
    """
    # Load video
    clip = VideoFileClip(input_path)

    # Trim clip if start and end times are given
    if start_time is not None or end_time is not None:
        clip = clip.subclip(start_time, end_time)

    # Resize if specified
    if resize_width is not None:
        clip = clip.resize(width=resize_width)

    # Write to GIF
    clip.write_gif(output_path, fps=15)  # Adjust fps if needed

    print(f"GIF saved to: {output_path}")

# Example usage
if __name__ == "__main__":
    video_path = "input_video.mp4"
    gif_path = "output.gif"
    video_to_gif(video_path, gif_path, start_time=2, end_time=6, resize_width=480)

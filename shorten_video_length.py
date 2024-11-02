from moviepy.editor import VideoFileClip


def shorten_video(input_file, output_file, start_time=0, end_time=10):
    """
    Shorten a video to the specified start and end times.

    Parameters:
    - input_file: str, the path to the input video file.
    - output_file: str, the path to save the shortened video file.
    - start_time: float, the start time in seconds from where to begin the cut (default is 0).
    - end_time: float, the end time in seconds where to end the cut (default is 10 seconds).
    """
    # Load the video clip
    with VideoFileClip(input_file) as video:
        # Cut the video from start_time to end_time
        shortened_clip = video.subclip(start_time, end_time)
        # Write the shortened video to the output file
        shortened_clip.write_videofile(
            output_file, codec="libx264", audio_codec="aac")


# Example usage
input_video_path = "video.mp4"   # Replace with your video file path
output_video_path = "shortened_video.mp4"
start = 0                              # Start time in seconds
end = 5                                # End time in seconds

shorten_video(input_video_path, output_video_path, start, end)

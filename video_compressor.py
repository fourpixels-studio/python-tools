from moviepy.editor import VideoFileClip


def compress_video(input_file, output_file, target_resolution=(640, 360), target_bitrate="500k"):
    """
    Compress a video by adjusting resolution and bitrate.

    Parameters:
    - input_file: str, path to the input video file.
    - output_file: str, path to save the compressed video.
    - target_resolution: tuple, target resolution for the compressed video (width, height).
    - target_bitrate: str, target bitrate for video quality, e.g., "500k" (500 kilobits per second).
    """
    # Load the video
    with VideoFileClip(input_file) as video:
        # Resize the video to the target resolution
        compressed_clip = video.resize(newsize=target_resolution)
        # Write the video file with specified bitrate
        compressed_clip.write_videofile(
            output_file,
            codec="libx264",
            bitrate=target_bitrate,
            audio_codec="aac"
        )


# Example usage
input_video_path = "video.mp4"   # Replace with your video file path
output_video_path = "compressed_video.mp4"
compress_video(
    input_video_path, output_video_path,
    target_resolution=(540, 810), target_bitrate="700k"
)

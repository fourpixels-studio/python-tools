from moviepy.editor import VideoFileClip

def split_audio_from_mp4(input_file, output_audio_file):
    try:
        # Load the video clip
        video_clip = VideoFileClip(input_file)

        # Extract audio from the video clip
        audio_clip = video_clip.audio

        # Save the audio to a new file
        audio_clip.write_audiofile(output_audio_file)

        print(f"Audio extracted and saved to {output_audio_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'input.mp4' with the path to your MP4 file
    input_file_path = 'input.mp4'

    # Replace 'output_audio.wav' with the desired output audio file path
    output_audio_path = 'output_audio.wav'

    split_audio_from_mp4(input_file_path, output_audio_path)

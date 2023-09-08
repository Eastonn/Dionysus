from moviepy.editor import *
from .utils import hms_to_seconds
from .audio_processor import AudioProcessor


class VideoProcessor:
    @staticmethod
    def process_video(input_path: str, mode: str = 'split', audio_path: str = None, duration: str = None, start: str = None):
        if duration:
            duration = hms_to_seconds(duration)

        if start:
            start = hms_to_seconds(start)
        else:
            start = 0

        clip = VideoFileClip(input_path)

        # If duration is not None, make sure combined start and duration do not exceed total clip duration
        if duration and start + duration > clip.duration:
            raise ValueError(f"The start and duration point beyond the end of the video. Video length: {clip.duration}s")

        # If start is beyond total clip duration
        if start > clip.duration:
            raise ValueError(f"The start time is beyond the end of the video. Video length: {clip.duration}s")

        clip_duration = (start + duration) if duration else clip.duration
        clip = clip.subclip(start, clip_duration)

        # Extract base path, file name and file extension
        base_path, file_name = os.path.split(input_path)
        file_base_name, file_extension = os.path.splitext(file_name)

        if mode == 'split':
            # If the mode is split, output is an audio file with "_audio" appended to the base file name.
            output_file_path = os.path.join(base_path, f"{file_base_name}_audio.mp3")
            clip.audio.write_audiofile(output_file_path)
            AudioProcessor.normalize_audio(output_file_path, output_file_path)
        elif mode == 'merge' and audio_path is not None:
            # If the mode is merge, output is a video file with "_merged" appended to the base file name.
            output_file_path = os.path.join(base_path, f"{file_base_name}_merged{file_extension}")
            audioclip = AudioFileClip(audio_path)
            if duration:
                audioclip = audioclip.subclip(0, duration)
            clip.set_audio(audioclip).write_videofile(output_file_path)

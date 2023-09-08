import argparse
from src.video_processor import VideoProcessor


def parse_arguments():
    parser = argparse.ArgumentParser(description="Split or merge audio and video.")
    parser.add_argument("input_path", help="Path to the input video file.")
    parser.add_argument("--mode", default='split', help="Mode of operation, 'split' or 'merge'. Default is 'split'.")
    parser.add_argument("--audio_path", help="Path to the input audio file. Required if mode is merge.")
    parser.add_argument("--start", help="Start time of the video to process in seconds or 'h:m:s' format. If not given, it will start from the beginning.")
    parser.add_argument("--duration", help="Duration of the video to process in seconds or 'h:m:s' format. If not given, it will process the entire video.")
    return parser.parse_args()


def main():
    args = parse_arguments()
    VideoProcessor.process_video(args.input_path, mode=args.mode, audio_path=args.audio_path, duration=args.duration, start=args.start)

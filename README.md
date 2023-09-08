# 🍇 Dionysus Project

Dionysus is a Python-based command-line tool that provides a simple way to split and merge audio from and into video files.

## 🎉 Features

1. **Audio Splitting**: Extracts audio from a video file.
2. **Audio Merging**: Merges enhanced or processed audio back into the video.

These features are particularly useful when you need to improve the audio quality of a video. With Dionysus, you can efficiently extract the audio, apply any AI enhancements or processing, and then merge the enhanced audio back into the video.

## 🚀 Installation
```python
pip install git+https://github.com/Eastonn/dionysus.git
```
## 💡 Usage

Here's how to use the command-line tool:
Replace `<path_to_video_file>` with the path of the video file you want to process, and replace `<path_to_output_file>` with the output path where you want your processed video to be saved.

Here are the options you can use:

- **input_path**: Path to the input video file.
- **mode**: Mode of operation. It can either be 'split' (default) or 'merge'.
- **audio_path**: Path to the input audio file. **Required if the mode is 'merge'**.
- **duration**: Duration of the video to process in seconds or in ```h:m:s``` format. If not given, the entire video will be processed.
- **start**: Start time of the video to process in seconds or ```h:m:s``` format. If not given, it will start from the beginning..
## 🌟 Examples

**To split audio from a video file**: 

```python 
dionysus "input.mp4" --mode "split"
```

**To merge audio into a video file:**: 
```python
dionysus "input.mp4" --mode "merge" --audio_path "input.mp3"
```

**To split first 60 seconds from a video file:**: 
```python
dionysus "input.mp4" --mode "split" --duration "60"
```

**To split first 1.5 minutes starts from 10 minute from a video file:**: 
```python
dionysus "input.mp4" --mode "split" --duration "1:30" --start "10:00"
```

**To merge two clips of first 60 seconds into one video file:**: 
```python
dionysus "input.mp4" --mode "merge" --audio_path "input.mp3" --duration "60"
```


from pydub import AudioSegment

class AudioProcessor:
    @staticmethod
    def normalize_audio(audio_file_path, normalised_audio_file_path):
        audio = AudioSegment.from_file(audio_file_path)
        target_dBFS = -20.0
        change_in_dBFS = target_dBFS - audio.dBFS
        normalize_audio = audio.apply_gain(change_in_dBFS)
        normalize_audio.export(normalised_audio_file_path, format="mp3")
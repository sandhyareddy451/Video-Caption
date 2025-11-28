import whisper
import srt
from datetime import timedelta


def transcribe(audio_path):
    
    model = whisper.load_model("base")
    result =model.transcribe(audio_path)
    return result


def convert_to_srt(transcription_results):
    
    segments = transcription_results['segments']
    sub_titles = []
    
    for i, seg in enumerate(segments):
        subtitle =srt.Subtitle(
            
            
            index = i+1,
            start = timedelta(seconds=seg['start']),
            end =timedelta(seconds = seg['end']),
            content =seg['text'].strip()
        )
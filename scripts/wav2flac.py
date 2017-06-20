# 
from pydub import AudioSegment

song = AudioSegment.from_wav("voice.wav")
song.export("testme.flac",format = "flac")

from turtledemo.minimal_hanoi import play
import torch
from TTS.api import TTS

from TextToSpeech.tts_Interface import TextToSpeechInterface


class Coqui(TextToSpeechInterface):
    def __init__(self):
        self.__model = 'tts_models/multilingual/multi-dataset/xtts_v2'
        self.audio = None
        self.__text: str = ''
        self.__file_path = 'Assets/output.wav'
        self.__language = 'pl'
        self.__split_sentences = True
        # self.voice = '' #nazwa profilu uzytkownika
        self.__speaker_wav = []
        self.__device = "cuda" if torch.cuda.is_available() else "cpu"
        self.__tts = TTS(model_name=self.__model, gpu=False)

    def set_recordings(self, recordings: list):
        self.__speaker_wav = recordings

    def clone(self, name: str, description=None):
        pass

    def generate(self):
        self.audio = self.__tts.tts(text=self.__text, speaker_wav=self.__speaker_wav[0], language=self.__language, split_sentences=self.__split_sentences)


    def play(self):
        if self.audio is None:
            raise Exception('Audio not generated')
        play(self.audio, use_ffmpeg=False)

    def set_text(self, text: str):
        self.__text = text

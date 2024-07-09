from turtledemo.minimal_hanoi import play
import torch
import pygame
from TTS.api import TTS
from elevenlabs import play

from TextToSpeech.tts_Interface import TextToSpeechInterface


class Coqui(TextToSpeechInterface):
    def __init__(self):
        self.__model = 'tts_models/multilingual/multi-dataset/xtts_v2'
        self.audio = None
        self.__text: str = 'Siema jestem Marcin! Co tam?'
        self.__file_path = 'Assets/output.wav'
        self.__language = 'pl'
        self.__split_sentences = True
        # self.voice = '' #nazwa profilu uzytkownika
        self.__speaker_wav = "Assets/Voices/plik1.wav"
        self.__device = "cuda" if torch.cuda.is_available() else "cpu"
        self.__tts = TTS(model_name=self.__model, gpu=False)
        pygame.mixer.init()

    def set_recordings(self, recordings: list):
        self.__speaker_wav = recordings

    def clone(self, name: str, description=None):
        pass

    def set_voice(self, voice_name):
        pass

    def generate(self):
        self.audio = self.__tts.tts_to_file(text=self.__text,
                                    speaker_wav=self.__speaker_wav,
                                    language=self.__language,
                                    file_path=self.__file_path,
                                    split_sentences=self.__split_sentences)

    def play(self):
        # if self.audio is None:
        #     raise Exception('Audio not generated')
        # play(self.audio, use_ffmpeg=False)
        pygame.mixer.music.load(self.__file_path)
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def set_text(self, text: str):
        self.__text = text

    def save(self, path: str):
        pass

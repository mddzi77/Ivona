import json
import uuid
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
        self.audio_bytes = None
        self.__text: str = 'Siema jestem Marcin! Co tam?'
        self.__file_path = 'Assets/temp.wav'
        self.__language = 'pl'
        self.__voice = None
        self.__split_sentences = True
        # self.voice = '' #nazwa profilu uzytkownika
        self.__speaker_wav = None
        self.__device = "cuda" if torch.cuda.is_available() else "cpu"
        self.__tts = TTS(model_name=self.__model, gpu=False)
        pygame.mixer.init()

    def set_recordings(self, recordings: list):
        self.__speaker_wav = recordings

    def clone(self, name: str, description=None):
        pass

    def set_voice(self, voice_name):
        try:
            with open("Assets/settings.json", "r") as f:
                profiles = json.load(f)['profiles']
                for profile in profiles:
                    if profile["ProfileName"] == voice_name:
                        self.__speaker_wav = profile["Path"]
                        self.__voice = voice_name
                        break
        except FileNotFoundError as e:
            print(e)

    def generate(self):
        self.audio = self.__tts.tts_to_file(text=self.__text,
                                    speaker_wav=self.__speaker_wav,
                                    language=self.__language,
                                    file_path=self.__file_path,
                                    split_sentences=self.__split_sentences)
        with open(self.__file_path, 'rb') as f:
            self.audio_bytes = f.read()

    def play(self):
        if self.__voice is None:
            raise Exception('Voice not set')
        elif self.audio is None:
            raise Exception('Audio not generated')
        pygame.mixer.music.load(self.__file_path)
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def set_text(self, text: str):
        self.__text = text

    def save(self, path: str):
        save_file_path = f"{path}\\{uuid.uuid4()}.wav"
        with open(save_file_path, "wb") as f:
            f.write(self.audio_bytes)
        print(f"{save_file_path}: plik audio zapisany")

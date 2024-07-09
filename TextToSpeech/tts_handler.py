import json

from .Coqui.coqui import Coqui
from .tts_Interface import TextToSpeechInterface
from TextToSpeech.ElevenLabs.eleven_labs import ElevenLabs
from enum import Enum


class ModelType(Enum):
    Default = 'built_in_model'
    ElevenLabs = 'eleven_labs_model'


class TTSHandler:

    __model: TextToSpeechInterface = None
    __model_type: ModelType = None
    __eleven_labs = ElevenLabs()
    __default = Coqui()

    @staticmethod
    def get_model_type():
        return TTSHandler.__model_type.value

    @staticmethod
    def set_model(model_type: ModelType):
        if model_type == ModelType.Default:
            TTSHandler.__model = TTSHandler.__default
            TTSHandler.__model_type = ModelType.Default
            # raise NotImplementedError('Model not implemented') TODO: Implement free default __model
        elif model_type == ModelType.ElevenLabs:
            TTSHandler.__model = TTSHandler.__eleven_labs
            TTSHandler.__model_type = ModelType.ElevenLabs
        else:
            raise Exception('Invalid __model type')

        with open('Assets/settings.json', 'r', encoding='UTF-8') as f:
            data = json.load(f)
            data['model'] = TTSHandler.__model_type.value
        with open('Assets/settings.json', 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def set_recordings(recordings: list):
        TTSHandler.__model.set_recordings(recordings)

    @staticmethod
    def set_text(text: str):
        TTSHandler.__model.set_text(text)

    @staticmethod
    def set_voice(voice_name):
        TTSHandler.__model.set_voice(voice_name)

    @staticmethod
    def clone(name: str, description=None):
        TTSHandler.__model.clone(name, description)

    @staticmethod
    def generate():
        TTSHandler.__model.generate()

    @staticmethod
    def play():
        TTSHandler.__model.play()

    @staticmethod
    def stop():
        TTSHandler.__model.stop()

    @staticmethod
    def resume():
        TTSHandler.__model.resume()
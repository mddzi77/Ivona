from .tts_Interface import TextToSpeechInterface
from .text_to_speech import ElevenLabs
from enum import Enum


class ModelType(Enum):
    Default = 0
    ElevenLabs = 1


class TTSHandler:

    __model: TextToSpeechInterface = None
    __eleven_labs = ElevenLabs()
    __default = None

    @staticmethod
    def set_model(model_type: ModelType):
        if model_type == ModelType.Default:
            raise NotImplementedError('Model not implemented')  # TODO: Implement free default __model
        elif model_type == ModelType.ElevenLabs:
            TTSHandler.__model = TTSHandler.__eleven_labs
        else:
            raise Exception('Invalid __model type')

    @staticmethod
    def set_recordings(recordings: list):
        TTSHandler.__model.set_recordings(recordings)

    @staticmethod
    def set_text(text: str):
        TTSHandler.__model.set_text(text)

    @staticmethod
    def set_voice(voice_id):
        TTSHandler.__model.set_voice(voice_id)

    @staticmethod
    def clone(name: str, description=None):
        return TTSHandler.__model.clone(name, description)

    @staticmethod
    def generate():
        TTSHandler.__model.generate()

    @staticmethod
    def play():
        TTSHandler.__model.play()

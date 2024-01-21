from elevenlabs import voices, generate, clone, play, Voice, set_api_key
from tts_Interface import TextToSpeechInterface


class ElevenLabs(TextToSpeechInterface):

    def __init__(self):
        self.voices_list = []
        self.__model = 'eleven_multilingual_v2'
        self.__api_key = open('api_key.txt', 'r').read()
        self.audio = None
        self.__text: str = ''
        self.__voice: str | Voice = None
        self.__recordings = []
        set_api_key(self.__api_key)

    def set_text(self, text: str):
        self.__text = text

    def set_voice(self, name: str | Voice = None, id: int = None):
        pass

    def set_recordings(self, recordings: list):
        self.__recordings = recordings

    def clone(self, name: str, description=None):
        v = clone(name=name, description=description, files=self.__recordings, api_key=self.__api_key)
        self.__voice = v

    def play(self):
        self.audio = generate(self.__text, self.__api_key, self.__voice, self.__model)
        play(self.audio, use_ffmpeg=False)


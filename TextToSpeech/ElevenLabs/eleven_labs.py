from elevenlabs import generate, clone, play, Voice, set_api_key
from texttospeech.tts_Interface import TextToSpeechInterface


class ElevenLabs(TextToSpeechInterface):

    def __init__(self):
        self.voices_list = []
        self.__model = 'eleven_multilingual_v2'
        self.__api_key = open('TextToSpeech/api_key.txt', 'r').read()
        self.audio = None
        self.name = 'Name'
        self.__voice: Voice = None
        self.__text: str = ''
        self.__recordings = []
        set_api_key(self.__api_key)

    def set_text(self, text: str):
        self.__text = text

    def set_recordings(self, recordings: list):
        self.__recordings = recordings

    def set_voice(self, voice_id):
        self.__voice = Voice(voice_id=voice_id, api_key=self.__api_key)

    def clone(self, name: str, description=None):
        return clone(name=name, files=self.__recordings, api_key=self.__api_key)

    def generate(self):
        if self.__voice is None:
            raise Exception('Voice not set')
        self.audio = generate(self.__text, self.__api_key, self.__voice, self.__model)
        # with open(f'TextToSpeech/{self.__voice}.mp3', 'wb') as f:
        #     f.write(self.audio)

    def play(self):
        if self.__voice is None:
            raise Exception('Voice not set')
        elif self.audio is None:
            raise Exception('Audio not generated')
        play(self.audio, use_ffmpeg=False)

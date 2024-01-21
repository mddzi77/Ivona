from elevenlabs import Voice


class TextToSpeechInterface:

    def set_text(self, text: str):
        pass

    def set_voice(self, name: str | Voice):
        pass

    def set_recordings(self, recordings: list):
        pass

    def clone(self, name: str, description=None):
        pass

    def play(self):
        pass

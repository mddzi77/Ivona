class TextToSpeechInterface:

    def set_text(self, text: str):
        pass

    def set_recordings(self, recordings: list):
        pass

    def clone(self, name: str, description=None):
        pass

    def generate(self):
        pass

    def play(self):
        pass

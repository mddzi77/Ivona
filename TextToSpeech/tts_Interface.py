from abc import abstractmethod, ABC


class TextToSpeechInterface(ABC):

    @abstractmethod
    def set_text(self, text: str):
        pass

    @abstractmethod
    def set_recordings(self, recordings: list):
        pass

    @abstractmethod
    def set_voice(self, voice_name):
        pass

    @abstractmethod
    def clone(self, name: str, description=None):
        pass

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def save(self, path: str):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def resume(self):
        pass
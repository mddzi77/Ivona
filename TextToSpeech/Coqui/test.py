import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

voice_path = open()

tts.tts_to_file(text="jakis tekst",
                file_path="output.wav",
                speaker_wav="Ivona/",
                language="it",
                split_sentences=True
                )

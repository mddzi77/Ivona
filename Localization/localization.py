import csv
import json
from enum import Enum


def t(key):
    return Localization().translate(key)


class Language(Enum):
    English = 'english'
    Polish = 'polish'


class Localization:

    __instance = None
    __language = None
    __lang_dict = {Language.English: 'english', Language.Polish: 'polish'}
    __data = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Localization, cls).__new__(cls)
            cls.__instance.__initialize()
        return cls.__instance

    def get_language(self):
        return self.__language

    def translate(self, key):
        try:
            return self.__data[key]
        except KeyError:
            print(f'Key {key} not found in translation file')
            return f'key <{key}> not found'

    def set_language(self, lang: Language):
        self.__language = lang.value
        self.__write_lang()
        self.__load_data()

    # def find_key(self, text):
    #     with open('Assets/translation.csv', mode='r', encoding='UTF-8') as f:
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             for lang in Language:
    #                 try:
    #                     if row[lang.value] == text:
    #                         return row['key']
    #                 except KeyError:
    #                     pass

    def __initialize(self):
        with open('Assets/settings.json', 'r', encoding='UTF-8') as f:
            data = json.load(f)
            self.__language = data['language']
            self.__load_data()

    def __write_lang(self):
        with open('Assets/settings.json', 'r', encoding='UTF-8') as f:
            data = json.load(f)
            data['language'] = self.__language
        with open('Assets/settings.json', 'w') as f:
            json.dump(data, f, indent=2)

    def __load_data(self):
        with open('Assets/translation.csv', mode='r', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.__data[row['key']] = row[self.__language]

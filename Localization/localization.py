import csv
import json
from enum import Enum


def t(key):
    return Localization().t(key)


class Language(Enum):
    English = 0
    Polish = 1


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

    def t(self, key):
        try:
            return self.__data[key]
        except KeyError:
            print(f'Key {key} not found in translation file')

    def set_lang(self, lang: Language):
        self.__language = self.__lang_dict[lang]
        self.__write_lang()
        self.__load_data()

    def __initialize(self):
        with open('Assets/settings.json', 'r') as f:
            data = json.load(f)
            self.__language = data['language']
            self.__load_data()

    def __write_lang(self):
        with open('Assets/settings.json', 'r') as f:
            data = json.load(f)
            data['language'] = self.__language
        with open('Assets/settings.json', 'w') as f:
            json.dump(data, f, indent=2)

    def __load_data(self):
        with open('Assets/translation.csv', mode='r', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.__data[row['key']] = row[self.__language]

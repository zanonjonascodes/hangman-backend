import json


class WordsDAO:
    @staticmethod
    def get_all_words() -> dict:
        with open('db/words.json') as json_file:
            words = json.load(json_file)
        return words




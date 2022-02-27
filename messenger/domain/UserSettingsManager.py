from typing import IO, Text, Callable

from messenger.domain.Settings import Settings


Stream = bytes | IO[bytes] | Text | IO[Text]


class UserSettingsManager(object):
    def __init__(self, reader: Callable[[Stream], Settings], filepath: str):
        self.reader = reader
        self.filepath = filepath

    def get_all(self):
        with open(self.filepath, 'r') as file:
            return self.reader(file)



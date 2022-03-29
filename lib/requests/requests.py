from json import load, loads
from urllib.request import urlopen

from .creds import Creds


@abs
class Requester:
    def __init__(self) -> None:
        pass
    def request():
        pass


class MockRequester:
    def __init__(self) -> None:
        pass


class BoardsRequester:
    def __init__(self, id="None", name="None") -> None:
        self.id = id
        self.name = name

    def request(self) -> dict:
        if self.id is None or self.name is None:
            pass
        return
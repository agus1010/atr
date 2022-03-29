from json import load

class Creds:

    __apiKey = None
    __apiToken = None

    @classmethod
    @property
    def values(cls) -> tuple[str | str]:
        return [ Creds.apiKey, Creds.apiToken ]

    @classmethod
    @property
    def apiKey(cls) -> str:
        if Creds.__apiKey == None:
            Creds.__apiKey = str(load(open("creds/auth.json", "r"))["apiKey"])
        return Creds.__apiKey

    @classmethod
    @property
    def apiToken(cls) -> str:
        if Creds.__apiToken == None:
            Creds.__apiToken = str(load(open("creds/auth.json", "r"))["apiToken"])
        return Creds.__apiToken
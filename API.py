

class _Route:

    def __init__(self, path):
        self.Base = "https://api.tracker.gg/api/"
        self.Version = "v2"
        self.Path = self._path(p=path)

    def _path(self, p: str):
        if not p.startswith('/'): return '/' + p
        else: return p

    def __str__(self) -> str: 
        return self.Base + self.Version + self.Path
    

class Route:

    def __init__(self, path):
        self.Base = "https://public-api.tracker.gg/api/"
        self.Version = "v1"
        self.Path = self._path(p=path)

    def _path(self, p: str):
        if not p.startswith('/'): return '/' + p
        else: return p

    def __str__(self) -> str: 
        return self.Base + self.Version + self.Path
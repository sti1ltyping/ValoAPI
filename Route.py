
import cloudscraper
import json
import asyncio
import time

scraper = cloudscraper.create_scraper()

class Route:

    def __init__(self, path):
        self.Base = "https://api.tracker.gg/api/"
        self.Version = "v2"
        self.Path = self._path(p=path)

    def _path(self, p: str):
        if not p.startswith('/'): return '/' + p
        else: return p

    def __str__(self) -> str: 
        return self.Base + self.Version + self.Path
    
    async def call(self, **kwargs):

        response = await asyncio.to_thread(scraper.get, self.__str__(), **kwargs)
        
        if response.status_code == 200:
            data = json.loads(response.text)

            # -------- Remove After Wrapper is completed ------
            with open("data.txt", "w") as f:
                json.dump(data, f, indent=4)
            #--------------------------------------------------

            return data
        
        else:
            print("Error fetching data:", response.status_code)
            with open(f"Error Logs/{int(time.time())}.txt", "w") as f:
                f.write(response.text + f"\n\nURL: {self.__str__()}" + f"\n\nStatus Code: {response.status_code}")

            return None
    
    async def _call(self, **kwargs):
        scraper = cloudscraper.create_scraper()

        proxies = kwargs.pop("proxies", None)

        if proxies:
            kwargs["proxies"] = proxies
            kwargs["auth"] = None  # prevent conflicts

        response = await asyncio.to_thread(
            scraper.get,
            self.__str__(),
            **kwargs
        )

        if response.status_code == 200:
            print("Data fetched successfully!")
            return json.loads(response.text)

class _Route:

    def __init__(self, path):
        self.Base = "https://public-api.tracker.gg/api/"
        self.Version = "v2"
        self.Path = self._path(p=path)

    def _path(self, p: str):
        if not p.startswith('/'): return '/' + p
        else: return p

    def __str__(self) -> str: 
        return self.Base + self.Version + self.Path
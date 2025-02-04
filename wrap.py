# Key: 04e0535a-5cfb-4fc2-aa9c-983c4d540236

# https://api.tracker.gg/api/v2/valorant/standard/matches/riot/Alya%20Nyan%23Kawai?type=competitive&season=0&agent=all&map=all

# https://api.tracker.gg/api/v2/valorant/standard/profile/riot/Alya%20Nyan%23Kawai/stats/season/headshotsPercentage?seasonId=476b0893-4c2e-abd6-c5fe-708facff0772&playlist=competitive

# https://api.tracker.gg/api/v2/valorant/standard/profile/riot/Alya%20Nyan%23Kawai/segments/season-report?playlist=competitive

import aiohttp
import asyncio

from API import Route

from utils import *


class Valorant:

    def __init__(self, *, session: aiohttp.ClientSession = ...) -> None:
        self.session = session
        self.cache = {...}

    async def __aenter__(self):
        if self.session is Ellipsis:
            self.session = aiohttp.ClientSession(
                cookies = cookie(),
                headers = header()
            )
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.session and self.session != ...:
            await self.session.close()

    async def matches(self, username: str, mode: GameMode, *, agent: Agents = ...):

        userbase = Userbase(username)
        agentbase = AgentBase(agent)
        route = Route(f'/valorant/standard/matches/riot/{userbase}?type={mode}&season=0&agent={agentbase}&map=all')
        url = str(route)

        async with self.session.get(url) as resp:

            # Func...

            # --------- Debug ----------
            print(url)
            data = await resp.text()
            with open('web.htm', 'w') as f: f.write(data)
            print("!status:", resp.status)
            # --------------------------


if __name__ == "__main__":

    async def main():

        async with Valorant() as api:
            await api.matches("Alya Nyan#Kawai", mode="competitive", agent="Jett")

    asyncio.run(main())
# Key: 04e0535a-5cfb-4fc2-aa9c-983c4d540236

# https://api.tracker.gg/api/v2/valorant/standard/matches/riot/Alya%20Nyan%23Kawai?type=competitive&season=0&agent=all&map=all

# https://api.tracker.gg/api/v2/valorant/standard/profile/riot/Alya%20Nyan%23Kawai/stats/season/headshotsPercentage?seasonId=476b0893-4c2e-abd6-c5fe-708facff0772&playlist=competitive

# https://api.tracker.gg/api/v2/valorant/standard/profile/riot/Alya%20Nyan%23Kawai/segments/season-report?playlist=competitive


import aiohttp
import asyncio

from Route import Route

from Extract.Match import MatchData

from utils import *


class Valorant:

    def __init__(self, *, session: aiohttp.ClientSession = ...) -> None:
        self.session = session
        self.cache = {}

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

    async def matches(self, username: str, mode: GameMode, agent: Agents = "all", page: int = 0, **kwargs) -> MatchData | None:

        userbase = Userbase(username)
        agentbase = Agent.get(agent, "all")
        route = Route(f'/valorant/standard/matches/riot/{userbase}?type={mode}&season=0&agent={agentbase}&map=all&next={page}')
        data = await route.call(**kwargs)

        if data:
            return MatchData(data)
        
        else:
            print("Failed to fetch match data.")
            return None
        
    async def profile(self, username: str, **kwargs):
        userbase = Userbase(username)
        route = Route(f'https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{userbase}/segments/season-report?playlist=competitive')
        data = await route.call(**kwargs)

        if data:
            return data
        
        else:
            print("Failed to fetch profile data.")
            return None


if __name__ == "__main__":

    proxies = {
        "http": "http://45.38.107.97:6014",
        "https": "http://45.38.107.97:6014"
    }

    async def main():

        async with Valorant() as api:
            match_data = await api.matches(
                "Alya is a cutie#Kawai",
                mode="competitive",
                agent="Reyna",
                
                proxies=proxies, 
                headers=header(),
                cookies=cookie()
            )

        if match_data:

            latest = match_data.matches[0]
            print(f"""

Latest Match Details:

- Username: {match_data.username}
- Rank: {latest.rank.rank_name}
- Rank Image: {latest.rank.rank_image_url}

- Time: {latest.metadata.timestamp}

- Map: {latest.metadata.mapname}
- Map Image: {latest.metadata.mapimageurl}
- Season: {latest.metadata.seasonname}
- Result: {latest.metadata.result}
- Max Rounds: {latest.metadata.modemaxrounds}

- Agent Used: {latest.agent_name}
- Kills: {latest.stats.kills}
- Deaths: {latest.stats.deaths}
- Assists: {latest.stats.assists}
- K/D Ratio: {latest.stats.kdr}

- Headshot Percentage: {latest.stats.headshot_percentage}

- Ability 1 Usage: {latest.stats.ability1casts}
- Ability 2 Usage: {latest.stats.ability2casts}
- Ability 3 Usage: {latest.stats.ability3casts}
- Ability 4 Usage: {latest.stats.ability4casts}

- First Bloods: {latest.stats.first_bloods}
- First Deaths: {latest.stats.first_deaths}

- Headshot Kills: {latest.stats.headshot_kills}
- Headshot Dealts: {latest.stats.headshots_dealt}
- Bodyshot Dealts: {latest.stats.bodyshots_dealt}
- Legshot Dealts: {latest.stats.legshots_dealt}

- Plants: {latest.stats.plants}
- Defuses: {latest.stats.defuses}

- Clutches Won: {latest.stats.clutches_won}
- Clutches Lost: {latest.stats.clutches_lost}
""")

    asyncio.run(main())
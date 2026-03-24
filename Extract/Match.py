from . import *

@dataclass
class Attributes:
    id: str
    mapId: str
    modeId: str
    seasonId: str

@dataclass
class Metadata:
    modekey: str
    modename: str
    modeimageurl: str
    modemaxrounds: int
    isavailable: bool
    timestamp: UnixTimestamp
    result: str
    map: str
    mapname: str
    mapimageurl: str
    seasonname: str

@dataclass
class Stats:
    playtime: int
    roundsplayed: int
    roundswon: int
    roundslost: int
    roundsdisconnected: int
    placement: int
    score: int

    kills: int
    deaths: int
    assists: int
    kdr: float

    damage_dealt: int
    damage_received: int
    damage_delta: int

    damage_per_round: float
    damage_delta_per_round: float

    ability1casts: int
    ability2casts: int
    ability3casts: int
    ability4casts: int

    headshot_kills: int

    headshots_dealt: int
    bodyshots_dealt: int
    legshots_dealt: int

    econ_rating: float

    self_deaths: int
    revives: int

    first_bloods: int
    first_deaths: int
    last_deaths: int
    survived: int

    traded: int
    kasted: int

    flawless: int
    thrifty: int

    aces: int
    team_aces: int

    clutches_won: int
    clutches_lost: int

    plants: int
    defuses: int

    score_per_round: float

    headshot_percentage: float

@dataclass
class Rank:
    rank_name: None | str
    rank_image_url: None | str

class Match:
    """Represents a single match entry."""
    def __init__(self, data: dict[str, Any]):
        self.data = data

    @property
    def attributes(self) -> Attributes:
        return Attributes(
            id=self.data["attributes"]["id"],
            mapId=self.data["attributes"]["mapId"],
            modeId=self.data["attributes"]["modeId"],
            seasonId=self.data["attributes"]["seasonId"]
        )
    
    @property
    def metadata(self) -> Metadata:
        return Metadata(
            modekey=self.data["metadata"]["modeKey"],
            modename=self.data["metadata"]["modeName"],
            modeimageurl=self.data["metadata"]["modeImageUrl"],
            modemaxrounds=self.data["metadata"]["modeMaxRounds"],
            isavailable=self.data["metadata"]["isAvailable"],
            timestamp=UnixTimestamp(convert_to_unix(self.data["metadata"]["timestamp"])),
            result=self.data["metadata"]["result"],
            map=self.data["metadata"]["map"],
            mapname=self.data["metadata"]["mapName"],
            mapimageurl=self.data["metadata"]["mapImageUrl"],
            seasonname=self.data["metadata"]["seasonName"]
        )
    
    @property
    def type(self):
        return self.data["segments"][0]["type"]
    
    @property
    def haswon(self) -> bool:
        return self.data["segments"][0]["metadata"]["hasWon"]
    
    @property
    def game_result(self) -> str:
        return self.data["segments"][0]["metadata"]["result"]
    
    @property
    def agent_id(self) -> int:
        return self.data["segments"][0]["metadata"]["agent"]
    
    @property
    def agent_name(self) -> str:
        return self.data["segments"][0]["metadata"]["agentName"]

    @property
    def agent_color(self) -> str:
        return self.data["segments"][0]["metadata"]["agentColor"]
    
    @property
    def agent_image_url(self) -> str:
        return self.data["segments"][0]["metadata"]["agentImageUrl"]
    
    @property
    def tags(self) -> list[dict[str, str]]:
        return self.data["segments"][0]["metadata"]["tags"]
    
    @property
    def expiry_date(self) -> str:
        return self.data["segments"][0]["expiryDate"]

    @property
    def stats(self) -> Stats:
        return Stats(
            playtime=self.data["segments"][0]["stats"]["playtime"]["value"] if self.data["segments"][0]["stats"]["playtime"]["value"] else 0,
            roundsplayed=self.data["segments"][0]["stats"]["roundsPlayed"]["value"] if self.data["segments"][0]["stats"]["roundsPlayed"]["value"] else 0,
            roundswon=self.data["segments"][0]["stats"]["roundsWon"]["value"] if self.data["segments"][0]["stats"]["roundsWon"]["value"] else 0,
            roundslost=self.data["segments"][0]["stats"]["roundsLost"]["value"] if self.data["segments"][0]["stats"]["roundsLost"]["value"] else 0,
            roundsdisconnected=self.data["segments"][0]["stats"]["roundsDisconnected"]["value"] if self.data["segments"][0]["stats"]["roundsDisconnected"]["value"] else 0,
            placement=self.data["segments"][0]["stats"]["placement"]["value"] if self.data["segments"][0]["stats"]["placement"]["value"] else 0,
            score=self.data["segments"][0]["stats"]["score"]["value"] if self.data["segments"][0]["stats"]["score"]["value"] else 0,

            kills=self.data["segments"][0]["stats"]["kills"]["value"] if self.data["segments"][0]["stats"]["kills"]["value"] else 0,
            deaths=self.data["segments"][0]["stats"]["deaths"]["value"] if self.data["segments"][0]["stats"]["deaths"]["value"] else 0,
            assists=self.data["segments"][0]["stats"]["assists"]["value"] if self.data["segments"][0]["stats"]["assists"]["value"] else 0,
            kdr=self.data["segments"][0]["stats"]["kdRatio"]["value"] if self.data["segments"][0]["stats"]["kdRatio"]["value"] else 0.0,

            damage_dealt=self.data["segments"][0]["stats"]["damage"]["value"] if self.data["segments"][0]["stats"]["damage"]["value"] else 0,
            damage_received=self.data["segments"][0]["stats"]["damageReceived"]["value"] if self.data["segments"][0]["stats"]["damageReceived"]["value"] else 0,
            damage_delta=self.data["segments"][0]["stats"]["damageDelta"]["value"] if self.data["segments"][0]["stats"]["damageDelta"]["value"] else 0,

            damage_per_round=self.data["segments"][0]["stats"]["damagePerRound"]["value"] if self.data["segments"][0]["stats"]["damagePerRound"]["value"] else 0,
            damage_delta_per_round=self.data["segments"][0]["stats"]["damageDeltaPerRound"]["value"] if self.data["segments"][0]["stats"]["damageDeltaPerRound"]["value"] else 0,


            ability1casts=self.data["segments"][0]["stats"]["grenadeCasts"]["value"] if self.data["segments"][0]["stats"]["grenadeCasts"]["value"] else 0,
            ability2casts=self.data["segments"][0]["stats"]["ability1Casts"]["value"] if self.data["segments"][0]["stats"]["ability1Casts"]["value"] else 0,
            ability3casts=self.data["segments"][0]["stats"]["ability2Casts"]["value"] if self.data["segments"][0]["stats"]["ability2Casts"]["value"] else 0,
            ability4casts=self.data["segments"][0]["stats"]["ultimateCasts"]["value"] if self.data["segments"][0]["stats"]["ultimateCasts"]["value"] else 0,

            headshot_kills=self.data["segments"][0]["stats"]["headshots"]["value"] if self.data["segments"][0]["stats"]["headshots"]["value"] else 0,

            headshots_dealt=self.data["segments"][0]["stats"]["dealtHeadshots"]["value"] if self.data["segments"][0]["stats"]["dealtHeadshots"]["value"] else 0,
            bodyshots_dealt=self.data["segments"][0]["stats"]["dealtBodyshots"]["value"] if self.data["segments"][0]["stats"]["dealtBodyshots"]["value"] else 0,
            legshots_dealt=self.data["segments"][0]["stats"]["dealtLegshots"]["value"] if self.data["segments"][0]["stats"]["dealtLegshots"]["value"] else 0,

            econ_rating=self.data["segments"][0]["stats"]["econRating"]["value"] if self.data["segments"][0]["stats"]["econRating"]["value"] else 0.0,

            self_deaths=self.data["segments"][0]["stats"]["suicides"]["value"] if self.data["segments"][0]["stats"]["suicides"]["value"] else 0,
            revives=self.data["segments"][0]["stats"]["revived"]["value"] if self.data["segments"][0]["stats"]["revived"]["value"] else 0,

            first_bloods=self.data["segments"][0]["stats"]["firstBloods"]["value"] if self.data["segments"][0]["stats"]["firstBloods"]["value"] else 0,
            first_deaths=self.data["segments"][0]["stats"]["firstDeaths"]["value"] if self.data["segments"][0]["stats"]["firstDeaths"]["value"] else 0,
            last_deaths=self.data["segments"][0]["stats"]["lastDeaths"]["value"] if self.data["segments"][0]["stats"]["lastDeaths"]["value"] else 0,
            survived=self.data["segments"][0]["stats"]["survived"]["value"] if self.data["segments"][0]["stats"]["survived"]["value"] else 0,

            traded=self.data["segments"][0]["stats"]["traded"]["value"] if self.data["segments"][0]["stats"]["traded"]["value"] else 0,
            kasted=self.data["segments"][0]["stats"]["kAST"]["value"] if self.data["segments"][0]["stats"]["kAST"]["value"] else 0,

            flawless=self.data["segments"][0]["stats"]["flawless"]["value"] if self.data["segments"][0]["stats"]["flawless"]["value"] else 0,
            thrifty=self.data["segments"][0]["stats"]["thrifty"]["value"] if self.data["segments"][0]["stats"]["thrifty"]["value"] else 0,

            aces=self.data["segments"][0]["stats"]["aces"]["value"] if self.data["segments"][0]["stats"]["aces"]["value"] else 0,
            team_aces=self.data["segments"][0]["stats"]["teamAces"]["value"] if self.data["segments"][0]["stats"]["teamAces"]["value"] else 0,

            clutches_won=self.data["segments"][0]["stats"]["clutches"]["value"] if self.data["segments"][0]["stats"]["clutches"]["value"] else 0,
            clutches_lost=self.data["segments"][0]["stats"]["clutchesLost"]["value"] if self.data["segments"][0]["stats"]["clutchesLost"]["value"] else 0,

            plants=self.data["segments"][0]["stats"]["plants"]["value"] if self.data["segments"][0]["stats"]["plants"]["value"] else 0,
            defuses=self.data["segments"][0]["stats"]["defuses"]["value"] if self.data["segments"][0]["stats"]["defuses"]["value"] else 0,

            score_per_round=self.data["segments"][0]["stats"]["scorePerRound"]["value"] if self.data["segments"][0]["stats"]["scorePerRound"]["value"] else 0.0,

            headshot_percentage=self.data["segments"][0]["stats"]["headshotsPercentage"]["value"] if self.data["segments"][0]["stats"]["headshotsPercentage"]["value"] else 0.0,
        )
    
    @property
    def rank(self) -> Rank:
        return Rank(
            rank_name=self.data["segments"][0]["stats"]["rank"]["metadata"]["tierName"],
            rank_image_url=self.data["segments"][0]["stats"]["rank"]["metadata"]["iconUrl"]
        )

class MatchList:
    """Represents a list of match entries and makes it iterable."""
    def __init__(self, data: List[dict[str, Any]]):
        self.data = [Match(entry) for entry in data]

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index: int) -> Match:
        return self.data[index]

    def __len__(self):
        return len(self.data)
    
class MatchData:
    def __init__(self, data: dict[str, str]):
        self.data = data["data"]
    
    @property
    def expiry(self) -> str:
        if "expiryDate" in self.data:
            return self.data["expiryDate"]
        return None
    
    @property
    def username(self) -> str:
        return self.data["requestingPlayerAttributes"]["platformUserIdentifier"]
    
    @property
    def matches(self) -> MatchList:
        return MatchList(self.data["matches"])
    
    
    
    
    

        
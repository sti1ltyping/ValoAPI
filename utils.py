import random
from typing import Literal, Union, List, Dict, ClassVar, Optional

import Identity.Agent

Agents = Literal[
    "Astra",
    "Breach"
    # Etc...
    ] 
GameMode = Literal[
    "competitive",
    "unrated"
    # Etc...
    ]

class Userbase:
    def __init__(self, username):
        self.username = self._username(a=username)

    def _username(self, a: str):
        return a.replace(' ', '%20').replace('#', '%23')
    
    def __str__(self):
        return self.username
    
class AgentBase:

    def __init__(self, agent: Agents):
        self.agent = self._agent(a=agent)

    def _agent(self, a: str):
        return Identity.Agent.data.get(a, "-1")
        
    def __str__(self):
        return self.agent

class aiohttpClientHeader:
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/97.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/97.0.1072.62 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0',
        'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14.6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14.4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.66 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.4.11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5173.13 Safari/537.36'
    ]

    device_ids = [
        '0123456789abcdef',
        '9876543210abcdef',
        'abcdef0123456789',
        '1234567890abcdef',
        '4567890123abcdef',
        'feedfacecafebeef',
        'deadbeef12345678',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '9b8c7d6e5f4a3b2c',
        'c3b2a1d4e5f6g7h8',
        '7h8g6f5e4d3c2b1a',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '9b8c7d6e5f4a3b2c',
        'c3b2a1d4e5f6g7h8',
        '7h8g6f5e4d3c2b1a',
        '8a9b7c6d5e4f3g2h',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '9b8c7d6e5f4a3b2c',
        'c3b2a1d4e5f6g7h8',
        '7h8g6f5e4d3c2b1a',
        '8a9b7c6d5e4f3g2h',
        '9a8b7c6d5e4f3g2h',
        '0123456789abcdef',
        '9876543210abcdef',
        'abcdef0123456789',
        '1234567890abcdef',
        '4567890123abcdef',
        'feedfacecafebeef',
        'deadbeef12345678',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '9b8c7d6e5f4a3b2c',
        'c3b2a1d4e5f6g7h8',
        '7h8g6f5e4d3c2b1a',
        '8a9b7c6d5e4f3g2h',
        '1122334455667788',
        '99aabbccddeeff00',
        '0011223344556677',
        '8899aabbccddeeff',
        'ffeeddccbbaa9988',
        '7766554433221100',
        '0102030405060708',
        'a1b2c3d4e5f6g7h8',
        '1a2b3c4d5e6f7g8h',
        'f1e2d3c4b5a69788',
        '98a7b6c5d4e3f2f1',
        '0f1e2d3c4b5a6978',
        '9b8c7d6e5f4a3b2c'
    ]


def header() -> aiohttpClientHeader:
    headers = {
        'User-Agent': random.choice(aiohttpClientHeader.user_agents),
        'Device-Id': random.choice(aiohttpClientHeader.device_ids),
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "TRN-Api-Key": "04e0535a-5cfb-4fc2-aa9c-983c4d540236"
    }
    headers = {
        "Content-Type": "application/json",
        "TRN-Api-Key": "04e0535a-5cfb-4fc2-aa9c-983c4d540236"
    }
    return headers

def cookie():
    cookies = {
            "__cflb": "02DiuFQAkRrzD1P1mdjW28WYn2UPf2uFA39AFrhBG8sn4",
            "_ga": "GA1.1.1964448456.1738607562",
            "panoramaId_expiry": "1738693972380",
            "_cc_id": "2082e228ee25dfa8cda6191b607a4f7b",
            "panoramaId": "e017800fcebea23292a539cb1bcca9fb927aa5e047811d57cb5fbe848ee69a62",
            "cf_clearance": "_wASImG7E100td0IdhK5Pxmv1P_dd5BDQnlbBhVo1T8-1738613231-1.2.1.1-.R1Af0oqD8t_ZOmBdk_h9cnmqtK7GFj7_q0uGOVc42kql.fWP5CRqzl.IEuu0M3vuTs0HD3FuaEhmFHhc3h90VLPh6VY1RqHw3UBlOOLlWGkLMth8HyRzCOR_zpPz..sL1GtZVBTR.r7.EyWo5xmiMupH001K26qmJU9qkK0e3Ahj.4eYL9ykicSt5pDVyzAEN2N.49yf3JM5ApqoElOcXl_hdMfzaOJrKeSDplPvqRKxjv_oLFi_kTZhohICqthxpWCZ6GyFRtMUoiOAO_EBI_IWx9Mb3eaHbJrSPMYvp0",
            "_ga_HWSV72GK8X": "GS1.1.1738607562.1.1.1738613275.0.0.0",
            "cto_bundle": "BrHHtF9iUFdXWnZkVmRZMm1DYUclMkJMS1ElMkJGRmFjMGFxSGRZdkh4RnZPekk0dWlZR1ppVmcwN0ZTQnhjczlaT3Z5eEkxRlladDE3OGR1WHFDbTBVdDloQ1doNzVaUlVqRCUyRklTZkxsSEpSVFA2b1dkVFVZMjdXdDdWUHdxY1E3dlVsVmlPNVFCS0NBR1IyakJWSGZodVRvOVRQVVElM0QlM0Q",
            "__gads": "ID=e8a8ec13fa66a683:T=1738607570:RT=1738613451:S=ALNI_Mb0vpddX0oPvBBZ5YaPwkg7Snsfqg",
            "__gpi": "UID=00000fe0a7b30e46:T=1738607570:RT=1738613451:S=ALNI_MZOHI0pzcFNa2cZS5LZC21s3jnKdg",
            "__eoi": "ID=cb06e36f61a864d9:T=1738607570:RT=1738613451:S=AA-Afjbx1wBe9QdibcGCeS4VSv9i",
            "__cf_bm": "U44wRX7T8DqBof6eAlOWEj1UWFsmNEItjDqp8Xen9.s-1738618435-1.0.1.1-eWhZkKfkGUrvEun0TPVKcIUAmRih1KZklF6G.4wvCqsiy6JkzqORgfZtOjL.zcQAb_IBMoFoJJPx9fzK0T8Iy2skM68OIybTrGUU652vCnA"
        }
    
    return cookies
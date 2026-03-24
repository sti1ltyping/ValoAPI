from typing import Any, List, Literal, Union
from datetime import datetime, timezone
from dataclasses import dataclass


class UnixTimestamp(int):
    def __new__(cls, value):
        if not isinstance(value, int):
            raise TypeError("UnixTimestamp must be an integer")
        return super().__new__(cls, value)

    def to_datetime(self):
        """Convert the Unix timestamp to a timezone-aware datetime object."""
        return datetime.fromtimestamp(self, tz=timezone.utc)

    def last_seen_format(self) -> str:
        try:
            now = datetime.now(timezone.utc)
            time_difference = now - self.to_datetime()

            if time_difference.days > 0:
                return "1 day ago" if time_difference.days == 1 else f"{time_difference.days} days ago"
                    
            elif time_difference.seconds < 60:
                return "just now"
            
            elif time_difference.seconds < 3600:
                minutes = time_difference.seconds // 60
                return "1 min ago" if minutes == 1 else f"{minutes} mins ago"
            
            else:
                hours = time_difference.seconds // 3600
                return "1 hr ago" if hours == 1 else f"{hours} hrs ago"

        except Exception as e:
            print(e)
            return ''
        
    def since_time_format(self) -> str:
        try:
            now = datetime.now(timezone.utc)
            time_difference = now - self.to_datetime()

            if time_difference.days > 0:
                return "in 1 day" if time_difference.days == 1 else f"in {time_difference.days} days"
                    
            elif time_difference.seconds < 60:
                return f"in {time_difference.seconds} sec"
            
            elif time_difference.seconds < 3600:
                minutes = time_difference.seconds // 60
                return "in 1 min" if minutes == 1 else f"in {minutes} mins"
            
            else:
                hours = time_difference.seconds // 3600
                return "in 1 hr" if hours == 1 else f"in {hours} hrs"

        except Exception as e:
            print(e)
            return ''


def convert_to_unix(nix: str) -> (UnixTimestamp | None):
    if nix:
        return UnixTimestamp(int(
            datetime.fromisoformat(
            nix.replace("Z", "+00:00")).timestamp()
            ))
    return None

if __name__ == "__main__":

    c = convert_to_unix("2025-02-26T06:10:35+00:00")

    print(c)
from dataclasses import dataclass
from typing import Optional


@dataclass
class Arrivals:
    destination: str
    flight: str
    airline: str
    terminal: int
    std: str = ""
    status: str = "On Time"
    id: Optional[int] = None

import random
import enum
import attr


class AirportProblem(RuntimeError):
    """Raised when there's a problem with an airport."""


@attr.s(auto_attribs=True, frozen=True)
class Airport:
    display_name: str
    location: str

    def __str__(self):
        return self.display_name


class Airports(enum.Enum):
    LIM = Airport("Lima Airport", "South America")
    LOS = Airport("Lagos Airport", "Africa")
    PEK = Airport("Beijing Airport", "Asia")
    YVR = Airport("Vancouver Airport", "North America")
    SYD = Airport("Sydney Airport", "Australia")
    TXL = Airport("Berlin Airport", "Europe")


def closest_airport(location):
    for airport in Airports:
        if airport.value.location == location:
            return airport
    raise ValueError


def fly(from_location, to_location):

    # Get closest airports for locations
    from_airport = closest_airport(from_location)
    to_airport = closest_airport(to_location)

    # Well, we all know how it works at Tegel
    if from_airport == Airports.TXL:
        if random.random() < 0.5:
            raise AirportProblem(f"Problems at {from_airport.value} 🚧")

    if to_airport == Airports.TXL:
        if random.random() < 0.5:
            raise AirportProblem(f"Problems at {to_airport.value} 🚧")

    return to_airport.value.location

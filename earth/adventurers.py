import time
import typing

import attr

from .year import Months
from .travel import fly, AirportProblem


class Busy(RuntimeError):
    """Raised when Adventurer is busy."""


def pack(adventurer):
    print(f"{adventurer.profile} {adventurer.name} is packing 👜")


@attr.s(auto_attribs=True, kw_only=True)
class Adventurer:
    name: str
    location: str
    profile: str
    _availability: typing.List = attr.ib(repr=False)
    _calendar: typing.Dict = attr.ib(repr=False, init=False)
    _getting_ready: typing.List[typing.Callable] = attr.ib(repr=False)
    _ready: bool = attr.ib(repr=False, default=False, init=False)

    def __str__(self):
        return f"{self.profile} {self.name}"

    @_getting_ready.default
    def default_activities(self):
        return [pack]

    @_availability.default
    def default_availability(self):
        return list(Months)

    def __attrs_post_init__(self):
        self._calendar = {
            month: month in self._availability for month in Months
        }

    def hello(self):
        print(f"{self.profile} Hello, my name is {self.name}!")

    def rsvp(self, event):
        available = self._calendar[event.month]
        if not available:
            raise Busy(f"{self} sorry, I'm busy!")
        self._calendar[event.month] = False

    def get_ready(self):
        if self._ready is not True:
            for activity in self._getting_ready:
                activity(self)
            self._ready = True
        return self._ready

    def travel_to(self, event):
        if self.location != event.location:
            try:
                location = fly(self.location, event.location)
            except AirportProblem as exc:
                print(f"{self}'s flight was cancelled 😞 {exc}")
            else:
                print(
                    f"{self} is travelling: "
                    f"{self.location} ✈️  {event.location}"
                )
                self.location = location


def new_panda(name, **kwargs):
    def eat(panda):
        for i in range(4):
            print(f"{panda.profile} {panda.name} is eating... 🌱")
            time.sleep(5)

    kwargs.setdefault("location", "Asia")
    return Adventurer(
        name=name, profile="🐼", getting_ready=[eat, pack], **kwargs
    )


def new_bear(name, **kwargs):
    kwargs.setdefault("location", "North America")
    kwargs.setdefault("availability", [Months.JUN, Months.JUL, Months.AUG])
    return Adventurer(name=name, profile="🐻", **kwargs)


def new_tiger(name, **kwargs):
    # Tigers travel light; do not pack
    kwargs.setdefault("location", "Asia")
    return Adventurer(name=name, profile="🐯", getting_ready=[], **kwargs)


def new_koala(name, **kwargs):
    kwargs.setdefault("location", "Australia")
    return Adventurer(name=name, profile="🐨", **kwargs)


def new_lion(name, **kwargs):
    kwargs.setdefault("location", "Africa")
    return Adventurer(name=name, profile="🦁", **kwargs)


def new_frog(name, **kwargs):
    kwargs.setdefault("location", "South America")
    return Adventurer(name=name, profile="🐸", **kwargs)


def new_fox(name, **kwargs):
    kwargs.setdefault("location", "Europe")
    return Adventurer(name=name, profile="🦊", getting_ready=[pack], **kwargs)

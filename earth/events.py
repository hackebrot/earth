import typing
import attr

from .adventurers import Busy
from .year import Months


class MissingAttendee(RuntimeError):
    """Raised when an event attendee is missing."""


@attr.s(auto_attribs=True, frozen=True)
class Event:
    name: str
    location: str
    month: Months
    attendees: typing.List = attr.ib(factory=list)

    def invite(self, attendee):
        try:
            attendee.rsvp(self)
        except Busy:
            print(f"{attendee.name} is not available in {self.month.value}! 😢")
        else:
            self.attendees.append(attendee)
            print(f"{attendee.name} accepted our invite! 😃")

    def start(self):
        print(f"Welcome to {self.name} in {self.location}! 🎉")
        print(f"Let's start with introductions...💬")

        for attendee in self.attendees:
            if attendee.location != self.location:
                raise MissingAttendee(f"Oh no! {attendee.name} is not here! 😟")
            attendee.hello()

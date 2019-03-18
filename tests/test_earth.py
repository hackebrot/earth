import pytest

from earth import adventurers, Event, Months


@pytest.fixture
def event():
    return Event("PyCon US", "North America", Months.MAY)


@pytest.fixture
def friends():
    return [
        adventurers.new_frog("Bruno"),
        adventurers.new_lion("Michael"),
        adventurers.new_koala("Brianna"),
        adventurers.new_tiger("Julia"),
    ]


@pytest.mark.wip
@pytest.mark.happy
def test_earth(event, friends):
    for adventurer in friends:
        event.invite(adventurer)

    for attendee in event.attendees:
        attendee.get_ready()
        attendee.travel_to(event)

    event.start()

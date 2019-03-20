import pytest

from earth import adventurers, Event, Months


@pytest.fixture(name="event")
def fixture_event():
    return Event("PyCon US", "North America", Months.MAY)


@pytest.fixture(name="small_group")
def fixture_small_group():
    return [
        adventurers.new_frog("Bruno"),
        adventurers.new_lion("Michael"),
        adventurers.new_koala("Brianna"),
        adventurers.new_tiger("Julia"),
    ]


@pytest.fixture(name="large_group")
def fixture_large_group():
    return [
        adventurers.new_frog("Bruno"),
        adventurers.new_panda("Po"),
        adventurers.new_fox("Dave"),
        adventurers.new_lion("Michael"),
        adventurers.new_koala("Brianna"),
        adventurers.new_tiger("Julia"),
        adventurers.new_fox("Raphael"),
        adventurers.new_fox("Caro"),
        adventurers.new_bear("Chris"),
        # Bears in warm climates don't hibernate 🐻
        adventurers.new_bear("Danny", availability=[*Months]),
        adventurers.new_bear("Audrey", availability=[*Months]),
    ]


@pytest.mark.wip
@pytest.mark.happy
def test_small_group(event, small_group):
    for adventurer in small_group:
        event.invite(adventurer)

    for attendee in event.attendees:
        attendee.get_ready()
        attendee.travel_to(event)

    event.start()


@pytest.mark.wip
@pytest.mark.happy
def test_large_group(event, large_group):
    for adventurer in small_group:
        event.invite(adventurer)

    for attendee in event.attendees:
        attendee.get_ready()
        attendee.travel_to(event)

    event.start()

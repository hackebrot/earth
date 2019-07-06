import pytest

from earth import adventurers, Event, Months


pytest.mark.txl = pytest.mark.xfail(reason="Problems with TXL airport")


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


@pytest.fixture(name="no_pandas_group")
def fixture_no_pandas_group():
    return [
        adventurers.new_frog("Bruno"),
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
@pytest.mark.slow
@pytest.mark.happy
@pytest.mark.xfail(reason="Problems with TXL airport")
def test_large_group(event, large_group):
    for adventurer in large_group:
        event.invite(adventurer)

    for attendee in event.attendees:
        attendee.get_ready()
        attendee.travel_to(event)

    event.start()


@pytest.mark.wip
@pytest.mark.happy
@pytest.mark.xfail(reason="Problems with TXL airport")
def test_no_pandas_group(event, no_pandas_group):
    for adventurer in no_pandas_group:
        event.invite(adventurer)

    for attendee in event.attendees:
        attendee.get_ready()
        attendee.travel_to(event)

    event.start()


@pytest.fixture(name="group")
def fixture_group(request, small_group, large_group, no_pandas_group):
    group_name = request.param
    groups = {
        "small_group": small_group,
        "large_group": large_group,
        "no_pandas_group": no_pandas_group,
    }
    return groups[group_name]


@pytest.mark.wip
@pytest.mark.happy
@pytest.mark.parametrize(
    "group",
    [
        pytest.param("small_group"),
        pytest.param("large_group", marks=[pytest.mark.txl, pytest.mark.slow]),
        pytest.param("no_pandas_group", marks=[pytest.mark.txl]),
    ],
    indirect=True,
)
def test_earth(group, event):
    for adventurer in group:
        event.invite(adventurer)

    for attendee in event.attendees:
        attendee.get_ready()
        attendee.travel_to(event)

    event.start()

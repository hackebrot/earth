# earth

Example Python project for my PyBerlin talk 🌍

## Example Usage

```python
from earth import adventurers, Event, Months


def main():
    print("Hello adventurers! 🏕")
    print("-" * 40)

    friends = [
        adventurers.new_frog("Bruno"),
        adventurers.new_lion("Michael"),
        adventurers.new_koala("Brianna"),
        adventurers.new_tiger("Julia"),
    ]

    event = Event("PyCon US", "North America", Months.MAY)

    for adventurer in friends:
        event.invite(adventurer)

    print("-" * 40)

    for attendee in event.attendees:
        attendee.get_ready()
        attendee.travel_to(event)

    print("-" * 40)

    event.start()


if __name__ == "__main__":
    main()
```

## Community

Please note that **earth** is released with a [Contributor Code of
Conduct][code of conduct]. By participating in this project you agree to abide
by its terms.

[code of conduct]: https://github.com/hackebrot/earth/blob/master/.github/CODE_OF_CONDUCT.md

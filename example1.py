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

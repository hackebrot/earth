def pytest_addoption(parser):
    group = parser.getgroup("earth")
    group.addoption(
        "--slow",
        action="store_true",
        default=False,
        help="Include slow tests in test run",
    )


def pytest_collection_modifyitems(items, config):
    """Deselect tests marked as slow if --slow is set."""

    if config.option.slow is True:
        return

    selected_items = []
    deselected_items = []

    for item in items:
        if item.get_closest_marker("slow"):
            deselected_items.append(item)
        else:
            selected_items.append(item)

    config.hook.pytest_deselected(items=deselected_items)
    items[:] = selected_items

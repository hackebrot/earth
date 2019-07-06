from collections import defaultdict

import pytest


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


class Turtle:
    """Plugin for adding markers to slow running tests."""

    def __init__(self, config):
        self.config = config
        self.durations = defaultdict(dict)
        self.durations.update(self.config.cache.get("cache/turtle", defaultdict(dict)))
        self.slow = 5.0

    def pytest_runtest_logreport(self, report):
        self.durations[report.nodeid][report.when] = report.duration

    def pytest_sessionfinish(self, session):
        cached_durations = self.config.cache.get("cache/turtle", defaultdict(dict))
        cached_durations.update(self.durations)
        self.config.cache.set("cache/turtle", cached_durations)


def pytest_configure(config):
    config.pluginmanager.register(Turtle(config), "turtle")

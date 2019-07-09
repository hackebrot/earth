from collections import defaultdict

import pytest

from .github import create_issue


def pytest_addoption(parser):
    group = parser.getgroup("earth")
    group.addoption(
        "--slow",
        action="store_true",
        default=False,
        help="Include slow tests in test run",
    )

    group.addoption(
        "--owl",
        action="store",
        type=str,
        default=None,
        metavar="fixture",
        help="Run test using the fixture",
    )


def pytest_collection_modifyitems(items, config):
    """Deselect tests marked as slow if --slow is set."""

    if config.option.slow is True:
        return

    selected_items = []
    deselected_items = []

    for item in items:
        if item.get_closest_marker("slow") or item.get_closest_marker("turtle"):
            deselected_items.append(item)
        else:
            selected_items.append(item)

    config.hook.pytest_deselected(items=deselected_items)
    items[:] = selected_items


class Elephant:
    """Plugin for creating GitHub issues for test regressions."""

    def __init__(self, config):
        self.config = config
        self.failed = {}

    def pytest_runtest_logreport(self, report):
        if report.failed:
            self.failed[report.nodeid] = report

    def pytest_terminal_summary(self, terminalreporter):
        """Hook implementation that writes the URL to the generated GitHub
        issue to the terminal summary.
        """

        if not self.failed:
            return

        md = self.config.pluginmanager.getplugin("md_plugin")

        # TODO: Create GitHub issue here 🚧

        data = create_issue(
            "hackebrot",
            "earth",
            "Test regression detected by pytest-elephant 🐘",
            md.report,
            ["regression"],
        )

        issue = data["html_url"]

        terminalreporter.write_sep("-", f"created GitHub issue: {issue}")


class Owl:
    """Plugin for running tests using a specific fixture."""

    def __init__(self, config):
        self.config = config

    def pytest_collection_modifyitems(self, items, config):
        if not config.option.owl:
            return

        selected_items = []
        deselected_items = []

        for item in items:
            if config.option.owl in getattr(item, "fixturenames", ()):
                selected_items.append(item)
            else:
                deselected_items.append(item)

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

    @pytest.mark.tryfirst
    def pytest_collection_modifyitems(self, session, config, items):
        for item in items:
            duration = sum(self.durations[item.nodeid].values())
            if duration > self.slow:
                item.add_marker(pytest.mark.turtle)

    def pytest_sessionfinish(self, session):
        cached_durations = self.config.cache.get("cache/turtle", defaultdict(dict))
        cached_durations.update(self.durations)
        self.config.cache.set("cache/turtle", cached_durations)

    def pytest_configure(self, config):
        config.addinivalue_line("markers", "turtle: marker for slow running tests")


def pytest_configure(config):
    config.pluginmanager.register(Turtle(config), "turtle")
    config.pluginmanager.register(Owl(config), "owl")
    config.pluginmanager.register(Elephant(config), "elephant")

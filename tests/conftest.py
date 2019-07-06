def pytest_addoption(parser):
    group = parser.getgroup("earth")
    group.addoption(
        "--slow",
        action="store_true",
        default=False,
        help="Include slow tests in test run",
    )

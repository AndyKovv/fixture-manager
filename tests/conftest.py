import pytest
from os import path
from fixture_utils import FixtureManager


@pytest.fixture(scope='session')
def root():
    """
        Fixture should return root path
        for accounts tests

    """
    root_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
    return lambda *x: path.join(root_dir, *x)


@pytest.fixture(scope='session')
def fixture_path(root):
    """
        Method should get fixture
    """

    return open(root('auto_ria_api', 'tests', 'fixtures'))


@pytest.fixture(scope='session')
def fixture_manager(root, fixture_path):
    """
        Fixture should get fixture manager
    """
    return FixtureManager.build_(root, fixture_path)

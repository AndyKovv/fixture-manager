import shutil
import json
import pytest
from os import path, makedirs
from fixture_utils import FixtureManager, Fixture, FixtureNotFound


@pytest.fixture(scope='function')
def mocked_fixture_path(root):
    """
        Fixture should create mocked fixture path
        for create mocked fixture files
    """
    dir_path = root('auto_ria_api', 'tests', 'moked_fixtures')
    if path.exists(dir_path):
        # Perform remove path
        shutil.rmtree(dir_path)

    makedirs(dir_path, mode=0o777)
    return dir_path


class TestsFixturesManager:

    fixture_names = ['fixture_one', 'fixture_two', 'fixture_three']

    def create_fixtures(self, fixture_path):
        """
            Hook for create fixture in fixture path
        """
        payload = json.dumps({"sucess": "true"})
        for name in self.fixture_names:
            file_name = f"{name}.json"
            file_path = f"{fixture_path}/{file_name}"
            with open(file_path, 'w') as f:
                f.writelines(payload)
                f.close()

    def test_should_autodiscover_fixtures_in_directory(self, root, mocked_fixture_path):
        """ Check autodiscover fixture in directory"""
        self.create_fixtures(mocked_fixture_path)
        manager = FixtureManager.build_(root, mocked_fixture_path)
        assert manager.fixture_one is not None

        assert isinstance(manager.fixture_one, Fixture)
        data = manager.fixture_one.to_dict()
        assert data['sucess'] == "true"

    def test_should_raise_exception_if_fixture_not_found(self, root, mocked_fixture_path):
        """ Check raise exception if fixture not found """
        manager = FixtureManager.build_(root, mocked_fixture_path)
        with pytest.raises(FixtureNotFound):
            assert manager.not_exist_fixture is not None

    def test_should_create_fixture_and_convert_it_to_json_from_dict(self):
        """ Fixture should create fixture from dict """
        pass
        # instance = os.walk

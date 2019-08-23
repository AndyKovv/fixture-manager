# fixture_utils

Library for easy maintain fixtures files.

Example of usage:

Structure of the project:

```
example_module:
  example_fixtures:
    fixture_one.json
    fixture_two.json

```

from fixture_utils import FixtureManager
manager = FixtureManager.build_(mocked_fixture_path)
manager.fixture_one -> returns Fixture object 

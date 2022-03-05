import pytest
import os

random_var: int = int(os.getenv('RANDOM_VAR'))

class TestRandomClass:
    """ Random test class. """

    def test_random_method(self) -> None:
        """ Tests a random var's value. """

        assert random_var == 121212
import pytest

from tests.end_to_end_tests.run_directory_manipulations import run_trial_with_output_file_cleaning


@pytest.mark.slow
def test_advanced_dseek():
    run_trial_with_output_file_cleaning(__file__)

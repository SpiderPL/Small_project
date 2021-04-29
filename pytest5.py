import os
from unittest.mock import patch

def dir_exist(name):
    return name in os.listdir()

@patch('os.listdir')
def test_dir_is_in_list(listdir_mock):
    listdir_mock.return_value = ['tmp', 'tmp1']
    assert dir_exist('tmp')
    listdir_mock.assert_called_once()
import os.path
import pytest

from src.load_grid import LoadGrid
from src.exceptions import FileFormException, InvalidDataException
from unittest.mock import patch


class TestLoadGrid:

    def setup_class(self):
        self.loader = LoadGrid()

    @patch("src.load_grid.LoadGrid.validate_data")
    def test_correct_file_format(self, mock_validate_data):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/sample.txt")
        data = self.loader.read_file(file_path=path)

        mock_validate_data.assert_called()

    def test_data_not_rectangle(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/wrong_data1.txt")

        with pytest.raises(FileFormException):
            data = self.loader.read_file(file_path=path)

    def test_data_contains_invalid_character(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/wrong_data2.txt")

        with pytest.raises(InvalidDataException):
            data = self.loader.read_file(file_path=path)

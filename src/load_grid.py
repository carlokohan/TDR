"""
    Consumes the text file, verifies the form and every character, and creates
    a 2D array.
"""

import re

from exceptions import FileFormException, InvalidDataException


class LoadGrid:
    def __init__(self):
        self.file_path = ""
        self.columns = 0
        self.rows = 0
        self.file_data = []

    def read_file(self, file_path):
        self.file_path = file_path
        line_count = 0

        with open(self.file_path, "r") as file_reader:
            line = file_reader.readline()
            line = line.rstrip("\n")
            line_count += 1
            self.columns = len(line)
            self.validate_data(line, line_count)
            self.file_data.append(list(line))

            for line in file_reader:
                line = line.rstrip("\n")
                line_count += 1
                if len(line) != self.columns:
                    raise FileFormException(
                        f"Data is not rectangular form. line: {line_count}"
                    )

                self.validate_data(line, line_count)
                self.file_data.append(list(line))

        self.rows = line_count
        return self.file_data

    @staticmethod
    def validate_data(line, line_count):
        pattern = re.compile("^[XO ]+$")

        if not pattern.match(line):
            raise InvalidDataException(
                f"Data contains invalid character at line: {line_count}"
            )

    @staticmethod
    def print_data(data):
        for row in data:
            print(row)

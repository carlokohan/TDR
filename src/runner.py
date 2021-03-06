"""
    Runs the whole system
"""

from load_grid import LoadGrid


if __name__ == "__main__":
    loader = LoadGrid()
    data = loader.read_file(file_path="/tests/data/wrong_data2.txt")
    print(data)
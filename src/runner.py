"""
    Runs the whole system
"""

from load_grid import LoadGrid
from models.segregation_model import SegregationModel


if __name__ == "__main__":
    loader = LoadGrid()
    data = loader.read_file(file_path="/home/jhusmillo/PycharmProjects/TDR/tests/data/sample.txt")

    segragation_model = SegregationModel(data)
    index = segragation_model.dissimilarity_index(1, 1, 3, 3)
    print(f"dissimilation index: {index}")



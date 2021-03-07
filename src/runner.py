"""
    Runs the whole system
"""

from argparse import ArgumentParser
from exceptions import MissingParametersException
from load_grid import LoadGrid
from models.segregation_model import SegregationModel


def parse_args():
    parser = ArgumentParser(
        description="Segragation Model and Schelling Model"
    )
    parser.add_argument(
        "--file_path",
        type=str,
        help="Absolute path of file to be used",
    )
    parser.add_argument(
        "--model_type",
        type=str,
        help="Choose either 'dissimilarity' or 'schelling'",
    )

    #for dissimilarity model
    parser.add_argument(
        "--start_row",
        type=int,
        help="start row",
    )
    parser.add_argument(
        "--start_column",
        type=int,
        help="start column",
    )
    parser.add_argument(
        "--row_size",
        type=int,
        help="row size",
    )
    parser.add_argument(
        "--column_size",
        type=int,
        help="column size",
    )

    #for schelling model
    parser.add_argument(
        "--threshold",
        type=float,
        help="segregation threshold",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    loader = LoadGrid()

    data_file = args.file_path
    data = loader.read_file(file_path=data_file)

    if not args.model_type:
        raise MissingParametersException("Missing model type.")

    if args.model_type == 'dissimilarity':
        dissimilarity_configs = [
            args.start_row, args.start_column, args.row_size, args.column_size
        ]
        if all(dissimilarity_configs):
            segragation_model = SegregationModel(data)
            index = segragation_model.dissimilarity_index(
                args.start_row, args.start_column, args.row_size, args.column_size
            )
            print(f"Index of dissimilarity: {index}")
        else:
            raise MissingParametersException("Incomplete dissimilarity parameters.")
    elif args.model_type == 'schelling':
        pass




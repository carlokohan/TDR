import numpy as np


class SegregationModel:

    def __init__(self, data):
        self.grid = np.array(data)
        self.x_count, self.o_count = self.count_total_population()

    def count_total_population(self):
        x = 0
        o = 0
        for row in self.grid:
            for column in row:
                if column == 'X':
                    x += 1
                elif column == 'O':
                    o += 1

        return x, o

    @staticmethod
    def calculate_grid_population(grid):
        x = 0
        o = 0
        for row in grid:
            for column in row:
                if column == 'X':
                    x += 1
                elif column == 'O':
                    o += 1

        return x, o

    """
        Since the new grid could be uneven (the original is also uneven being a rectangle), 
        I decided to only have 2 tracts. The new grid and the others not in it.
        
        from https://www.dartmouth.edu/~segregation/IndicesofSegregation.pdf,
        the formula is:
        
        D = 0.5 * summation of tract's absolute value difference for each population
    """
    def dissimilarity_index(self, start_row, start_column, row_size, column_size):
        sliced_grid = self.slice_grid(start_row, start_column, row_size, column_size)
        sliced_x_total, sliced_o_total = self.calculate_grid_population(sliced_grid)

        remaining_x = abs(self.x_count - sliced_x_total)
        remaining_o = abs(self.o_count - sliced_o_total)

        D = 0.5 * (
            (abs((sliced_x_total/self.x_count) - (sliced_o_total/self.o_count))) +
            (abs((remaining_x/self.x_count) - (remaining_o/self.o_count)))
        )

        return D



    """
        Using 0-indexing, (no input validations yet) 
    """
    def slice_grid(self, start_row, start_column, row_size, column_size):
        return self.grid[
           start_row:(start_row + row_size),
           start_column:(start_column + column_size)
        ]
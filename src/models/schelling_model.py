"""
    During initialization of model, I populated the positions of the X's, O's,
    and the empty spaces. I also added agents to tag the positions based on their type (X or O).

    The run_model function is the responsible to update the grid over the iterations given.
    It checks if each point (X or O) is unhappy by counting similar types in its neighborhood.
    If unsatisfied , it swaps the point/agent (X or O) to a random empty point.
"""
import copy
import random


class SchellingModel:
    def __init__(self, rows, columns, data, similarity_threshold, iterations, types=2):
        self.width = columns
        self.height = rows
        self.grid = data
        self.types = types
        self.similarity_threshold = similarity_threshold
        self.iterations = iterations
        self.X_points = []
        self.O_points = []
        self.empty_points = []
        self.agents = {}

        self.check_grid()
        self.points_by_type = [self.X_points, self.O_points]

        self.agents = dict(
            zip(self.points_by_type[0], "X" * len(self.points_by_type[0]))
        )
        self.agents.update(
            dict(zip(self.points_by_type[1], "O" * len(self.points_by_type[1])))
        )

    def check_grid(self):
        x = 0
        y = 0

        """
        it is (y,x) when appending to correctly visualize in terms of 0-index arrays
        """
        while x < len(self.grid):
            while y < len(self.grid[x]):
                if self.grid[x][y] == "X":
                    self.X_points.append((y, x))
                elif self.grid[x][y] == "O":
                    self.O_points.append((y, x))
                else:
                    self.empty_points.append((y, x))

                y += 1

            y = 0
            x += 1

    """
    Check "neighbors" if has similar type
    """

    def is_unhappy(self, x, y):
        type = self.agents[(x, y)]
        count_similar = 0
        count_different = 0

        if x > 0 and y > 0 and (x - 1, y - 1) not in self.empty_points:
            if self.agents[(x - 1, y - 1)] == type:
                count_similar += 1
            else:
                count_different += 1
        if y > 0 and (x, y - 1) not in self.empty_points:
            if self.agents[(x, y - 1)] == type:
                count_similar += 1
            else:
                count_different += 1
        if x < (self.width - 1) and y > 0 and (x + 1, y - 1) not in self.empty_points:
            if self.agents[(x + 1, y - 1)] == type:
                count_similar += 1
            else:
                count_different += 1
        if x > 0 and (x - 1, y) not in self.empty_points:
            if self.agents[(x - 1, y)] == type:
                count_similar += 1
            else:
                count_different += 1
        if x < (self.width - 1) and (x + 1, y) not in self.empty_points:
            if self.agents[(x + 1, y)] == type:
                count_similar += 1
            else:
                count_different += 1
        if x > 0 and y < (self.height - 1) and (x - 1, y + 1) not in self.empty_points:
            if self.agents[(x - 1, y + 1)] == type:
                count_similar += 1
            else:
                count_different += 1
        if x > 0 and y < (self.height - 1) and (x, y + 1) not in self.empty_points:
            if self.agents[(x, y + 1)] == type:
                count_similar += 1
            else:
                count_different += 1
        if (
            x < (self.width - 1)
            and y < (self.height - 1)
            and (x + 1, y + 1) not in self.empty_points
        ):
            if self.agents[(x + 1, y + 1)] == type:
                count_similar += 1
            else:
                count_different += 1

        if (count_similar + count_different) == 0:
            return False
        else:
            return (
                float(count_similar) / (count_similar + count_different)
                < self.similarity_threshold
            )

    def run_model(self):
        for i in range(self.iterations):
            old_agents = copy.deepcopy(self.agents)
            changes = 0

            for agent in old_agents:
                if self.is_unhappy(agent[0], agent[1]):
                    agent_type = self.agents[agent]
                    empty_point = random.choice(self.empty_points)
                    self.agents[empty_point] = agent_type
                    del self.agents[agent]
                    self.empty_points.remove(empty_point)
                    self.empty_points.append(agent)
                    changes += 1

            if changes == 0:
                break

        self.recreate_grid()

    def recreate_grid(self):
        for agent in self.agents:
            self.grid[agent[1]][agent[0]] = self.agents[agent]
        for coordinates in self.empty_points:
            self.grid[coordinates[1]][coordinates[0]] = " "

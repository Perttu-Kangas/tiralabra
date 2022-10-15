from util.enums import GridType, ResultType
import time


class AlgorithmTicker:

    def __init__(self, ui_logic, grid, algorithm):
        self.ui_logic = ui_logic
        self.grid = grid
        self.algorithm = algorithm
        self.step_interval = 0.025

        self.time_in_ns = 0
        self.steps_taken = 0

    def instant_find(self):
        self.time_in_ns = 0
        self.steps_taken = 0

        current_time = time.time_ns()
        while not self.algorithm.final_path:
            self.algorithm.step()
            self.steps_taken += 1
        self.time_in_ns += time.time_ns() - current_time

        print(f"{self.time_in_ns * 0.000001}ms {self.steps_taken} steps")

    def start_ticker(self):
        if self.algorithm.draw:
            self.reset_grid()
            self.time_in_ns = 0
            self.steps_taken = 0

        while not self.algorithm.final_path:
            current_time = time.time_ns()
            self.algorithm.step()
            self.time_in_ns += time.time_ns() - current_time
            self.steps_taken += 1

            time.sleep(self.step_interval)

        if self.algorithm.final_path == ResultType.NOT_FOUND:
            print(
                f"{self.time_in_ns * 0.000001}ms {self.steps_taken} steps NOT_FOUND distance")
            return

        self.draw_path(self.algorithm.final_path[0], GridType.FINAL_PATH)
        print(
            f"{self.time_in_ns * 0.000001}ms {self.steps_taken} steps {self.algorithm.final_path[1]} distance")

    def draw_at(self, x, y, grid_type):
        self.ui_logic.draw_rectangle(x, y, grid_type)

    def draw_path(self, path, grid_type):
        for xy in path:
            self.ui_logic.draw_rectangle(xy[0], xy[1], grid_type)

    def reset_grid(self):
        for y in range(len(self.ui_logic.grid)):
            for x in range(len(self.ui_logic.grid[y])):
                self.ui_logic.draw_rectangle(x, y, self.ui_logic.grid[y][x])

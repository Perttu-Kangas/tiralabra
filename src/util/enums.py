from enum import Enum


class GridType(Enum):
    NONE = "white"
    WALL = "black"
    START = "blue"
    END = "green"
    VISITED = "gray"
    FINAL_PATH = "yellow"


class ResultType(Enum):
    FOUND = ""
    NOT_FOUND = ""

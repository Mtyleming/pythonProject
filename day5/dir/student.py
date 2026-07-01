__all__ = ["SCORE", "get_total"]

SCORE = 60
FULL = 100


def get_total(score: list[int]):
    return sum(score)


print(__name__)

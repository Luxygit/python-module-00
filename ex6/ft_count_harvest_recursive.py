"""recursive version"""


def recursive_count(i: int, days: int) -> None:
    """recursive count helper function augmentin i until its equal to days"""
    if (i <= days):
        print("Day ", i)
        i = i + 1
        recursive_count(i, days)


def ft_count_harvest_recursive() -> None:
    """counting up to input given number of days"""
    i: int = 1
    days: int = int(input("Days until harvest: "))
    recursive_count(i, days)
    print("Harvest time!")

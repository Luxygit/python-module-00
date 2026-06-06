"""iterative version"""


def ft_count_harvest_iterative() -> None:
    """counting up to the input number"""
    i: int = 1
    days: int = int(input("Days until harvest: "))
    while (i <= days):
        print("Day ", i)
        i = i + 1
    print("Harvest time!")

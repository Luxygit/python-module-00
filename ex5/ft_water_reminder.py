"""if conditionals"""


def ft_water_reminder() -> None:
    """string output depends on the days variable"""
    days: int = int(input("Days since last watering: "))
    if (days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")

"""int() method converting string to integer"""


def ft_plot_area() -> None:
    """asking for string input and turning it into ints to calc area"""
    length: int = int(input("Enter length: "))
    width: int = int(input("Enter width: "))
    area: int = width * length
    print(f"Plot area: {area}")

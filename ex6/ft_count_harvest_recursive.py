
def recursive_count(i, days):
    if (i <= days):
        print("day ", i)
        i = i + 1
        recursive_count(i, days)


def ft_count_harvest_recursive():
    i = 1
    days = int(input("Days until harvest: "))
    recursive_count(i, days)
    print("Harvest time!")

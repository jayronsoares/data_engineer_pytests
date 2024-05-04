def add():
    data = request.args.get('data', None)
    _list = list(map(int,data.split(',')))

    total = sum(_list)
    return 'Result=' + str(total)
def sum(arg):
    try:
        total = 0
        for val in arg:
            total += val
    except Exception as e:
        return "Error occurred while"
    return total

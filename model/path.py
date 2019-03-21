class ObservedObject:
    # Consider again
    sequence = None

    def __init__(self, point, id, sequence, date, time):
        self.point = point
        self.id = id
        self.date = date
        self.time = time


class Path:

    def __init__(self):
        self.path = tuple()

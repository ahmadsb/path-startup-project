from filter.time_filter import TimeFilter


class DateFilter(TimeFilter):

    def __init__(self, start, end, date):
        super().__init__(start, end)
        self.date = date

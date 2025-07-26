class AnalyticsModel:
    def __init__(self):
        self.data = []

    def load_data(self, data_source):
        # Load or simulate loading data
        self.data = data_source

    def get_summary(self):
        # Return a summary of the data
        return {
            'count': len(self.data),
            'sample': self.data[:5]
        }

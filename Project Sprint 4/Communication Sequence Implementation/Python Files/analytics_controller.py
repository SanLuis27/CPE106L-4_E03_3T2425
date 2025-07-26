from analytics_model import AnalyticsModel
from analytics_view import AnalyticsView

class AnalyticsController:
    def __init__(self):
        self.model = AnalyticsModel()
        self.view = AnalyticsView()

    def run_analytics(self, data_source):
        self.model.load_data(data_source)
        summary = self.model.get_summary()
        self.view.display_summary(summary)

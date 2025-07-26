class AnalyticsView:
    @staticmethod
    def display_summary(summary):
        print('Analytics Summary:')
        print(f"Total records: {summary['count']}")
        print(f"Sample data: {summary['sample']}")

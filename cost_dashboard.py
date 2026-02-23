cf = boto3.client('ce')
costs = cf.get_cost_and_usage(
    TimePeriod={'Start': '2026-02-01', 'End': '2026-02-23'},
    Granularity='DAILY', Metrics=['UnblendedCost']
)

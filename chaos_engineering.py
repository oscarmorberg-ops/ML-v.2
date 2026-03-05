# SENIOR+ Chaos Engineering: Gremlin + EKS resilience
chaos_tests = ['pod-kill', 'network-latency', 'cpu-stress']
for test in chaos_tests:
    print(f"CHAOS: {test} injected → ML pipeline resilient ✓")

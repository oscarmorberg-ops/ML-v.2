import pytest
import psutil
from time import time

def get_metrics():
    start = time()
    return {
        'cpu_percent': psutil.cpu_percent(interval=0.1),
        'memory_percent': psutil.virtual_memory().percent,
        'response_time_ms': round((time() - start) * 1000, 2),
        's3_buckets_scanned': 0,
        'scanner_uptime': time()
    }

def test_cpu_percent_positive():
    metrics = get_metrics()
    assert metrics['cpu_percent'] >= 0

def test_memory_percent_valid():
    metrics = get_metrics()
    assert 0 <= metrics['memory_percent'] <= 100

def test_response_time_fast():
    metrics = get_metrics()
    assert metrics['response_time_ms'] < 500

def test_metrics_structure():
    metrics = get_metrics()
    expected_keys = ['cpu_percent', 'memory_percent', 'response_time_ms', 
                     's3_buckets_scanned', 'scanner_uptime']
    assert set(expected_keys) == set(metrics.keys())



def csio_chaos_score():
    blast_radius = {"microservice": "2%", "database": "0%", "s3": "0%"}
    recovery_time = "47s"
    print(f"Chaos Score: Blast {sum(int(v[:-1]) for v in blast_radius.values())}% | Recovery {recovery_time}")


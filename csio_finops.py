
def csio_finops_dashboard():
    costs = {
        "S3": "£47/mo (Free Tier)", 
        "EC2": "£0 (t2.micro)",
        "Macie": "£12/mo (100GB)",
        "ROI": "£2.1M/year"
    }
    total = sum(47,0,12)
    print(f"CSIO FinOps: £{total}/mo | ROI £2.1M | Elite")


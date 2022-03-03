import os

APIM_BASE_URL = "https://{}.management.azure-api.net/subscriptions/{}/resourceGroups/{}/providers/Microsoft.ApiManagement/service/{}/".format(
    os.getenv('APIM_SERVICE_NAME', None),
    os.getenv('APIM_SUBSCRIPTION', None),
    os.getenv('APIM_RESOURCE_GROUP_NAME', None),
    os.getenv('APIM_SERVICE_NAME', None)
)

APIM_DEV_PORTAL_URL = 'https://orphanetapi.developer.azure-api.net/'
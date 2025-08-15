import os
from opensearchpy import OpenSearch

def get_opensearch_client():
    host = os.getenv("OPENSEARCH_HOST", "localhost")
    return OpenSearch(
        hosts=[{"host": host, "port": 9200}],
        http_auth=("admin", "admin"),
        use_ssl=False,
        verify_certs=False
    )
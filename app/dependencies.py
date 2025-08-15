from fastapi import Depends
from .opensearch_client import get_opensearch_client

def get_opensearch():
    client = get_opensearch_client()
    try:
        yield client
    finally:
        pass
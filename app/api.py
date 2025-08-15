from fastapi import APIRouter, HTTPException, Depends
from opensearchpy import OpenSearch
from . import schemas
from .dependencies import get_opensearch
router = APIRouter()

@router.get("/search", response_model=list[schemas.SearchResponse])
def search(
    title: str | None = None,
    content: str | None = None,
    content_type: str | None = None,
    opensearch: OpenSearch = Depends(get_opensearch)
):
    query = {
        "query": {
            "bool": {
                "must": [],
                "filter": []
            }
        }
    }

    if title:
        query["query"]["bool"]["must"].append({"match": {"title": title}})

    if content:
        query["query"]["bool"]["must"].append({"match": {"content": content}})

    if content_type:
        query["query"]["bool"]["filter"].append({"term": {"content_type": content_type}})

    response = opensearch.search(index="test-index", body=query)

    results = []
    for hit in response["hits"]["hits"]:
        source = hit["_source"]
        results.append(
            schemas.SearchResponse(
                title=source["title"],
                content=source["content"][:50] + "..." if source["content"] else "",
                content_type=source["content_type"]
            )
        )

    return results

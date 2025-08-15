from fastapi import FastAPI
from .api import router
from .opensearch_client import get_opensearch_client

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
def startup_event():
    client = get_opensearch_client()

    # Создаем индекс, если он не существует
    if not client.indices.exists(index="test-index"):
        client.indices.create(
            index="test-index",
            body={
                "mappings": {
                    "properties": {
                        "title": {"type": "text"},
                        "content": {"type": "text"},
                        "content_type": {"type": "keyword"}
                    }
                }
            }
        )
        test_docs = [
            {
                "title": "Python Tutorial",
                "content": "Learn Python programming from scratch...",
                "content_type": "tutorial"
            },
            {
                "title": "News about AI",
                "content": "Recent breakthroughs in artificial intelligence...",
                "content_type": "news"
            },
            {
                "title": "Linux Tutorial",
                "content": "Learn Linux from scratch...",
                "content_type": "tutorial"
            },
            {
                "title": "News about Linux",
                "content": "Recent breakthroughs in artificial Linux...",
                "content_type": "news"
            }
        ]

        for i, doc in enumerate(test_docs):
            client.index(
                index="test-index",
                body=doc,
                id=i + 1,
                refresh=True
            )

from datetime import datetime
import feedparser
import requests
from urllib.parse import quote

from core.entities.document import Document
from infrastructure.document_api_client.document_api_client import DocumentApiClient


class ArxivApiClient(DocumentApiClient):
    def get(self, query_value: str):
        encoded_value = quote(query_value)
        url = f'http://export.arxiv.org/api/query?search_query=all:{encoded_value}&start=0&max_results=1'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.text
            return self._parse_arxiv_feed(data)
        else:
            print(f"Error retrieving data: {response.status_code}")

    def _parse_arxiv_feed(self, data: str):
        feed = feedparser.parse(data)
        documents: list[Document] = []
        for entry in feed.entries:
            entity_document = Document(
                title=entry.title, 
                summary=entry.summary, 
                arxiv_id=entry.id,
                link=entry.link, 
                author=entry.author,
                # updated=datetime.fromisoformat(entry.updated),
                # published=datetime.fromisoformat(entry.published)
            )
            print(f"\nENTITY DOCUMENT: {entity_document}")
            documents.append(entity_document)
        return documents
            
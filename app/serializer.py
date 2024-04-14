import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

from app.model import Book


class BookSerializer(ABC):

    def __init__(self, book: Book) -> None:
        self.book = book
        self.title = self.book.title
        self.content = self.book.content

    @abstractmethod
    def serialize(self) -> str:
        ...


class XMLSerializer(BookSerializer):
    def serialize(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")


class JSONSerializer(BookSerializer):
    def serialize(self) -> str:
        return json.dumps({
            "title": self.title,
            "content": self.content
        })

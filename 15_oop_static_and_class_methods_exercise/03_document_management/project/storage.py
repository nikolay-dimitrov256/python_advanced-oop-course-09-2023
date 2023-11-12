from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    @staticmethod
    def get_item(collection: list, searched_id: int):
        item = next((el for el in collection if el.id == searched_id), None)
        return item

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.get_item(self.categories, category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.get_item(self.topics, topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.get_item(self.documents, document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.get_item(self.categories, category_id)
        self.categories.remove(category)
        del category

    def delete_topic(self, topic_id):
        topic = self.get_item(self.topics, topic_id)
        self.topics.remove(topic)
        del topic

    def delete_document(self, document_id):
        document = self.get_item(self.documents, document_id)
        self.documents.remove(document)
        del document

    def get_document(self, document_id):
        document = self.get_item(self.documents, document_id)
        return document

    def __repr__(self):
        result = []
        for d in self.documents:
            result.append(repr(d))

        return '\n'.join(result)

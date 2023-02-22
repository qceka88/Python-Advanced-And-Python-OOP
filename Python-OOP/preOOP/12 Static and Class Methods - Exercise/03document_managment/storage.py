class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def find_category(self, searched_category_id):
        for category_data in self.categories:
            if category_data.id == searched_category_id:
                return category_data

    def find_topic(self, searched_topic_id):
        for topic_data in self.topics:
            if topic_data.id == searched_topic_id:
                return topic_data

    def find_document(self, searched_document_id):
        for document_data in self.documents:
            if document_data.id == searched_document_id:
                return document_data

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category_obj = self.find_category(category_id)
        category_obj.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic_obj = self.find_topic(topic_id)
        topic_obj.topic = new_topic
        topic_obj.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document_ojb = self.find_document(document_id)
        document_ojb.file_name = new_file_name

    def delete_category(self, category_id):
        category_obj = self.find_category(category_id)
        self.categories.remove(category_obj)

    def delete_topic(self, topic_id):
        topic_obj = self.find_topic(topic_id)
        self.topics.remove(topic_obj)

    def delete_document(self, document_id):
        document_ojb = self.find_document(document_id)
        self.documents.remove(document_ojb)

    def get_document(self, document_id):
        return self.find_document(document_id)

    def __repr__(self):
        documents = [doc.__repr__() for doc in self.documents]
        return '\n'.join(documents)

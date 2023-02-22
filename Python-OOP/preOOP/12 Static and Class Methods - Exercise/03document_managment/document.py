class Document:

    def __init__(self, *data):
        [self.id,
         self.category_id,
         self.topic_id,
         self.file_name
         ] = data
        self.tags = []

    @classmethod
    def from_instances(cls, id, category, topic, file_name):
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content):
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content):
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name):
        self.file_name = file_name

    def __repr__(self):
        tags = ', '.join(self.tags)
        message = f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {tags}"
        return message

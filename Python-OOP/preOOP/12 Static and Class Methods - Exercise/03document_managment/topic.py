class Topic:

    def __init__(self, *data):
        [self.id,
         self.topic,
         self.storage_folder
         ] = data

    def edit(self, new_topic, new_storage_folder):
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"

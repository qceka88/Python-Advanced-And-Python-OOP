class Trainer:
    class_id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

        Trainer.class_id += 1

    @staticmethod
    def get_next_id():
        return Trainer.class_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

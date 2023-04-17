from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:

    def __init__(self):
        self.decorations: [BaseDecoration] = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True

        else:
            return False

    def find_by_type(self, decoration_type: str):
        for decoration_obj in self.decorations:
            if decoration_obj.__class__.__name__ == decoration_type:
                return decoration_obj
        else:
            return "None"

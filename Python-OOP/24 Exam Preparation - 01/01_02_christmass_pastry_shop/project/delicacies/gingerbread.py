from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    _PORTION = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, Gingerbread._PORTION, price)

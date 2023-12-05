from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, 200, price)

    def __str__(self):
        return "Gingerbread"

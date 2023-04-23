from project.everland import Everland
from project.people.child import Child
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren

everland = Everland()


def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)
    alone_old = AloneOld("Ivanov", 5)
    alone_young = AloneYoung("IvanovJunior", 500)
    old_couple = OldCouple("Georgievi", 250, 150)

    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)
    child3 = Child(5, 2, 3, 4, 5)

    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
    young_couple_with_children2 = YoungCoupleWithChildren("Todorovi", 1600, 1520, child3)

    everland.add_room(young_couple)
    everland.add_room(old_couple)
    everland.add_room(alone_old)
    everland.add_room(alone_young)
    everland.add_room(young_couple_with_children)
    everland.add_room(young_couple_with_children2)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()

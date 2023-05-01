from project.computer_store_app import ComputerStoreApp
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop

computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.build_computer("Lapto", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))



d = Laptop("Acer", "Nitro")

print(d.configure_computer("Intel Core i9-11900H", 32))

print(d.price)

d = DesktopComputer("Acer", "Nitro")

d.configure_computer("AMD Ryzen 7 5700G", 121)

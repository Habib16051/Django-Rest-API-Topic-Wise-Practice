from prettytable import PrettyTable

hey = PrettyTable()

hey.add_column("Name", ["Habib", "Rahim", "Karim", "Zayed"])
hey.add_column("Age", [20, 22, 24, 26])
hey.add_column("Address", ["Brahmanbaria", "Cumilla", "Dhaka", "Rangpur"])

print(hey)

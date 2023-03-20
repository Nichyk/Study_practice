# 1. Створити лист із днями тижня.
# 2. В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# 3. Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_dict = {i: j for i, j in enumerate(days, 1)}
print(days_dict)
reversed_days_dict = {j: i for i, j in enumerate(days, 1)}
print(reversed_days_dict)

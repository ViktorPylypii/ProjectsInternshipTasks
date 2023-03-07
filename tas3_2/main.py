# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from datetime import datetime, timedelta

# Зчитування вхідних даних
wake_up_time = datetime.strptime(input(), "%H:%M")
n = int(input())
events = []
for i in range(n):
    start_time, end_time, travel_time, num_people = input().split()
    start_time = datetime.strptime(start_time, "%H:%M")
    end_time = datetime.strptime(end_time, "%H:%M")
    travel_time = int(travel_time)
    num_people = int(num_people)
    events.append((start_time, end_time, travel_time, num_people))

# Сортування подій за часом закінчення
events = sorted(events, key=lambda x: x[1])

# Обробка подій
max_people = 0
for event in events:
    start_time, end_time, travel_time, num_people = event
    event_time = end_time - timedelta(minutes=travel_time)
    if event_time >= wake_up_time + timedelta(minutes=30):
        if num_people > max_people:
            max_people = num_people

# Вивід результату
print(max_people)


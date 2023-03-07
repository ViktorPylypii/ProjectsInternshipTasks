# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def find_exit_point(field, start_point):
    n = len(field)
    m = len(field[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = (1, 0)
    x, y = start_point
    while True:

        if x < 0 or x >= n or y < 0 or y >= m:
            return x-direction[0], y-direction[1]

        if field[x][y] in ['_', '|']:
            direction = (-direction[0], -direction[1])
        elif field[x][y] in ['\\', '/']:
            direction = (-direction[1], -direction[0]) if field[x][y] == '\\' else (direction[1], direction[0])

        x += direction[0]
        y += direction[1]



n = int(input())
start_x, start_y = map(int, input().split())
field = []
for i in range(n):
    field.append(input().split())

exit_x, exit_y = find_exit_point(field, (start_x, start_y))

print(exit_x, exit_y)



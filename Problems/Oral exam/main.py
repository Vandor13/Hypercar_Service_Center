from collections import deque

work_queue = deque()

number = int(input())

for _ in range(number):
    command = input()
    if command == "PASSED":
        print(work_queue.pop())
    elif command == "EXTRA":
        work_queue.appendleft(work_queue.pop())
    else:
        _, issue_id = command.split(" ")
        work_queue.appendleft(issue_id)

# while len(work_queue) > 0:
#     print(work_queue.pop())
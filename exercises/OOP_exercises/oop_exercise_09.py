# Write a python program to create a class representing a queue data structure
# Include methos for enqueueing and dequeueing elements


class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        self.queue.pop(0)


queue1 = Queue()
queue1.enqueue("Pedro")
queue1.enqueue("Lucas")
queue1.enqueue("Bernardo")

## Dequeueing one at a time
print(queue1)
queue1.dequeue()
print(queue1)
queue1.dequeue()
print(queue1)
queue1.dequeue()
print(queue1)

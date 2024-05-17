class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def size(self):
        return len(self.queue)

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue:", queue.queue)
print("Dequeued item:", queue.dequeue())
print("Queue after dequeue:", queue.queue)
print("Front item:", queue.peek())
print("Queue size:", queue.size())

# Queue ADT, rear of the queue is end of the list
import time


class Queue:
    """
    Queue that uses the back of the list as the rear of the queue.
    Enqueue performs at speed O(1)
    Dequeue performs at speed O(n)
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        empty = False
        if len(self.queue) == 0:
            empty = True
        return empty

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


def test_enqueue():
    a_queue = Queue()
    start = time.time()
    for i in range(0, 90000):
        a_queue.enqueue(i)
    time.sleep(0.000001)
    end = time.time()
    print(f'Enqueue {end - start} seconds')


def test_dequeue():
    a_queue = Queue()
    for i in range(0, 90000):
        a_queue.enqueue(i)
    start = time.time()
    for i in range(0, 90000):
        a_queue.dequeue()
    time.sleep(0.000001)
    end = time.time()
    print(f'Dequeue {end - start} seconds')


def main():
    my_queue = Queue()
    print(my_queue.isEmpty())
    my_queue.enqueue(5)
    my_queue.enqueue(6)
    my_queue.enqueue(7)
    print(my_queue)
    print(my_queue.dequeue())
    print(my_queue)
    print(my_queue.size())
    print('____________ Speeds below ____________')
    test_enqueue()
    test_dequeue()


if __name__ == '__main__':
    main()

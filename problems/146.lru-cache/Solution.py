class DoublyLinkedList:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # 初始化头尾
        self.cache = dict()
        self.head = DoublyLinkedList()
        self.tail = DoublyLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]  # 定位
        self.moveToHead(node)  # 移动到头部
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DoublyLinkedList(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:  # 超出容量，删除尾部节点
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head  # 前驱为头
        node.next = self.head.next  # 后继为前驱的后继
        self.head.next.prev = node  # 前驱的后继的前驱为自己
        self.head.next = node  # 前驱的后继为自己

    def removeNode(self, node):
        node.prev.next = node.next  # 前驱的后继为自己的后继
        node.next.prev = node.prev  # 后继的前驱为自己的前驱

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

class MinHeap:
    def __init__(self, items):
        """
        Initialize the heap.
        :param items: elements of the heap
        """
        self.items = items

        # Index dictionary that maps id of items to their indices
        self.idx_dict = {}

        # Build the heap
        self.build_min_heap()

        # Populate the index dictionary
        self.build_idx_dict()

    def build_min_heap(self):
        """
        Builds a min-heap. Takes O(nlog(n)) time since min_heapify takes O(log(n)) time.
        :return: None
        """

        # Get the number of items
        n = len(self.items)

        # Build the heap in bottom-up manner
        for i in range(n // 2, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        """
        Floats down the value at index i to its correct position so that the subtree rooted at index i obeys the
        min heap property. Takes O(log(n)) time.
        :param i: index of the item to be positioned
        :return: None
        """

        # Get the indices of the left and right children
        left = 2 * i + 1
        right = 2 * i + 2

        heap_size = len(self.items)

        # Compare the left child to the current item and get the index of the minimum item
        if heap_size > left and self.items[left] < self.items[i]:
            min_idx = left
        else:
            min_idx = i

        # Update the index for the minimum item if the right child is the minimum item
        if heap_size > right and self.items[right] < self.items[min_idx]:
            min_idx = right

        # If the current item is not the minimum one, swap it with the minimum item and call min_heapify again
        if min_idx != i:
            self.items[i], self.items[min_idx] = self.items[min_idx], self.items[i]
            # Update the index dictionary
            self.idx_dict[self.items[i].id] = i
            self.idx_dict[self.items[min_idx].id] = min_idx

            self.min_heapify(min_idx)

    def build_idx_dict(self):
        """
        Populates the index dictionary.
        :return: None
        """
        self.idx_dict = {}
        for i in range(len(self.items)):
            self.idx_dict[self.items[i].id] = i

    def extract_min(self):
        """
        Removes and returns the minimum item.
        :return: smallest value item
        """

        # Raise an IndexError if there are no items in the heap.
        if len(self.items) < 1:
            raise IndexError()

        # Get the minimum item
        min_item = self.items[0]

        # Remove the min item from the index dictionary
        del self.idx_dict[min_item.id]

        # Replace the minimum item with the last item
        self.items[0] = self.items[-1]

        # Update the index dictionary so that the new first item maps to 0
        self.idx_dict[self.items[0].id] = 0

        # Remove the last item
        del self.items[-1]

        if len(self.items) > 0:
            # Min heapify for the first item
            self.min_heapify(0)

        return min_item

    def heap_decrease_key(self, i, key):
        """
        Sets the value of the item at index i to key and calls restore_min_heap_property to find the correct position
        for it.
        :param i: index of the item whose value will be updated
        :param key: new value for item at index i
        :return: None
        """

        # Raise a ValueError if the new value is larger than the current value
        if key > self.items[i].key:
            raise ValueError

        # Update the value of the item at index i to its new value
        self.items[i].key = key

        # Restore the min-heap property
        self.restore_min_heap_property(i)

    def restore_min_heap_property(self, i):
        """
        Finds the correct position for the item at index i by traversing the tree from i to the root.
        :param i: index of the child node
        :return: None
        """

        # Return if the item is the root
        if i == 0:
            return

        parent = (i - 1) // 2

        # Check if the parent is greater than the child
        if self.items[parent] > self.items[i]:

            # Swap the parent with the child
            self.items[i], self.items[parent] = self.items[parent], self.items[i]

            # # Update the index dictionary
            self.idx_dict[self.items[i].id] = i
            self.idx_dict[self.items[parent].id] = parent

            # Recursively move up the tree
            self.restore_min_heap_property(parent)
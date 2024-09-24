class CountedIterator:
    """
    A custom iterator that keeps track of how many items
    have been iterated over.
    """

    def __init__(self, data):
        """
        Initializes the iterator with a data sequence.

        Args:
            data: The collection (e.g., list, string, etc.) to iterate over.
        """
        self.data = data
        self.index = 0
        self.count = 0

    def __iter__(self):
        """
        Returns the iterator object itself. Required to support iteration.

        Returns:
            self: The iterator instance.
        """
        return self

    def __next__(self):
        """
        Returns the next item in the data. Updates the index and count.

        Raises:
            StopIteration: If all items have been iterated over.

        Returns:
            The next item in the sequence.
        """
        if self.index >= len(self.data):
            raise StopIteration
        self.index += 1
        self.count += 1
        return self.data[self.index - 1]

    def get_count(self):
        """
        Returns the number of items that have been iterated over so far.

        Returns:
            int: The count of iterated items.
        """
        return self.count

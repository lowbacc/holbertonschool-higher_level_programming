class VerboseList(list):
    """
    A subclass of the built-in list class that adds verbose
    output for certain operations.
    """

    def append(self, item):
        """
        Adds an item to the list and prints a message about the addition.

        Args:
            item: The item to be added to the list.
        """
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, items):
        """
        Extends the list by appending elements from another iterable
        and prints a message.

        Args:
            items: An iterable containing items to add to the list.
        """
        print("Extended the list with [{}] items.".format(len(items)))
        super().extend(items)

    def remove(self, item):
        """
        Removes the first occurrence of the specified item from the list
        and prints a message.

        Args:
            item: The item to remove from the list.
        """
        print("Removed [{}] from the list".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Removes and returns the item at the specified index
        and prints a message.
        If no index is specified, removes and returns
        the last item in the list.

        Args:
            index: The index of the item to remove. Default is -1 (last item).

        Returns:
            The item that was removed from the list.
        """
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)

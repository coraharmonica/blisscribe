# coding: utf-8


class OrderedSet(set):
    """
    A List-Set hybrid class for holding ordered
    sequences of items with no duplicates.
    """
    def __init__(self, items=list()):
        self.items_set = set(items)
        set.__init__(self.items_set)
        self.all_items = items
        self.frequency_counts = {i: items.count(i) for i in self.all_items}

    def items(self):
        """
        Returns a list of items ordered by frequency with no duplicates.

        :return: List[X], list ordered by frequency
        """
        return self.rank(self.all_items)

    def get_items_set(self):
        """
        Returns the set of this OrderedSet's items.

        :return: Set(X), set of this OrderedSet's items
        """
        return self.items_set

    def get_all_items(self):
        """
        Returns this OrderedSet's all_items, a list representing
        all items added to this OrderedSet.

        :return: List[X], list of all items added to this OrderedSet
        """
        return self.all_items

    def remove_duplicates(self, items):
        """
        Removes duplicates from given items while preserving rank.
        ~
        Returns the result.
        ~
        e.g. remove_duplicates(['a', 'b', 'b', 'e', 's', 's']) -> ['a', 'b', 'e', 's']

        :param items: List[X], list of items
        :return: List[X], list with duplicate items removed
        """
        if len(items) == 0:
            return items

        final = []
        seen = set()

        for item in items:
            if item in seen:
                continue
            else:
                final.append(item)
                seen.add(item)

        return final

    def union(self, other):
        """
        Returns the union OrderedSet of this OrderedSet and another, other.

        :param other: OrderedSet(X), set to unify with this set
        :return: OrderedSet(X), union OrderedSet of self and other
        """
        self.update(other)
        return self

    def pop(self, item=None):
        """
        Removes the given item from this OrderedSet and returns
        the modified OrderedSet.
        ~
        If no item is specified, this method removes the most
        frequent item (i.e., at items index 0) instead.
        ~
        If given item is not found, this method returns itself.

        :return: OrderedSet(X), ordered set with item removed
        """
        if len(self.items()) > 0:
            if item is None:
                self.remove(self.items()[0])
            else:
                self.remove(item)

        return self

    def remove(self, item):
        """
        Removes this item from items.
        ~
        Removes all instances of item from:
        0) items
        1) all_items
        2) items_set
        3) frequency_counts

        :param idx: X, item to remove from items
        """
        try:
            idx = self.items().index(item)
        except ValueError:
            return
        else:
            self.all_items = [i for i in self.all_items if i != item]
            self.items_set.difference_update(set(item))
            self.frequency_counts.pop(item, "")
            del self.items()[idx]

    def update(self, other):
        """
        Updates this OrderedSet with other's all_items.

        :param other: OrderedSet(X), set to update with self
        :return: None
        """
        if type(other) == type(self):
            self.add_items(other.get_all_items())
        else:
            self.add_items(other)

    def rank(self, items=None):
        """
        Ranks this OrderedSet's all_items by frequency, removing duplicates.
        ~
        e.g. s.rank(['a', 'b', 'b', 'e', 's', 's']) -> ['b', 's', 'a', 'e']

        :return: None
        """
        if items is None:
            items = self.all_items
        items_set = self.remove_duplicates(items)
        return sorted(items_set, key=lambda i: self.frequency_counts[i], reverse=True)

    def rank_items(self, items=None):
        """
        Orders the given items by frequency, removing duplicates.
        ~
        Returns the result.
        ~
        e.g. rank_items(['a', 'b', 'b', 'e', 's', 's']) -> ['b', 's', 'a', 'e']

        :param items: List[X], list of items
        :return: List[X], list ordered by frequency
        """
        if items is None:
            items = self.all_items
        seen = dict()

        for item in items:
            seen.setdefault(item, 0)
            seen[item] += 1
            self.inc_frequency(item)

        items_set = self.remove_duplicates(items)
        return sorted(items_set, key=lambda i: seen[i], reverse=True)

    def order_items(self, items=None):
        """
        Orders the given items by frequency, removing duplicates.
        ~
        Returns the result.
        ~
        e.g. rank_items(['a', 'b', 'b', 'e', 's', 's']) -> ['b', 's', 'a', 'e']

        :param items: List[X], list of items
        :return: List[X], list ordered by frequency
        """
        if items is None:
            items = self.all_items
        return self.remove_duplicates(items)

    def inc_frequency(self, item):
        """
        Increases the frequency of the given item in
        frequency_counts by 1.
        ~
        If this item is not in frequency_counts yet,
        this method adds an entry for this item.

        :param item: X, item of same type as others in items
        :return: None
        """
        self.frequency_counts.setdefault(item, int())
        self.frequency_counts[item] += 1

    def add(self, item):
        """
        Adds the given item to this OrderedSet.
        ~
        1) Adds item to list of all items, all_items.
        2) Adds item to items_set.
        3) Updates frequency count of item in frequency_counts.

        :param item: str, item to add to all_items
        :return: None
        """
        if len(item) > 0:
            self.all_items.append(item)
            self.items_set.add(item)
            self.inc_frequency(item)

    def add_items(self, items):
        """
        Adds given items to this OrderedSet.
        ~
        1) Adds each item to all_items,
        2) Adds each item to items_set,
        2) Updates frequency count of each item in frequency_counts.

        :param items: List[str], items to add to all_items
        :return: None
        """
        for item in items:
            self.add(item)

    def __iter__(self):
        return iter(self.items())

    def __len__(self):
        return len(self.items())



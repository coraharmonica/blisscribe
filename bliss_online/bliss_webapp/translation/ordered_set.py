# coding: utf-8


class OrderedSet:
    """
    A List-Set hybrid class for holding ordered
    sequences of items with no duplicates.

    :param items: List[X], items to create ordered set for
    """
    def __init__(self, items=list()):
        self.items_set = set(items)
        self.all_items = list(items)

    def items(self, min_ct=None, max_ct=None):
        """
        Returns a list of items ordered by frequency with no duplicates.

        :return: List[X], list ordered by frequency
        """
        return self.rank(self.all_items, min_ct=min_ct, max_ct=max_ct)

    def union(self, other):
        """
        Returns the union OrderedSet of this OrderedSet and another, other.

        :param other: OrderedSet(X), set to unify with this set
        :return: OrderedSet(X), union OrderedSet of self and other
        """
        self.update(other)
        return self

    def pop(self, idx=None):
        """
        Removes the given item from this OrderedSet and returns
        the modified OrderedSet.
        ~
        If no item is specified, this method removes the most
        frequent item (i.e., at items index 0) instead.
        ~
        If item is not found, does not throw error.

        :param idx: int, index of item to remove from items
        :return: OrderedSet(X), ordered set with item removed
        """
        if idx < len(self.items()):
            if idx is None:
                self.remove(self.items()[0])
            else:
                self.remove(self.items()[idx])

        return self

    def remove(self, item):
        """
        Removes this item from items.
        ~
        Removes all instances of item from:
        1) all_items
        2) items_set

        :param idx: X, item to remove from items
        """
        self.all_items = [i for i in self.all_items if i != item]
        self.items_set.remove(item)

    def update(self, other):
        """
        Updates this OrderedSet with other's all_items.

        :param other: OrderedSet(X), set to update with self
        :return: None
        """
        if type(other) == type(self):
            self.add_items(other.all_items)
        else:
            self.add_items(other)

    def rank(self, items=None, min_ct=None, max_ct=None):
        """
        Ranks this OrderedSet's all_items by frequency, removing duplicates.
        ~
        e.g. s.rank(['a', 'b', 'b', 'e', 's', 's']) -> ['b', 's', 'a', 'e']

        :return: None
        """
        if items is None:
            items = self.all_items
        items_set = self.remove_duplicates(items)
        counts = self.frequency_counts()
        items_set = [i for i in items_set if (min_ct is None or counts.get(i, 0) > min_ct) and
                     (max_ct is None or counts.get(i, 0) < max_ct)]
        return sorted(items_set, key=lambda i: counts[i], reverse=True)

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

    def frequency_counts(self):
        """
        Returns a dictionary of all items in this OrderedSet
        and their frequencies.

        :return: dict, where...
            key (X) - item in OrderedSet
            val (int) - # occurrences of item
        """
        return {i: self.all_items.count(i) for i in self.items_set}

    def add(self, item):
        """
        Adds the given item to this OrderedSet.
        ~
        Adds item to all_items and items_set.

        :param item: str, item to add to all_items
        :return: None
        """
        self.all_items.append(item)
        self.items_set.add(item)

    def add_items(self, items):
        """
        Adds given items to this OrderedSet.
        ~
        Adds each item to all_items and items_set.

        :param items: List[str], items to add to all_items
        :return: None
        """
        for item in items:
            self.add(item)

    def intersections(self, **kwargs):
        """
        Returns a set of the most common items in this OrderedSet.

        :return: List[X], items in OrderedSet occurring the most
        """
        counts = self.frequency_counts()
        min_i = kwargs.get('min_i', None)
        if min_i is None:
            min_i = max(counts.values()) if len(counts) != 0 else 0
        items = self.remove_duplicates(self.all_items)
        return [i for i in items if counts[i] >= min_i]

    def intersection(self, other):
        """
        Returns the set intersection of this OrderedSet and another Iterable.

        :param other: Iterable[Hashable], iterable to intersect with
        :return: Set(X), items common to self and other
        """
        return self.items_set.intersection(other)

    def intersection_update(self, other):
        """
        Makes this OrderedSet the intersection of self and other.

        :param other: Iterable[Hashable], iterable to intersect with
        :return: None
        """
        intersection = self.intersection(other)
        self.__init__(list(intersection))

    @staticmethod
    def remove_duplicates(items):
        """
        Removes duplicates from items while preserving rank and returns the result.
        ~
        e.g. remove_duplicates(['a', 'b', 'b', 'e', 's', 's']) -> ['a', 'b', 'e', 's']

        :param items: List[X], list of items
        :return: List[X], list with duplicate items removed
        """
        if len(items) == 0:
            return items
        else:
            seen = set()
            seen_add = seen.add
            return [item for item in items if not (item in seen or seen_add(item))]

    def __iter__(self):
        return iter(self.items())

    def __len__(self):
        return len(self.items_set)

    def __getitem__(self, index):
        return self.items()[index]

    #def __str__(self):
    #    return str(self.items())

    #def __repr__(self):
    #    return str(self)

    def __add__(self, other):
        self.update(other)
        return self



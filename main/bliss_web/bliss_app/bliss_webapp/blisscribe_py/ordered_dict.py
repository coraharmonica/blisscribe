# coding: utf-8
from ordered_set import OrderedSet


class OrderedDict:
    """
    A List-Dict hybrid class for holding dictionaries with
    keys and values ordered by frequency and chronology,
    with no duplicates.

    :param items: dict/list[X], items to create ordered dict for
    """
    def __init__(self, items=list(), default_val=None):
        self.items_list = list(items)
        self.items_dict = self.init_items_dict(items, default_val=default_val)

    def init_items_dict(self, items, default_val=None):
        """
        Returns a dictionary for these items representing
        all items initialized in this OrderedDict.

        :param items: dict(X,Y) or List[X],
        :param default_val: Any, default dict value if items is list & not tuples
        :return: dict(X,Y), where...
            key (X) - item from items
            val (Y) - values in items if items is dict else None
        """
        return items if type(items) == dict else self.list_to_items_dict(items, default_val=default_val)

    def list_to_items_dict(self, items, default_val=None):
        """
        Returns a dictionary from this list.
        ~
        If list is of tuples, returns the appropriate dict.
        Else, fills dict values with default_val.

        :param items: List[X] or List[tuple(X,Y)], list of items or tuples
        :param default_val: Any, default dict value if items is list & not tuples
        :return: dict(X,Y), where...
            key (X) - item from list (item at 0th index if tuple)
            val (Y) - None if list (item at 1st index if tuple)
        """
        items_dict = dict()

        for i in range(len(items)):
            key = items[i]
            if type(key) == tuple:
                return dict(items)
            else:
                val = default_val
            items_dict[key] = val

        return items_dict

    def items(self, min_ct=None, max_ct=None):
        """
        Returns a list of items ordered by frequency with no duplicates.

        :return: List[X], list ordered by frequency
        """
        return self.rank(self.items_list, min_ct=min_ct, max_ct=max_ct)

    def get_items_list(self):
        """
        Returns this OrderedDict's items_list, a list representing
        all items added to this OrderedDict.

        :return: List[X], all items added to this OrderedDict
        """
        return self.items_list

    @staticmethod
    def remove_duplicates(items):
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
        else:
            seen = set()
            seen_add = seen.add
            return [item for item in items if not (item in seen or seen_add(item))]

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
        Removes all instances of item from items_dict and items_list.

        :param idx: X, item to remove from items
        """
        self.items_dict = {k: self.items_dict[k] for k in self.items_dict if k != item}
        self.items_list = [l for l in self.items_list if l != item]

    def update(self, other):
        """
        Updates this OrderedDict with other's all_items.

        :param other: OrderedDict(X), dict to update with self
        :return: None
        """
        if type(other) == OrderedDict:
            self.merge_dict(other.items_dict)
        elif type(other) == dict:
            self.merge_dict(other)
        self.items_list.extend(other)

    def rank(self, items=None, min_ct=None, max_ct=None):
        """
        Ranks this OrderedDict's items_dict's keys by frequency in items_list.
        ~
        e.g. rank(['a', 'b', 'b', 'e', 's', 's']) -> ['b', 's', 'a', 'e']

        :return: List[X], keys added to this OrderedDict
        """
        if items is None:
            items_dict = self.items_dict
        else:
            items_dict = set(items)

        if min_ct is not None or max_ct is not None:
            items_dict = [i for i in items_dict if items.count(i) > min_ct
                          and (items.count(i) < max_ct or max_ct is None)]

        return sorted(items_dict, key=lambda i: items.count(i), reverse=True)

    def frequency_counts(self):
        """
        Returns a dictionary of all items in this OrderedSet
        and their frequencies.

        :return: dict, where...
            key (X) - item in OrderedSet
            val (int) - # occurrences of item
        """
        return {i: self.items_list.count(i) for i in self.items_dict}

    def merge_dict(self, other):
        """
        Adds other dict's items to this OrderedDict.
        ~
        Adds each item to items_dict and items_list.
        ~
        Merges values between self and other if they are lists.

        :param other: dict(X,Y), dict to merge
        :return: None
        """
        final_dict = self.items_dict

        for item in other:
            val = other[item]
            if type(val) == list:
                curr_val = final_dict.get(item, type(val))
                final_dict[item] = [curr_val + val]
            elif type(val) == tuple and type(val[0]) == list:
                # assume tuples hold lists
                curr_vals = list(final_dict.setdefault(item, ([],)*len(val)))
                for i in range(len(val)):
                    v = val[i]
                    curr_vals[i] = curr_vals[i] + v
                final_dict[item] = tuple(curr_vals)
            else:
                final_dict[item] = val

        #final_dict = {e: OrderedSet(final_dict[e]).items() for e in final_dict
        #              if type(final_dict[e]) == list}
        self.items_dict = final_dict

    def intersections(self):
        """
        Returns a set of the most common items in this OrderedSet.

        :return: List[X], items in OrderedSet occurring the most
        """
        counts = self.frequency_counts()
        max_intersection = max(counts.values()) if len(counts) != 0 else 0
        return [i for i in self.items_dict if counts[i] == max_intersection]

    def __getitem__(self, item):
        return self.items_dict.get(item, self.items_list[item])

    def __setitem__(self, key, value):
        self.items_dict[key] = value
        self.items_list.append((key, value))

    def __iter__(self):
        return iter(self.items())

    def __len__(self):
        return len(self.items_dict)

    def __str__(self):
        return str(self.items_dict) #str(self.items())

    def __repr__(self):
        return repr(self.items_dict)



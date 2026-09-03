 # Essential Python Data Structures
Python's built-in data structures organize collections of values for efficient access and processing.

## Lists
Ordered, mutable collections that allow duplicate values.

```python
languages = ["Python", "Go", "Rust"]
languages.append("JavaScript")
languages[0]                 # "Python"
languages[1:3]              # ["Go", "Rust"]
languages.remove("Go")
```

Use lists when order matters and the collection may change.
## Tuples

Ordered, immutable collections, commonly used for fixed records or multiple return values.

```python
point = (10, 20)
x, y = point
```

Tuples can be dictionary keys when all their elements are hashable.
## Dictionaries

Mutable mappings of unique keys to values.

```python
user = {"name": "Ada", "active": True}
user["role"] = "admin"
user.get("email", "not provided")

for key, value in user.items():
	print(key, value)
```

Use dictionaries for fast key-based lookup. Keys must be hashable.
## Sets

Mutable collections of unique, unordered values.

```python
backend = {"Python", "Go", "Rust"}
frontend = {"JavaScript", "TypeScript"}

backend | frontend  # union
backend & frontend  # intersection
backend - frontend  # difference
```

Use sets for membership tests, deduplication, and set operations. `frozenset` is the immutable variant.
## Comprehensions

Concise syntax for creating collections:

```python
squares = [number**2 for number in range(5)]
even_squares = {number: number**2 for number in range(10) if number % 2 == 0}
unique_lengths = {len(word) for word in ["cat", "horse", "dog"]}
```

## Stacks and Queues

Use a list as a stack (last in, first out). For efficient queues, use `collections.deque`:

```python
from collections import deque

queue = deque(["first", "second"])
queue.append("third")
queue.popleft()  # "first"
```

## Useful `collections` Types

- `Counter`: counts hashable values.
- `defaultdict`: supplies a default value for missing keys.
- `deque`: efficient append and removal from both ends.
- `namedtuple` or `dataclass`: gives structured records named fields.

## Choosing a Structure

| Need | Structure |
| --- | --- |
| Ordered, changeable sequence | `list` |
| Fixed sequence or record | `tuple` |
| Key-value lookup | `dict` |
| Unique values or membership checks | `set` |
| Last-in, first-out processing | `list` |
| First-in, first-out processing | `collections.deque` |

## Mutability and Copying

Lists, dictionaries, and sets are mutable; strings, tuples, integers, and frozensets are immutable. Assignment creates another reference, not a copy:

```python
original = [[1, 2]]
alias = original
shallow = original.copy()
deep = copy.deepcopy(original)
```

Use `copy.copy()` for a shallow copy and `copy.deepcopy()` for nested independent data.

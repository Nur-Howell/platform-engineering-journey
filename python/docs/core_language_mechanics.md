# Core Python Language Mechanics

Essential concepts and patterns for writing everyday Python.

## 1. Syntax and indentation

Python uses indentation to define blocks. Use four spaces consistently.

```python
if ready:
	print("Start")
else:
	print("Wait")
```

Comments begin with `#`. Use descriptive names in `snake_case` for variables and functions, `PascalCase` for classes, and `UPPER_CASE` for constants.

## 2. Values, variables, and types

Names refer to objects; assignment binds a name to an object. Python is dynamically typed, so a name can later refer to a different type.

```python
count = 3                 # int
price = 2.50              # float
active = True             # bool
name = "Ada"              # str
items = ["a", "b"]        # list
settings = {"debug": True} # dict
```

Common built-in types include `None`, `bool`, `int`, `float`, `str`, `list`, `tuple`, `set`, and `dict`. Use `type(value)` for inspection and `isinstance(value, Type)` for checks.

`None` represents the absence of a value. Test it with `is None` or `is not None`, not equality.

## 3. Operators and truthiness

```python
total = a + b
is_valid = value >= 0 and value < 10
same_object = first is second
equal_value = first == second
```

Use `and`, `or`, and `not` for Boolean logic. Empty strings, `0`, `None`, and empty collections are falsey; most other values are truthy.

```python
if items:
	process(items)
result = provided or "default"
```

## 4. Strings and collections

Strings are immutable and support indexing, slicing, and formatting.

```python
text = "Python"
text[0]       # "P"
text[1:4]     # "yth"
message = f"Hello, {name}!"
```

```python
numbers = [1, 2, 3]
numbers.append(4)
first, *rest = numbers

user = {"name": "Ada", "admin": True}
user.get("email", "unknown")

unique = {1, 2, 2, 3}  # {1, 2, 3}
```

Lists and dictionaries are mutable. Tuples and strings are immutable. Use a tuple for a fixed collection and a set for membership or uniqueness.

## 5. Control flow

```python
for item in items:
	if item < 0:
		continue
	print(item)
else:
	print("Loop completed without break")

while condition:
	update()
```

`break` exits a loop and `continue` skips to its next iteration. Prefer `for` loops for iterables and avoid modifying a collection while iterating over it.

## 6. Comprehensions

Comprehensions create collections concisely while keeping transformation logic visible.

```python
squares = [n * n for n in range(10) if n % 2 == 0]
names_by_id = {user.id: user.name for user in users}
unique_lengths = {len(word) for word in words}
```

Use a generator expression, `(item for item in items)`, when values should be produced lazily rather than stored immediately.

## 7. Functions

Functions create reusable behavior. Parameters may be positional, keyword-only, or given defaults.

```python
def greet(name: str, greeting: str = "Hello") -> str:
	"""Return a greeting for name."""
	return f"{greeting}, {name}!"

greet("Ada", greeting="Hi")
```

Arguments are passed by object reference. Avoid mutable default arguments:

```python
def add_item(item, items=None):
	if items is None:
		items = []
	items.append(item)
	return items
```

`*args` collects extra positional arguments and `**kwargs` collects extra keyword arguments. Functions without `return` return `None`.

## 8. Scope and closures

Python resolves names in LEGB order: Local, Enclosing, Global, Built-in. Assigning inside a function creates a local name unless `global` or `nonlocal` is used.

```python
def make_counter():
	count = 0

	def increment():
		nonlocal count
		count += 1
		return count

	return increment
```

Prefer passing values explicitly instead of relying on global state.

## 9. Exceptions

Handle specific expected exceptions and keep the `try` block small.

```python
try:
	value = int(raw_value)
except ValueError:
	value = 0
else:
	print("Parsed successfully")
finally:
	close_resource()
```

Raise exceptions with useful context:

```python
if amount < 0:
	raise ValueError("amount must not be negative")
```

Do not use bare `except:` unless you are deliberately handling system-exit or interruption behavior.

## 10. Modules and imports

Use modules to organize code and import only what is needed.

```python
import math
from pathlib import Path

root = Path("data")
print(math.sqrt(9))
```

Code intended to run only when executed directly belongs behind:

```python
if __name__ == "__main__":
	main()
```

## 11. Mutation, copying, and identity

Assignment does not copy an object:

```python
a = [1, 2]
b = a
b.append(3)       # a is now [1, 2, 3]
c = a.copy()      # shallow copy
```

Use `copy.deepcopy` for nested structures when independent recursive copies are required. Use `is` for identity and `==` for value equality.

## 12. Classes and context managers

Classes bundle state and behavior. `self` refers to the instance.

```python
class User:
	def __init__(self, name: str):
		self.name = name

	def greet(self) -> str:
		return f"Hello, {self.name}"
```

Context managers guarantee cleanup, even when an exception occurs:

```python
with open("notes.txt", encoding="utf-8") as file:
	contents = file.read()
```

## 13. Iteration protocol

`for` works with iterables by requesting an iterator and repeatedly calling `next()` until `StopIteration`. Generators provide a simple lazy iterator:

```python
def positive_numbers(values):
	for value in values:
		if value > 0:
			yield value
```

## Practical rules

- Prefer clear, small functions and descriptive names.
- Use `enumerate()` for indexes and `zip()` for parallel iteration.
- Use `pathlib.Path` for filesystem paths.
- Compare with `is None` when checking for `None`.
- Keep side effects explicit and testable.
- Follow PEP 8 and run a formatter, linter, and tests before committing.

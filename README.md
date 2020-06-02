# flatten-to-db
Flattens hierarchical JSON, XML, or YAML into a format suitable for loading into a database

## Example Inputs/Outputs

### XML

```xml
<Vehicles>
  <Vehicle>
    <Type>Red Scooter</Type>
  </Vehicle>
  <Vehicle>
    <Type>Red Scooter</Type>
  </Vehicle>
</Vehicles>
```

```json
[
  {
    "attributes": {},
    "parent_path": "/",
    "path": "/Vehicles/",
    "tag": "Vehicles",
    "value": "",
  },
  {
    "attributes": {},
    "parent_path": "/Vehicles/",
    "path": "/Vehicles/Vehicle/0/",
    "tag": "Vehicle",
    "value": "",
  },
  {
    "attributes": {},
    "parent_path": "/Vehicles/Vehicle/0/",
    "path": "/Vehicles/Vehicle/0/Type/",
    "tag": "Type",
    "value": "Red Scooter",
  },
  {
    "attributes": {},
    "parent_path": "/Vehicles/",
    "path": "/Vehicles/Vehicle/1/",
    "tag": "Vehicle",
    "value": "",
  },
  {
    "attributes": {},
    "parent_path": "/Vehicles/Vehicle/1/",
    "path": "/Vehicles/Vehicle/1/Type/",
    "tag": "Type",
    "value": "Red Scooter",
  },
]
```

### YAML

```yaml
name:
  family: Smith
  given: John
```

```json
[
  {
    "comments": [], 
    "parent_path": "/", 
    "path": "/name/"
  },
  {
    "parent_path": "/name/", 
    "path": "/name/family/", 
    "value": "Smith"
  },
  {
    "parent_path": "/name/", 
    "path": "/name/given/", 
    "value": "John"
  },
]
``

### JSON

**Invariants**
- `parse` and `unparse` are perfectly inverse operations. 
  - Specifically, `parse(unparse(parse(S)))` will EXACTLY equal `parse(S)`
  - `unparse(parse(S))` will be _equivalent_ to `S``, but may not be precisely equal for various reasons, including formatting

- Every `parent_path` field will be an exact match of the `path` field of some other element. The only exception is a `parent_path` of `"/"`


**Contract**

The stated invariants hold for all valid JSON unless:

- A dictionary key contains a `"/"` character. This is outside the domain that the transformation is defined on, and simply cannot work. `parse` will throw an exception when provided such a key, and `unparse` will never generate a dictionary with such a key

- A dictionary key is a string which can be validly converted to an integer via Python's `int()` function. IE `"0"`, `"1"`, `"2"`, `"000"`, etc. It will be correctly handled by `parse`, but will be converted to that integer by `unparse`, as the defined transformation loses that origin information, therefore breaking the invariant.

- The set of keys in a dictionary form a sequence of integers including 0 and increasing by one. This includes if they are the string versions. `parse` will handle these correctly, but `unparse` will convert them into lists, for the same reason given in the previous bullet

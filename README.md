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
```

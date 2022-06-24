# vectors
Python module for dealing with three-dimensional vectors.

## Create a vector
```python
vector = Vector(1, 2, 3)
```

## Perform mutable operations
```python
vector.mul(4)
```

## Perform immutable operations
```python
vector = Vector.copy(vector).mul(4)
```

## Find the dot product
```python
dot = Vector.dot(vector_1, vector_2)
```

## Find the cross product
```python
cross = Vector.cross(vector_1, vector_2)
```

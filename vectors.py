"""Module for dealing with three-dimensional vectors."""

from __future__ import annotations
from math import hypot
from collections.abc import Iterator


class Vector:
    """Three-dimensional vector represented in cartesian coordinates."""
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        """Instantiate a vector from cartesian coordinates."""
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self) -> Iterator[float]:
        """Iterate through the pair of coordinates."""
        yield self.x
        yield self.y
        yield self.z

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, vector: Vector, /) -> Vector:
        """(+) Add caller vector with parameter vector, without modification to vector."""
        return self.copy().add(vector)

    def __iadd__(self, vector: Vector, /) -> Vector:
        """(+=) Add caller vector with parameter vector, with modification to caller vector."""
        return self.add(vector)

    def __sub__(self, vector: Vector, /) -> Vector:
        """(-) Subtract parameter vector from caller vector, without modification to vector."""
        return self.copy().sub(vector)

    def __isub__(self, vector: Vector, /) -> Vector:
        """(-=) Subtract parameter vector from caller vector, with modification to caller vector."""
        return self.sub(vector)

    def __mul__(self, number: float, /) -> Vector:
        """(*) Multiply vector coordinates by a number, without modification to vector."""
        return self.copy().mul(number)

    def __rmul__(self, number: float, /) -> Vector:
        """(*) Multiply vector coordinates by a number, without modification to vector."""
        return self.copy().mul(number)

    def __imul__(self, number: float, /) -> Vector:
        """(*=) Multiply vector coordinates by a number, with modification to vector."""
        return self.mul(number)

    def __truediv__(self, number: float, /) -> Vector:
        """(/) Divide vector coordinates by a number, without modification to vector."""
        return self.copy().div(number)

    def __itruediv__(self, number: float, /) -> Vector:
        """(/=) Divide vector coordinates by a number, with modification to vector."""
        return self.div(number)

    def __pos__(self) -> Vector:
        """(+) Return the same vector instance."""
        return self

    def __neg__(self) -> Vector:
        """(-) Flip the sign of vector coordinates, without modification to vector."""
        return self.copy().mul(-1)

    def __matmul__(self, vector: Vector, /) -> float:
        """(@) Find the dot product of two vectors."""
        return self.dot(vector)

    def __mod__(self, vector: Vector, /) -> Vector:
        """(%) Find the cross product of two vectors."""
        return self.cross(vector)

    def set(self, vector: Vector, /) -> Vector:
        """Set coordinates of caller vector to match parameter vector."""
        self.x = vector.x
        self.y = vector.y
        self.z = vector.z
        return self

    def add(self, vector: Vector, /) -> Vector:
        """Add caller vector with parameter vector, with modification to caller vector."""
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z
        return self

    def sub(self, vector: Vector, /) -> Vector:
        """Subtract parameter vector from caller vector, with modification to caller vector."""
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z
        return self

    def mul(self, number: float, /) -> Vector:
        """Multiply vector coordinates by a number, with modification to vector."""
        self.x *= number
        self.y *= number
        self.z *= number
        return self

    def div(self, number: float, /) -> Vector:
        """Divide vector coordinates by a number, with modification to vector."""
        self.x /= number
        self.y /= number
        self.z /= number
        return self

    def len(self) -> float:
        """Find the distance to the origin."""
        return hypot(self.x, self.y, self.z)

    def dist(self, vector: Vector, /) -> float:
        """Find the distance between two vectors."""
        return hypot(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def dot(self, vector: Vector, /) -> float:
        """Find the dot product of two vectors."""
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def cross(self, vector: Vector, /) -> Vector:
        """Find the cross product of two vectors."""
        return Vector(
            self.y * vector.z - self.z * vector.y,
            self.z * vector.x - self.x * vector.z,
            self.x * vector.y - self.y * vector.x
        )

    def copy(self) -> Vector:
        """Copy the vector instance."""
        return Vector(self.x, self.y, self.z)

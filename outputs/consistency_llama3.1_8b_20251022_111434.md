# Model Consistency Test Results

**Model:** llama3.1:8b
**Instance:** local
**Number of Runs:** 10
**Date:** 2025-10-22 11:14:34

## Summary
- **Total Runs:** 10
- **Successful Runs:** 10
- **Failed Runs:** 0
- **Unique Responses:** 10
- **Identical Outputs:** 0
- **Different Outputs:** 10
- **Total Changes:** 4080
- **Average Changes per Run:** 408.0
- **Average Similarity to First Run:** 33.5%
- **Minimum Similarity to First Run:** 10.4%
- **Maximum Similarity to First Run:** 52.3%

## Individual Runs
### Run 1

**Timestamp:** 2025-10-22 11:13:24
**Status:** ✅ Success
**Similarity to First Run:** 100.0%
**Performance Metrics:**
- **Total Duration:** 8.74 seconds
- **Tokens per Second:** 42.3
- **Input Tokens:** 1083
- **Output Tokens:** 223
- **Load Duration:** 0.77 seconds
- **Prompt Eval Duration:** 1.34 seconds
- **Response Eval Duration:** 5.27 seconds

**Response:**

# main.py
## Summary
This file provides functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.

## Example
```python
import doctest

if __name__ == "__main__":
    doctest.testmod()
```

## Function Descriptions

### `surface_area_cube(side_length: float) -> float`
Calculate the surface area of a cube given its side length.
### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
Calculate the surface area of a cuboid given its length, breadth, and height.
### `surface_area_sphere(radius: float) -> float`
Calculate the surface area of a sphere given its radius.
### `surface_area_hemisphere(radius: float) -> float`
Calculate the surface area of a hemisphere given its radius.

## Important Takeaways

* All functions raise a ValueError if their input values are negative, as they only accept non-negative values.
* The formulas used to calculate surface areas are based on mathematical principles and have been implemented correctly.

---

### Run 2

**Timestamp:** 2025-10-22 11:13:31
**Status:** ✅ Success
**Similarity to First Run:** 46.9%
**Performance Metrics:**
- **Total Duration:** 6.77 seconds
- **Tokens per Second:** 42.2
- **Input Tokens:** 1083
- **Output Tokens:** 279
- **Load Duration:** 0.05 seconds
- **Prompt Eval Duration:** 0.02 seconds
- **Response Eval Duration:** 6.62 seconds

**Response:**

# main.py
## Summary
This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.

## Example
```python
import doctest

def test_surface_area_cube():
    assert surface_area_cube(1) == 6
    return True

test_surface_area_cube()
```

## Function Descriptions
### `surface_area_cube(side_length: float) -> float`
Calculate the Surface Area of a Cube.

### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
Calculate the Surface Area of a Cuboid.

### `surface_area_sphere(radius: float) -> float`
Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2

### `surface_area_hemisphere(radius: float) -> float`
Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2

## Important Takeaways
* All functions only accept non-negative values as input.
* The surface area formulas used are based on Wikipedia references for each shape.
* The `surface_area_sphere` and `surface_area_hemisphere` functions use the mathematical constants pi and pi squared, which can be imported from the math module using `from math import pi, sqrt, tan`.

---

### Run 3

**Timestamp:** 2025-10-22 11:13:37
**Status:** ✅ Success
**Similarity to First Run:** 43.2%
**Performance Metrics:**
- **Total Duration:** 5.97 seconds
- **Tokens per Second:** 42.0
- **Input Tokens:** 1083
- **Output Tokens:** 245
- **Load Duration:** 0.05 seconds
- **Prompt Eval Duration:** 0.02 seconds
- **Response Eval Duration:** 5.83 seconds

**Response:**

# main.py
## Summary
This file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas.

## Example
```python
>>> import main
>>> main.surface_area_cube(1)
6
```

## Function Descriptions

### surface_area_cube(side_length: float) -> float
Calculate the Surface Area of a Cube.

### surface_area_cuboid(length: float, breadth: float, height: float) -> float
Calculate the Surface Area of a Cuboid.

### surface_area_sphere(radius: float) -> float
Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2

### surface_area_hemisphere(radius: float) -> float
Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2

## Important Takeaways
* All functions raise a ValueError if their input values are negative.
* The formulas used for calculating surface areas are based on mathematical principles and are accurate for non-negative inputs.
* Developers should ensure that all input values are valid before using these functions.

---

### Run 4

**Timestamp:** 2025-10-22 11:13:49
**Status:** ✅ Success
**Similarity to First Run:** 34.0%
**Performance Metrics:**
- **Total Duration:** 11.86 seconds
- **Tokens per Second:** 40.4
- **Input Tokens:** 1083
- **Output Tokens:** 471
- **Load Duration:** 0.05 seconds
- **Prompt Eval Duration:** 0.03 seconds
- **Response Eval Duration:** 11.65 seconds

**Response:**

# main.py
## Summary
This Python script calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. The script uses mathematical formulas to compute the surface areas based on the given dimensions.

## Example
```python
import doctest

def test_surface_area_cube():
    assert surface_area_cube(1) == 6
    return True

if __name__ == "__main__":
    doctest.testmod()
```

## Function Descriptions

### `surface_area_cube(side_length: float) -> float`
Calculate the Surface Area of a Cube.

*   Parameters:
    *   `side_length`: The length of one side of the cube.
*   Returns:
    *   The surface area of the cube.
*   Raises:
    *   ValueError: If `side_length` is negative.

### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
Calculate the Surface Area of a Cuboid.

*   Parameters:
    *   `length`: The length of the cuboid.
    *   `breadth`: The breadth of the cuboid.
    *   `height`: The height of the cuboid.
*   Returns:
    *   The surface area of the cuboid.
*   Raises:
    *   ValueError: If any dimension is negative.

### `surface_area_sphere(radius: float) -> float`
Calculate the Surface Area of a Sphere.

*   Parameters:
    *   `radius`: The radius of the sphere.
*   Returns:
    *   The surface area of the sphere.
*   Raises:
    *   ValueError: If `radius` is negative.

### `surface_area_hemisphere(radius: float) -> float`
Calculate the Surface Area of a Hemisphere.

*   Parameters:
    *   `radius`: The radius of the hemisphere.
*   Returns:
    *   The surface area of the hemisphere.
*   Raises:
    *   ValueError: If `radius` is negative.

## Important Takeaways
This script relies on mathematical formulas to calculate the surface areas of geometric shapes. It assumes that input values are non-negative and raises a ValueError if this assumption is violated. When using or maintaining this script, developers should be aware of these assumptions and handle potential errors accordingly.

---

### Run 5

**Timestamp:** 2025-10-22 11:13:56
**Status:** ✅ Success
**Similarity to First Run:** 43.4%
**Performance Metrics:**
- **Total Duration:** 7.03 seconds
- **Tokens per Second:** 41.6
- **Input Tokens:** 1083
- **Output Tokens:** 286
- **Load Duration:** 0.05 seconds
- **Prompt Eval Duration:** 0.02 seconds
- **Response Eval Duration:** 6.87 seconds

**Response:**

# main.py
## Summary
This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.

## Example
```python
from main import surface_area_cube, surface_area_sphere

print(surface_area_cube(4))  # Output: 96.0
print(surface_area_sphere(2))  # Output: 50.26548245743669
```

## Function Descriptions
### surface_area_cube(side_length: float) -> float
Calculate the Surface Area of a Cube.

### surface_area_cuboid(length: float, breadth: float, height: float) -> float
Calculate the Surface Area of a Cuboid.

### surface_area_sphere(radius: float) -> float
Calculate the Surface Area of a Sphere.

### surface_area_hemisphere(radius: float) -> float
Calculate the Surface Area of a Hemisphere.

## Important Takeaways
* All functions in this script assume non-negative input values.
* The surface area of a cube is calculated as 6 times the square of its side length.
* The surface area of a cuboid is calculated as twice the sum of the products of its adjacent sides' lengths.
* The surface area of a sphere is calculated as 4 times pi times the square of its radius.
* The surface area of a hemisphere is calculated as 3 times pi times the square of its radius.

---

### Run 6

**Timestamp:** 2025-10-22 11:14:04
**Status:** ✅ Success
**Similarity to First Run:** 23.6%
**Performance Metrics:**
- **Total Duration:** 7.82 seconds
- **Tokens per Second:** 41.0
- **Input Tokens:** 1083
- **Output Tokens:** 314
- **Load Duration:** 0.05 seconds
- **Prompt Eval Duration:** 0.02 seconds
- **Response Eval Duration:** 7.66 seconds

**Response:**

# main.py
## Summary
This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.

## Example
```python
print(surface_area_cube(4))
```

## Function Descriptions

### surface_area_cube(side_length: float) -> float
Calculate the Surface Area of a Cube.
#### Parameters:
- side_length (float): The length of one side of the cube.
#### Returns:
- float: The surface area of the cube.

### surface_area_cuboid(length: float, breadth: float, height: float) -> float
Calculate the Surface Area of a Cuboid.
#### Parameters:
- length (float): The length of the cuboid.
- breadth (float): The breadth of the cuboid.
- height (float): The height of the cuboid.
#### Returns:
- float: The surface area of the cuboid.

### surface_area_sphere(radius: float) -> float
Calculate the Surface Area of a Sphere.
#### Parameters:
- radius (float): The radius of the sphere.
#### Returns:
- float: The surface area of the sphere.

### surface_area_hemisphere(radius: float) -> float
Calculate the Surface Area of a Hemisphere.
#### Parameters:
- radius (float): The radius of the hemisphere.
#### Returns:
- float: The surface area of the hemisphere.

## Important Takeaways
- All functions raise a ValueError if any dimension is negative.
- The formulas used are based on Wikipedia references for the respective shapes.

---

### Run 7

**Timestamp:** 2025-10-22 11:14:14
**Status:** ✅ Success
**Similarity to First Run:** 13.5%
**Performance Metrics:**
- **Total Duration:** 10.32 seconds
- **Tokens per Second:** 41.0
- **Input Tokens:** 1083
- **Output Tokens:** 415
- **Load Duration:** 0.05 seconds
- **Prompt Eval Duration:** 0.03 seconds
- **Response Eval Duration:** 10.13 seconds

**Response:**

# main.py
## Summary
This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions to compute the surface area based on the input dimensions.

## Example
```python
import doctest

def surface_area_cube(side_length: float) -> float:
    """
    Calculate the Surface Area of a Cube.

    >>> surface_area_cube(1)
    6
    >>> surface_area_cube(1.6)
    15.360000000000003
    >>> surface_area_cube(0)
    0
    >>> surface_area_cube(3)
    54
    >>> surface_area_cube(-1)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cube() only accepts non-negative values
    """
    if side_length < 0:
        raise ValueError("surface_area_cube() only accepts non-negative values")
    return 6 * side_length**2

print(surface_area_cube(4))  # Output: 96
```

## Function Descriptions

### surface_area_cube(side_length: float) -> float
Calculate the Surface Area of a Cube.

### surface_area_cuboid(length: float, breadth: float, height: float) -> float
Calculate the Surface Area of a Cuboid.

### surface_area_sphere(radius: float) -> float
Calculate the Surface Area of a Sphere.
Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
Formula: 4 * pi * r^2

### surface_area_hemisphere(radius: float) -> float
Calculate the Surface Area of a Hemisphere.
Formula: 3 * pi * r^2

## Important Takeaways

* All functions raise a ValueError if the input values are negative.
* The formulas used for calculating the surface area are based on mathematical principles and are accurate for non-negative input values.
* This script provides a simple way to calculate the surface area of various geometric shapes, making it useful for educational or practical purposes.

---

### Run 8

**Timestamp:** 2025-10-22 11:14:21
**Status:** ✅ Success
**Similarity to First Run:** 52.3%
**Performance Metrics:**
- **Total Duration:** 7.43 seconds
- **Tokens per Second:** 40.6
- **Input Tokens:** 1083
- **Output Tokens:** 295
- **Load Duration:** 0.05 seconds
- **Prompt Eval Duration:** 0.02 seconds
- **Response Eval Duration:** 7.27 seconds

**Response:**

# main.py
## Summary
This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.

## Example
```python
>>> print(surface_area_cube(5))
150.0
```
## Function Descriptions
### `surface_area_cube(side_length: float) -> float`

Calculate the Surface Area of a Cube.

*   `side_length`: The length of one side of the cube.
*   Returns: The surface area of the cube.

### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`

Calculate the Surface Area of a Cuboid.

*   `length`, `breadth`, `height`: The dimensions of the cuboid.
*   Returns: The surface area of the cuboid.

### `surface_area_sphere(radius: float) -> float`

Calculate the Surface Area of a Sphere.

*   `radius`: The radius of the sphere.
*   Returns: The surface area of the sphere.

### `surface_area_hemisphere(radius: float) -> float`

Calculate the Surface Area of a Hemisphere.

*   `radius`: The radius of the hemisphere.
*   Returns: The surface area of the hemisphere.

## Important Takeaways
*   All functions expect non-negative input values, and raising negative values will result in a ValueError.
*   The surface areas are calculated using the respective formulas for each shape.

---

### Run 9

**Timestamp:** 2025-10-22 11:14:28
**Status:** ✅ Success
**Similarity to First Run:** 10.4%
**Performance Metrics:**
- **Total Duration:** 6.29 seconds
- **Tokens per Second:** 41.0
- **Input Tokens:** 1083
- **Output Tokens:** 252
- **Load Duration:** 0.05 seconds
- **Prompt Eval Duration:** 0.03 seconds
- **Response Eval Duration:** 6.14 seconds

**Response:**

# main.py
## Summary
This file calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions for each shape to compute their respective surface areas.

## Example
```python
import doctest

def test_surface_area_cube():
    return doctest.testmod(surface_area_cube)

test_surface_area_cube()
```
## Function Descriptions

*   **surface_area_cube(side_length: float) -> float**: Calculate the Surface Area of a Cube.
*   **surface_area_cuboid(length: float, breadth: float, height: float) -> float**: Calculate the Surface Area of a Cuboid.
*   **surface_area_sphere(radius: float) -> float**: Calculate the Surface Area of a Sphere.
*   **surface_area_hemisphere(radius: float) -> float**: Calculate the Surface Area of a Hemisphere.

## Important Takeaways

*   All functions accept non-negative values for their respective dimensions. Any negative value will raise a `ValueError`.
*   The formulas used to calculate surface areas are based on the Wikipedia references provided.
*   The code uses the `math` module for mathematical constants and functions like `pi`, `sqrt`, and `tan`.

---

### Run 10

**Timestamp:** 2025-10-22 11:14:34
**Status:** ✅ Success
**Similarity to First Run:** 34.2%
**Performance Metrics:**
- **Total Duration:** 6.39 seconds
- **Tokens per Second:** 42.5
- **Input Tokens:** 1083
- **Output Tokens:** 265
- **Load Duration:** 0.05 seconds
- **Prompt Eval Duration:** 0.03 seconds
- **Response Eval Duration:** 6.23 seconds

**Response:**

# main.py
## Summary
This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas based on the given dimensions.

## Example
```python
>>> from main import surface_area_cube
>>> surface_area_cube(2)
24
```

## Function Descriptions

### `surface_area_cube(side_length: float) -> float`
Calculates the Surface Area of a Cube.

### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
Calculates the Surface Area of a Cuboid.

### `surface_area_sphere(radius: float) -> float`
Calculates the Surface Area of a Sphere.
Wikipedia reference: https://en.wikipedia.org/wiki/Sphere

### `surface_area_hemisphere(radius: float) -> float`
Calculates the Surface Area of a Hemisphere.

## Important Takeaways
* All functions in this file only accept non-negative values for their inputs. Any attempt to pass negative values will raise a ValueError.
* The formulas used for calculating surface areas are based on mathematical principles and are accurate for the respective shapes.
* Developers using or maintaining this code should ensure that they understand the logic behind each function, including error handling for invalid input.

---

## Difference Analysis
### Comparison: Run 1 vs Run 2
**Similarity:** 46.94%

**Diff:**
```diff
--- Run 1+++ Run 2@@ -1,27 +1,32 @@ # main.py
 ## Summary
-This file provides functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
 import doctest
 
-if __name__ == "__main__":
-    doctest.testmod()
+def test_surface_area_cube():
+    assert surface_area_cube(1) == 6
+    return True
+
+test_surface_area_cube()
 ```
 
 ## Function Descriptions
+### `surface_area_cube(side_length: float) -> float`
+Calculate the Surface Area of a Cube.
 
-### `surface_area_cube(side_length: float) -> float`
-Calculate the surface area of a cube given its side length.
 ### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the surface area of a cuboid given its length, breadth, and height.
+Calculate the Surface Area of a Cuboid.
+
 ### `surface_area_sphere(radius: float) -> float`
-Calculate the surface area of a sphere given its radius.
+Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+
 ### `surface_area_hemisphere(radius: float) -> float`
-Calculate the surface area of a hemisphere given its radius.
+Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
 
 ## Important Takeaways
-
-* All functions raise a ValueError if their input values are negative, as they only accept non-negative values.
-* The formulas used to calculate surface areas are based on mathematical principles and have been implemented correctly.+* All functions only accept non-negative values as input.
+* The surface area formulas used are based on Wikipedia references for each shape.
+* The `surface_area_sphere` and `surface_area_hemisphere` functions use the mathematical constants pi and pi squared, which can be imported from the math module using `from math import pi, sqrt, tan`.
```

### Comparison: Run 1 vs Run 3
**Similarity:** 43.21%

**Diff:**
```diff
--- Run 1+++ Run 3@@ -1,27 +1,29 @@ # main.py
 ## Summary
-This file provides functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas.
 
 ## Example
 ```python
-import doctest
-
-if __name__ == "__main__":
-    doctest.testmod()
+>>> import main
+>>> main.surface_area_cube(1)
+6
 ```
 
 ## Function Descriptions
 
-### `surface_area_cube(side_length: float) -> float`
-Calculate the surface area of a cube given its side length.
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the surface area of a cuboid given its length, breadth, and height.
-### `surface_area_sphere(radius: float) -> float`
-Calculate the surface area of a sphere given its radius.
-### `surface_area_hemisphere(radius: float) -> float`
-Calculate the surface area of a hemisphere given its radius.
+### surface_area_cube(side_length: float) -> float
+Calculate the Surface Area of a Cube.
+
+### surface_area_cuboid(length: float, breadth: float, height: float) -> float
+Calculate the Surface Area of a Cuboid.
+
+### surface_area_sphere(radius: float) -> float
+Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+
+### surface_area_hemisphere(radius: float) -> float
+Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
 
 ## Important Takeaways
-
-* All functions raise a ValueError if their input values are negative, as they only accept non-negative values.
-* The formulas used to calculate surface areas are based on mathematical principles and have been implemented correctly.+* All functions raise a ValueError if their input values are negative.
+* The formulas used for calculating surface areas are based on mathematical principles and are accurate for non-negative inputs.
+* Developers should ensure that all input values are valid before using these functions.
```

### Comparison: Run 1 vs Run 4
**Similarity:** 33.98%

**Diff:**
```diff
--- Run 1+++ Run 4@@ -1,10 +1,14 @@ # main.py
 ## Summary
-This file provides functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python script calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. The script uses mathematical formulas to compute the surface areas based on the given dimensions.
 
 ## Example
 ```python
 import doctest
+
+def test_surface_area_cube():
+    assert surface_area_cube(1) == 6
+    return True
 
 if __name__ == "__main__":
     doctest.testmod()
@@ -13,15 +17,46 @@ ## Function Descriptions
 
 ### `surface_area_cube(side_length: float) -> float`
-Calculate the surface area of a cube given its side length.
+Calculate the Surface Area of a Cube.
+
+*   Parameters:
+    *   `side_length`: The length of one side of the cube.
+*   Returns:
+    *   The surface area of the cube.
+*   Raises:
+    *   ValueError: If `side_length` is negative.
+
 ### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the surface area of a cuboid given its length, breadth, and height.
+Calculate the Surface Area of a Cuboid.
+
+*   Parameters:
+    *   `length`: The length of the cuboid.
+    *   `breadth`: The breadth of the cuboid.
+    *   `height`: The height of the cuboid.
+*   Returns:
+    *   The surface area of the cuboid.
+*   Raises:
+    *   ValueError: If any dimension is negative.
+
 ### `surface_area_sphere(radius: float) -> float`
-Calculate the surface area of a sphere given its radius.
+Calculate the Surface Area of a Sphere.
+
+*   Parameters:
+    *   `radius`: The radius of the sphere.
+*   Returns:
+    *   The surface area of the sphere.
+*   Raises:
+    *   ValueError: If `radius` is negative.
+
 ### `surface_area_hemisphere(radius: float) -> float`
-Calculate the surface area of a hemisphere given its radius.
+Calculate the Surface Area of a Hemisphere.
+
+*   Parameters:
+    *   `radius`: The radius of the hemisphere.
+*   Returns:
+    *   The surface area of the hemisphere.
+*   Raises:
+    *   ValueError: If `radius` is negative.
 
 ## Important Takeaways
-
-* All functions raise a ValueError if their input values are negative, as they only accept non-negative values.
-* The formulas used to calculate surface areas are based on mathematical principles and have been implemented correctly.+This script relies on mathematical formulas to calculate the surface areas of geometric shapes. It assumes that input values are non-negative and raises a ValueError if this assumption is violated. When using or maintaining this script, developers should be aware of these assumptions and handle potential errors accordingly.
```

### Comparison: Run 1 vs Run 5
**Similarity:** 43.37%

**Diff:**
```diff
--- Run 1+++ Run 5@@ -1,27 +1,31 @@ # main.py
 ## Summary
-This file provides functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-import doctest
+from main import surface_area_cube, surface_area_sphere
 
-if __name__ == "__main__":
-    doctest.testmod()
+print(surface_area_cube(4))  # Output: 96.0
+print(surface_area_sphere(2))  # Output: 50.26548245743669
 ```
 
 ## Function Descriptions
+### surface_area_cube(side_length: float) -> float
+Calculate the Surface Area of a Cube.
 
-### `surface_area_cube(side_length: float) -> float`
-Calculate the surface area of a cube given its side length.
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the surface area of a cuboid given its length, breadth, and height.
-### `surface_area_sphere(radius: float) -> float`
-Calculate the surface area of a sphere given its radius.
-### `surface_area_hemisphere(radius: float) -> float`
-Calculate the surface area of a hemisphere given its radius.
+### surface_area_cuboid(length: float, breadth: float, height: float) -> float
+Calculate the Surface Area of a Cuboid.
+
+### surface_area_sphere(radius: float) -> float
+Calculate the Surface Area of a Sphere.
+
+### surface_area_hemisphere(radius: float) -> float
+Calculate the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-
-* All functions raise a ValueError if their input values are negative, as they only accept non-negative values.
-* The formulas used to calculate surface areas are based on mathematical principles and have been implemented correctly.+* All functions in this script assume non-negative input values.
+* The surface area of a cube is calculated as 6 times the square of its side length.
+* The surface area of a cuboid is calculated as twice the sum of the products of its adjacent sides' lengths.
+* The surface area of a sphere is calculated as 4 times pi times the square of its radius.
+* The surface area of a hemisphere is calculated as 3 times pi times the square of its radius.
```

### Comparison: Run 1 vs Run 6
**Similarity:** 23.56%

**Diff:**
```diff
--- Run 1+++ Run 6@@ -1,27 +1,44 @@ # main.py
 ## Summary
-This file provides functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-import doctest
-
-if __name__ == "__main__":
-    doctest.testmod()
+print(surface_area_cube(4))
 ```
 
 ## Function Descriptions
 
-### `surface_area_cube(side_length: float) -> float`
-Calculate the surface area of a cube given its side length.
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the surface area of a cuboid given its length, breadth, and height.
-### `surface_area_sphere(radius: float) -> float`
-Calculate the surface area of a sphere given its radius.
-### `surface_area_hemisphere(radius: float) -> float`
-Calculate the surface area of a hemisphere given its radius.
+### surface_area_cube(side_length: float) -> float
+Calculate the Surface Area of a Cube.
+#### Parameters:
+- side_length (float): The length of one side of the cube.
+#### Returns:
+- float: The surface area of the cube.
+
+### surface_area_cuboid(length: float, breadth: float, height: float) -> float
+Calculate the Surface Area of a Cuboid.
+#### Parameters:
+- length (float): The length of the cuboid.
+- breadth (float): The breadth of the cuboid.
+- height (float): The height of the cuboid.
+#### Returns:
+- float: The surface area of the cuboid.
+
+### surface_area_sphere(radius: float) -> float
+Calculate the Surface Area of a Sphere.
+#### Parameters:
+- radius (float): The radius of the sphere.
+#### Returns:
+- float: The surface area of the sphere.
+
+### surface_area_hemisphere(radius: float) -> float
+Calculate the Surface Area of a Hemisphere.
+#### Parameters:
+- radius (float): The radius of the hemisphere.
+#### Returns:
+- float: The surface area of the hemisphere.
 
 ## Important Takeaways
-
-* All functions raise a ValueError if their input values are negative, as they only accept non-negative values.
-* The formulas used to calculate surface areas are based on mathematical principles and have been implemented correctly.+- All functions raise a ValueError if any dimension is negative.
+- The formulas used are based on Wikipedia references for the respective shapes.
```

### Comparison: Run 1 vs Run 7
**Similarity:** 13.47%

**Diff:**
```diff
--- Run 1+++ Run 7@@ -1,27 +1,54 @@ # main.py
 ## Summary
-This file provides functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions to compute the surface area based on the input dimensions.
 
 ## Example
 ```python
 import doctest
 
-if __name__ == "__main__":
-    doctest.testmod()
+def surface_area_cube(side_length: float) -> float:
+    """
+    Calculate the Surface Area of a Cube.
+
+    >>> surface_area_cube(1)
+    6
+    >>> surface_area_cube(1.6)
+    15.360000000000003
+    >>> surface_area_cube(0)
+    0
+    >>> surface_area_cube(3)
+    54
+    >>> surface_area_cube(-1)
+    Traceback (most recent call last):
+        ...
+    ValueError: surface_area_cube() only accepts non-negative values
+    """
+    if side_length < 0:
+        raise ValueError("surface_area_cube() only accepts non-negative values")
+    return 6 * side_length**2
+
+print(surface_area_cube(4))  # Output: 96
 ```
 
 ## Function Descriptions
 
-### `surface_area_cube(side_length: float) -> float`
-Calculate the surface area of a cube given its side length.
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the surface area of a cuboid given its length, breadth, and height.
-### `surface_area_sphere(radius: float) -> float`
-Calculate the surface area of a sphere given its radius.
-### `surface_area_hemisphere(radius: float) -> float`
-Calculate the surface area of a hemisphere given its radius.
+### surface_area_cube(side_length: float) -> float
+Calculate the Surface Area of a Cube.
+
+### surface_area_cuboid(length: float, breadth: float, height: float) -> float
+Calculate the Surface Area of a Cuboid.
+
+### surface_area_sphere(radius: float) -> float
+Calculate the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
+Formula: 4 * pi * r^2
+
+### surface_area_hemisphere(radius: float) -> float
+Calculate the Surface Area of a Hemisphere.
+Formula: 3 * pi * r^2
 
 ## Important Takeaways
 
-* All functions raise a ValueError if their input values are negative, as they only accept non-negative values.
-* The formulas used to calculate surface areas are based on mathematical principles and have been implemented correctly.+* All functions raise a ValueError if the input values are negative.
+* The formulas used for calculating the surface area are based on mathematical principles and are accurate for non-negative input values.
+* This script provides a simple way to calculate the surface area of various geometric shapes, making it useful for educational or practical purposes.
```

### Comparison: Run 1 vs Run 8
**Similarity:** 52.27%

**Diff:**
```diff
--- Run 1+++ Run 8@@ -1,27 +1,41 @@ # main.py
 ## Summary
-This file provides functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-import doctest
+>>> print(surface_area_cube(5))
+150.0
+```
+## Function Descriptions
+### `surface_area_cube(side_length: float) -> float`
 
-if __name__ == "__main__":
-    doctest.testmod()
-```
+Calculate the Surface Area of a Cube.
 
-## Function Descriptions
+*   `side_length`: The length of one side of the cube.
+*   Returns: The surface area of the cube.
 
-### `surface_area_cube(side_length: float) -> float`
-Calculate the surface area of a cube given its side length.
 ### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the surface area of a cuboid given its length, breadth, and height.
+
+Calculate the Surface Area of a Cuboid.
+
+*   `length`, `breadth`, `height`: The dimensions of the cuboid.
+*   Returns: The surface area of the cuboid.
+
 ### `surface_area_sphere(radius: float) -> float`
-Calculate the surface area of a sphere given its radius.
+
+Calculate the Surface Area of a Sphere.
+
+*   `radius`: The radius of the sphere.
+*   Returns: The surface area of the sphere.
+
 ### `surface_area_hemisphere(radius: float) -> float`
-Calculate the surface area of a hemisphere given its radius.
+
+Calculate the Surface Area of a Hemisphere.
+
+*   `radius`: The radius of the hemisphere.
+*   Returns: The surface area of the hemisphere.
 
 ## Important Takeaways
-
-* All functions raise a ValueError if their input values are negative, as they only accept non-negative values.
-* The formulas used to calculate surface areas are based on mathematical principles and have been implemented correctly.+*   All functions expect non-negative input values, and raising negative values will result in a ValueError.
+*   The surface areas are calculated using the respective formulas for each shape.
```

### Comparison: Run 1 vs Run 9
**Similarity:** 10.43%

**Diff:**
```diff
--- Run 1+++ Run 9@@ -1,27 +1,25 @@ # main.py
 ## Summary
-This file provides functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions for each shape to compute their respective surface areas.
 
 ## Example
 ```python
 import doctest
 
-if __name__ == "__main__":
-    doctest.testmod()
+def test_surface_area_cube():
+    return doctest.testmod(surface_area_cube)
+
+test_surface_area_cube()
 ```
-
 ## Function Descriptions
 
-### `surface_area_cube(side_length: float) -> float`
-Calculate the surface area of a cube given its side length.
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the surface area of a cuboid given its length, breadth, and height.
-### `surface_area_sphere(radius: float) -> float`
-Calculate the surface area of a sphere given its radius.
-### `surface_area_hemisphere(radius: float) -> float`
-Calculate the surface area of a hemisphere given its radius.
+*   **surface_area_cube(side_length: float) -> float**: Calculate the Surface Area of a Cube.
+*   **surface_area_cuboid(length: float, breadth: float, height: float) -> float**: Calculate the Surface Area of a Cuboid.
+*   **surface_area_sphere(radius: float) -> float**: Calculate the Surface Area of a Sphere.
+*   **surface_area_hemisphere(radius: float) -> float**: Calculate the Surface Area of a Hemisphere.
 
 ## Important Takeaways
 
-* All functions raise a ValueError if their input values are negative, as they only accept non-negative values.
-* The formulas used to calculate surface areas are based on mathematical principles and have been implemented correctly.+*   All functions accept non-negative values for their respective dimensions. Any negative value will raise a `ValueError`.
+*   The formulas used to calculate surface areas are based on the Wikipedia references provided.
+*   The code uses the `math` module for mathematical constants and functions like `pi`, `sqrt`, and `tan`.
```

### Comparison: Run 1 vs Run 10
**Similarity:** 34.16%

**Diff:**
```diff
--- Run 1+++ Run 10@@ -1,27 +1,30 @@ # main.py
 ## Summary
-This file provides functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas based on the given dimensions.
 
 ## Example
 ```python
-import doctest
-
-if __name__ == "__main__":
-    doctest.testmod()
+>>> from main import surface_area_cube
+>>> surface_area_cube(2)
+24
 ```
 
 ## Function Descriptions
 
 ### `surface_area_cube(side_length: float) -> float`
-Calculate the surface area of a cube given its side length.
+Calculates the Surface Area of a Cube.
+
 ### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the surface area of a cuboid given its length, breadth, and height.
+Calculates the Surface Area of a Cuboid.
+
 ### `surface_area_sphere(radius: float) -> float`
-Calculate the surface area of a sphere given its radius.
+Calculates the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
+
 ### `surface_area_hemisphere(radius: float) -> float`
-Calculate the surface area of a hemisphere given its radius.
+Calculates the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-
-* All functions raise a ValueError if their input values are negative, as they only accept non-negative values.
-* The formulas used to calculate surface areas are based on mathematical principles and have been implemented correctly.+* All functions in this file only accept non-negative values for their inputs. Any attempt to pass negative values will raise a ValueError.
+* The formulas used for calculating surface areas are based on mathematical principles and are accurate for the respective shapes.
+* Developers using or maintaining this code should ensure that they understand the logic behind each function, including error handling for invalid input.
```

### Comparison: Run 2 vs Run 3
**Similarity:** 67.19%

**Diff:**
```diff
--- Run 2+++ Run 3@@ -1,32 +1,29 @@ # main.py
 ## Summary
-This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas.
 
 ## Example
 ```python
-import doctest
-
-def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
-
-test_surface_area_cube()
+>>> import main
+>>> main.surface_area_cube(1)
+6
 ```
 
 ## Function Descriptions
-### `surface_area_cube(side_length: float) -> float`
+
+### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
 
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+### surface_area_cuboid(length: float, breadth: float, height: float) -> float
 Calculate the Surface Area of a Cuboid.
 
-### `surface_area_sphere(radius: float) -> float`
+### surface_area_sphere(radius: float) -> float
 Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
 
-### `surface_area_hemisphere(radius: float) -> float`
+### surface_area_hemisphere(radius: float) -> float
 Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
 
 ## Important Takeaways
-* All functions only accept non-negative values as input.
-* The surface area formulas used are based on Wikipedia references for each shape.
-* The `surface_area_sphere` and `surface_area_hemisphere` functions use the mathematical constants pi and pi squared, which can be imported from the math module using `from math import pi, sqrt, tan`.+* All functions raise a ValueError if their input values are negative.
+* The formulas used for calculating surface areas are based on mathematical principles and are accurate for non-negative inputs.
+* Developers should ensure that all input values are valid before using these functions.
```

### Comparison: Run 2 vs Run 4
**Similarity:** 43.67%

**Diff:**
```diff
--- Run 2+++ Run 4@@ -1,6 +1,6 @@ # main.py
 ## Summary
-This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python script calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. The script uses mathematical formulas to compute the surface areas based on the given dimensions.
 
 ## Example
 ```python
@@ -10,23 +10,53 @@     assert surface_area_cube(1) == 6
     return True
 
-test_surface_area_cube()
+if __name__ == "__main__":
+    doctest.testmod()
 ```
 
 ## Function Descriptions
+
 ### `surface_area_cube(side_length: float) -> float`
 Calculate the Surface Area of a Cube.
+
+*   Parameters:
+    *   `side_length`: The length of one side of the cube.
+*   Returns:
+    *   The surface area of the cube.
+*   Raises:
+    *   ValueError: If `side_length` is negative.
 
 ### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
 Calculate the Surface Area of a Cuboid.
 
+*   Parameters:
+    *   `length`: The length of the cuboid.
+    *   `breadth`: The breadth of the cuboid.
+    *   `height`: The height of the cuboid.
+*   Returns:
+    *   The surface area of the cuboid.
+*   Raises:
+    *   ValueError: If any dimension is negative.
+
 ### `surface_area_sphere(radius: float) -> float`
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+Calculate the Surface Area of a Sphere.
+
+*   Parameters:
+    *   `radius`: The radius of the sphere.
+*   Returns:
+    *   The surface area of the sphere.
+*   Raises:
+    *   ValueError: If `radius` is negative.
 
 ### `surface_area_hemisphere(radius: float) -> float`
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+Calculate the Surface Area of a Hemisphere.
+
+*   Parameters:
+    *   `radius`: The radius of the hemisphere.
+*   Returns:
+    *   The surface area of the hemisphere.
+*   Raises:
+    *   ValueError: If `radius` is negative.
 
 ## Important Takeaways
-* All functions only accept non-negative values as input.
-* The surface area formulas used are based on Wikipedia references for each shape.
-* The `surface_area_sphere` and `surface_area_hemisphere` functions use the mathematical constants pi and pi squared, which can be imported from the math module using `from math import pi, sqrt, tan`.+This script relies on mathematical formulas to calculate the surface areas of geometric shapes. It assumes that input values are non-negative and raises a ValueError if this assumption is violated. When using or maintaining this script, developers should be aware of these assumptions and handle potential errors accordingly.
```

### Comparison: Run 2 vs Run 5
**Similarity:** 50.52%

**Diff:**
```diff
--- Run 2+++ Run 5@@ -1,32 +1,31 @@ # main.py
 ## Summary
-This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-import doctest
+from main import surface_area_cube, surface_area_sphere
 
-def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
-
-test_surface_area_cube()
+print(surface_area_cube(4))  # Output: 96.0
+print(surface_area_sphere(2))  # Output: 50.26548245743669
 ```
 
 ## Function Descriptions
-### `surface_area_cube(side_length: float) -> float`
+### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
 
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+### surface_area_cuboid(length: float, breadth: float, height: float) -> float
 Calculate the Surface Area of a Cuboid.
 
-### `surface_area_sphere(radius: float) -> float`
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+### surface_area_sphere(radius: float) -> float
+Calculate the Surface Area of a Sphere.
 
-### `surface_area_hemisphere(radius: float) -> float`
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+### surface_area_hemisphere(radius: float) -> float
+Calculate the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-* All functions only accept non-negative values as input.
-* The surface area formulas used are based on Wikipedia references for each shape.
-* The `surface_area_sphere` and `surface_area_hemisphere` functions use the mathematical constants pi and pi squared, which can be imported from the math module using `from math import pi, sqrt, tan`.+* All functions in this script assume non-negative input values.
+* The surface area of a cube is calculated as 6 times the square of its side length.
+* The surface area of a cuboid is calculated as twice the sum of the products of its adjacent sides' lengths.
+* The surface area of a sphere is calculated as 4 times pi times the square of its radius.
+* The surface area of a hemisphere is calculated as 3 times pi times the square of its radius.
```

### Comparison: Run 2 vs Run 6
**Similarity:** 37.67%

**Diff:**
```diff
--- Run 2+++ Run 6@@ -1,32 +1,44 @@ # main.py
 ## Summary
-This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-import doctest
-
-def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
-
-test_surface_area_cube()
+print(surface_area_cube(4))
 ```
 
 ## Function Descriptions
-### `surface_area_cube(side_length: float) -> float`
+
+### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
+#### Parameters:
+- side_length (float): The length of one side of the cube.
+#### Returns:
+- float: The surface area of the cube.
 
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+### surface_area_cuboid(length: float, breadth: float, height: float) -> float
 Calculate the Surface Area of a Cuboid.
+#### Parameters:
+- length (float): The length of the cuboid.
+- breadth (float): The breadth of the cuboid.
+- height (float): The height of the cuboid.
+#### Returns:
+- float: The surface area of the cuboid.
 
-### `surface_area_sphere(radius: float) -> float`
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+### surface_area_sphere(radius: float) -> float
+Calculate the Surface Area of a Sphere.
+#### Parameters:
+- radius (float): The radius of the sphere.
+#### Returns:
+- float: The surface area of the sphere.
 
-### `surface_area_hemisphere(radius: float) -> float`
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+### surface_area_hemisphere(radius: float) -> float
+Calculate the Surface Area of a Hemisphere.
+#### Parameters:
+- radius (float): The radius of the hemisphere.
+#### Returns:
+- float: The surface area of the hemisphere.
 
 ## Important Takeaways
-* All functions only accept non-negative values as input.
-* The surface area formulas used are based on Wikipedia references for each shape.
-* The `surface_area_sphere` and `surface_area_hemisphere` functions use the mathematical constants pi and pi squared, which can be imported from the math module using `from math import pi, sqrt, tan`.+- All functions raise a ValueError if any dimension is negative.
+- The formulas used are based on Wikipedia references for the respective shapes.
```

### Comparison: Run 2 vs Run 7
**Similarity:** 55.54%

**Diff:**
```diff
--- Run 2+++ Run 7@@ -1,32 +1,54 @@ # main.py
 ## Summary
-This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions to compute the surface area based on the input dimensions.
 
 ## Example
 ```python
 import doctest
 
-def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
+def surface_area_cube(side_length: float) -> float:
+    """
+    Calculate the Surface Area of a Cube.
 
-test_surface_area_cube()
+    >>> surface_area_cube(1)
+    6
+    >>> surface_area_cube(1.6)
+    15.360000000000003
+    >>> surface_area_cube(0)
+    0
+    >>> surface_area_cube(3)
+    54
+    >>> surface_area_cube(-1)
+    Traceback (most recent call last):
+        ...
+    ValueError: surface_area_cube() only accepts non-negative values
+    """
+    if side_length < 0:
+        raise ValueError("surface_area_cube() only accepts non-negative values")
+    return 6 * side_length**2
+
+print(surface_area_cube(4))  # Output: 96
 ```
 
 ## Function Descriptions
-### `surface_area_cube(side_length: float) -> float`
+
+### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
 
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+### surface_area_cuboid(length: float, breadth: float, height: float) -> float
 Calculate the Surface Area of a Cuboid.
 
-### `surface_area_sphere(radius: float) -> float`
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+### surface_area_sphere(radius: float) -> float
+Calculate the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
+Formula: 4 * pi * r^2
 
-### `surface_area_hemisphere(radius: float) -> float`
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+### surface_area_hemisphere(radius: float) -> float
+Calculate the Surface Area of a Hemisphere.
+Formula: 3 * pi * r^2
 
 ## Important Takeaways
-* All functions only accept non-negative values as input.
-* The surface area formulas used are based on Wikipedia references for each shape.
-* The `surface_area_sphere` and `surface_area_hemisphere` functions use the mathematical constants pi and pi squared, which can be imported from the math module using `from math import pi, sqrt, tan`.+
+* All functions raise a ValueError if the input values are negative.
+* The formulas used for calculating the surface area are based on mathematical principles and are accurate for non-negative input values.
+* This script provides a simple way to calculate the surface area of various geometric shapes, making it useful for educational or practical purposes.
```

### Comparison: Run 2 vs Run 8
**Similarity:** 55.62%

**Diff:**
```diff
--- Run 2+++ Run 8@@ -1,32 +1,41 @@ # main.py
 ## Summary
-This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-import doctest
-
-def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
-
-test_surface_area_cube()
+>>> print(surface_area_cube(5))
+150.0
 ```
-
 ## Function Descriptions
 ### `surface_area_cube(side_length: float) -> float`
+
 Calculate the Surface Area of a Cube.
 
+*   `side_length`: The length of one side of the cube.
+*   Returns: The surface area of the cube.
+
 ### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+
 Calculate the Surface Area of a Cuboid.
 
+*   `length`, `breadth`, `height`: The dimensions of the cuboid.
+*   Returns: The surface area of the cuboid.
+
 ### `surface_area_sphere(radius: float) -> float`
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+
+Calculate the Surface Area of a Sphere.
+
+*   `radius`: The radius of the sphere.
+*   Returns: The surface area of the sphere.
 
 ### `surface_area_hemisphere(radius: float) -> float`
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+
+Calculate the Surface Area of a Hemisphere.
+
+*   `radius`: The radius of the hemisphere.
+*   Returns: The surface area of the hemisphere.
 
 ## Important Takeaways
-* All functions only accept non-negative values as input.
-* The surface area formulas used are based on Wikipedia references for each shape.
-* The `surface_area_sphere` and `surface_area_hemisphere` functions use the mathematical constants pi and pi squared, which can be imported from the math module using `from math import pi, sqrt, tan`.+*   All functions expect non-negative input values, and raising negative values will result in a ValueError.
+*   The surface areas are calculated using the respective formulas for each shape.
```

### Comparison: Run 2 vs Run 9
**Similarity:** 22.48%

**Diff:**
```diff
--- Run 2+++ Run 9@@ -1,32 +1,25 @@ # main.py
 ## Summary
-This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions for each shape to compute their respective surface areas.
 
 ## Example
 ```python
 import doctest
 
 def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
+    return doctest.testmod(surface_area_cube)
 
 test_surface_area_cube()
 ```
+## Function Descriptions
 
-## Function Descriptions
-### `surface_area_cube(side_length: float) -> float`
-Calculate the Surface Area of a Cube.
-
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the Surface Area of a Cuboid.
-
-### `surface_area_sphere(radius: float) -> float`
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
-
-### `surface_area_hemisphere(radius: float) -> float`
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+*   **surface_area_cube(side_length: float) -> float**: Calculate the Surface Area of a Cube.
+*   **surface_area_cuboid(length: float, breadth: float, height: float) -> float**: Calculate the Surface Area of a Cuboid.
+*   **surface_area_sphere(radius: float) -> float**: Calculate the Surface Area of a Sphere.
+*   **surface_area_hemisphere(radius: float) -> float**: Calculate the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-* All functions only accept non-negative values as input.
-* The surface area formulas used are based on Wikipedia references for each shape.
-* The `surface_area_sphere` and `surface_area_hemisphere` functions use the mathematical constants pi and pi squared, which can be imported from the math module using `from math import pi, sqrt, tan`.+
+*   All functions accept non-negative values for their respective dimensions. Any negative value will raise a `ValueError`.
+*   The formulas used to calculate surface areas are based on the Wikipedia references provided.
+*   The code uses the `math` module for mathematical constants and functions like `pi`, `sqrt`, and `tan`.
```

### Comparison: Run 2 vs Run 10
**Similarity:** 55.47%

**Diff:**
```diff
--- Run 2+++ Run 10@@ -1,32 +1,30 @@ # main.py
 ## Summary
-This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas based on the given dimensions.
 
 ## Example
 ```python
-import doctest
-
-def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
-
-test_surface_area_cube()
+>>> from main import surface_area_cube
+>>> surface_area_cube(2)
+24
 ```
 
 ## Function Descriptions
+
 ### `surface_area_cube(side_length: float) -> float`
-Calculate the Surface Area of a Cube.
+Calculates the Surface Area of a Cube.
 
 ### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the Surface Area of a Cuboid.
+Calculates the Surface Area of a Cuboid.
 
 ### `surface_area_sphere(radius: float) -> float`
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+Calculates the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
 
 ### `surface_area_hemisphere(radius: float) -> float`
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+Calculates the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-* All functions only accept non-negative values as input.
-* The surface area formulas used are based on Wikipedia references for each shape.
-* The `surface_area_sphere` and `surface_area_hemisphere` functions use the mathematical constants pi and pi squared, which can be imported from the math module using `from math import pi, sqrt, tan`.+* All functions in this file only accept non-negative values for their inputs. Any attempt to pass negative values will raise a ValueError.
+* The formulas used for calculating surface areas are based on mathematical principles and are accurate for the respective shapes.
+* Developers using or maintaining this code should ensure that they understand the logic behind each function, including error handling for invalid input.
```

### Comparison: Run 3 vs Run 4
**Similarity:** 40.50%

**Diff:**
```diff
--- Run 3+++ Run 4@@ -1,29 +1,62 @@ # main.py
 ## Summary
-This file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas.
+This Python script calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. The script uses mathematical formulas to compute the surface areas based on the given dimensions.
 
 ## Example
 ```python
->>> import main
->>> main.surface_area_cube(1)
-6
+import doctest
+
+def test_surface_area_cube():
+    assert surface_area_cube(1) == 6
+    return True
+
+if __name__ == "__main__":
+    doctest.testmod()
 ```
 
 ## Function Descriptions
 
-### surface_area_cube(side_length: float) -> float
+### `surface_area_cube(side_length: float) -> float`
 Calculate the Surface Area of a Cube.
 
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
+*   Parameters:
+    *   `side_length`: The length of one side of the cube.
+*   Returns:
+    *   The surface area of the cube.
+*   Raises:
+    *   ValueError: If `side_length` is negative.
+
+### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
 Calculate the Surface Area of a Cuboid.
 
-### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+*   Parameters:
+    *   `length`: The length of the cuboid.
+    *   `breadth`: The breadth of the cuboid.
+    *   `height`: The height of the cuboid.
+*   Returns:
+    *   The surface area of the cuboid.
+*   Raises:
+    *   ValueError: If any dimension is negative.
 
-### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+### `surface_area_sphere(radius: float) -> float`
+Calculate the Surface Area of a Sphere.
+
+*   Parameters:
+    *   `radius`: The radius of the sphere.
+*   Returns:
+    *   The surface area of the sphere.
+*   Raises:
+    *   ValueError: If `radius` is negative.
+
+### `surface_area_hemisphere(radius: float) -> float`
+Calculate the Surface Area of a Hemisphere.
+
+*   Parameters:
+    *   `radius`: The radius of the hemisphere.
+*   Returns:
+    *   The surface area of the hemisphere.
+*   Raises:
+    *   ValueError: If `radius` is negative.
 
 ## Important Takeaways
-* All functions raise a ValueError if their input values are negative.
-* The formulas used for calculating surface areas are based on mathematical principles and are accurate for non-negative inputs.
-* Developers should ensure that all input values are valid before using these functions.+This script relies on mathematical formulas to calculate the surface areas of geometric shapes. It assumes that input values are non-negative and raises a ValueError if this assumption is violated. When using or maintaining this script, developers should be aware of these assumptions and handle potential errors accordingly.
```

### Comparison: Run 3 vs Run 5
**Similarity:** 50.75%

**Diff:**
```diff
--- Run 3+++ Run 5@@ -1,16 +1,16 @@ # main.py
 ## Summary
-This file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas.
+This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
->>> import main
->>> main.surface_area_cube(1)
-6
+from main import surface_area_cube, surface_area_sphere
+
+print(surface_area_cube(4))  # Output: 96.0
+print(surface_area_sphere(2))  # Output: 50.26548245743669
 ```
 
 ## Function Descriptions
-
 ### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
 
@@ -18,12 +18,14 @@ Calculate the Surface Area of a Cuboid.
 
 ### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+Calculate the Surface Area of a Sphere.
 
 ### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+Calculate the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-* All functions raise a ValueError if their input values are negative.
-* The formulas used for calculating surface areas are based on mathematical principles and are accurate for non-negative inputs.
-* Developers should ensure that all input values are valid before using these functions.+* All functions in this script assume non-negative input values.
+* The surface area of a cube is calculated as 6 times the square of its side length.
+* The surface area of a cuboid is calculated as twice the sum of the products of its adjacent sides' lengths.
+* The surface area of a sphere is calculated as 4 times pi times the square of its radius.
+* The surface area of a hemisphere is calculated as 3 times pi times the square of its radius.
```

### Comparison: Run 3 vs Run 6
**Similarity:** 40.80%

**Diff:**
```diff
--- Run 3+++ Run 6@@ -1,29 +1,44 @@ # main.py
 ## Summary
-This file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas.
+This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
->>> import main
->>> main.surface_area_cube(1)
-6
+print(surface_area_cube(4))
 ```
 
 ## Function Descriptions
 
 ### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
+#### Parameters:
+- side_length (float): The length of one side of the cube.
+#### Returns:
+- float: The surface area of the cube.
 
 ### surface_area_cuboid(length: float, breadth: float, height: float) -> float
 Calculate the Surface Area of a Cuboid.
+#### Parameters:
+- length (float): The length of the cuboid.
+- breadth (float): The breadth of the cuboid.
+- height (float): The height of the cuboid.
+#### Returns:
+- float: The surface area of the cuboid.
 
 ### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+Calculate the Surface Area of a Sphere.
+#### Parameters:
+- radius (float): The radius of the sphere.
+#### Returns:
+- float: The surface area of the sphere.
 
 ### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+Calculate the Surface Area of a Hemisphere.
+#### Parameters:
+- radius (float): The radius of the hemisphere.
+#### Returns:
+- float: The surface area of the hemisphere.
 
 ## Important Takeaways
-* All functions raise a ValueError if their input values are negative.
-* The formulas used for calculating surface areas are based on mathematical principles and are accurate for non-negative inputs.
-* Developers should ensure that all input values are valid before using these functions.+- All functions raise a ValueError if any dimension is negative.
+- The formulas used are based on Wikipedia references for the respective shapes.
```

### Comparison: Run 3 vs Run 7
**Similarity:** 64.63%

**Diff:**
```diff
--- Run 3+++ Run 7@@ -1,12 +1,33 @@ # main.py
 ## Summary
-This file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas.
+This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions to compute the surface area based on the input dimensions.
 
 ## Example
 ```python
->>> import main
->>> main.surface_area_cube(1)
-6
+import doctest
+
+def surface_area_cube(side_length: float) -> float:
+    """
+    Calculate the Surface Area of a Cube.
+
+    >>> surface_area_cube(1)
+    6
+    >>> surface_area_cube(1.6)
+    15.360000000000003
+    >>> surface_area_cube(0)
+    0
+    >>> surface_area_cube(3)
+    54
+    >>> surface_area_cube(-1)
+    Traceback (most recent call last):
+        ...
+    ValueError: surface_area_cube() only accepts non-negative values
+    """
+    if side_length < 0:
+        raise ValueError("surface_area_cube() only accepts non-negative values")
+    return 6 * side_length**2
+
+print(surface_area_cube(4))  # Output: 96
 ```
 
 ## Function Descriptions
@@ -18,12 +39,16 @@ Calculate the Surface Area of a Cuboid.
 
 ### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+Calculate the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
+Formula: 4 * pi * r^2
 
 ### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+Calculate the Surface Area of a Hemisphere.
+Formula: 3 * pi * r^2
 
 ## Important Takeaways
-* All functions raise a ValueError if their input values are negative.
-* The formulas used for calculating surface areas are based on mathematical principles and are accurate for non-negative inputs.
-* Developers should ensure that all input values are valid before using these functions.+
+* All functions raise a ValueError if the input values are negative.
+* The formulas used for calculating the surface area are based on mathematical principles and are accurate for non-negative input values.
+* This script provides a simple way to calculate the surface area of various geometric shapes, making it useful for educational or practical purposes.
```

### Comparison: Run 3 vs Run 8
**Similarity:** 55.03%

**Diff:**
```diff
--- Run 3+++ Run 8@@ -1,29 +1,41 @@ # main.py
 ## Summary
-This file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas.
+This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
->>> import main
->>> main.surface_area_cube(1)
-6
+>>> print(surface_area_cube(5))
+150.0
 ```
+## Function Descriptions
+### `surface_area_cube(side_length: float) -> float`
 
-## Function Descriptions
-
-### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
 
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
+*   `side_length`: The length of one side of the cube.
+*   Returns: The surface area of the cube.
+
+### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+
 Calculate the Surface Area of a Cuboid.
 
-### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+*   `length`, `breadth`, `height`: The dimensions of the cuboid.
+*   Returns: The surface area of the cuboid.
 
-### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+### `surface_area_sphere(radius: float) -> float`
+
+Calculate the Surface Area of a Sphere.
+
+*   `radius`: The radius of the sphere.
+*   Returns: The surface area of the sphere.
+
+### `surface_area_hemisphere(radius: float) -> float`
+
+Calculate the Surface Area of a Hemisphere.
+
+*   `radius`: The radius of the hemisphere.
+*   Returns: The surface area of the hemisphere.
 
 ## Important Takeaways
-* All functions raise a ValueError if their input values are negative.
-* The formulas used for calculating surface areas are based on mathematical principles and are accurate for non-negative inputs.
-* Developers should ensure that all input values are valid before using these functions.+*   All functions expect non-negative input values, and raising negative values will result in a ValueError.
+*   The surface areas are calculated using the respective formulas for each shape.
```

### Comparison: Run 3 vs Run 9
**Similarity:** 20.54%

**Diff:**
```diff
--- Run 3+++ Run 9@@ -1,29 +1,25 @@ # main.py
 ## Summary
-This file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas.
+This file calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions for each shape to compute their respective surface areas.
 
 ## Example
 ```python
->>> import main
->>> main.surface_area_cube(1)
-6
+import doctest
+
+def test_surface_area_cube():
+    return doctest.testmod(surface_area_cube)
+
+test_surface_area_cube()
 ```
-
 ## Function Descriptions
 
-### surface_area_cube(side_length: float) -> float
-Calculate the Surface Area of a Cube.
-
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
-Calculate the Surface Area of a Cuboid.
-
-### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
-
-### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+*   **surface_area_cube(side_length: float) -> float**: Calculate the Surface Area of a Cube.
+*   **surface_area_cuboid(length: float, breadth: float, height: float) -> float**: Calculate the Surface Area of a Cuboid.
+*   **surface_area_sphere(radius: float) -> float**: Calculate the Surface Area of a Sphere.
+*   **surface_area_hemisphere(radius: float) -> float**: Calculate the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-* All functions raise a ValueError if their input values are negative.
-* The formulas used for calculating surface areas are based on mathematical principles and are accurate for non-negative inputs.
-* Developers should ensure that all input values are valid before using these functions.+
+*   All functions accept non-negative values for their respective dimensions. Any negative value will raise a `ValueError`.
+*   The formulas used to calculate surface areas are based on the Wikipedia references provided.
+*   The code uses the `math` module for mathematical constants and functions like `pi`, `sqrt`, and `tan`.
```

### Comparison: Run 3 vs Run 10
**Similarity:** 61.80%

**Diff:**
```diff
--- Run 3+++ Run 10@@ -1,29 +1,30 @@ # main.py
 ## Summary
-This file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas.
+This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas based on the given dimensions.
 
 ## Example
 ```python
->>> import main
->>> main.surface_area_cube(1)
-6
+>>> from main import surface_area_cube
+>>> surface_area_cube(2)
+24
 ```
 
 ## Function Descriptions
 
-### surface_area_cube(side_length: float) -> float
-Calculate the Surface Area of a Cube.
+### `surface_area_cube(side_length: float) -> float`
+Calculates the Surface Area of a Cube.
 
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
-Calculate the Surface Area of a Cuboid.
+### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+Calculates the Surface Area of a Cuboid.
 
-### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere. Wikipedia reference: https://en.wikipedia.org/wiki/Sphere Formula: 4 * pi * r^2
+### `surface_area_sphere(radius: float) -> float`
+Calculates the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
 
-### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere. Formula: 3 * pi * r^2
+### `surface_area_hemisphere(radius: float) -> float`
+Calculates the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-* All functions raise a ValueError if their input values are negative.
-* The formulas used for calculating surface areas are based on mathematical principles and are accurate for non-negative inputs.
-* Developers should ensure that all input values are valid before using these functions.+* All functions in this file only accept non-negative values for their inputs. Any attempt to pass negative values will raise a ValueError.
+* The formulas used for calculating surface areas are based on mathematical principles and are accurate for the respective shapes.
+* Developers using or maintaining this code should ensure that they understand the logic behind each function, including error handling for invalid input.
```

### Comparison: Run 4 vs Run 5
**Similarity:** 39.85%

**Diff:**
```diff
--- Run 4+++ Run 5@@ -1,62 +1,31 @@ # main.py
 ## Summary
-This Python script calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. The script uses mathematical formulas to compute the surface areas based on the given dimensions.
+This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-import doctest
+from main import surface_area_cube, surface_area_sphere
 
-def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
-
-if __name__ == "__main__":
-    doctest.testmod()
+print(surface_area_cube(4))  # Output: 96.0
+print(surface_area_sphere(2))  # Output: 50.26548245743669
 ```
 
 ## Function Descriptions
-
-### `surface_area_cube(side_length: float) -> float`
+### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
 
-*   Parameters:
-    *   `side_length`: The length of one side of the cube.
-*   Returns:
-    *   The surface area of the cube.
-*   Raises:
-    *   ValueError: If `side_length` is negative.
-
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+### surface_area_cuboid(length: float, breadth: float, height: float) -> float
 Calculate the Surface Area of a Cuboid.
 
-*   Parameters:
-    *   `length`: The length of the cuboid.
-    *   `breadth`: The breadth of the cuboid.
-    *   `height`: The height of the cuboid.
-*   Returns:
-    *   The surface area of the cuboid.
-*   Raises:
-    *   ValueError: If any dimension is negative.
-
-### `surface_area_sphere(radius: float) -> float`
+### surface_area_sphere(radius: float) -> float
 Calculate the Surface Area of a Sphere.
 
-*   Parameters:
-    *   `radius`: The radius of the sphere.
-*   Returns:
-    *   The surface area of the sphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
-
-### `surface_area_hemisphere(radius: float) -> float`
+### surface_area_hemisphere(radius: float) -> float
 Calculate the Surface Area of a Hemisphere.
 
-*   Parameters:
-    *   `radius`: The radius of the hemisphere.
-*   Returns:
-    *   The surface area of the hemisphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
-
 ## Important Takeaways
-This script relies on mathematical formulas to calculate the surface areas of geometric shapes. It assumes that input values are non-negative and raises a ValueError if this assumption is violated. When using or maintaining this script, developers should be aware of these assumptions and handle potential errors accordingly.+* All functions in this script assume non-negative input values.
+* The surface area of a cube is calculated as 6 times the square of its side length.
+* The surface area of a cuboid is calculated as twice the sum of the products of its adjacent sides' lengths.
+* The surface area of a sphere is calculated as 4 times pi times the square of its radius.
+* The surface area of a hemisphere is calculated as 3 times pi times the square of its radius.
```

### Comparison: Run 4 vs Run 6
**Similarity:** 23.20%

**Diff:**
```diff
--- Run 4+++ Run 6@@ -1,62 +1,44 @@ # main.py
 ## Summary
-This Python script calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. The script uses mathematical formulas to compute the surface areas based on the given dimensions.
+This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-import doctest
-
-def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
-
-if __name__ == "__main__":
-    doctest.testmod()
+print(surface_area_cube(4))
 ```
 
 ## Function Descriptions
 
-### `surface_area_cube(side_length: float) -> float`
+### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
+#### Parameters:
+- side_length (float): The length of one side of the cube.
+#### Returns:
+- float: The surface area of the cube.
 
-*   Parameters:
-    *   `side_length`: The length of one side of the cube.
-*   Returns:
-    *   The surface area of the cube.
-*   Raises:
-    *   ValueError: If `side_length` is negative.
+### surface_area_cuboid(length: float, breadth: float, height: float) -> float
+Calculate the Surface Area of a Cuboid.
+#### Parameters:
+- length (float): The length of the cuboid.
+- breadth (float): The breadth of the cuboid.
+- height (float): The height of the cuboid.
+#### Returns:
+- float: The surface area of the cuboid.
 
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the Surface Area of a Cuboid.
+### surface_area_sphere(radius: float) -> float
+Calculate the Surface Area of a Sphere.
+#### Parameters:
+- radius (float): The radius of the sphere.
+#### Returns:
+- float: The surface area of the sphere.
 
-*   Parameters:
-    *   `length`: The length of the cuboid.
-    *   `breadth`: The breadth of the cuboid.
-    *   `height`: The height of the cuboid.
-*   Returns:
-    *   The surface area of the cuboid.
-*   Raises:
-    *   ValueError: If any dimension is negative.
-
-### `surface_area_sphere(radius: float) -> float`
-Calculate the Surface Area of a Sphere.
-
-*   Parameters:
-    *   `radius`: The radius of the sphere.
-*   Returns:
-    *   The surface area of the sphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
-
-### `surface_area_hemisphere(radius: float) -> float`
+### surface_area_hemisphere(radius: float) -> float
 Calculate the Surface Area of a Hemisphere.
-
-*   Parameters:
-    *   `radius`: The radius of the hemisphere.
-*   Returns:
-    *   The surface area of the hemisphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
+#### Parameters:
+- radius (float): The radius of the hemisphere.
+#### Returns:
+- float: The surface area of the hemisphere.
 
 ## Important Takeaways
-This script relies on mathematical formulas to calculate the surface areas of geometric shapes. It assumes that input values are non-negative and raises a ValueError if this assumption is violated. When using or maintaining this script, developers should be aware of these assumptions and handle potential errors accordingly.+- All functions raise a ValueError if any dimension is negative.
+- The formulas used are based on Wikipedia references for the respective shapes.
```

### Comparison: Run 4 vs Run 7
**Similarity:** 21.88%

**Diff:**
```diff
--- Run 4+++ Run 7@@ -1,62 +1,54 @@ # main.py
 ## Summary
-This Python script calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. The script uses mathematical formulas to compute the surface areas based on the given dimensions.
+This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions to compute the surface area based on the input dimensions.
 
 ## Example
 ```python
 import doctest
 
-def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
+def surface_area_cube(side_length: float) -> float:
+    """
+    Calculate the Surface Area of a Cube.
 
-if __name__ == "__main__":
-    doctest.testmod()
+    >>> surface_area_cube(1)
+    6
+    >>> surface_area_cube(1.6)
+    15.360000000000003
+    >>> surface_area_cube(0)
+    0
+    >>> surface_area_cube(3)
+    54
+    >>> surface_area_cube(-1)
+    Traceback (most recent call last):
+        ...
+    ValueError: surface_area_cube() only accepts non-negative values
+    """
+    if side_length < 0:
+        raise ValueError("surface_area_cube() only accepts non-negative values")
+    return 6 * side_length**2
+
+print(surface_area_cube(4))  # Output: 96
 ```
 
 ## Function Descriptions
 
-### `surface_area_cube(side_length: float) -> float`
+### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
 
-*   Parameters:
-    *   `side_length`: The length of one side of the cube.
-*   Returns:
-    *   The surface area of the cube.
-*   Raises:
-    *   ValueError: If `side_length` is negative.
-
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+### surface_area_cuboid(length: float, breadth: float, height: float) -> float
 Calculate the Surface Area of a Cuboid.
 
-*   Parameters:
-    *   `length`: The length of the cuboid.
-    *   `breadth`: The breadth of the cuboid.
-    *   `height`: The height of the cuboid.
-*   Returns:
-    *   The surface area of the cuboid.
-*   Raises:
-    *   ValueError: If any dimension is negative.
+### surface_area_sphere(radius: float) -> float
+Calculate the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
+Formula: 4 * pi * r^2
 
-### `surface_area_sphere(radius: float) -> float`
-Calculate the Surface Area of a Sphere.
-
-*   Parameters:
-    *   `radius`: The radius of the sphere.
-*   Returns:
-    *   The surface area of the sphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
-
-### `surface_area_hemisphere(radius: float) -> float`
+### surface_area_hemisphere(radius: float) -> float
 Calculate the Surface Area of a Hemisphere.
-
-*   Parameters:
-    *   `radius`: The radius of the hemisphere.
-*   Returns:
-    *   The surface area of the hemisphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
+Formula: 3 * pi * r^2
 
 ## Important Takeaways
-This script relies on mathematical formulas to calculate the surface areas of geometric shapes. It assumes that input values are non-negative and raises a ValueError if this assumption is violated. When using or maintaining this script, developers should be aware of these assumptions and handle potential errors accordingly.+
+* All functions raise a ValueError if the input values are negative.
+* The formulas used for calculating the surface area are based on mathematical principles and are accurate for non-negative input values.
+* This script provides a simple way to calculate the surface area of various geometric shapes, making it useful for educational or practical purposes.
```

### Comparison: Run 4 vs Run 8
**Similarity:** 43.50%

**Diff:**
```diff
--- Run 4+++ Run 8@@ -1,62 +1,41 @@ # main.py
 ## Summary
-This Python script calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. The script uses mathematical formulas to compute the surface areas based on the given dimensions.
+This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-import doctest
+>>> print(surface_area_cube(5))
+150.0
+```
+## Function Descriptions
+### `surface_area_cube(side_length: float) -> float`
 
-def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
-
-if __name__ == "__main__":
-    doctest.testmod()
-```
-
-## Function Descriptions
-
-### `surface_area_cube(side_length: float) -> float`
 Calculate the Surface Area of a Cube.
 
-*   Parameters:
-    *   `side_length`: The length of one side of the cube.
-*   Returns:
-    *   The surface area of the cube.
-*   Raises:
-    *   ValueError: If `side_length` is negative.
+*   `side_length`: The length of one side of the cube.
+*   Returns: The surface area of the cube.
 
 ### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+
 Calculate the Surface Area of a Cuboid.
 
-*   Parameters:
-    *   `length`: The length of the cuboid.
-    *   `breadth`: The breadth of the cuboid.
-    *   `height`: The height of the cuboid.
-*   Returns:
-    *   The surface area of the cuboid.
-*   Raises:
-    *   ValueError: If any dimension is negative.
+*   `length`, `breadth`, `height`: The dimensions of the cuboid.
+*   Returns: The surface area of the cuboid.
 
 ### `surface_area_sphere(radius: float) -> float`
+
 Calculate the Surface Area of a Sphere.
 
-*   Parameters:
-    *   `radius`: The radius of the sphere.
-*   Returns:
-    *   The surface area of the sphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
+*   `radius`: The radius of the sphere.
+*   Returns: The surface area of the sphere.
 
 ### `surface_area_hemisphere(radius: float) -> float`
+
 Calculate the Surface Area of a Hemisphere.
 
-*   Parameters:
-    *   `radius`: The radius of the hemisphere.
-*   Returns:
-    *   The surface area of the hemisphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
+*   `radius`: The radius of the hemisphere.
+*   Returns: The surface area of the hemisphere.
 
 ## Important Takeaways
-This script relies on mathematical formulas to calculate the surface areas of geometric shapes. It assumes that input values are non-negative and raises a ValueError if this assumption is violated. When using or maintaining this script, developers should be aware of these assumptions and handle potential errors accordingly.+*   All functions expect non-negative input values, and raising negative values will result in a ValueError.
+*   The surface areas are calculated using the respective formulas for each shape.
```

### Comparison: Run 4 vs Run 9
**Similarity:** 17.39%

**Diff:**
```diff
--- Run 4+++ Run 9@@ -1,62 +1,25 @@ # main.py
 ## Summary
-This Python script calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. The script uses mathematical formulas to compute the surface areas based on the given dimensions.
+This file calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions for each shape to compute their respective surface areas.
 
 ## Example
 ```python
 import doctest
 
 def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
+    return doctest.testmod(surface_area_cube)
 
-if __name__ == "__main__":
-    doctest.testmod()
+test_surface_area_cube()
 ```
-
 ## Function Descriptions
 
-### `surface_area_cube(side_length: float) -> float`
-Calculate the Surface Area of a Cube.
-
-*   Parameters:
-    *   `side_length`: The length of one side of the cube.
-*   Returns:
-    *   The surface area of the cube.
-*   Raises:
-    *   ValueError: If `side_length` is negative.
-
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the Surface Area of a Cuboid.
-
-*   Parameters:
-    *   `length`: The length of the cuboid.
-    *   `breadth`: The breadth of the cuboid.
-    *   `height`: The height of the cuboid.
-*   Returns:
-    *   The surface area of the cuboid.
-*   Raises:
-    *   ValueError: If any dimension is negative.
-
-### `surface_area_sphere(radius: float) -> float`
-Calculate the Surface Area of a Sphere.
-
-*   Parameters:
-    *   `radius`: The radius of the sphere.
-*   Returns:
-    *   The surface area of the sphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
-
-### `surface_area_hemisphere(radius: float) -> float`
-Calculate the Surface Area of a Hemisphere.
-
-*   Parameters:
-    *   `radius`: The radius of the hemisphere.
-*   Returns:
-    *   The surface area of the hemisphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
+*   **surface_area_cube(side_length: float) -> float**: Calculate the Surface Area of a Cube.
+*   **surface_area_cuboid(length: float, breadth: float, height: float) -> float**: Calculate the Surface Area of a Cuboid.
+*   **surface_area_sphere(radius: float) -> float**: Calculate the Surface Area of a Sphere.
+*   **surface_area_hemisphere(radius: float) -> float**: Calculate the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-This script relies on mathematical formulas to calculate the surface areas of geometric shapes. It assumes that input values are non-negative and raises a ValueError if this assumption is violated. When using or maintaining this script, developers should be aware of these assumptions and handle potential errors accordingly.+
+*   All functions accept non-negative values for their respective dimensions. Any negative value will raise a `ValueError`.
+*   The formulas used to calculate surface areas are based on the Wikipedia references provided.
+*   The code uses the `math` module for mathematical constants and functions like `pi`, `sqrt`, and `tan`.
```

### Comparison: Run 4 vs Run 10
**Similarity:** 39.06%

**Diff:**
```diff
--- Run 4+++ Run 10@@ -1,62 +1,30 @@ # main.py
 ## Summary
-This Python script calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. The script uses mathematical formulas to compute the surface areas based on the given dimensions.
+This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas based on the given dimensions.
 
 ## Example
 ```python
-import doctest
-
-def test_surface_area_cube():
-    assert surface_area_cube(1) == 6
-    return True
-
-if __name__ == "__main__":
-    doctest.testmod()
+>>> from main import surface_area_cube
+>>> surface_area_cube(2)
+24
 ```
 
 ## Function Descriptions
 
 ### `surface_area_cube(side_length: float) -> float`
-Calculate the Surface Area of a Cube.
-
-*   Parameters:
-    *   `side_length`: The length of one side of the cube.
-*   Returns:
-    *   The surface area of the cube.
-*   Raises:
-    *   ValueError: If `side_length` is negative.
+Calculates the Surface Area of a Cube.
 
 ### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-Calculate the Surface Area of a Cuboid.
-
-*   Parameters:
-    *   `length`: The length of the cuboid.
-    *   `breadth`: The breadth of the cuboid.
-    *   `height`: The height of the cuboid.
-*   Returns:
-    *   The surface area of the cuboid.
-*   Raises:
-    *   ValueError: If any dimension is negative.
+Calculates the Surface Area of a Cuboid.
 
 ### `surface_area_sphere(radius: float) -> float`
-Calculate the Surface Area of a Sphere.
-
-*   Parameters:
-    *   `radius`: The radius of the sphere.
-*   Returns:
-    *   The surface area of the sphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
+Calculates the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
 
 ### `surface_area_hemisphere(radius: float) -> float`
-Calculate the Surface Area of a Hemisphere.
-
-*   Parameters:
-    *   `radius`: The radius of the hemisphere.
-*   Returns:
-    *   The surface area of the hemisphere.
-*   Raises:
-    *   ValueError: If `radius` is negative.
+Calculates the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-This script relies on mathematical formulas to calculate the surface areas of geometric shapes. It assumes that input values are non-negative and raises a ValueError if this assumption is violated. When using or maintaining this script, developers should be aware of these assumptions and handle potential errors accordingly.+* All functions in this file only accept non-negative values for their inputs. Any attempt to pass negative values will raise a ValueError.
+* The formulas used for calculating surface areas are based on mathematical principles and are accurate for the respective shapes.
+* Developers using or maintaining this code should ensure that they understand the logic behind each function, including error handling for invalid input.
```

### Comparison: Run 5 vs Run 6
**Similarity:** 48.58%

**Diff:**
```diff
--- Run 5+++ Run 6@@ -1,31 +1,44 @@ # main.py
 ## Summary
-This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-from main import surface_area_cube, surface_area_sphere
-
-print(surface_area_cube(4))  # Output: 96.0
-print(surface_area_sphere(2))  # Output: 50.26548245743669
+print(surface_area_cube(4))
 ```
 
 ## Function Descriptions
+
 ### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
+#### Parameters:
+- side_length (float): The length of one side of the cube.
+#### Returns:
+- float: The surface area of the cube.
 
 ### surface_area_cuboid(length: float, breadth: float, height: float) -> float
 Calculate the Surface Area of a Cuboid.
+#### Parameters:
+- length (float): The length of the cuboid.
+- breadth (float): The breadth of the cuboid.
+- height (float): The height of the cuboid.
+#### Returns:
+- float: The surface area of the cuboid.
 
 ### surface_area_sphere(radius: float) -> float
 Calculate the Surface Area of a Sphere.
+#### Parameters:
+- radius (float): The radius of the sphere.
+#### Returns:
+- float: The surface area of the sphere.
 
 ### surface_area_hemisphere(radius: float) -> float
 Calculate the Surface Area of a Hemisphere.
+#### Parameters:
+- radius (float): The radius of the hemisphere.
+#### Returns:
+- float: The surface area of the hemisphere.
 
 ## Important Takeaways
-* All functions in this script assume non-negative input values.
-* The surface area of a cube is calculated as 6 times the square of its side length.
-* The surface area of a cuboid is calculated as twice the sum of the products of its adjacent sides' lengths.
-* The surface area of a sphere is calculated as 4 times pi times the square of its radius.
-* The surface area of a hemisphere is calculated as 3 times pi times the square of its radius.+- All functions raise a ValueError if any dimension is negative.
+- The formulas used are based on Wikipedia references for the respective shapes.
```

### Comparison: Run 5 vs Run 7
**Similarity:** 47.57%

**Diff:**
```diff
--- Run 5+++ Run 7@@ -1,16 +1,37 @@ # main.py
 ## Summary
-This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions to compute the surface area based on the input dimensions.
 
 ## Example
 ```python
-from main import surface_area_cube, surface_area_sphere
+import doctest
 
-print(surface_area_cube(4))  # Output: 96.0
-print(surface_area_sphere(2))  # Output: 50.26548245743669
+def surface_area_cube(side_length: float) -> float:
+    """
+    Calculate the Surface Area of a Cube.
+
+    >>> surface_area_cube(1)
+    6
+    >>> surface_area_cube(1.6)
+    15.360000000000003
+    >>> surface_area_cube(0)
+    0
+    >>> surface_area_cube(3)
+    54
+    >>> surface_area_cube(-1)
+    Traceback (most recent call last):
+        ...
+    ValueError: surface_area_cube() only accepts non-negative values
+    """
+    if side_length < 0:
+        raise ValueError("surface_area_cube() only accepts non-negative values")
+    return 6 * side_length**2
+
+print(surface_area_cube(4))  # Output: 96
 ```
 
 ## Function Descriptions
+
 ### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
 
@@ -19,13 +40,15 @@ 
 ### surface_area_sphere(radius: float) -> float
 Calculate the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
+Formula: 4 * pi * r^2
 
 ### surface_area_hemisphere(radius: float) -> float
 Calculate the Surface Area of a Hemisphere.
+Formula: 3 * pi * r^2
 
 ## Important Takeaways
-* All functions in this script assume non-negative input values.
-* The surface area of a cube is calculated as 6 times the square of its side length.
-* The surface area of a cuboid is calculated as twice the sum of the products of its adjacent sides' lengths.
-* The surface area of a sphere is calculated as 4 times pi times the square of its radius.
-* The surface area of a hemisphere is calculated as 3 times pi times the square of its radius.+
+* All functions raise a ValueError if the input values are negative.
+* The formulas used for calculating the surface area are based on mathematical principles and are accurate for non-negative input values.
+* This script provides a simple way to calculate the surface area of various geometric shapes, making it useful for educational or practical purposes.
```

### Comparison: Run 5 vs Run 8
**Similarity:** 49.86%

**Diff:**
```diff
--- Run 5+++ Run 8@@ -1,31 +1,41 @@ # main.py
 ## Summary
-This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-from main import surface_area_cube, surface_area_sphere
+>>> print(surface_area_cube(5))
+150.0
+```
+## Function Descriptions
+### `surface_area_cube(side_length: float) -> float`
 
-print(surface_area_cube(4))  # Output: 96.0
-print(surface_area_sphere(2))  # Output: 50.26548245743669
-```
-
-## Function Descriptions
-### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
 
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
+*   `side_length`: The length of one side of the cube.
+*   Returns: The surface area of the cube.
+
+### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+
 Calculate the Surface Area of a Cuboid.
 
-### surface_area_sphere(radius: float) -> float
+*   `length`, `breadth`, `height`: The dimensions of the cuboid.
+*   Returns: The surface area of the cuboid.
+
+### `surface_area_sphere(radius: float) -> float`
+
 Calculate the Surface Area of a Sphere.
 
-### surface_area_hemisphere(radius: float) -> float
+*   `radius`: The radius of the sphere.
+*   Returns: The surface area of the sphere.
+
+### `surface_area_hemisphere(radius: float) -> float`
+
 Calculate the Surface Area of a Hemisphere.
 
+*   `radius`: The radius of the hemisphere.
+*   Returns: The surface area of the hemisphere.
+
 ## Important Takeaways
-* All functions in this script assume non-negative input values.
-* The surface area of a cube is calculated as 6 times the square of its side length.
-* The surface area of a cuboid is calculated as twice the sum of the products of its adjacent sides' lengths.
-* The surface area of a sphere is calculated as 4 times pi times the square of its radius.
-* The surface area of a hemisphere is calculated as 3 times pi times the square of its radius.+*   All functions expect non-negative input values, and raising negative values will result in a ValueError.
+*   The surface areas are calculated using the respective formulas for each shape.
```

### Comparison: Run 5 vs Run 9
**Similarity:** 17.06%

**Diff:**
```diff
--- Run 5+++ Run 9@@ -1,31 +1,25 @@ # main.py
 ## Summary
-This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions for each shape to compute their respective surface areas.
 
 ## Example
 ```python
-from main import surface_area_cube, surface_area_sphere
+import doctest
 
-print(surface_area_cube(4))  # Output: 96.0
-print(surface_area_sphere(2))  # Output: 50.26548245743669
+def test_surface_area_cube():
+    return doctest.testmod(surface_area_cube)
+
+test_surface_area_cube()
 ```
+## Function Descriptions
 
-## Function Descriptions
-### surface_area_cube(side_length: float) -> float
-Calculate the Surface Area of a Cube.
-
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
-Calculate the Surface Area of a Cuboid.
-
-### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere.
-
-### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere.
+*   **surface_area_cube(side_length: float) -> float**: Calculate the Surface Area of a Cube.
+*   **surface_area_cuboid(length: float, breadth: float, height: float) -> float**: Calculate the Surface Area of a Cuboid.
+*   **surface_area_sphere(radius: float) -> float**: Calculate the Surface Area of a Sphere.
+*   **surface_area_hemisphere(radius: float) -> float**: Calculate the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-* All functions in this script assume non-negative input values.
-* The surface area of a cube is calculated as 6 times the square of its side length.
-* The surface area of a cuboid is calculated as twice the sum of the products of its adjacent sides' lengths.
-* The surface area of a sphere is calculated as 4 times pi times the square of its radius.
-* The surface area of a hemisphere is calculated as 3 times pi times the square of its radius.+
+*   All functions accept non-negative values for their respective dimensions. Any negative value will raise a `ValueError`.
+*   The formulas used to calculate surface areas are based on the Wikipedia references provided.
+*   The code uses the `math` module for mathematical constants and functions like `pi`, `sqrt`, and `tan`.
```

### Comparison: Run 5 vs Run 10
**Similarity:** 57.99%

**Diff:**
```diff
--- Run 5+++ Run 10@@ -1,31 +1,30 @@ # main.py
 ## Summary
-This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas based on the given dimensions.
 
 ## Example
 ```python
-from main import surface_area_cube, surface_area_sphere
-
-print(surface_area_cube(4))  # Output: 96.0
-print(surface_area_sphere(2))  # Output: 50.26548245743669
+>>> from main import surface_area_cube
+>>> surface_area_cube(2)
+24
 ```
 
 ## Function Descriptions
-### surface_area_cube(side_length: float) -> float
-Calculate the Surface Area of a Cube.
 
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
-Calculate the Surface Area of a Cuboid.
+### `surface_area_cube(side_length: float) -> float`
+Calculates the Surface Area of a Cube.
 
-### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere.
+### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+Calculates the Surface Area of a Cuboid.
 
-### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere.
+### `surface_area_sphere(radius: float) -> float`
+Calculates the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
+
+### `surface_area_hemisphere(radius: float) -> float`
+Calculates the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-* All functions in this script assume non-negative input values.
-* The surface area of a cube is calculated as 6 times the square of its side length.
-* The surface area of a cuboid is calculated as twice the sum of the products of its adjacent sides' lengths.
-* The surface area of a sphere is calculated as 4 times pi times the square of its radius.
-* The surface area of a hemisphere is calculated as 3 times pi times the square of its radius.+* All functions in this file only accept non-negative values for their inputs. Any attempt to pass negative values will raise a ValueError.
+* The formulas used for calculating surface areas are based on mathematical principles and are accurate for the respective shapes.
+* Developers using or maintaining this code should ensure that they understand the logic behind each function, including error handling for invalid input.
```

### Comparison: Run 6 vs Run 7
**Similarity:** 20.08%

**Diff:**
```diff
--- Run 6+++ Run 7@@ -1,44 +1,54 @@ # main.py
 ## Summary
-This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions to compute the surface area based on the input dimensions.
 
 ## Example
 ```python
-print(surface_area_cube(4))
+import doctest
+
+def surface_area_cube(side_length: float) -> float:
+    """
+    Calculate the Surface Area of a Cube.
+
+    >>> surface_area_cube(1)
+    6
+    >>> surface_area_cube(1.6)
+    15.360000000000003
+    >>> surface_area_cube(0)
+    0
+    >>> surface_area_cube(3)
+    54
+    >>> surface_area_cube(-1)
+    Traceback (most recent call last):
+        ...
+    ValueError: surface_area_cube() only accepts non-negative values
+    """
+    if side_length < 0:
+        raise ValueError("surface_area_cube() only accepts non-negative values")
+    return 6 * side_length**2
+
+print(surface_area_cube(4))  # Output: 96
 ```
 
 ## Function Descriptions
 
 ### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
-#### Parameters:
-- side_length (float): The length of one side of the cube.
-#### Returns:
-- float: The surface area of the cube.
 
 ### surface_area_cuboid(length: float, breadth: float, height: float) -> float
 Calculate the Surface Area of a Cuboid.
-#### Parameters:
-- length (float): The length of the cuboid.
-- breadth (float): The breadth of the cuboid.
-- height (float): The height of the cuboid.
-#### Returns:
-- float: The surface area of the cuboid.
 
 ### surface_area_sphere(radius: float) -> float
 Calculate the Surface Area of a Sphere.
-#### Parameters:
-- radius (float): The radius of the sphere.
-#### Returns:
-- float: The surface area of the sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
+Formula: 4 * pi * r^2
 
 ### surface_area_hemisphere(radius: float) -> float
 Calculate the Surface Area of a Hemisphere.
-#### Parameters:
-- radius (float): The radius of the hemisphere.
-#### Returns:
-- float: The surface area of the hemisphere.
+Formula: 3 * pi * r^2
 
 ## Important Takeaways
-- All functions raise a ValueError if any dimension is negative.
-- The formulas used are based on Wikipedia references for the respective shapes.+
+* All functions raise a ValueError if the input values are negative.
+* The formulas used for calculating the surface area are based on mathematical principles and are accurate for non-negative input values.
+* This script provides a simple way to calculate the surface area of various geometric shapes, making it useful for educational or practical purposes.
```

### Comparison: Run 6 vs Run 8
**Similarity:** 67.42%

**Diff:**
```diff
--- Run 6+++ Run 8@@ -4,41 +4,38 @@ 
 ## Example
 ```python
-print(surface_area_cube(4))
+>>> print(surface_area_cube(5))
+150.0
 ```
+## Function Descriptions
+### `surface_area_cube(side_length: float) -> float`
 
-## Function Descriptions
+Calculate the Surface Area of a Cube.
 
-### surface_area_cube(side_length: float) -> float
-Calculate the Surface Area of a Cube.
-#### Parameters:
-- side_length (float): The length of one side of the cube.
-#### Returns:
-- float: The surface area of the cube.
+*   `side_length`: The length of one side of the cube.
+*   Returns: The surface area of the cube.
 
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
+### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+
 Calculate the Surface Area of a Cuboid.
-#### Parameters:
-- length (float): The length of the cuboid.
-- breadth (float): The breadth of the cuboid.
-- height (float): The height of the cuboid.
-#### Returns:
-- float: The surface area of the cuboid.
 
-### surface_area_sphere(radius: float) -> float
+*   `length`, `breadth`, `height`: The dimensions of the cuboid.
+*   Returns: The surface area of the cuboid.
+
+### `surface_area_sphere(radius: float) -> float`
+
 Calculate the Surface Area of a Sphere.
-#### Parameters:
-- radius (float): The radius of the sphere.
-#### Returns:
-- float: The surface area of the sphere.
 
-### surface_area_hemisphere(radius: float) -> float
+*   `radius`: The radius of the sphere.
+*   Returns: The surface area of the sphere.
+
+### `surface_area_hemisphere(radius: float) -> float`
+
 Calculate the Surface Area of a Hemisphere.
-#### Parameters:
-- radius (float): The radius of the hemisphere.
-#### Returns:
-- float: The surface area of the hemisphere.
+
+*   `radius`: The radius of the hemisphere.
+*   Returns: The surface area of the hemisphere.
 
 ## Important Takeaways
-- All functions raise a ValueError if any dimension is negative.
-- The formulas used are based on Wikipedia references for the respective shapes.+*   All functions expect non-negative input values, and raising negative values will result in a ValueError.
+*   The surface areas are calculated using the respective formulas for each shape.
```

### Comparison: Run 6 vs Run 9
**Similarity:** 15.30%

**Diff:**
```diff
--- Run 6+++ Run 9@@ -1,44 +1,25 @@ # main.py
 ## Summary
-This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions for each shape to compute their respective surface areas.
 
 ## Example
 ```python
-print(surface_area_cube(4))
+import doctest
+
+def test_surface_area_cube():
+    return doctest.testmod(surface_area_cube)
+
+test_surface_area_cube()
 ```
-
 ## Function Descriptions
 
-### surface_area_cube(side_length: float) -> float
-Calculate the Surface Area of a Cube.
-#### Parameters:
-- side_length (float): The length of one side of the cube.
-#### Returns:
-- float: The surface area of the cube.
-
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
-Calculate the Surface Area of a Cuboid.
-#### Parameters:
-- length (float): The length of the cuboid.
-- breadth (float): The breadth of the cuboid.
-- height (float): The height of the cuboid.
-#### Returns:
-- float: The surface area of the cuboid.
-
-### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere.
-#### Parameters:
-- radius (float): The radius of the sphere.
-#### Returns:
-- float: The surface area of the sphere.
-
-### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere.
-#### Parameters:
-- radius (float): The radius of the hemisphere.
-#### Returns:
-- float: The surface area of the hemisphere.
+*   **surface_area_cube(side_length: float) -> float**: Calculate the Surface Area of a Cube.
+*   **surface_area_cuboid(length: float, breadth: float, height: float) -> float**: Calculate the Surface Area of a Cuboid.
+*   **surface_area_sphere(radius: float) -> float**: Calculate the Surface Area of a Sphere.
+*   **surface_area_hemisphere(radius: float) -> float**: Calculate the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-- All functions raise a ValueError if any dimension is negative.
-- The formulas used are based on Wikipedia references for the respective shapes.+
+*   All functions accept non-negative values for their respective dimensions. Any negative value will raise a `ValueError`.
+*   The formulas used to calculate surface areas are based on the Wikipedia references provided.
+*   The code uses the `math` module for mathematical constants and functions like `pi`, `sqrt`, and `tan`.
```

### Comparison: Run 6 vs Run 10
**Similarity:** 43.39%

**Diff:**
```diff
--- Run 6+++ Run 10@@ -1,44 +1,30 @@ # main.py
 ## Summary
-This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas based on the given dimensions.
 
 ## Example
 ```python
-print(surface_area_cube(4))
+>>> from main import surface_area_cube
+>>> surface_area_cube(2)
+24
 ```
 
 ## Function Descriptions
 
-### surface_area_cube(side_length: float) -> float
-Calculate the Surface Area of a Cube.
-#### Parameters:
-- side_length (float): The length of one side of the cube.
-#### Returns:
-- float: The surface area of the cube.
+### `surface_area_cube(side_length: float) -> float`
+Calculates the Surface Area of a Cube.
 
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
-Calculate the Surface Area of a Cuboid.
-#### Parameters:
-- length (float): The length of the cuboid.
-- breadth (float): The breadth of the cuboid.
-- height (float): The height of the cuboid.
-#### Returns:
-- float: The surface area of the cuboid.
+### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+Calculates the Surface Area of a Cuboid.
 
-### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere.
-#### Parameters:
-- radius (float): The radius of the sphere.
-#### Returns:
-- float: The surface area of the sphere.
+### `surface_area_sphere(radius: float) -> float`
+Calculates the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
 
-### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere.
-#### Parameters:
-- radius (float): The radius of the hemisphere.
-#### Returns:
-- float: The surface area of the hemisphere.
+### `surface_area_hemisphere(radius: float) -> float`
+Calculates the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-- All functions raise a ValueError if any dimension is negative.
-- The formulas used are based on Wikipedia references for the respective shapes.+* All functions in this file only accept non-negative values for their inputs. Any attempt to pass negative values will raise a ValueError.
+* The formulas used for calculating surface areas are based on mathematical principles and are accurate for the respective shapes.
+* Developers using or maintaining this code should ensure that they understand the logic behind each function, including error handling for invalid input.
```

### Comparison: Run 7 vs Run 8
**Similarity:** 42.97%

**Diff:**
```diff
--- Run 7+++ Run 8@@ -1,54 +1,41 @@ # main.py
 ## Summary
-This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions to compute the surface area based on the input dimensions.
+This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
 
 ## Example
 ```python
-import doctest
+>>> print(surface_area_cube(5))
+150.0
+```
+## Function Descriptions
+### `surface_area_cube(side_length: float) -> float`
 
-def surface_area_cube(side_length: float) -> float:
-    """
-    Calculate the Surface Area of a Cube.
-
-    >>> surface_area_cube(1)
-    6
-    >>> surface_area_cube(1.6)
-    15.360000000000003
-    >>> surface_area_cube(0)
-    0
-    >>> surface_area_cube(3)
-    54
-    >>> surface_area_cube(-1)
-    Traceback (most recent call last):
-        ...
-    ValueError: surface_area_cube() only accepts non-negative values
-    """
-    if side_length < 0:
-        raise ValueError("surface_area_cube() only accepts non-negative values")
-    return 6 * side_length**2
-
-print(surface_area_cube(4))  # Output: 96
-```
-
-## Function Descriptions
-
-### surface_area_cube(side_length: float) -> float
 Calculate the Surface Area of a Cube.
 
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
+*   `side_length`: The length of one side of the cube.
+*   Returns: The surface area of the cube.
+
+### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+
 Calculate the Surface Area of a Cuboid.
 
-### surface_area_sphere(radius: float) -> float
+*   `length`, `breadth`, `height`: The dimensions of the cuboid.
+*   Returns: The surface area of the cuboid.
+
+### `surface_area_sphere(radius: float) -> float`
+
 Calculate the Surface Area of a Sphere.
-Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
-Formula: 4 * pi * r^2
 
-### surface_area_hemisphere(radius: float) -> float
+*   `radius`: The radius of the sphere.
+*   Returns: The surface area of the sphere.
+
+### `surface_area_hemisphere(radius: float) -> float`
+
 Calculate the Surface Area of a Hemisphere.
-Formula: 3 * pi * r^2
+
+*   `radius`: The radius of the hemisphere.
+*   Returns: The surface area of the hemisphere.
 
 ## Important Takeaways
-
-* All functions raise a ValueError if the input values are negative.
-* The formulas used for calculating the surface area are based on mathematical principles and are accurate for non-negative input values.
-* This script provides a simple way to calculate the surface area of various geometric shapes, making it useful for educational or practical purposes.+*   All functions expect non-negative input values, and raising negative values will result in a ValueError.
+*   The surface areas are calculated using the respective formulas for each shape.
```

### Comparison: Run 7 vs Run 9
**Similarity:** 19.03%

**Diff:**
```diff
--- Run 7+++ Run 9@@ -1,54 +1,25 @@ # main.py
 ## Summary
-This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions to compute the surface area based on the input dimensions.
+This file calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions for each shape to compute their respective surface areas.
 
 ## Example
 ```python
 import doctest
 
-def surface_area_cube(side_length: float) -> float:
-    """
-    Calculate the Surface Area of a Cube.
+def test_surface_area_cube():
+    return doctest.testmod(surface_area_cube)
 
-    >>> surface_area_cube(1)
-    6
-    >>> surface_area_cube(1.6)
-    15.360000000000003
-    >>> surface_area_cube(0)
-    0
-    >>> surface_area_cube(3)
-    54
-    >>> surface_area_cube(-1)
-    Traceback (most recent call last):
-        ...
-    ValueError: surface_area_cube() only accepts non-negative values
-    """
-    if side_length < 0:
-        raise ValueError("surface_area_cube() only accepts non-negative values")
-    return 6 * side_length**2
-
-print(surface_area_cube(4))  # Output: 96
+test_surface_area_cube()
 ```
-
 ## Function Descriptions
 
-### surface_area_cube(side_length: float) -> float
-Calculate the Surface Area of a Cube.
-
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
-Calculate the Surface Area of a Cuboid.
-
-### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere.
-Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
-Formula: 4 * pi * r^2
-
-### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere.
-Formula: 3 * pi * r^2
+*   **surface_area_cube(side_length: float) -> float**: Calculate the Surface Area of a Cube.
+*   **surface_area_cuboid(length: float, breadth: float, height: float) -> float**: Calculate the Surface Area of a Cuboid.
+*   **surface_area_sphere(radius: float) -> float**: Calculate the Surface Area of a Sphere.
+*   **surface_area_hemisphere(radius: float) -> float**: Calculate the Surface Area of a Hemisphere.
 
 ## Important Takeaways
 
-* All functions raise a ValueError if the input values are negative.
-* The formulas used for calculating the surface area are based on mathematical principles and are accurate for non-negative input values.
-* This script provides a simple way to calculate the surface area of various geometric shapes, making it useful for educational or practical purposes.+*   All functions accept non-negative values for their respective dimensions. Any negative value will raise a `ValueError`.
+*   The formulas used to calculate surface areas are based on the Wikipedia references provided.
+*   The code uses the `math` module for mathematical constants and functions like `pi`, `sqrt`, and `tan`.
```

### Comparison: Run 7 vs Run 10
**Similarity:** 47.21%

**Diff:**
```diff
--- Run 7+++ Run 10@@ -1,54 +1,30 @@ # main.py
 ## Summary
-This Python script calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions to compute the surface area based on the input dimensions.
+This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas based on the given dimensions.
 
 ## Example
 ```python
-import doctest
-
-def surface_area_cube(side_length: float) -> float:
-    """
-    Calculate the Surface Area of a Cube.
-
-    >>> surface_area_cube(1)
-    6
-    >>> surface_area_cube(1.6)
-    15.360000000000003
-    >>> surface_area_cube(0)
-    0
-    >>> surface_area_cube(3)
-    54
-    >>> surface_area_cube(-1)
-    Traceback (most recent call last):
-        ...
-    ValueError: surface_area_cube() only accepts non-negative values
-    """
-    if side_length < 0:
-        raise ValueError("surface_area_cube() only accepts non-negative values")
-    return 6 * side_length**2
-
-print(surface_area_cube(4))  # Output: 96
+>>> from main import surface_area_cube
+>>> surface_area_cube(2)
+24
 ```
 
 ## Function Descriptions
 
-### surface_area_cube(side_length: float) -> float
-Calculate the Surface Area of a Cube.
+### `surface_area_cube(side_length: float) -> float`
+Calculates the Surface Area of a Cube.
 
-### surface_area_cuboid(length: float, breadth: float, height: float) -> float
-Calculate the Surface Area of a Cuboid.
+### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+Calculates the Surface Area of a Cuboid.
 
-### surface_area_sphere(radius: float) -> float
-Calculate the Surface Area of a Sphere.
+### `surface_area_sphere(radius: float) -> float`
+Calculates the Surface Area of a Sphere.
 Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
-Formula: 4 * pi * r^2
 
-### surface_area_hemisphere(radius: float) -> float
-Calculate the Surface Area of a Hemisphere.
-Formula: 3 * pi * r^2
+### `surface_area_hemisphere(radius: float) -> float`
+Calculates the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-
-* All functions raise a ValueError if the input values are negative.
-* The formulas used for calculating the surface area are based on mathematical principles and are accurate for non-negative input values.
-* This script provides a simple way to calculate the surface area of various geometric shapes, making it useful for educational or practical purposes.+* All functions in this file only accept non-negative values for their inputs. Any attempt to pass negative values will raise a ValueError.
+* The formulas used for calculating surface areas are based on mathematical principles and are accurate for the respective shapes.
+* Developers using or maintaining this code should ensure that they understand the logic behind each function, including error handling for invalid input.
```

### Comparison: Run 8 vs Run 9
**Similarity:** 16.30%

**Diff:**
```diff
--- Run 8+++ Run 9@@ -1,41 +1,25 @@ # main.py
 ## Summary
-This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This file calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions for each shape to compute their respective surface areas.
 
 ## Example
 ```python
->>> print(surface_area_cube(5))
-150.0
+import doctest
+
+def test_surface_area_cube():
+    return doctest.testmod(surface_area_cube)
+
+test_surface_area_cube()
 ```
 ## Function Descriptions
-### `surface_area_cube(side_length: float) -> float`
 
-Calculate the Surface Area of a Cube.
-
-*   `side_length`: The length of one side of the cube.
-*   Returns: The surface area of the cube.
-
-### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-
-Calculate the Surface Area of a Cuboid.
-
-*   `length`, `breadth`, `height`: The dimensions of the cuboid.
-*   Returns: The surface area of the cuboid.
-
-### `surface_area_sphere(radius: float) -> float`
-
-Calculate the Surface Area of a Sphere.
-
-*   `radius`: The radius of the sphere.
-*   Returns: The surface area of the sphere.
-
-### `surface_area_hemisphere(radius: float) -> float`
-
-Calculate the Surface Area of a Hemisphere.
-
-*   `radius`: The radius of the hemisphere.
-*   Returns: The surface area of the hemisphere.
+*   **surface_area_cube(side_length: float) -> float**: Calculate the Surface Area of a Cube.
+*   **surface_area_cuboid(length: float, breadth: float, height: float) -> float**: Calculate the Surface Area of a Cuboid.
+*   **surface_area_sphere(radius: float) -> float**: Calculate the Surface Area of a Sphere.
+*   **surface_area_hemisphere(radius: float) -> float**: Calculate the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-*   All functions expect non-negative input values, and raising negative values will result in a ValueError.
-*   The surface areas are calculated using the respective formulas for each shape.+
+*   All functions accept non-negative values for their respective dimensions. Any negative value will raise a `ValueError`.
+*   The formulas used to calculate surface areas are based on the Wikipedia references provided.
+*   The code uses the `math` module for mathematical constants and functions like `pi`, `sqrt`, and `tan`.
```

### Comparison: Run 8 vs Run 10
**Similarity:** 47.49%

**Diff:**
```diff
--- Run 8+++ Run 10@@ -1,41 +1,30 @@ # main.py
 ## Summary
-This file contains functions to calculate the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres.
+This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas based on the given dimensions.
 
 ## Example
 ```python
->>> print(surface_area_cube(5))
-150.0
+>>> from main import surface_area_cube
+>>> surface_area_cube(2)
+24
 ```
+
 ## Function Descriptions
+
 ### `surface_area_cube(side_length: float) -> float`
-
-Calculate the Surface Area of a Cube.
-
-*   `side_length`: The length of one side of the cube.
-*   Returns: The surface area of the cube.
+Calculates the Surface Area of a Cube.
 
 ### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
-
-Calculate the Surface Area of a Cuboid.
-
-*   `length`, `breadth`, `height`: The dimensions of the cuboid.
-*   Returns: The surface area of the cuboid.
+Calculates the Surface Area of a Cuboid.
 
 ### `surface_area_sphere(radius: float) -> float`
-
-Calculate the Surface Area of a Sphere.
-
-*   `radius`: The radius of the sphere.
-*   Returns: The surface area of the sphere.
+Calculates the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
 
 ### `surface_area_hemisphere(radius: float) -> float`
-
-Calculate the Surface Area of a Hemisphere.
-
-*   `radius`: The radius of the hemisphere.
-*   Returns: The surface area of the hemisphere.
+Calculates the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-*   All functions expect non-negative input values, and raising negative values will result in a ValueError.
-*   The surface areas are calculated using the respective formulas for each shape.+* All functions in this file only accept non-negative values for their inputs. Any attempt to pass negative values will raise a ValueError.
+* The formulas used for calculating surface areas are based on mathematical principles and are accurate for the respective shapes.
+* Developers using or maintaining this code should ensure that they understand the logic behind each function, including error handling for invalid input.
```

### Comparison: Run 9 vs Run 10
**Similarity:** 38.93%

**Diff:**
```diff
--- Run 9+++ Run 10@@ -1,25 +1,30 @@ # main.py
 ## Summary
-This file calculates the surface areas of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It provides functions for each shape to compute their respective surface areas.
+This Python file calculates the surface area of various geometric shapes, including cubes, cuboids, spheres, and hemispheres. It uses mathematical formulas to compute these areas based on the given dimensions.
 
 ## Example
 ```python
-import doctest
+>>> from main import surface_area_cube
+>>> surface_area_cube(2)
+24
+```
 
-def test_surface_area_cube():
-    return doctest.testmod(surface_area_cube)
-
-test_surface_area_cube()
-```
 ## Function Descriptions
 
-*   **surface_area_cube(side_length: float) -> float**: Calculate the Surface Area of a Cube.
-*   **surface_area_cuboid(length: float, breadth: float, height: float) -> float**: Calculate the Surface Area of a Cuboid.
-*   **surface_area_sphere(radius: float) -> float**: Calculate the Surface Area of a Sphere.
-*   **surface_area_hemisphere(radius: float) -> float**: Calculate the Surface Area of a Hemisphere.
+### `surface_area_cube(side_length: float) -> float`
+Calculates the Surface Area of a Cube.
+
+### `surface_area_cuboid(length: float, breadth: float, height: float) -> float`
+Calculates the Surface Area of a Cuboid.
+
+### `surface_area_sphere(radius: float) -> float`
+Calculates the Surface Area of a Sphere.
+Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
+
+### `surface_area_hemisphere(radius: float) -> float`
+Calculates the Surface Area of a Hemisphere.
 
 ## Important Takeaways
-
-*   All functions accept non-negative values for their respective dimensions. Any negative value will raise a `ValueError`.
-*   The formulas used to calculate surface areas are based on the Wikipedia references provided.
-*   The code uses the `math` module for mathematical constants and functions like `pi`, `sqrt`, and `tan`.+* All functions in this file only accept non-negative values for their inputs. Any attempt to pass negative values will raise a ValueError.
+* The formulas used for calculating surface areas are based on mathematical principles and are accurate for the respective shapes.
+* Developers using or maintaining this code should ensure that they understand the logic behind each function, including error handling for invalid input.
```

## Overall Test Accuracy Summary

**Test Accuracy Metrics:**
- **Average Similarity to First Run:** 33.5%
- **Minimum Similarity to First Run:** 10.4%
- **Maximum Similarity to First Run:** 52.3%
- **Consistency Range:** 41.8%

**Interpretation:** 🔴 **Low Consistency** - Model shows significant variation across runs.


# Project Structure

## Directory: 0x0C-python-almost_a_circle

### File: models/base.py

This file contains a class Base. It is the 'base' of all other classes in this project. The main goal is to manage the 'id' attribute to avoid code duplication.

### File: models/rectangle.py

This file contains the Rectangle class that implements the base class.

### File: models/square.py

In this file, you'll find a class called Square, which implements the class Rectangle.

### File: models/**init**.py

The presence of this file in a directory makes it a Python module.

## Directory: tests

This folder contains the test files and folders for this project.

### Directory: tests/test_models

This subdirectory has unit tests specifically created for the model folder. Still being Implemented.

#### File: tests/test_base.py

This test case is designed to evaluate the functionality of base.py.

#### File: tests/test_rectangle.py

Similar to test_base.py, this test case focuses on assessing the functionality of rectangle.py.

#### File: tests/test_square.py

This test case assesses the behaviors and functionalities of square.py and the Square class.

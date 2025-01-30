import pytest
from sympy import S, Symbol
from sympy.core.sympify import SympifyError
from HelperFunctions import replace_log, drawUserFunctions  # Replace `your_module` with the file name of your module.

# Define a fixture for a symbolic variable
@pytest.fixture
def x():
    return Symbol("x")


# Test replace_log function
@pytest.mark.parametrize(
    "input_expression, expected_output",
    [
        ("log2(x)", "log(x, 2)"),
        ("log10(y)", "log(y, 10)"),
        ("log5(a + b)", "log(a + b, 5)"),
        ("x + log3(y) + log4(z)", "x + log(y, 3) + log(z, 4)"),
        ("sin(x) + log(x)", "sin(x) + log(x)"),  # Ensure no unnecessary changes
    ],
)
def test_replace_log(input_expression, expected_output):
    assert replace_log(input_expression) == expected_output


# Test drawUserFunctions for expected behaviors
@pytest.mark.parametrize(
    "exp1, exp2, resolution, expected_x_range",
    [
        ("x**2", "x", 10, (-1, 2)),  # Expect range when no intersections
        ("x**2", "x**2", 10, (-100, 100)),  # Same functions, limited range
        ("log2(x)", "x", 10, (-100, 100)),  # Handles logarithmic expressions
    ],
)
def test_drawUserFunctions(exp1, exp2, resolution, expected_x_range, x):
    result = drawUserFunctions(exp1, exp2, resolution)
    x_vals, y1, y2, points_to_annotate = result

    # Check x range
    assert min(x_vals) == expected_x_range[0]
    assert max(x_vals) == expected_x_range[1]



    if exp1 == exp2:
        assert len(points_to_annotate) == 0


# Test invalid inputs to drawUserFunctions
@pytest.mark.parametrize(
    "exp1, exp2, resolution",
    [
        ("x**2", "1/0", 10),  # Division by zero in the expression
        ("x**2", "x + 1", -5),  # Negative resolution
        ("x**2", "invalid expression", 10),  # Invalid sympy expression
    ],
)
def test_drawUserFunctions_exceptions(exp1, exp2, resolution):
    with pytest.raises((SympifyError, ValueError)):
        drawUserFunctions(exp1, exp2, resolution)




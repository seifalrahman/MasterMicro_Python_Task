import pytest
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication
from main import Window  # Replace 'main' with the filename where your Window class is defined
from unittest.mock import patch
from PySide2.QtWidgets import  QMessageBox
@pytest.fixture
def app(qtbot):
    # Create the application window
    window = Window()
    qtbot.addWidget(window)
    window.show()
    return window

def test_window_initialization(app):
    """Test if the window initializes correctly."""
    assert app.windowTitle() == "Master Equations Solver"
    assert app.txtbox1.placeholderText() == "Enter your first Equation "
    assert app.txtbox2.placeholderText() == "Enter your Second Equation "
    assert not app.solve_button.isEnabled()  # Solve button should be disabled
    assert not app.info1_button.isEnabled()  # Info1 button should be disabled
    assert not app.info2_button.isEnabled()  # Info2 button should be disabled



def test_quit_button(qtbot, app):
    """Test the functionality of the Exit button."""
    button = app.layout.itemAtPosition(7, 7).widget()
    assert button.text() == "Exit"

    # Mock the quitApp method
    with patch.object(app, "quitApp") as mocked_quitApp:
        qtbot.mouseClick(button, Qt.LeftButton)

    # Assert the method was called
    mocked_quitApp.assert_called_once()

def test_solve_button(qtbot, app):
    """Test the functionality of the Solve button."""
    button = app.layout.itemAtPosition(6, 2).widget()
    assert button.text() == "Solve"

    # Simulate entering text and clicking the button
    qtbot.keyClicks(app.txtbox1, "x**2 - 4")
    qtbot.keyClicks(app.txtbox2, "x + 2")
    qtbot.mouseClick(button, Qt.LeftButton)

    # Assert that the plot is added to the layout
    assert app.layout.itemAtPosition(3, 5) is not None
    assert app.layout.itemAtPosition(2, 5) is not None

def test_textbox_inputs(qtbot, app):
    """Test user inputs in the textboxes."""
    qtbot.keyClicks(app.txtbox1, "x**2 - 4")
    qtbot.keyClicks(app.txtbox2, "x + 2")

    assert app.txtbox1.text() == "x**2 - 4"
    assert app.txtbox2.text() == "x + 2"


def test_text_input_and_button_state(app, qtbot):
    """Test that buttons are enabled/disabled based on text input."""
    # Simulate entering text in the first textbox
    qtbot.keyClicks(app.txtbox1, "x")
    assert app.info1_button.isEnabled()  # Info1 button should be enabled
    assert not app.solve_button.isEnabled()  # Solve button should still be disabled

    # Simulate entering text in the second textbox
    qtbot.keyClicks(app.txtbox2, "x**2")
    assert app.solve_button.isEnabled()  # Solve button should be enabled
    assert app.info2_button.isEnabled()  # Info2 button should be enabled

    # Clear the first textbox
    app.txtbox1.clear()
    assert not app.solve_button.isEnabled()  # Solve button should be disabled
    assert not app.info1_button.isEnabled()  # Info1 button should be disabled



def test_info_buttons(app, qtbot):
    """Test that clicking the info buttons opens new windows."""
    # Enter valid equations
    qtbot.keyClicks(app.txtbox1, "x")
    qtbot.keyClicks(app.txtbox2, "x**2")

    # Click the info1 button
    qtbot.mouseClick(app.info1_button, Qt.LeftButton)
    assert app.smallWindow1 is not None  # Ensure the window is created
    assert app.smallWindow1.isVisible()  # Ensure the window is visible

    # Click the info2 button
    qtbot.mouseClick(app.info2_button, Qt.LeftButton)
    assert app.smallWindow2 is not None  # Ensure the window is created
    assert app.smallWindow2.isVisible()  # Ensure the window is visible


def test_input_validation_with_log_functions(app, qtbot):
    """Test that invalid input disables buttons and shows a warning."""
    # Enter valid input with log10(x)
    qtbot.keyClicks(app.txtbox1, "log10(x) + x^2")

    assert app.info1_button.isEnabled()  # Info1 button should be enabled
    app.txtbox1.clear()
    # Enter invalid input (using 'y' instead of 'x')
    qtbot.keyClicks(app.txtbox1, "log10(y) + y^2")
    qtbot.mouseClick(app.info1_button, Qt.LeftButton)



    assert not app.info1_button.isEnabled()  # Info1 button should be disabled
    app.txtbox1.clear()
    #qtbot.mouseClick(app.warning.button(QMessageBox.Ok), Qt.LeftButton)
    # Check that the textbox border is red
    assert "red" in app.txtbox1.styleSheet()


    # Enter valid input with log2(x)
    qtbot.keyClicks(app.txtbox1, "log2(x) + 3")
    qtbot.mouseClick(app.info1_button, Qt.LeftButton)

    assert app.info1_button.isEnabled()  # Info1 button should be enabled

    # Check that the textbox border is reset
    assert "red" not in app.txtbox1.styleSheet()
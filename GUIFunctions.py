from PySide2.QtWidgets import QGridLayout,\
                            QApplication ,\
                            QMainWindow ,\
                            QMessageBox,\
                            QDesktopWidget,\
                            QPushButton,\
                            QWidget,\
                            QLineEdit,\
                            QVBoxLayout,\
                            QHBoxLayout,\
                            QSpacerItem,\
                            QSizePolicy

from sympy import  Symbol , sympify,diff,integrate
import random
import sys
from PySide2.QtGui import QIcon , QPalette, QBrush, QPixmap
from HelperFunctions import drawUserFunctions ,drawInfoFunctions ,replace_log ,insert_multiplication_operator
from PySide2.QtCore import Qt
import re
myApp = QApplication(sys.argv)
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg , NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

 def __init__(self, parent=None, width=5, height=4, dpi=100):
     fig = Figure(figsize=(width, height), dpi=dpi)
     self.axes = fig.add_subplot(111)
     super().__init__(fig)


class Window (QMainWindow) :

    def __init__(self):
        super().__init__()
        self.smallWindow1=None
        self.smallWindow2=None
        self.txtbox1 = QLineEdit()
        self.txtbox2 = QLineEdit()
        self.warning=None
        self.txtbox1.setStyleSheet("""
                  QLineEdit {
                      border: 2px solid #3498db;
                      border-radius: 10px;
                      padding: 5px;
                      font-size: 18px;
                  }
              """)
        self.txtbox2.setStyleSheet("""
                          QLineEdit {
                              border: 2px solid #3498db;
                              border-radius: 10px;
                              padding: 5px;
                              font-size: 18px;
                          }
                      """)
        self.vertical_spacer = QSpacerItem(20, 240, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.layout=QGridLayout()
        self.setWindowTitle("Master Equations Solver")
        self.setGeometry(700,300,700,700)
        self.setIcon()
        self.setQuitButton()
        self.center()
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.setQLineEdit()
        self.solve_button = None
        self.setEnterButton()
        self.info1_button = None
        self.setInfo1()
        self.info2_button = None
        self.setInfo2()

        self.background_image_path = "Background.jpg"
        self.set_background_image()

        self.txtbox1.textChanged.connect(self.check_inputs)
        self.txtbox2.textChanged.connect(self.check_inputs)

    def setIcon(self):
        appIcon = QIcon("img.png")
        self.setWindowIcon(appIcon)
    def quitApp (self):
        userinfo = QMessageBox.question(self ,"Confirmation" , "Do you want to quit the application ?"
                                        ,QMessageBox.Yes| QMessageBox.No)
        if userinfo == QMessageBox.Yes :
            myApp.quit()
        elif userinfo == QMessageBox.No :
            pass
    def setQuitButton (self):
        btn1 = QPushButton("Exit" ,self)
        self.layout.addWidget(btn1,7,7)
        btn1.setFixedWidth(70)
        btn1.setFixedHeight(28)
        btn1.clicked.connect (self.quitApp)
        btn1.setStyleSheet("""
                          QPushButton {
                              border: 2px solid #3498db;
                              border-radius: 7px;
                              padding: 5px;
                              font-size: 18px;
                              background-color :white
                          }
                      """)

    def setEnterButton (self):
        self.solve_button = QPushButton("Solve", self)
        self.layout.addWidget(self.solve_button, 6, 2)
        self.solve_button.setFixedWidth(70)
        self.solve_button.setFixedHeight(28)
        self.solve_button.clicked.connect(self.SolveEquations)
        self.solve_button.setStyleSheet("""
                          QPushButton {
                              border: 2px solid #3498db;
                              border-radius: 7px;
                              padding: 5px;
                              font-size: 18px;
                              background-color :white
                          }
                      """)
        self.solve_button.setEnabled(False)

    def setInfo1(self):
        self.info1_button = QPushButton("Info",self)
        self.layout.addWidget(self.info1_button, 2, 3)
        self.info1_button.setFixedWidth(70)
        self.info1_button.setFixedHeight(28)
        self.info1_button.clicked.connect(self.showWindow1)
        self.info1_button.setStyleSheet("""
                          QPushButton {
                              border: 2px solid #3498db;
                              border-radius: 7px;
                              padding: 5px;
                              font-size: 18px;
                              background-color :white
                          }
                      """)
        self.info1_button.setEnabled(False)
    def show_warning(self, message):
        """
        Display a warning message to the user.
        """
        self.warning=QMessageBox
        self.warning.warning(self, "Invalid Input", message)
    def setInfo2(self):

        self.info2_button = QPushButton("Info",self)
        self.layout.addWidget(self.info2_button, 4, 3)
        self.info2_button.setFixedWidth(70)
        self.info2_button.setFixedHeight(28)
        self.info2_button.clicked.connect(self.showWindow2)
        self.info2_button.setStyleSheet("""
                          QPushButton {
                              border: 2px solid #3498db;
                              border-radius: 7px;
                              padding: 5px;
                              font-size: 18px;
                              background-color :white
                          }
                      """)
        self.info2_button.setEnabled(False)


    def showWindow1(self):
        if self.validate_input1():
            appIcon = QIcon("img.png")
            self.smallWindow1 = QWidget()
            graph=drawInfoFunctions(self.txtbox1.text(),200)
            sc = MplCanvas(self, width=4, height=3, dpi=100)
            sc.axes.clear()
            x = Symbol('x')
            expression = replace_log(self.txtbox1.text())
            expression = insert_multiplication_operator(expression)
            expression = sympify(expression)
            diffExp = diff(expression, x)
            integrateExp =integrate(expression, x)
            sc.axes.plot(graph[0], graph[1],label=f"Differentiated f{diffExp}")
            sc.axes.plot(graph[0], graph[2],label=f"Integrated f{integrateExp}")
            legend = sc.axes.get_legend()  # Get the current legend
            sc.axes.legend()
            sc.axes.legend()
            toolbar = NavigationToolbar(sc, self)

            smalllayout = QGridLayout()
            smalllayout.addWidget(toolbar,3,0)
            smalllayout.addWidget(sc,1,0)

            self.smallWindow1.setLayout(smalllayout)
            self.smallWindow1.show()
            self.smallWindow1.setWindowTitle("INFO")
            self.smallWindow1.setWindowIcon(appIcon)

    def showWindow2(self):
        if self.validate_input2():
            self.smallWindow2 = QWidget()
            appIcon = QIcon("img.png")
            graph=drawInfoFunctions(self.txtbox2.text(),200)
            sc = MplCanvas(self, width=4, height=3, dpi=100)
            x = Symbol('x')
            expression = replace_log(self.txtbox2.text())
            expression = insert_multiplication_operator(expression)
            expression = sympify(expression)
            diffExp = diff(expression, x)
            integrateExp =integrate(expression, x)
            sc.axes.plot(graph[0], graph[1],label=f"Differentiated f{diffExp}")
            sc.axes.plot(graph[0], graph[2],label=f"Integrated f{integrateExp}")
            sc.axes.legend()
            sc.axes.legend()
            toolbar = NavigationToolbar(sc, self)
            smalllayout = QVBoxLayout()
            smalllayout.addWidget(toolbar)
            smalllayout.addWidget(sc)
            self.smallWindow2.setLayout(smalllayout)
            self.smallWindow2.show()
            self.smallWindow2.setWindowTitle("INFO")
            self.smallWindow2.setWindowIcon(appIcon)

    def SolveEquations(self):
        if self.validate_input1() and self.validate_input2() :
            graph=drawUserFunctions(self.txtbox1.text(), self.txtbox2.text(), 1000)
            sc = MplCanvas(self, width=5, height=4, dpi=100)
            sc.axes.plot(graph[0], graph[1])
            sc.axes.plot(graph[0], graph[2])

            points_to_annotate=graph[3]
            i =1

            for point in points_to_annotate :
                print(point)
                sc.axes.annotate(
                    f"({point[0]}, {point[1]})",  # Annotation text
                    xy=point,  # Point to annotate
                    xytext=(point[0] + random.randint(-10, 10), point[1] + random.randint(-20, 10)),  # Position of text
                    textcoords='offset points',  # Text relative to point
                    arrowprops=dict(arrowstyle="->", color='blue'),  # Arrow properties
                    fontsize=10,
                    color='red'
                )
            toolbar = NavigationToolbar(sc, self)
            self.layout.addWidget(toolbar,2,5)
            self.layout.addWidget(sc, 3, 5)

    def setQLineEdit (self):
        self.layout.addWidget(self.txtbox1,2,2)
        self.layout.addItem(self.vertical_spacer,3,2)
        self.layout.addWidget(self.txtbox2, 4, 2)
        self.txtbox1.setPlaceholderText("Enter your first Equation ")
        self.txtbox2.setPlaceholderText("Enter your Second Equation ")
        self.txtbox1.returnPressed.connect(self.return_pressed1)
        self.txtbox2.returnPressed.connect(self.return_pressed2)

    def return_pressed1 (self):
        print("First Equation : " ,self.txtbox1.text())


    def return_pressed2(self):
        print("Second Equation : ", self.txtbox2.text())


    def center (self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def check_inputs(self):
        # Enable the solve button only if both textboxes have text
        if self.txtbox1.text() and self.txtbox2.text():
            self.solve_button.setEnabled(True)
        else:
            self.solve_button.setEnabled(False)
        if self.txtbox1.text() :
            self.info1_button.setEnabled(True)
        else:
            self.info1_button.setEnabled(False)

        if self.txtbox2.text() :
            self.info2_button.setEnabled(True)
        else:
            self.info2_button.setEnabled(False)



    def set_background_image(self):
        # Load the image
        self.pixmap = QPixmap(self.background_image_path)

        # Scale the pixmap to the size of the widget
        self.scaled_pixmap = self.pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        # Create a palette and set the scaled pixmap as the background
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(self.scaled_pixmap))

        # Apply the palette to the widget
        self.setPalette(palette)
    def resizeEvent(self, event):
        self.set_background_image()
        super().resizeEvent(event)

    def validate_input1(self):

        """
        Validate the input in txtbox1 to ensure only 'x' is used as a variable
        and only specific functions are allowed.
        """
        # Regular expression to allow numbers, 'x', basic math operators, and specific functions
        flag= True
        valid_pattern = re.compile(r'^([0-9]+|x|[-+*/^()]|log\d*\(x\)|log\(x\)|sin\(x\)|cos\(x\)|sqrt\(x\)|\s)+$')

        # Validate txtbox1
        if not valid_pattern.match(self.txtbox1.text()):
            self.show_warning(
                "Invalid input in Equation 1. Only 'x' is allowed as a variable, and only specific functions (logN, sin, cos) are supported.")
            self.txtbox1.setStyleSheet("border: 2px solid red; border-radius: 10px; padding: 5px; font-size: 18px;")
            self.solve_button.setEnabled(False)
            self.info1_button.setEnabled(False)
            flag= False

        else:
            self.txtbox1.setStyleSheet("border: 2px solid #3498db; border-radius: 10px; padding: 5px; font-size: 18px;")
            self.check_inputs()  # Re-enable buttons if input is valid

        return flag



    def validate_input2(self):
        valid_pattern = re.compile(r'^([0-9]+|x|[-+*/^()]|log\d*\(x\)|log\(x\)|sin\(x\)|cos\(x\)|sqrt\(x\)|\s)+$')
        flag=True
        # Validate txtbox2
        if not valid_pattern.match(self.txtbox2.text()):
            self.show_warning(
                "Invalid input in Equation 2. Only 'x' is allowed as a variable, and only specific functions (logN, sin, cos) are supported.")
            self.txtbox2.setStyleSheet("border: 2px solid red; border-radius: 10px; padding: 5px; font-size: 18px;")
            self.solve_button.setEnabled(False)
            self.info2_button.setEnabled(False)
            flag= False
        else:
            self.txtbox2.setStyleSheet("border: 2px solid #3498db; border-radius: 10px; padding: 5px; font-size: 18px;")
            self.check_inputs()  # Re-enable buttons if input is valid


        return  flag

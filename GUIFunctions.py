from PySide2.QtWidgets import QGridLayout,\
                            QApplication ,\
                            QMainWindow ,\
                            QMessageBox,\
                            QDesktopWidget,\
                            QPushButton,\
                            QWidget,\
                            QLineEdit


import sys
from PySide2.QtGui import QIcon , QPalette, QBrush, QPixmap
from HelperFunctions import drawUserFunctions

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
        self.txtbox1 = QLineEdit()
        self.txtbox2 = QLineEdit()
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
        self.setEnterButton()
        palette = QPalette()
        pixmap = QPixmap("C:\\MYCOMPUTER\\Leonardo_Phoenix_09_A_futuristic_and_minimalist_background_ima_1.jpg")

        palette.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(palette)

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
        btn1 = QPushButton("Solve", self)
        self.layout.addWidget(btn1, 6, 2)
        btn1.setFixedWidth(70)
        btn1.setFixedHeight(28)
        btn1.clicked.connect(self.SolveEquations)
        btn1.setStyleSheet("""
                          QPushButton {
                              border: 2px solid #3498db;
                              border-radius: 7px;
                              padding: 5px;
                              font-size: 18px;
                              background-color :white
                          }
                      """)

    def SolveEquations(self):
        graph=drawUserFunctions(self.txtbox1.text(), self.txtbox2.text(), 1000)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot(graph[0], graph[1])
        sc.axes.plot(graph[0], graph[2])

        points_to_annotate=graph[3]
        for point in points_to_annotate :
            sc.axes.annotate(
                f"({point[0]}, {point[1]})",  # Annotation text
                xy=point,  # Point to annotate
                xytext=(point[0] + 1, point[1] + 1),  # Position of text
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
        self.layout.addWidget(self.txtbox2, 5, 2)
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



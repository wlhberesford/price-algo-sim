import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QGuiApplication

def main():
   # Create the application instance
   app = QApplication(sys.argv)

   # Create the main window
   screen = QGuiApplication.primaryScreen()
   size= screen.geometry()

   window = QMainWindow()
   window.setWindowTitle("Price Algorithm Simulator")
   window.setGeometry(0, 0, size.width(), size.height())

   # Create a label widget
   label = QLabel("Hello, PyQt!", window)

   # Show the window
   window.show()

   # Execute the application
   sys.exit(app.exec())

if __name__ == "__main__":
   main()
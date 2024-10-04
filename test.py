import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton

# Create the main application
app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("GridLayout Example")

# Create a QGridLayout instance
grid_layout = QGridLayout()

# Create widgets
label_1 = QLabel("Label 1")
label_2 = QLabel("Label 2")
button_1 = QPushButton("Button 1")
button_2 = QPushButton("Button 2")

# Add widgets to the grid layout (widget, row, column, rowspan, colspan)
grid_layout.addWidget(label_1, 0, 0)        # Add label_1 at row 0, column 0
grid_layout.addWidget(label_2, 0, 1)        # Add label_2 at row 0, column 1
grid_layout.addWidget(button_1, 1, 0, 1, 2) # Add button_1 at row 1, column 0, spanning 1 row and 2 columns
grid_layout.addWidget(button_2, 2, 0)        # Add button_2 at row 2, column 0

# Set the layout on the main window
window.setLayout(grid_layout)

# Show the main window
window.show()

# Execute the application's event loop
sys.exit(app.exec())

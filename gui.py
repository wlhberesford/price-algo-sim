import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QListWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QWidget
from PyQt6.QtCore import Qt

class PriceAlgorithmSimulator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Price Algorithm Simulator")
        self.setGeometry(100, 100, 1000, 600)

        # Main Layout
        main_layout = QVBoxLayout()

        # Top Bar
        top_bar = QLabel("Price Algorithm Simulator")
        top_bar.setStyleSheet("background-color: red; color: black; font-size: 24px; padding: 10px;")
        top_bar.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(top_bar)

        # Horizontal Layout for Body
        body_layout = QHBoxLayout()

        # Left side - Competition and Player Selection
        left_layout = QVBoxLayout()

        # Competition List
        competition_label = QLabel("Select Competition")
        competition_label.setStyleSheet("background-color: red; color: black; padding: 5px; font-size: 18px;")
        left_layout.addWidget(competition_label)

        competition_list = QListWidget()
        competition_list.addItems(["- Bertrand.py", "- Cournot.py", "- Custom1.py", "- Custom2.py"])
        left_layout.addWidget(competition_list)

        # Player List
        player_label = QLabel("Select Players")
        player_label.setStyleSheet("background-color: red; color: black; padding: 5px; font-size: 18px;")
        left_layout.addWidget(player_label)

        player_list = QListWidget()
        player_list.addItems(["- DeepLearning.py", "- Regresion.py", "- Competitor.py", "- Rulebased1.py", "- Rulebased2.py"])
        left_layout.addWidget(player_list)

        body_layout.addLayout(left_layout)

        # Middle - Placeholder for Graph Visualization
        graph_label = QLabel()
        graph_label.setStyleSheet("background-color: #333333; border: 1px solid black;")
        graph_label.setMinimumSize(400, 300)
        body_layout.addWidget(graph_label)

        # Right Side - Notes Section
        right_layout = QVBoxLayout()

        notes_label = QLabel("Notes:")
        notes_label.setStyleSheet("color: black; font-size: 18px; padding: 5px;")
        right_layout.addWidget(notes_label)

        notes_area = QTextEdit()
        notes_area.setPlaceholderText("Players: ..., ...\nGame: ..., ...\nPayoff:___________")
        right_layout.addWidget(notes_area)

        body_layout.addLayout(right_layout)

        main_layout.addLayout(body_layout)

        # Bottom Console Section
        console_label = QLabel("Console")
        console_label.setStyleSheet("background-color: red; color: black; font-size: 18px; padding: 5px;")
        main_layout.addWidget(console_label)

        console_output = QLabel("Running Simulation\nResults\nRuleBased1.py: 367\nDeepLearning.py: 867\nWould you like to export results (y/n):")
        console_output.setStyleSheet("background-color: #333333; color: white; padding: 5px;")
        console_output.setMinimumHeight(50)
        main_layout.addWidget(console_output)

        # Main widget to hold the layout
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

# Run the application
app = QApplication(sys.argv)
window = PriceAlgorithmSimulator()
window.show()
sys.exit(app.exec())

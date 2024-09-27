import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QListWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QApplication, QMainWindow, QPushButton, QMenu, QLabel
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
        top_bar.setStyleSheet("background-color: #ab2328; color: black; font-size: 42px; margin: 0; padding: 10px; font-family: Georgia")
        top_bar.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(top_bar)
        
        # Menu Bar
        menu_layout = QHBoxLayout()
        
        #File menu
        file_layout = QVBoxLayout()
        file_button = QPushButton("File", self)

        file_menu = QMenu()

        file_rewind = file_menu.addAction("Restart Window")
        file_close = file_menu.addAction("Close")
        file_help = file_menu.addAction("Help")
        
        file_rewind.triggered.connect(lambda: print("Restart window"))
        file_close.triggered.connect(lambda: print("Close window"))
        file_help.triggered.connect(lambda: print("Help"))

        file_button.setMenu(file_menu)
        file_layout.addWidget(file_button)
        
        menu_layout.addLayout(file_layout)
        
        
        #import menu
        import_layout = QVBoxLayout()
        import_button = QPushButton("Import", self)

        import_menu = QMenu()

        import_comp = import_menu.addAction("Import New Competition")
        import_algo = import_menu.addAction("Import New Algorithm")
        
        import_comp.triggered.connect(lambda: print("import Competition"))
        import_algo.triggered.connect(lambda: print("import Algorithm"))

        import_button.setMenu(import_menu)
        import_layout.addWidget(import_button)
        menu_layout.addLayout(import_layout)
        
        #Export menu
        export_layout = QVBoxLayout()
        export_button = QPushButton("Export", self)

        export_menu = QMenu()

        export_csv = export_menu.addAction(".csv")
        export_txt = export_menu.addAction(".txt")
        export_json = export_menu.addAction(".json")
        
        
        export_csv.triggered.connect(lambda: print("Export csv"))
        export_txt.triggered.connect(lambda: print("Export txt"))
        export_json.triggered.connect(lambda: print("Export json"))
        

        export_button.setMenu(export_menu)
        export_layout.addWidget(export_button)
        menu_layout.addLayout(export_layout)
        
        
        
        
        main_layout.addLayout(menu_layout)


        # Horizontal Layout for Body
        body_layout = QHBoxLayout()

        # Left side - Competition and Player Selection
        left_layout = QVBoxLayout()

        # Competition List
        competition_label = QLabel("Select Competition")
        competition_label.setStyleSheet("background-color: #ab2328; color: black; padding: 5px; font-size: 18px;")
        left_layout.addWidget(competition_label)

        competition_list = QListWidget()
        competition_list.addItems(["- Bertrand.py", "- Cournot.py", "- Custom1.py", "- Custom2.py"])
        left_layout.addWidget(competition_list)

        # Player List
        player_label = QLabel("Select Players")
        player_label.setStyleSheet("background-color: #ab2328; color: black; padding: 5px; font-size: 18px;")
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
        console_label.setStyleSheet("background-color: #ab2328; color: black; font-size: 18px; padding: 5px;")
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

import sys
from PyQt6.QtWidgets import QGridLayout, QApplication, QMainWindow, QLabel, QListWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QPushButton, QMenu, QAbstractItemView
from PyQt6.QtCore import Qt
import os

class PASGui(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #instance variables
        
        try:
            # List only files in the folder
            self.sims = [
                file for file in os.listdir('./sims')
                if os.path.isfile(os.path.join('./sims', file))
            ]
        except FileNotFoundError:
            print(f"Error: The folder '{'./sims'}' does not exist.")
            self.sims = []
        except PermissionError:
            print(f"Error: Permission denied to access '{'./sims'}'.")
            self.sims = []
            
        try:
            # List only files in the folder
            self.algos = [
                file for file in os.listdir('./algos')
                if os.path.isfile(os.path.join('./algos', file))
            ]
        except FileNotFoundError:
            print(f"Error: The folder '{'./algos'}' does not exist.")
            self.algos = []
        except PermissionError:
            print(f"Error: Permission denied to access '{'./algos'}'.")
            self.algos = []
            
        

        

        #Make front end
        self.setWindowTitle("Price Algorithm Simulator")
        self.setStyleSheet("background-color: #9ea2a2;")
        self.setGeometry(100, 100, 1000, 600)

        # Main Layout
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        header = self.header()
        selection = self.selection_section()
        sim = self.sim_visualiization()
        notes = self.notes()
        console = self.console()
        
        main_layout.addLayout(header, 0,0,1,3)
        main_layout.addLayout(selection, 1,0,4,1)
        main_layout.addLayout(sim, 1,1,3,1)
        main_layout.addLayout(notes,1,2,3,1 )
        main_layout.addLayout(console,4, 1, 1, 2)
        
        for col in range(3):  # Set stretch for 3 columns
            main_layout.setColumnStretch(col, 1)
        
        # Main widget to hold the layout
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        
        

    #visual Methods
    def header(self):
        header = QVBoxLayout()
        
        # Top Bar
        top_bar = QLabel("Price Algorithm Simulator")
        top_bar.setStyleSheet("background-color: #ab2328; color: black; font-size: 42px; margin: 0; padding: 10px; font-family: Georgia")
        top_bar.setAlignment(Qt.AlignmentFlag.AlignLeft)
        header.addWidget(top_bar)
        
        # Menu Bar
        menu_layout = QHBoxLayout()
        menu_layout.setContentsMargins(0, 0, 0, 0)
        
        
        #File menu
        file_layout = QVBoxLayout()
        file_button = QPushButton("File", self)
        file_button.setStyleSheet("color: #000;\
                                    margin: 0; \
                                    padding: 0px;\
                                    font-size: 18px;\
                                    font-family: Arial;")        
        file_menu = QMenu()

        file_run_sim = file_menu.addAction("Run Simulation")
        file_rewind = file_menu.addAction("Restart Window")
        file_close = file_menu.addAction("Close")
        file_help = file_menu.addAction("Help")
        
        file_run_sim.triggered.connect(lambda: print(self.competition_list.currentItem().text()))
        file_rewind.triggered.connect(lambda: print("Restart window"))
        file_close.triggered.connect(lambda: print("Close window"))
        file_help.triggered.connect(lambda: print("Help"))

        file_button.setMenu(file_menu)
        file_layout.addWidget(file_button)
        
        menu_layout.addLayout(file_layout)
        
        
        #import menu
        import_layout = QVBoxLayout()
        import_button = QPushButton("Import", self)
        import_button.setStyleSheet("color: #000;\
                                    margin: 0; \
                                    padding: 0px;\
                                    font-size: 18px;\
                                    font-family: Arial;")  

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
        export_button.setStyleSheet("color: #000;\
                                    margin: 0; \
                                    padding: 0px;\
                                    font-size: 18px;\
                                    font-family: Arial;")  

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
        
        header.addLayout(menu_layout)
        
        return header

    def selection_section(self):
        select = QVBoxLayout()
        # Competition List
        competition_label = QLabel("Select Competition")
        competition_label.setStyleSheet("background-color: #ab2328; color: black; padding: 5px; font-size: 18px; font-family: Verdana; font-weight: bold")
        select.addWidget(competition_label)

        self.competition_list = QListWidget()
        self.competition_list.addItems(self.sims)
        self.competition_list.setStyleSheet("background-color: #9ea2a2;\
                                        font-family: Georgia ;\
                                        font-size: 18px")
        select.addWidget(self.competition_list)

        # Player List
        player_label = QLabel("Select Players")
        player_label.setStyleSheet("background-color: #ab2328; color: black; padding: 5px; font-size: 18px; font-family: Verdana; font-weight: bold")
        select.addWidget(player_label)

        self.player_list = QListWidget()
        self.player_list.addItems(self.algos)
        self.player_list.setStyleSheet("background-color: #9ea2a2;\
                                        font-family: Georgia ;\
                                        font-size: 18px")
        self.player_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        select.addWidget(self.player_list)
        
        return select

    def sim_visualiization(self):
        # Middle - Placeholder for Graph Visualization
        graph_label = QLabel()
        graph_label.setStyleSheet("background-color: #333333; border: 1px solid black;")
        
        graph_layout = QVBoxLayout()
        graph_layout.addWidget(graph_label)
        
        return graph_layout

    def notes(self):
        # Right Side - Notes Section

        notes_label = QLabel("Notes:")
        notes_label.setStyleSheet("background-color: #ab2328; color: black; padding: 5px; font-size: 18px; font-family: Verdana; font-weight: bold")
        notes_area = QTextEdit()
        notes_area.setPlaceholderText("Players: ..., ...\nGame: ..., ...\nPayoff:___________")
        notes_area.setStyleSheet("color: black; background-color: #9ea2a2; font-size: 18px; padding: 5px;")
        
        notes_layout = QVBoxLayout()
        notes_layout.addWidget(notes_label)
        notes_layout.addWidget(notes_area)
        
        return notes_layout
        
    def console(self):
        # Bottom Console Section
        console_layout = QVBoxLayout()
        console_label = QLabel("Console")
        console_label.setStyleSheet("background-color: #ab2328; color: black; padding: 5px; font-size: 18px; font-family: Verdana; font-weight: bold")
        
        console_layout.addWidget(console_label)

        console_output = QLabel("Running Simulation\nResults\nRuleBased1.py: 367\nDeepLearning.py: 867\nWould you like to export results (y/n):")
        console_output.setStyleSheet("background-color: #333333; color: white; padding: 5px;")
        console_output.setMinimumHeight(50)
        console_layout.addWidget(console_output)
        
        return console_layout


    


# Run the application
app = QApplication(sys.argv)
window = PASGui()
window.show()
sys.exit(app.exec())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QFileDialog, QComboBox, QSplashScreen
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import csv
import time

# Create a list to store the questions and answers
qa_list = []

def add_flashcards():
    # Get the text from the text box
    qa_input = text_box.toPlainText()

    # Split the input into separate lines and ignore empty lines
    lines = [line for line in qa_input.split('\n') if line]

    # Add the question and answer to the list
    for i in range(0, len(lines), 2):
        if lines[i].startswith('Q:') and lines[i+1].startswith('A:'):
            question = lines[i][2:].strip()
            answer = lines[i+1][2:].strip()
            qa_list.append([question, answer])

    # Clear the text box
    text_box.clear()

def save_flashcards():
    # Ask the user for the filename
    filename, _ = QFileDialog.getSaveFileName(None, "Save File", "", "CSV Files (*.csv)")

    # Open the CSV file in write mode ('w') so that the file is overwritten each time
    with open(filename, 'w', newline='', encoding='utf-8') as file:  # Add encoding='utf-8' for compatibility
        # Write the questions and answers as rows in the CSV file
        for qa in qa_list:
            file.write(f"{qa[0]},{qa[1]}\n")  # Write both question and answer in the same row, separated by a comma

    # Clear the list of questions and answers
    qa_list.clear()

def set_window_size(index):
    sizes = {
        "Small": (800, 600),
        "Medium": (1200, 800),
        "Large": (1600, 900),
        "Full HD": (1920, 1080)
    }
    window.resize(*sizes[index])

app = QApplication(sys.argv)

# Create a QPixmap object with the image you want to show in the splash screen
splash_pix = QPixmap('C:\\Users\\tahmi\\Downloads\\2908.jpg')
# Resize the QPixmap to the same size as the application window
splash_pix = splash_pix.scaled(800, 600, Qt.KeepAspectRatio)

# Create a QSplashScreen object and pass the QPixmap object to it
splash = QSplashScreen(splash_pix)
# Increase the font size for the splash screen message
font = QFont("Arial", 20, QFont.Bold)
splash.setFont(font)

splash.showMessage("Anki Card Creator\nDeveloped by Tahmid Nasif", alignment = Qt.AlignCenter, color = Qt.black)  # Show a message on the splash screen
splash.show()

# Ensure the splash screen is displayed for a minimum amount of time
time.sleep(3)

window = QWidget()
window.setWindowTitle('Anki Flashcard Creator')
window.setGeometry(100, 100, 800, 600)  # Set initial window size to "Small"
window.setStyleSheet("background-color: #2C2F33;")

layout = QVBoxLayout()

label = QLabel("Enter your questions and answers:")
label.setFont(QFont('Arial', 14))
label.setStyleSheet("color: #FFFFFF;")
layout.addWidget(label)

text_box = QTextEdit()
text_box.setFont(QFont('Arial', 12))
text_box.setStyleSheet("background-color: #23272A; color: #FFFFFF;")
layout.addWidget(text_box)

add_button = QPushButton('Add Flashcards')
add_button.setFont(QFont('Arial', 12))
add_button.setStyleSheet("background-color: #7289DA; color: #FFFFFF;")
add_button.clicked.connect(add_flashcards)
layout.addWidget(add_button)

save_button = QPushButton('Finish Flashcard Deck')
save_button.setFont(QFont('Arial', 12))
save_button.setStyleSheet("background-color: #7289DA; color: #FFFFFF;")
save_button.clicked.connect(save_flashcards)
layout.addWidget(save_button)

size_combo = QComboBox()
size_combo.addItem("Small")
size_combo.addItem("Medium")
size_combo.addItem("Large")
size_combo.addItem("Full HD")
size_combo.activated[str].connect(set_window_size)
size_combo.setStyleSheet("color: #FFFFFF;")  # Set text color to white
size_combo.setCurrentText("Small")  # Set initial selection to "Small"
layout.addWidget(size_combo)

author_label = QLabel("Made by Tahmid Nasif")
author_label.setFont(QFont('Arial', 10))
author_label.setStyleSheet("color: #FFFFFF;")
layout.addWidget(author_label)

window.setLayout(layout)

window.show()

# Close the splash screen once the main window is visible
splash.finish(window)

sys.exit(app.exec_())
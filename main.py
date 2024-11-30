import os
import sys
import pygame
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QListWidgetItem

# Initialize Pygame Mixer
pygame.mixer.init()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi('mainwindow.ui', self)

        # Set up the MIDI directory
        self.midi_dir = "./midi"
        if not os.path.exists(self.midi_dir):
            os.makedirs(self.midi_dir)

        # Populate the list widget with MIDI files
        self.populate_midi_list()

        # Connect the list widget's item click signal to the playback function
        self.midiListWidget.itemClicked.connect(self.play_midi)

    def populate_midi_list(self):
        """Populate the list widget with MIDI files."""
        midi_files = [f for f in os.listdir(self.midi_dir) if f.endswith(".mid")]
        self.midiListWidget.clear()  # Clear any existing items
        for file in midi_files:
            item = QListWidgetItem(file)
            self.midiListWidget.addItem(item)

    def play_midi(self, item):
        """Play the selected MIDI file."""
        midi_file = os.path.join(self.midi_dir, item.text())
        try:
            pygame.mixer.music.load(midi_file)
            pygame.mixer.music.play()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Playback Error", f"Error playing {midi_file}: {e}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

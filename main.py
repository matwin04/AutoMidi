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

        # Set up directories
        self.midi_dir = "./midi"
        self.soundfont_dir = "./soundfonts"
        for folder in [self.midi_dir, self.soundfont_dir]:
            if not os.path.exists(folder):
                os.makedirs(folder)

        # Populate the list widgets
        self.populate_midi_list()
        self.populate_soundfont_list()

        # Connect list widget signals
        self.midiListWidget.itemClicked.connect(self.play_midi)
        self.soundFontListWidget.itemClicked.connect(self.select_soundfont)

        # Connect Quit button
        self.quitButton.clicked.connect(self.close)

    def populate_midi_list(self):
        """Populate the MIDI list widget with MIDI files."""
        midi_files = [f for f in os.listdir(self.midi_dir) if f.endswith(".mid")]
        self.midiListWidget.clear()  # Clear existing items
        for file in midi_files:
            item = QListWidgetItem(file)
            self.midiListWidget.addItem(item)

    def populate_soundfont_list(self):
        """Populate the SoundFont list widget with SoundFont files."""
        soundfont_files = [f for f in os.listdir(self.soundfont_dir) if f.endswith(".sf2")]
        self.soundFontListWidget.clear()  # Clear existing items
        for file in soundfont_files:
            item = QListWidgetItem(file)
            self.soundFontListWidget.addItem(item)

    def play_midi(self, item):
        """Play the selected MIDI file."""
        midi_file = os.path.join(self.midi_dir, item.text())
        try:
            pygame.mixer.music.load(midi_file)
            pygame.mixer.music.play()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Playback Error", f"Error playing {midi_file}: {e}")

    def select_soundfont(self, item):
        """Select the SoundFont file."""
        soundfont_file = os.path.join(self.soundfont_dir, item.text())
        try:
            # Load the selected SoundFont (e.g., if using a library like fluidsynth)
            print(f"Selected SoundFont: {soundfont_file}")
            # Placeholder: Add integration with a library that supports SoundFonts
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "SoundFont Error", f"Error loading SoundFont: {e}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
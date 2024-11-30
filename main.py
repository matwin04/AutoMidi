import sys
import pygame
from PyQt5.QtWidgets import QApplication, QSlider, QLabel
from PyQt5.uic import loadUi

# Initialize Pygame Mixer for MIDI Playback
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)  # Default volume
currentMidi = None

def playMidi():
    """Play a MIDI file."""
    global currentMidi
    midiFile = "test.mid"  # Replace with your MIDI file path
    try:
        # Stop any current playback before starting a new one
        if currentMidi is not None:
            stopMidi()

        # Load and play the MIDI file
        pygame.mixer.music.load(midiFile)
        pygame.mixer.music.play()
        currentMidi = midiFile
        window.statusLabel.setText("Playing..")
    except Exception as e:
        window.statusLabel.setText(f"Error: {e}")

def stopMidi():
    """Stop MIDI playback."""
    global currentMidi
    try:
        if currentMidi is not None:
            pygame.mixer.music.stop()  # Stop playback
            currentMidi = None
        window.statusLabel.setText("Stopped")
    except Exception as e:
        window.statusLabel.setText(f"Error: {e}")

def adjustVolume():
    """Adjust volume based on the volume slider."""
    volume = window.volumeSlider.value() / 100  # Slider value (0-100)
    pygame.mixer.music.set_volume(volume)
    window.volumeLabel.setText(f"Volume: {volume:.2f}")

def adjustPitch():
    """Adjust pitch (not directly supported by Pygame, requires a workaround)."""
    pitch = window.pitchSlider.value()
    window.pitchLabel.setText(f"Pitch: {pitch}%")
    # Unfortunately, Pygame does not natively support pitch adjustment.
    # For advanced pitch shifting, you need a different library like PyDub or sounddevice.

# Application setup
app = QApplication(sys.argv)
window = loadUi("mainwindow.ui")

# Connect buttons to actions
window.playButton.clicked.connect(playMidi)
window.stopButton.clicked.connect(stopMidi)

# Connect sliders to actions
window.volumeSlider.valueChanged.connect(adjustVolume)  # Adjust volume
window.pitchSlider.valueChanged.connect(adjustPitch)  # Adjust pitch (UI feedback only)

# Set default slider values
window.volumeSlider.setValue(50)  # Default volume: 50%
window.pitchSlider.setValue(100)  # Default pitch: 100%

# Show the application
window.show()
sys.exit(app.exec_())
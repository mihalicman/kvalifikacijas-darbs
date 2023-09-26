from midiutil import MIDIFile
from flask import send_file  # Import send_file from Flask
from pydub import AudioSegment
import random
import subprocess

def generate_melody(notes):
    # Create a MIDI file
    midi_file = MIDIFile(1)
    midi_file.addTempo(0, 0, 120)  # Set the tempo

    # Define a mapping of user input to notes (you can expand this)
    note_mapping = {
        'C': 60,
        'D': 62,
        'E': 64,
        'F': 65,
        'G': 67,
        'A': 69,
        'B': 71
    }

    # Generate the melody based on user input
    melody = [note_mapping[note] for note in notes]

    # Add notes to the MIDI file
    for i, note in enumerate(melody):
        midi_file.addNote(0, 0, note, i, 1, 100)

    # Save the MIDI file with a unique name
    filename = "static/output.mid"
    with open(filename, "wb") as output_file:
        midi_file.writeFile(output_file)

    return filename  # Return the path to the generated MIDI file

def generate_random_notes():
    notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    random_notes = [random.choice(notes) for _ in range(8)]
    return ''.join(random_notes)

def convert_midi_to_mp3(midi_file_path):
    # Define the output MP3 file path
    mp3_file_path = midi_file_path.replace(".mid", ".mp3")
    
    # Use timidity to convert MIDI to WAV
    subprocess.run(["timidity", midi_file_path, "-Ow", "-o", mp3_file_path])

    # Load the WAV and export it as MP3
    wav = AudioSegment.from_wav(mp3_file_path.replace(".mid", ".wav"))
    wav.export(mp3_file_path, format="mp3")

    return mp3_file_path
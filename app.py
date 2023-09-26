from flask import Flask, render_template, request, jsonify, send_file, Response  # Import Response
from generate_melody import generate_melody, generate_random_notes, convert_midi_to_mp3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    notes = data.get("notes", "")
    
    if notes == "random":
        # Generate a random melody
        random_notes = generate_random_notes()
        midi_file_path = generate_melody(random_notes)

        # Convert MIDI to MP3
        mp3_file_path = convert_midi_to_mp3(midi_file_path)

        # Return the MP3 file for playback
        return send_file(mp3_file_path, as_attachment=True, mimetype='audio/mpeg')
    else:
        # Handle user input
        midi_file_path = generate_melody(notes)

        # Convert MIDI to MP3
        mp3_file_path = convert_midi_to_mp3(midi_file_path)

        # Return the MP3 file for playback
        return send_file(mp3_file_path, as_attachment=True, mimetype='audio/mpeg')

@app.route("/musical_bot.html")
def musical_bot():
    return render_template("musical_bot.html")

if __name__ == "__main__":
    app.run(debug=True)

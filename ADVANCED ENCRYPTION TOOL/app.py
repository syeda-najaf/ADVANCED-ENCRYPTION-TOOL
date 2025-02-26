"""
==========================================================
    Advanced Encryption Tool - Designed & Developed by
                 Syeda Najaf | AES-256 Encryption
==========================================================
"""

from flask import Flask, render_template, request, send_file, send_from_directory
from encryption import encrypt, decrypt  # Import encryption functions
import os

app = Flask(__name__, static_folder='static')

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt_file():
    if "file" not in request.files:
        return "No file part", 400
    
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    with open(file_path, "rb") as f:
        encrypted_data = encrypt(f.read())
    
    encrypted_path = os.path.join(PROCESSED_FOLDER, f"{file.filename}.aes")
    with open(encrypted_path, "wb") as f:
        f.write(encrypted_data)

    return send_file(encrypted_path, as_attachment=True)

@app.route("/decrypt", methods=["POST"])
def decrypt_file():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    with open(file_path, "rb") as f:
        decrypted_data = decrypt(f.read())

    decrypted_path = os.path.join(PROCESSED_FOLDER, "decrypted_" + file.filename.replace(".aes", ""))
    with open(decrypted_path, "wb") as f:
        f.write(decrypted_data)

    return send_file(decrypted_path, as_attachment=True)

@app.route('/static/sounds/<path:filename>')
def serve_sounds(filename):
    return send_from_directory('static/sounds', filename)

if __name__ == "__main__":
    print("\n=====================================")
    print("  Advanced Encryption Tool - Flask App")
    print("  Designed & Developed by Syeda Najaf")
    print("=====================================\n")
    app.run(debug=True)

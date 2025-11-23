# Whisper CLI Audio Transcription Helper

This script provides a quick way to convert audio files into WAV format and extract transcriptions using `whisper-cli`. It supports automatic detection of an audio file in the script's directory and saves the transcription as a `.md` file.

## Features
- Automatically finds an audio file in the script directory
- Converts audio to WAV (16-bit, mono, 16kHz) using `ffmpeg`
- Transcribes the audio using `whisper-cli`
- Saves the transcription as a text file
- Displays execution times with colored terminal output

## Installation

### Install Whisper CLI
You can install `whisper-cli` either by compiling it manually or using Homebrew:

#### Using Homebrew (Recommended):
```sh
brew install whisper-cpp
```

#### Compiling It Yourself:
Follow the instructions in the official `whisper.cpp` repository:
[Whisper.cpp GitHub](https://github.com/ggerganov/whisper.cpp)

### Download a Model
Whisper models are required for transcription. Download a model from:
[Whisper.cpp Models](https://huggingface.co/ggerganov/whisper.cpp/tree/main)

Once downloaded, set the `MODEL_PATH` variable in the script to point to the model file.

### Install Dependencies
This script requires `colorama` and `ffmpeg`.

#### Install `colorama` (for colored terminal output):
```sh
pip install colorama
```

#### Install `ffmpeg` (for audio conversion):
```sh
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Debian/Ubuntu
choco install ffmpeg  # Windows (Chocolatey)
```

## Configuration
Edit the script to specify your paths:
```python
WHISPER_PATH = '/opt/homebrew/bin/whisper-cli'  # Path to whisper-cli
MODEL_PATH = '/opt/homebrew/Cellar/whisper-cpp/1.7.4/ggml-large-v3-turbo.bin'  # Path to downloaded model
```
Modify these paths if you compiled `whisper-cli` yourself.

## Usage
1. Place an audio file (e.g., `.mp3`, `.wav`, `.m4a`, etc.) in the same directory as the script.
2. Run the script:
   ```sh
   python transcript.py
   ```
3. The transcript will be saved as `transcription.md` in the same directory.

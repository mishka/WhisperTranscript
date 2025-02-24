import os
import sys
import subprocess
import time
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init()

# Configuration
WHISPER_PATH = '/opt/homebrew/bin/whisper-cli'
MODEL_PATH = '/opt/homebrew/Cellar/whisper-cpp/1.7.4/ggml-large-v3-turbo.bin'
AUDIO_FORMAT = 'wav'  # Whisper works best with WAV files

def get_timestamp():
    return f"{Fore.CYAN}{datetime.now().strftime('%H:%M:%S.%f')[:-3]}{Style.RESET_ALL}"

def format_execution_time(start_time):
    elapsed_time = time.time() - start_time
    return f"{Fore.MAGENTA}{int(elapsed_time // 60):02}:{elapsed_time % 60:.3f}{Style.RESET_ALL}"

def print_colored(message):
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")

def convert_audio(input_file, output_file):
    '''Convert audio to 16-bit WAV mono format using ffmpeg'''
    start_time = time.time()
    try:
        subprocess.run(
            ['ffmpeg', '-i', input_file, '-ar', '16000', '-ac', '1', '-c:a', 'pcm_s16le', output_file],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError:
        print_colored('Error: ffmpeg failed to convert the audio file.')
        sys.exit(1)
    print(f'[{get_timestamp()}] - [{format_execution_time(start_time)}] - {Fore.GREEN}Audio conversion completed!{Style.RESET_ALL}')
    return output_file

def transcribe_audio(audio_path, output_txt):
    '''Run whisper-cpp and save output as markdown'''
    start_time = time.time()
    try:
        result = subprocess.run(
            [WHISPER_PATH, '-m', MODEL_PATH, '-f', audio_path, '--no-timestamps'],
            capture_output=True, text=True, check=True
        )
        whisper_output = result.stdout.strip()
        with open(output_txt, 'w') as txt_file:
            txt_file.write(whisper_output)
    except subprocess.CalledProcessError:
        print_colored('Error: whisper-cpp failed to transcribe the audio.')
        sys.exit(1)
    print(f'[{get_timestamp()}] - [{format_execution_time(start_time)}] - {Fore.GREEN}Transcription completed and saved to {Fore.BLUE}{output_txt}{Style.RESET_ALL}')

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    start_find_time = time.time()
    audio_file = next((os.path.join(script_dir, file) for file in os.listdir(script_dir) 
                       if file.endswith(('.mp3', '.wav', '.m4a', '.flac', '.ogg', '.aac', '.mp4'))), None)
    
    if not audio_file:
        print_colored('No audio file found in the script directory.')
        sys.exit(1)
    print(f'[{get_timestamp()}] - [{format_execution_time(start_find_time)}] - {Fore.GREEN}Found the audio file: {Fore.BLUE}{audio_file}{Style.RESET_ALL}')
    
    converted_audio = os.path.join(script_dir, 'converted_audio.wav')
    convert_audio(audio_file, converted_audio)
    
    output_txt = os.path.join(script_dir, 'transcription.md')
    transcribe_audio(converted_audio, output_txt)
    
    os.remove(converted_audio)

if __name__ == '__main__':
    main()

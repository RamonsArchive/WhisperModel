import whisper
import os
import pandas as pd
import csv

def store_full_transcript(full_text, results_dir):
    os.makedirs(results_dir, exist_ok=True)
    path = os.path.join(results_dir, "full_transcript.txt")
    with open(path, "w") as f:
        f.write(full_text)
    print(f"Full transcript stored in {path}")


def store_segment_csv(segments, results_dir):
    os.makedirs(results_dir, exist_ok=True)
    path = os.path.join(results_dir, "transcription.csv")
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["start", "end", "text"])
        writer.writeheader()
        for seg in segments:
            writer.writerow({
                "start": f"{seg['start']:.2f}",
                "end": f"{seg['end']:.2f}",
                "text": seg["text"].strip()
            })
    print(f"Segment CSV stored in {path}")
    

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(current_dir, "..", "assets/underwater.mp3")
    results_dir = os.path.join(current_dir, "..", "results")


    model = whisper.load_model(audio_path)
    result = model.transcribe("")
    store_full_transcript(result["text"], results_dir)
    store_segment_csv(result["segments"], results_dir)



if __name__ == "__main__":
    main()
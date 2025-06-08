# WhisperModel - Audio Transcription with OpenAI Whisper

## Overview
This project implements audio transcription using OpenAI's open-source Whisper model. It processes audio files and generates both full text transcripts and timestamped CSV outputs suitable for further analysis and processing.

## Project Structure
```
WhisperModel/
├── README.md              # This file - project documentation
├── src/                   # Source code directory
│   └── [transcription scripts]
├── assets/                # Input files directory
│   └── [audio files]
└── results/              # Output directory
    ├── full_transcript.txt    # Complete transcription text
    └── transcription.csv      # Timestamped segments with metadata
```

## Features
- **Audio Transcription**: Converts speech to text using Whisper
- **Timestamp Generation**: Provides precise timing for each segment
- **CSV Export**: Structured output with timestamps for easy data manipulation
- **Multiple Format Support**: Handles various audio formats (mp3, wav, m4a, etc.)
- **Automatic Precision Handling**: Adapts to CPU/GPU capabilities (FP32 on CPU, FP16 on GPU)

## Requirements
- Python 3.8+
- PyTorch
- OpenAI Whisper
- NumPy
- Pandas (for CSV handling)

## Installation

### 1. Clone the Repository
```bash
git clone [your-repo-url]
cd WhisperModel
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv whisper_env
source whisper_env/bin/activate  # On Windows: whisper_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install openai-whisper
pip install torch torchvision torchaudio
pip install pandas numpy
```

Alternatively, if you have a requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Transcription
1. Place your audio file in the `assets/` directory
2. Run the transcription script:
```bash
cd src
python transcribe.py
```

### Expected Output
The script will generate two files in the `results/` directory:
- `full_transcript.txt`: Complete transcription as plain text
- `transcription.csv`: Structured data with columns for:
  - Segment ID
  - Start time (seconds)
  - End time (seconds)
  - Transcribed text
  - Confidence scores (if available)

### Sample CSV Format
```csv
segment_id,start_time,end_time,text,confidence
0,0.00,2.45,"Hello, this is a sample transcription",0.95
1,2.45,5.12,"of audio content using Whisper model",0.92
```

## Configuration Options

### Model Selection
The script supports different Whisper model sizes:
- `tiny`: Fastest, least accurate
- `base`: Good balance of speed and accuracy
- `small`: Better accuracy, slower
- `medium`: High accuracy, requires more resources
- `large`: Best accuracy, slowest

### Language Settings
- **Auto-detection**: Default behavior
- **Specify language**: Add `--language en` for English, etc.

## Technical Notes

### Performance Considerations
- **CPU Usage**: Automatically uses FP32 precision (you may see the warning: "FP16 is not supported on CPU; using FP32 instead")
- **GPU Acceleration**: If CUDA is available, the model will automatically use GPU with FP16 precision
- **Memory Requirements**: Larger models require more RAM/VRAM

### File Format Support
Whisper supports various audio formats:
- WAV, MP3, M4A, FLAC
- Video files (extracts audio): MP4, AVI, MOV

## Troubleshooting

### Common Issues
1. **FP16 Warning**: This is normal on CPU and doesn't affect functionality
2. **Out of Memory**: Try using a smaller model size
3. **Audio Format Error**: Ensure your audio file is in a supported format

### Performance Tips
- For faster processing, use smaller model sizes
- GPU acceleration significantly improves speed
- Shorter audio segments process faster

## Output Analysis

### Full Transcript
- Complete text output suitable for reading
- Preserves natural flow and punctuation
- Ideal for content review and analysis

### CSV Timestamps
- Precise timing for each text segment
- Enables synchronization with other media
- Supports subtitle generation
- Facilitates automated analysis and processing

## Example Usage Scenarios
1. **Meeting Transcription**: Convert recorded meetings to searchable text
2. **Content Creation**: Generate subtitles for videos
3. **Research**: Transcribe interviews for qualitative analysis
4. **Accessibility**: Create text versions of audio content

## Development Notes
This implementation focuses on:
- **Simplicity**: Easy to run and understand
- **Reliability**: Robust error handling and format support
- **Flexibility**: Configurable options for different use cases
- **Output Quality**: Both human-readable and machine-processable formats

## Future Enhancements
- Speaker diarization (identifying different speakers)
- Real-time transcription capabilities
- Integration with other audio processing tools
- Custom model fine-tuning options

## Contact & Support
For questions about this implementation or suggestions for improvements, please refer to the project documentation or create an issue in the repository.

---

**Note**: This project uses the open-source OpenAI Whisper model for educational and development purposes. Processing times may vary based on hardware capabilities and audio file length.
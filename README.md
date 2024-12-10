# FLATswap Project - Decoding Number Station Transmissions

Welcome to **FLATswap** (Frequency Listening and Analysis Tool), a comprehensive platform designed to decode and analyze transmissions from number stations. This project focuses on automating the process of decoding voice transmissions, storing decoded messages, and providing a web interface for research and archival purposes.

---

## Project Overview

The goal of FLATswap is to:
1. **Decode Voice Transmissions**: Use a Python-based decoding model to transcribe voice recordings from number stations into text.
2. **Store Data in PostgreSQL**: Save decoded data in a PostgreSQL database for efficient retrieval and analysis.
3. **Provide a Web Interface**: Develop a web application using .NET (backend) and Angular (frontend) for browsing and analyzing archived transmissions.
4. **Automate Listening and Decoding**: Implement a script to continuously monitor frequencies, record transmissions, and process them automatically.

---

## Key Features

- **Voice-to-Text Decoding**: Automatically decode audio files containing number station transmissions into human-readable text.
- **Database Integration**: Store decoded messages in PostgreSQL for archival and research purposes.
- **Web Interface**:
  - View archived transmissions by date, station, or frequency.
  - Search and analyze historical data.
- **Automation**: Continuous monitoring of predefined frequencies with:
  - Automated recording of transmissions.
  - Automatic decoding and storage of messages.
- **Focus on Polish and Russian Stations**: Specialized tools to decode and analyze messages from Polish and Russian number stations.

---

## Technology Stack

### Backend:
- **Python**: Core logic for audio decoding using Whisper.
- **PostgreSQL**: Database for storing decoded transmissions and metadata.
- **.NET**: Backend for the web application to provide APIs and business logic.

### Frontend:
- **Angular**: For building a responsive and user-friendly web interface.

### Automation:
- Python scripts for:
  - Monitoring radio frequencies.
  - Recording transmissions.
  - Processing and decoding files automatically.

---

## Workflow

1. **Audio Input**: 
   - A recorded transmission file is fed into the Python decoding system.
   - Alternatively, the automation script records live transmissions.

2. **Decoding**:
   - Audio is transcribed into text using an AI-powered model.
   - Metadata (e.g., frequency, timestamp) is extracted.

3. **Database Storage**:
   - Decoded messages and metadata are saved into the PostgreSQL database.

4. **Web Access**:
   - Users can view and search archived transmissions via the Angular web interface.
   - Data is fetched from the backend (built with .NET).

---

## Installation and Setup

### Prerequisites:
- Python 3.10 with pip.
- PostgreSQL database.
- .NET 8 for backend development.
- Node.js and Angular CLI for frontend development.

## Future Plans
- Real-Time Monitoring: Display live decoded data from ongoing transmissions.
- API Access: Provide an API for external researchers to query the database.

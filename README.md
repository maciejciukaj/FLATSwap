# FLATswap Project - Transcribing Number Station Transmissions

Welcome to **FLATswap** (Frequency Listening and Automated Transcription System with Archival Processing), a comprehensive platform designed to transcribe and analyze voice transmissions from number stations. This project focuses on automating the process of converting spoken numeric transmissions into text format, storing them for archival purposes, and providing a web interface for research.

---

## Project Overview

The goal of FLATswap is to:
1. **Transcribe Voice Transmissions**: Use a Python-based transcription model to convert spoken numbers from number stations into text format.
2. **Store Data in PostgreSQL**: Save transcribed numeric data in a PostgreSQL database for efficient retrieval and analysis.
3. **Provide a Web Interface**: Develop a web application using .NET (backend) and Angular (frontend) for browsing and analyzing archived transmissions.
4. **Automate Listening and Transcription**: Implement a script to continuously monitor frequencies, record transmissions, and process them automatically.

---

## Key Features

- **Voice-to-Text Transcription**: Automatically transcribe numeric transmissions from audio files into text format.
- **Database Integration**: Store transcribed numbers and metadata (e.g., timestamp, frequency) in PostgreSQL for archival and research purposes.
- **Web Interface**:
  - View archived transmissions by date, station, or frequency.
  - Search and analyze historical data.
- **Automation**: Continuous monitoring of predefined frequencies with:
  - Automated recording of transmissions.
  - Automatic transcription and storage of numeric data.
- **Focus on Polish and Russian Stations**: Specialized tools to transcribe and organize data from Polish and Russian number stations.

---

## Technology Stack

### Backend:
- **Python**: Core logic for audio transcription using Whisper or similar AI models.
- **PostgreSQL**: Database for storing transcribed numbers and metadata.
- **.NET**: Backend for the web application to provide APIs and business logic.

### Frontend:
- **Angular**: For building a responsive and user-friendly web interface.

### Automation:
- Python scripts for:
  - Monitoring radio frequencies.
  - Recording transmissions.
  - Processing and transcribing files automatically.

---

## Workflow

1. **Audio Input**: 
   - A recorded transmission file is fed into the Python transcription system.
   - Alternatively, the automation script records live transmissions.

2. **Transcription**:
   - Spoken numbers are transcribed into text using an AI-powered model.
   - Metadata (e.g., frequency, timestamp) is extracted.

3. **Database Storage**:
   - Transcribed numbers and metadata are saved into the PostgreSQL database.

4. **Web Access**:
   - Users can view and search archived transmissions via the Angular web interface.
   - Data is fetched from the backend (built with .NET).

---

### Prerequisites:
- Python 3.10 with pip.
- PostgreSQL database.
- .NET SDK for backend development.
- Node.js and Angular CLI for frontend development.

### Future Plans:
- Multilingual Support: Extend transcription capabilities to other languages used by number stations.
- Real-Time Monitoring: Display live transcribed data from ongoing transmissions.
- API Access: Provide an API for external researchers to query the database.

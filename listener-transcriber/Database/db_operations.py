from datetime import datetime
import os

from Database.database_config import Session
from Models.stations import Stations
from Models.transcription import Transcriptions


def save_transcription_to_db(station_code, timestamp, frequency, transcribed_message):
    session = Session()

    try:
        formatted_timestamp = timestamp.replace("_", ":")
        formatted_timestamp = datetime.strptime(formatted_timestamp, "%Y-%m-%dT%H:%M:%S%z")

        station = session.query(Stations).filter_by(Name=station_code).first()
        if station is None:
            raise ValueError(f"Station code '{station_code}' not found in Stations table.")

        transcription = Transcriptions(
            StationId=station.Id,
            TranscribedText=transcribed_message,
            Frequency=frequency,
            Timestamp=formatted_timestamp
        )

        session.add(transcription)
        session.commit()
        print("Transcription successfully saved to database.")

    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
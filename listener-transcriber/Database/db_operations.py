from datetime import datetime
import os
import psycopg2

def save_transcription_to_db(station_code, timestamp, frequency, transcribed_message):
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    cursor = conn.cursor()

    try:
        formatted_timestamp = timestamp.replace("_", ":")
        formatted_timestamp = datetime.strptime(formatted_timestamp, "%Y-%m-%dT%H:%M:%S%z")

        cursor.execute(
            "SELECT Id FROM Stations WHERE Name = %s", (station_code,)
        )
        station_id = cursor.fetchone()
        if station_id is None:
            raise ValueError(f"Station code '{station_code}' not found in Stations table.")

        cursor.execute(
            """
            INSERT INTO Transcriptions (StationId, TranscribedText, Frequency, Timestamp)
            VALUES (%s, %s, %s, %s)
            """,
            (station_id[0], transcribed_message, frequency, formatted_timestamp)
        )
        conn.commit()
        print("Transcription successfully saved to database.")

    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

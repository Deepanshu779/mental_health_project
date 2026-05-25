import os
import pandas as pd
from datetime import datetime

# ==========================================
# --- Data Store for Mood Logging ---
# ==========================================

LOG_FILE = "mood_logs.csv"

def get_log_filepath():
    """Gets the absolute path of the local CSV file in the current directory."""
    # Always keep it in the workspace folder for clean local workspace structure
    return os.path.abspath(LOG_FILE)


def init_data_store():
    """Initializes the CSV log file if it doesn't already exist."""
    path = get_log_filepath()
    if not os.path.exists(path):
        # Create an empty dataframe with standard columns and save it
        df = pd.DataFrame(columns=["timestamp", "score", "mood", "influencers", "notes"])
        df.to_csv(path, index=False)
        
        # Add a baseline neutral entry so the dashboard always has at least 1 entry
        append_mood_log(
            score=0,
            mood="neutral",
            influencers="Baseline",
            notes="EmpathyBot 2.0 system initialized.",
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )


def load_mood_logs():
    """Loads all mood logs from the CSV file as a Pandas DataFrame."""
    init_data_store()
    path = get_log_filepath()
    try:
        df = pd.read_csv(path)
        # Parse timestamp column as datetime objects
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        # Ensure correct column formats
        df["score"] = pd.to_numeric(df["score"])
        df["mood"] = df["mood"].astype(str)
        df["influencers"] = df["influencers"].fillna("")
        df["notes"] = df["notes"].fillna("")
        return df.sort_values(by="timestamp")
    except Exception as e:
        print(f"Error loading logs: {e}")
        # Return empty df as fallback
        return pd.DataFrame(columns=["timestamp", "score", "mood", "influencers", "notes"])


def append_mood_log(score, mood, influencers="", notes="", timestamp=None):
    """Appends a new mood log entry to the CSV database."""
    init_data_store()
    path = get_log_filepath()
    
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    # Standardize empty lists/fields
    if isinstance(influencers, list):
        influencers = ", ".join(influencers)
    
    new_entry = pd.DataFrame([{
        "timestamp": timestamp,
        "score": float(score),
        "mood": str(mood),
        "influencers": str(influencers),
        "notes": str(notes)
    }])
    
    try:
        # Append to CSV without loading the whole file in memory
        new_entry.to_csv(path, mode='a', header=False, index=False)
        return True
    except Exception as e:
        print(f"Error appending log: {e}")
        return False


def clear_all_logs():
    """Resets the CSV file by clearing all entries."""
    path = get_log_filepath()
    if os.path.exists(path):
        try:
            os.remove(path)
        except Exception as e:
            print(f"Error deleting file: {e}")
    init_data_store()

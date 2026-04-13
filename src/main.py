"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"\Loaded songs: {len(songs)}\n")

    # --- Standard profiles ---
    profiles = {
        "High-Energy Pop":    {"genre": "pop",       "mood": "happy",   "energy": 0.9,  "acoustic": "false"},
        "Chill Lofi":         {"genre": "lofi",      "mood": "chill",   "energy": 0.3,  "acoustic": "true"},
        "Deep Intense Rock":  {"genre": "rock",      "mood": "intense", "energy": 0.95, "acoustic": "false"},
        "All Midpoints":      {"genre": "pop",       "mood": "chill",   "energy": 0.5,  "acoustic": "false"},
        "Unknown Genre":      {"genre": "bossa nova","mood": "happy",   "energy": 0.7,  "acoustic": "true"},
        "Max Energy Non-Acoustic": {"genre": "ambient", "mood": "chill", "energy": 1.0, "acoustic": "false"},
    }

    for label, user_prefs in profiles.items():
        print(f"\n=== {label} ===")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        for song, score, explanation in recommendations:
            print(f"  {song['title']} - Score: {score:.2f}")
            print(f"  Because: {explanation}")


if __name__ == "__main__":
    main()

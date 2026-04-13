from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def score_song(self, song: Song, user: UserProfile) -> float:
        """Return a weighted match score (max 4.5) between a song and a user profile."""
        score = 0.0
        if song.genre == user.favorite_genre:
            score += 1.0
        if song.mood == user.favorite_mood:
            score += 1.0
        score += 2.0 * (1.0 - abs(song.energy - user.target_energy))
        score += song.acousticness * 0.5 if user.likes_acoustic else (1.0 - song.acousticness) * 0.5
        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Score all songs and return the top k sorted from highest to lowest score."""
        scored = sorted(self.songs, key=lambda song: self.score_song(song, user), reverse=True)
        return scored[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a plain-language sentence describing why a song was recommended."""
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append(f"genre matches ({song.genre})")
        if song.mood == user.favorite_mood:
            reasons.append(f"mood matches ({song.mood})")
        energy_diff = abs(song.energy - user.target_energy)
        if energy_diff <= 0.1:
            reasons.append("energy is a close match")
        elif energy_diff <= 0.3:
            reasons.append("energy is somewhat close")
        if user.likes_acoustic and song.acousticness >= 0.6:
            reasons.append("acoustic feel you prefer")
        elif not user.likes_acoustic and song.acousticness <= 0.3:
            reasons.append("non-acoustic sound you prefer")
        if not reasons:
            return "Partial match on energy and acoustic preference."
        return ", ".join(reasons) + "."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # Convert raw dicts into typed objects so we can reuse Recommender.score_song
    song_objects = [Song(**s) for s in songs]
    rec = Recommender(song_objects)
    user = UserProfile(favorite_genre=user_prefs['genre'], favorite_mood=user_prefs['mood'],
                       target_energy=float(user_prefs['energy']), 
                       likes_acoustic = str(user_prefs.get('acoustic', 'false')).lower() == 'true')
    # Score every song and pair each score with its original dict
    results = []
    for song_dict, song_obj in zip(songs, song_objects):
        score = rec.score_song(song_obj, user)
        explanation = rec.explain_recommendation(user, song_obj)
        results.append((song_dict, score, explanation))

    # Sort highest score first and return the top k
    results.sort(key=lambda entry: entry[1], reverse=True)
    return results[:k]

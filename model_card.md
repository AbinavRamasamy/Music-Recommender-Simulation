# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

VibeFinder suggests up to 5 songs from a small catalog based on a user's genre, mood, energy level, and acoustic preference. It assumes the user has one favorite genre and mood. 

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Every song has a genre, mood, energy level, and acoustic feel — all stored as numbers between 0 and 1. The system compares each song to what the user likes and gives it a score. Genre match is worth the most, then mood, then how close the energy is, then acoustic preference. The top 5 scores win. I also added an explanation for each result so the user can see why a song was picked.

---

## 4. Data  

Describe the dataset the model uses.  

The system runs on a catalog of 18 songs. It covers 15 genres and 13 moods, but most genres have only 1 song — lofi and pop are the most represented. The data skews toward a Western, English-language taste profile. Tempo is stored but not used in scoring. Lyrics, key, and artist popularity are missing entirely.

---

## 5. Strengths  

Where does your system seem to work well  

It works best for users whose genre and mood are well-covered in the catalog — the lofi/chill and pop/happy profiles both returned results that felt accurate. The scoring is also fully transparent: each recommendation comes with a plain-language explanation, so it's easy to see exactly why a song was ranked where it was.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

When the "Unknown Genre" profile was tested with a genre not present in the catalog (bossa nova), the genre bonus never activated and all recommendations were driven entirely by mood and energy proximity. This means a user with a niche or unlisted genre preference receives the same results as a user with no genre preference at all. At scale, this would under-serve listeners whose tastes fall outside the catalog's represented genres. It also means two users with very different genre preferences but similar energy levels would receive nearly identical recommendations, making the system appear personalized when it is not.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Six profiles were tested — three standard, three adversarial — and top 5 results were checked against intuition. Standard profiles produced expected results. The "All Midpoints" profile was the most surprising: with energy scores clustered, ranking felt arbitrary. A weight-shift experiment (genre halved, energy doubled) confirmed the original genre weight was burying cross-genre matches with strong energy alignment.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

- Add tempo range as a preference (e.g., user likes 70–90 BPM).
- Enforce diversity so not all 5 results come from the same genre.
- Support a "neutral" acoustic option instead of a binary yes/no.
- Expand the catalog — most genres have only 1 song, which makes the system feel unreliable for niche tastes.

---

## 9. Personal Reflection  

My biggest learning moment was realizing that bias doesn't come from bad code — it comes from silent assumptions. When I tested the "Unknown Genre" profile, the system ran perfectly but completely failed the user. That gap between "technically correct" and "actually useful" is something I didn't expect to feel so clearly in a project this small.

Using AI tools helped me move quickly, especially for scaffolding the scoring logic and writing explanations. However, I had to double-check things like the overall content of the explanations and code — the AI confidently said "20–30 songs" when the actual answer was 18. Verifying against the real CSV was a good reminder that generated answers are not grounded in the actual data.

What surprised me most was how much the simple scoring formula felt like a real recommendation. The lofi/chill profile returned results that genuinely seemed right, even though the system has no understanding of music at all. It made me realize why users trust recommendation systems even when those systems are doing something much simpler than people assume.

If I extended this project, I'd add tempo as an additional feature and experiment with enforcing diversity (forcing the top 5 to span at least 2–3 genres). I'd also want to try a feedback loop where the user can thumbs-up/down a result and the weights adjust over time.

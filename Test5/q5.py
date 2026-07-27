import sqlite3

class Movie:

    def __init__(self, movie_id, title, genre, rating, watch_count):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.rating = rating
        self.watch_count = watch_count

    def display(self):
        print("--------------------------------")
        print("Movie ID    :", self.movie_id)
        print("Title       :", self.title)
        print("Genre       :", self.genre)
        print("Rating      :", self.rating)
        print("Watch Count :", self.watch_count)

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
    movie_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    rating REAL,
    watch_count INTEGER
)
""")

movies_data = [
    (101, "Inception", "Sci-Fi", 9.2, 5000),
    (102, "Interstellar", "Sci-Fi", 9.5, 6500),
    (103, "Avengers", "Action", 8.9, 9000),
    (104, "Titanic", "Romance", 8.7, 8000),
    (105, "The Dark Knight", "Action", 9.8, 12000),
    (106, "3 Idiots", "Comedy", 9.1, 9500),
    (107, "Dangal", "Sports", 8.8, 7000),
    (108, "Bahubali", "Action", 8.6, 11000),
    (109, "Frozen", "Animation", 8.5, 6000),
    (110, "Toy Story", "Animation", 9.0, 7500),
    (111, "PK", "Comedy", 8.9, 10500)
]

cursor.executemany(
    "INSERT OR REPLACE INTO movies VALUES (?, ?, ?, ?, ?)",
    movies_data
)

conn.commit()

cursor.execute("SELECT * FROM movies")
rows = cursor.fetchall()

movies = []

for row in rows:
    movies.append(Movie(row[0], row[1], row[2], row[3], row[4]))

movies.sort(key=lambda x: x.rating)

print("\n========== MOVIES SORTED BY RATING ==========\n")

for movie in movies:
    movie.display()

movies.sort(key=lambda x: x.movie_id)

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid].movie_id == target:
            return arr[mid]

        elif arr[mid].movie_id < target:
            low = mid + 1

        else:
            high = mid - 1

    return None

print("\n========== SEARCH MOVIE ==========\n")

movie_id = int(input("Enter Movie ID : "))

movie = binary_search(movies, movie_id)

if movie:
    print("\nMovie Found")
    movie.display()
else:
    print("Movie Not Found")

movies.sort(key=lambda x: x.rating)

print("\n========== TOP 10 HIGHEST RATED MOVIES ==========\n")

top_movies = movies[-10:]
top_movies.reverse()

for movie in top_movies:
    movie.display()

print("\n========== MOST WATCHED MOVIE IN EACH GENRE ==========\n")

cursor.execute("""
SELECT genre, MAX(watch_count)
FROM movies
GROUP BY genre
""")

results = cursor.fetchall()

for genre, max_watch in results:

    cursor.execute(
        """
        SELECT * FROM movies
        WHERE genre=? AND watch_count=?
        """,
        (genre, max_watch)
    )

    row = cursor.fetchone()

    if row:
        movie = Movie(row[0], row[1], row[2], row[3], row[4])
        movie.display()

conn.close()
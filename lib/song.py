class Song:
    count = 0
    genres = []             
    artists = []            
    genre_count = {}        
    artist_count = {}      

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the song count and update genre/artist data
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    # Class method to add unique genres to the list
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    # Class method to add unique artists to the list
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    # Class method to count songs by genre
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    # Class method to count songs by artist
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage:
song1 = Song("Blinding Lights", "The Weeknd", "Pop")
song2 = Song("Levitating", "Dua Lipa", "Pop")
song3 = Song("Good 4 U", "Olivia Rodrigo", "Rock")
song4 = Song("Peaches", "Justin Bieber", "R&B")
song5 = Song("Blinding Lights", "The Weeknd", "Pop")  # Duplicate to test counting


print(f"Songs per genre: {Song.genre_count}")   # Output: {'Pop': 3, 'Rock': 1, 'R&B': 1}
print(f"Songs per artist: {Song.artist_count}") # Output: {'The Weeknd': 2, 'Dua Lipa': 1, 'Olivia Rodrigo': 1, 'Justin Bieber': 1}
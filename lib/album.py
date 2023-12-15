class Album:
    def __init__(self, id, title, release_year, artist_id):
        self.id = id or None
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id or None
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
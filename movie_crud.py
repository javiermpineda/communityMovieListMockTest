from abstract_crud import AbstractCRUD
from models import Movie
from database import Session

class MovieCRUD(AbstractCRUD):
    def create(self, data):
        with Session() as session:
            # Check if a movie with the given ID already exists
            existing_movie = session.query(Movie).filter(Movie.movie_id == data['movie_id']).first()
            if existing_movie:
                raise ValueError("A movie with this ID already exists.")

            new_movie = Movie(**data)
            session.add(new_movie)
            session.commit()
            return new_movie.movie_id

    def read(self, movie_id):
        with Session() as session:
            return session.query(Movie).filter(Movie.movie_id == movie_id).first()

    def update(self, movie_id, data):
        with Session() as session:
            movie = session.query(Movie).filter(Movie.movie_id == movie_id).first()
            if movie:
                for key, value in data.items():
                    setattr(movie, key, value)
                session.commit()
            else:
                raise ValueError("Movie not found.")

    def delete(self, movie_id):
        with Session() as session:
            movie = session.query(Movie).filter(Movie.movie_id == movie_id).first()
            if movie:
                session.delete(movie)
                session.commit()
            else:
                raise ValueError("Movie not found.")

    def get_all_movies(self):
        with Session() as session:
            return session.query(Movie).all()

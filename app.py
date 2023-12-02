from flask import Flask, request, jsonify, render_template, redirect, url_for
from movie_crud import MovieCRUD
from database import init_db
from datetime import datetime

app = Flask(__name__)
crud = MovieCRUD()

@app.route('/')
def index():
    movies = crud.get_all_movies()
    return render_template('index.html', movies=movies)

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        try:
            data = {
                'movie_id': request.form['movie_id'],
                'title': request.form['title'],
                'image_url': request.form['image_url'],
                'updated': datetime.now(),
                'url_streaming': request.form['url_streaming']
            }
            crud.create(data)
        except ValueError as e:
            return str(e), 400  # Return the error message with a 400 Bad Request status

        return redirect(url_for('index'))

    return render_template('add_movie.html')

@app.route('/view_movie/<int:movie_id>')
def view_movie(movie_id):
    movie = crud.read(movie_id)
    if movie:
        return render_template('view_movie.html', movie=movie)
    return 'Movie not found', 404

@app.route('/delete_movie/<int:movie_id>', methods=['POST'])
def delete_movie(movie_id):
    crud.delete(movie_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=False)

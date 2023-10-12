from flask import Flask
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
api = Api(app)
client = MongoClient("mongodb://db:27017/")
db = client.books_db
movies = db.movies  # Use 'movies' collection instead of 'books'

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help="Title cannot be blank")
parser.add_argument('director', type=str, required=True, help="Director cannot be blank")
parser.add_argument('actor', type=str, required=True, help="Actor cannot be blank")
parser.add_argument('actress', type=str, required=True, help="Actress cannot be blank")


class MovieResource(Resource):
    def get(self, movie_id=None):
        if movie_id:
            movie = movies.find_one({"_id": ObjectId(movie_id)})
            if movie:
                movie['_id'] = str(movie['_id'])  # Convert ObjectID to string
                return movie, 200
            return {"message": "Movie not found"}, 404
        else:
            all_movies = list(movies.find())
            for movie in all_movies:
                movie['_id'] = str(movie['_id'])  # Convert ObjectID to string for all movies
            return all_movies, 200

    def post(self):
        args = parser.parse_args()
        result = movies.insert_one(
            {"title": args['title'], "director": args['director'], "actor": args['actor'], "actress": args['actress']})
        return {"id": str(result.inserted_id), "title": args['title'], "director": args['director'],
                "actor": args['actor'], "actress": args['actress']}, 201

    def put(self, movie_id):
        args = parser.parse_args()
        movies.update_one({"_id": ObjectId(movie_id)}, {
            "$set": {"title": args['title'], "director": args['director'], "actor": args['actor'],
                     "actress": args['actress']}})
        return {"id": movie_id, "title": args['title'], "director": args['director'], "actor": args['actor'],
                "actress": args['actress']}, 200

    def delete(self, movie_id):
        movies.delete_one({"_id": ObjectId(movie_id)})
        return {"message": "Movie deleted"}, 200


api.add_resource(MovieResource, '/movies', '/movies/<string:movie_id>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

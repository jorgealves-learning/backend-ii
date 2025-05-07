import uuid
from concurrent import futures
import grpc

from movies_grpc import movie_pb2 as pb2
from movies_grpc import movie_pb2_grpc as pb2_grpc

class MovieService(pb2_grpc.MovieServiceServicer):
    def __init__(self):
        self.movies = {}  # in-memory store

    def CreateMovie(self, request, context):
        m = request.movie
        new_id = str(uuid.uuid4())
        movie = pb2.Movie(id=new_id,
                          title=m.title,
                          director=m.director,
                          year=m.year)
        self.movies[new_id] = movie
        return pb2.CreateMovieResponse(movie=movie)

    def GetMovie(self, request, context):
        return pb2.GetMovieResponse(movies=list(self.movies.values()))

    def UpdateMovie(self, request, context):
        m = request.movie
        if m.id not in self.movies:
            context.abort(grpc.StatusCode.NOT_FOUND, "Movie not found")
        self.movies[m.id] = m
        return pb2.UpdateMovieResponse(movie=m)

    def DeleteMovie(self, request, context):
        success = False
        if request.id in self.movies:
            del self.movies[request.id]
            success = True
        return pb2.DeleteMovieResponse(success=success)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MovieServiceServicer_to_server(MovieService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server starting on port 50051…")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

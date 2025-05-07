import grpc
from movies_grpc import movie_pb2 as pb2
from movies_grpc import movie_pb2_grpc as pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.MovieServiceStub(channel)

    # Create
    resp = stub.CreateMovie(pb2.CreateMovieRequest(
        movie=pb2.Movie(id="1",title="Inception", director="Nolan", year="2010")
    ))
    m_id = resp.movie.id
    print("Created:", resp.movie)

    # List
    all_movies = stub.GetMovie(pb2.GetMovieRequest())
    print("All:", all_movies.movies)

    # Update
    updated = stub.UpdateMovie(pb2.UpdateMovieRequest(
        movie=pb2.Movie(id=m_id, title="Inception", director="Christopher Nolan", year="2010")
    ))
    print("Updated:", updated.movie)

    # Delete
    deleted = stub.DeleteMovie(pb2.DeleteMovieRequest(id=m_id))
    print("Deleted successfully?", deleted.success)

if __name__ == '__main__':
    run()

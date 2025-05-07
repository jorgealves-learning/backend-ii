from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Movie(_message.Message):
    __slots__ = ("id", "title", "director", "year")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DIRECTOR_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    director: str
    year: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., director: _Optional[str] = ..., year: _Optional[str] = ...) -> None: ...

class CreateMovieRequest(_message.Message):
    __slots__ = ("movie",)
    MOVIE_FIELD_NUMBER: _ClassVar[int]
    movie: Movie
    def __init__(self, movie: _Optional[_Union[Movie, _Mapping]] = ...) -> None: ...

class CreateMovieResponse(_message.Message):
    __slots__ = ("movie",)
    MOVIE_FIELD_NUMBER: _ClassVar[int]
    movie: Movie
    def __init__(self, movie: _Optional[_Union[Movie, _Mapping]] = ...) -> None: ...

class GetMovieRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMovieResponse(_message.Message):
    __slots__ = ("movies",)
    MOVIES_FIELD_NUMBER: _ClassVar[int]
    movies: _containers.RepeatedCompositeFieldContainer[Movie]
    def __init__(self, movies: _Optional[_Iterable[_Union[Movie, _Mapping]]] = ...) -> None: ...

class UpdateMovieRequest(_message.Message):
    __slots__ = ("movie",)
    MOVIE_FIELD_NUMBER: _ClassVar[int]
    movie: Movie
    def __init__(self, movie: _Optional[_Union[Movie, _Mapping]] = ...) -> None: ...

class UpdateMovieResponse(_message.Message):
    __slots__ = ("movie",)
    MOVIE_FIELD_NUMBER: _ClassVar[int]
    movie: Movie
    def __init__(self, movie: _Optional[_Union[Movie, _Mapping]] = ...) -> None: ...

class DeleteMovieRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteMovieResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

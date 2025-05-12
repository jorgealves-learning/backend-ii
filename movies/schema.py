import graphene
from graphene_django.types import DjangoObjectType
from .models import Movie, Publisher, Actor, TVShow


class PublisherType(DjangoObjectType):
    class Meta:
        model = Publisher
        fields = ("id", "name", "address", "city", "state", "country")


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "release_date", "publisher")


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor
        fields = ("id", "name", "age", "movies")


class TVShowType(DjangoObjectType):
    class Meta:
        model = TVShow
        fields = ("id", "title", "description", "release_date", "publisher")


class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    all_publishers = graphene.List(PublisherType)
    all_actors = graphene.List(ActorType)
    all_tvshows = graphene.List(TVShowType)

    def resolve_all_movies(self, info):
        return Movie.objects.all()

    def resolve_all_publishers(self, info):
        return Publisher.objects.all()

    def resolve_all_actors(self, info):
        return Actor.objects.all()

    def resolve_all_tvshows(self, info):
        return TVShow.objects.all()


class CreateMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        release_date = graphene.Date(required=True)
        publisher_id = graphene.Int(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, title, description, release_date, publisher_id):
        publisher = Publisher.objects.get(id=publisher_id)
        movie = Movie(
            title=title,
            description=description,
            release_date=release_date,
            publisher=publisher,
        )
        movie.save()
        return CreateMovie(movie=movie)


class CreatePublisher(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        city = graphene.String(required=True)
        state = graphene.String(required=True)
        country = graphene.String(required=True)

    publisher = graphene.Field(PublisherType)

    def mutate(self, info, name, address, city, state, country):
        publisher = Publisher(
            name=name, address=address, city=city, state=state, country=country
        )
        publisher.save()
        return CreatePublisher(publisher=publisher)


class CreateActor(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
        movie_ids = graphene.List(graphene.Int, required=True)

    actor = graphene.Field(ActorType)

    def mutate(self, info, name, age, movie_ids):
        movies = Movie.objects.filter(id__in=movie_ids)
        actor = Actor(name=name, age=age)
        actor.save()
        actor.movies.set(movies)
        return CreateActor(actor=actor)


class CreateTVShow(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        release_date = graphene.Date(required=True)
        publisher_id = graphene.Int(required=True)

    tvshow = graphene.Field(TVShowType)

    def mutate(self, info, title, description, release_date, publisher_id):
        publisher = Publisher.objects.get(id=publisher_id)
        tvshow = TVShow(
            title=title,
            description=description,
            release_date=release_date,
            publisher=publisher,
        )
        tvshow.save()
        return CreateTVShow(tvshow=tvshow)


class Mutation(graphene.ObjectType):
    create_movie = CreateMovie.Field()
    create_publisher = CreatePublisher.Field()
    create_actor = CreateActor.Field()
    create_tvshow = CreateTVShow.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

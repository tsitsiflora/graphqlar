import graphene
from graphene_django import DjangoObjectType

from .models import User, Trip


class UserType(DjangoObjectType):
    class Meta:
        model = User

class TripType(DjangoObjectType):
    class Meta:
        model = Trip

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    trips = graphene.List(TripType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_trips(self, info, **kwargs):
        return Trip.objects.all()

class CreateUser(graphene.Mutation):
    id = graphene.Int()
    username = graphene.String()
    name = graphene.String()
    password = graphene.String()

    class Arguments:
        username = graphene.String()
        name = graphene.String()
        password = graphene.String()

    def mutate(self, info, username, name, password):
        user = User(username=username, name=name, password=password)
        user.save()


        return CreateUser(
            id=user.id,
            username=user.username,
            name=user.name,
            password=user.password
            
        )

class CreateTrip(graphene.Mutation):
    id = graphene.Int()
    driver_name = graphene.String()
    reg_number = graphene.String()
    opening_milage = graphene.Int()
    closing_milage = graphene.Int()
    destination = graphene.String()
    comments = graphene.String()
    date = graphene.Date()

    class Arguments:
        driver_name = graphene.String()
        reg_number = graphene.String()
        opening_milage = graphene.Int()
        closing_milage = graphene.Int()
        destination = graphene.String()
        comments = graphene.String()
        date = graphene.Date()

    def mutate(self, info, driver_name, reg_number, opening_milage, closing_milage, destination, comments, date):
        trip = Trip(driver_name=driver_name, reg_number=reg_number, opening_milage=opening_milage,
            closing_milage=closing_milage, destination=destination, comments=comments, date=date)
        trip.save()

        return CreateTrip(
            id=trip.id,
            driver_name=trip.driver_name,
            reg_number=trip.reg_number,
            opening_milage=trip.opening_milage,
            closing_milage=trip.closing_milage,
            destination=trip.destination,
            comments=trip.comments,
            date=trip.date
        )

class UpdateTrip(graphene.Mutation):
    id = graphene.Int()
    driver_name = graphene.String()
    reg_number = graphene.String()
    opening_milage = graphene.Int()
    closing_milage = graphene.Int()
    destination = graphene.String()
    comments = graphene.String()
    date = graphene.Date()

    class Arguments:
        id = graphene.Int(required=True)
        driver_name = graphene.String(required=False)
        reg_number = graphene.String(required=False)
        opening_milage = graphene.Int(required=False)
        closing_milage = graphene.Int(required=False)
        destination = graphene.String(required=False)
        comments = graphene.String(required=False)
        date = graphene.Date(required=True)

    def mutate(self, info, id, driver_name, reg_number, opening_milage, closing_milage, destination, comments, date):
        trip = Trip(id=id, driver_name=driver_name, reg_number=reg_number, opening_milage=opening_milage,
            closing_milage=closing_milage, destination=destination, comments=comments, date=date)
        trip.save()

        return UpdateTrip(
            id=trip.id,
            driver_name=trip.driver_name,
            reg_number=trip.reg_number,
            opening_milage=trip.opening_milage,
            closing_milage=trip.closing_milage,
            destination=trip.destination,
            comments=trip.comments,
            date=trip.date
        )

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_trip = CreateTrip.Field()
    update_trip = UpdateTrip.Field()

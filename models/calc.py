from peewee import *


DATABASE = SqliteDatabase("calc.db")


class BaseModel(Model):
    class Meta:
        database = DATABASE


class Buff(BaseModel):
    """
    Buff, contains name, image, duration, ability to be put by friend and multiplicator
    """
    name = TextField(unique=True)
    image = TextField(default=None, null=True)
    duration = IntegerField()
    friendly = BooleanField(default=True)
    multiplicator = IntegerField(default=2)

    @classmethod
    def create_buff(cls, components, **kwargs):
        try:
            with DATABASE.transaction():
                cls.create(
                    name=kwargs.get('name'),
                    image=kwargs.get('image', None),
                    duration=kwargs.get('duration', 720),
                    friendly=kwargs.get('friendly', True),
                    multiplicator=kwargs.get('multiplicator', 2)
                )

                for component in components:
                    Component.create_component(
                        buff=Buff.get(Buff.name ** kwargs.get("name")),
                        resource=component["resource"],
                        amount=component["amount"]
                    )

        except IntegrityError:
            raise ValueError("Buff already exists")


class Building(BaseModel):
    name = CharField(unique=True)
    image = CharField(null=True)
    time_cycle = IntegerField()
    time_path = IntegerField()
    limit = IntegerField()
    note = TextField()

    @classmethod
    def create_building(cls, incomings, outcomings, **kwargs):
        with DATABASE.transaction():
            cls.create(
                name=kwargs.get('name'),
                image=kwargs.get('image', None),
                time_cycle=kwargs.get('time_cycle', 180),
                time_path=kwargs.get('time_path', 24),
                limit=kwargs.get('limit', 0),
                note = TextField()
            )

            for incoming in incomings:
                IncomingResource.create_incoming_recource(
                    building=Building.get(Building.name ** kwargs.get("name")),
                    resource=incoming["resource"],
                    amount=incoming["amount"],
                    lasting=incoming.get("lasting", True),
                )

            for outcoming in outcomings:
                OutcomingResource.create_outcoming_resource(
                    building=Building.get(Building.name ** kwargs.get("name")),
                    resource=outcoming["resource"],
                    amount=outcoming["amount"]
                )

    def get_incomings(self):
        return IncomingResource.select().where(IncomingResource.building ** Building.get(Building.name == self.name))

    def get_outcomings(self):
        return OutcomingResource.select().where(
            OutcomingResource.building ** Building.get(Building.name == self.name)
            )

    def get_limit(self):
        return self.limit



class Resource(BaseModel):
    name = CharField(unique=True)
    cost = IntegerField(default=0, null=True)

    @classmethod
    def create_resource(
            cls, name,
            cost):
        with DATABASE.transaction():
                cls.create(
                    name=name,
                    cost=cost
                )

    def set_cost(self, new_cost):
        self.cost = new_cost
        self.save()


class Component(BaseModel):
    """
    The table is required to connect buffs to it's ingridients
    """
    buff = ForeignKeyField(
        rel_model=Buff,
        related_name="buff"
    )
    resource = ForeignKeyField(
        rel_model=Resource,
        related_name="recources"
    )
    amount = IntegerField()

    @classmethod
    def create_component(cls, buff, resource, amount):
        cls.create(
            buff=buff,
            resource=resource,
            amount=amount
        )


class IncomingResource(BaseModel):
    """
    Table containing link between building and its incoming resources
    """
    building = ForeignKeyField(
        rel_model=Building,
        related_name="incoming"
    )
    resource = ForeignKeyField(
        rel_model=Resource,
        related_name="incoming"
    )
    amount = IntegerField()
    lasting = BooleanField()

    @classmethod
    def create_incoming_recource(cls, building, resource, amount, lasting=False):
        cls.create(
            building=building,
            resource=resource,
            lasting=lasting,
            amount=amount
        )


class OutcomingResource(BaseModel):
    """
    Table containing link between building and its outcoming resources
    """
    building = ForeignKeyField(
        rel_model=Building,
        related_name="outcoming"
    )
    resource = ForeignKeyField(
        rel_model=Resource,
        related_name="outcoming"
    )
    amount = IntegerField()

    @classmethod
    def create_outcoming_resource(cls, building, resource, amount, note):
        cls.create(
            building = building,
            resource = resource,
            amount=amount
        )

class UpgradeResource(BaseModel):
    """
    Table containing resources for each level of upgrade of building
    """
    building = ForeignKeyField(
        rel_model=Building,
        related_name="building"
    )
    level = IntegerField()
    resource = ForeignKeyField(
        rel_model=Resource,
        related_name="resource"
    )
    amount = IntegerField()

    @classmethod
    def create_upgrade_resource(cls, building, level, resource, amount):
        cls.create(
            building = building,
            level = level,
            resource = resource,
            amount=amount
        )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Buff, Resource, Building, Component, IncomingResource, OutcomingResource, UpgradeResource], safe=True)
    DATABASE.close()



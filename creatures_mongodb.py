from mongoengine import *

class Creatures(Document):
    name = StringField()
    element = StringField()
    atk = FloatField(default=0)
    defense = IntField(default=0)

    def __repr__(self):
        return f"<Creatures:{self.name} - element:{self.element} - atk:{self.atk} - defense:{self.defense}>"


connect("Creatures")

pass

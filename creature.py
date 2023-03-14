import os
from random import randint, sample
import logging
from mongoengine import *
from filler_creatures import creatures, abilities

logging.basicConfig(level=logging.DEBUG)

#Ojalá my internet fuera así

class Ability(Document):
    name = StringField(required=True, unique=True)
    effect_stat = IntField()
    effect_status = StringField()

    description = StringField()

    meta = {'strict': False}

class Creature(Document):
    name = StringField(required=True, unique=True)
    image = StringField()


    hp = IntField(default=50, required=True)
    attack = IntField(required=True)
    defense = IntField(required=True)
    speed = IntField(required=True)
    ability = ReferenceField(Ability)
    description = StringField()
    lore = StringField()

    meta = {'strict': False}

    def repr(self):
        ability_name = self.ability.name if self.ability else "NO ability yet"
        return f"<Creature {self.name} - Atk {self.attack}: {ability_name}>"



if os.getenv("USE_LOCAL"):
    connect("Creatures")
    logging.debug("Running on local database.")
else:
    connect(host=os.getenv("CREATURE_DEN_DATABASE_URL"))
    logging.debug("Running on the cloud.")


Creature.drop_collection()
Ability.drop_collection()

# _________________________________________________Your code goes ______________________________________________________


a = Ability(name="Látigo Eléctrico", effect_stat= "15", description="Reducción de defensa hacia la electricidad.")

c = Creature(name="Angalost", image="424", hp=35, attack=12, defense=5, speed=3, description="Una anguíla de colores oscuros y mandíbula afilada.", lore="Esta anguíla poderosa se encuentra en lugares humedos, es despiadada y odia que invadan su territorio.")

a.save()
c.ability = a
c.save()

#_______________________________________________________________________________________________________________________

a = Ability(name="Embestida Furiosa", effect_stat= "150", description="Un impacto que te rompe tu defensa y penetra tu salud.")

c = Creature(name="Taurium", image="632", hp=200, attack=120, defense=300, speed=10, description="Un gran toro con cuernos enormes y aspecto azulado.", lore="Un mamífero letal que fortalece su resistencia cada vez que lo hacen enojar. Se encuentra en valles o bosques.")

a.save()
c.ability = a
c.save()

#_______________________________________________________________________________________________________________________

a = Ability(name="Ácido Letal", effect_stat= "30", description="Veneno que te afecta constantemente.")

c = Creature(name="Venomy", image="427", hp=20, attack=35, defense=10, speed=100, description="Una araña pequeña con rostro aterrorizante similar a la viuda negra", lore="Una araña de las tinieblas, demonio de la oscuridad que te prepara el camino a la muerte.")

a.save()
c.ability = a
c.save()

#_______________________________________________________________________________________________________________________

a = Ability(name="Garras Heladas", effect_stat= "40", description=" Menor esistencia de Hielo y Congelamiento Progresivo.")

c = Creature(name="Andrius", image="659", hp=100, attack=50, defense=40, speed=50, description="Un lobo con aspecto oscuro y siniestro y con un tamaño mas grande de lo normal.", lore="Una leyenda entre los caninos salvajes del inframundo helado, acechador de la madrugada que se muestra cada media noche.")

a.save()
c.ability = a
c.save()

#_______________________________________________________________________________________________________________________

a = Ability(name="Aplasta-Mentos", effect_stat= "20", description="+Penetración de Armadura.")

c = Creature(name="Smasho", image="311", hp=25, attack=15, defense=10, speed=43, description="Ave reptil azulada con placas en sus manos; rostro enfurecido y ojos rojos.", lore="Arma letal de aplastamiento, fuerza diminuta pero espiritu luchador, vive en campos y caza insectos.")

a.save()
c.ability = a
c.save()

#_______________________________________________________________________________________________________________________

a = Ability(name="Rayos de Lumina", effect_stat= "100", description="Ceguedad y -Res a la Luminosidad.")

c = Creature(name="Rangezard", image="806", hp=300, attack=250, defense=100, speed=60, description="Reptil humanoide con armadura musculosa con espinas; garras de tamaño enorme.", lore="Guerrero mortífero, guardian de los cielos que protege las puertas hacia la entrada del reino angelical.")

a.save()
c.ability = a
c.save()


#_______________________________________________________________________________________________________________________

a = Ability(name="Mal Abrasador", effect_stat= "75", description="-Res al Fuego y Quemado Constante.")

c = Creature(name="Flamerom", image="339", hp=500, attack=200, defense=100, speed=40, description="Creatura irregular de masa llameante con aspecto azul oscuro y cabeza rojiza.", lore="Maldicion del fuego y mal augurio de las entidades demoniacas.")

a.save()
c.ability = a
c.save()


#_______________________________________________________________________________________________________________________

a = Ability(name="Perfume Sonámbulo", effect_stat= "10", description="-Res a la Estabilidad, Mareo y debil a quedar capturado en el sueño.")

c = Creature(name="BlueFany", image="275", hp=50, attack=15, defense=5, speed=32, description="Felino de baja estatura, rostro tierno y pelaje azulado.", lore="Un gato solitario de los valles de rosas, acostumbra a cazar roedores. Tienen una vista muy afinada y son muy astutos.")

a.save()
c.ability = a
c.save()


#_______________________________________________________________________________________________________________________

a = Ability(name="Hojas Destripantes", effect_stat= "50", description="-Res de Vegetación, Daño cortante.")

c = Creature(name="Leafast", image="250", hp=120, attack=76, defense=57, speed=90, description="Reptil de hojas, grandes garras y alas.", lore="Bestia bendecida por la naturaleza, camuflado por la vegetación; un ser hojil.")

a.save()
c.ability = a
c.save()


#_______________________________________________________________________________________________________________________

a = Ability(name="Veneno Gracioso", effect_stat= "10", description="-Res al Veneno, Infectado del Veneno de la Risa, Paralización Constante.")

c = Creature(name="Jesterpple", image="512", hp=10, attack=5, defense=5, speed=2, description="Insecto manzano de bufón.", lore="La risa de los payasos, una manzana letal con un deber indescriptible.")

a.save()
c.ability = a
c.save()


#_______________________________________________________________________________________________________________________

#a = Ability(name="", effect_stat= "", description="")

#c = Creature(name="", image="", hp=, attack=, defense=, speed=, description="", lore="")

#a.save()
#c.ability = a
#c.save()

#_______________________________________________________________________________________________________________________


#Generating filler creatures


# find already used images
pics_already_used = Creature.objects().distinct("image")

all_pics = [str(n) for n in range (1, 829)]

unused_pics = list(set(all_pics).difference(pics_already_used))

for each_filler_creature, each_ability in zip(creatures, abilities):
    creature_name = each_filler_creature
    ability_name = each_ability

    creature_description = creatures[creature_name]["description"]
    creature_lore = creatures[creature_name]["lore"]
    ability_description = abilities[ability_name]

    hp = randint(1, 100)
    attack = randint(1, 100)
    defense =randint(1, 100)
    speed = randint(1, 100)
    image = sample(unused_pics, 1)[0]

    c = Creature(name=creature_name, description=creature_description,
                 hp=hp, attack=attack, defense=defense, speed=speed,
                 lore=creature_lore, image=image)

    a = Ability(name=ability_name, description=ability_description)

    a.save()
    c.ability = a
    c.save()

    pass

pass
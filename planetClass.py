class Planet:
    def __init__(self, name, planet_type, star):           

        if not(isinstance(name,str) and isinstance(planet_type,str) and isinstance(star,str)):
            raise TypeError('name, planet type, and star must be strings')
        elif name == '' or planet_type == '' or star == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')
        
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return(f'{self.name} is orbiting around {self.star}...')

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet('a1','a2','a3')
planet_2 = Planet('b1','b2','b3')
planet_3 = Planet('c1','c2','c3')

print(planet_1)
print(planet_1.orbit())
#print(planet_1.__str__())

print(planet_2)
print(planet_2.orbit())
#print(planet_2.__str__())

print(planet_3)
print(planet_3.orbit())
#print(planet_3.__str__())
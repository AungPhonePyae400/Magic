class Inter:
   __instance = None 
   def __new__(cls, name, course, nationality):
       if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.name = name
            cls.__instance.course = course
            cls.__instance.nationality = nationality
       return cls.__instance
        
okan = Inter('Kyrenia University Student', 'Cmp 242', 'Turk')
print(okan.name)
print(okan.course)
print(okan.nationality)

aung = Inter('Kyrenia University Student', 'cmp 244', 'Asian')
print(aung.name)
print(aung.course)
print(aung.nationality)


print(okan is aung)

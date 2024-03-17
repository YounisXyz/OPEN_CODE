# GitHub : https://github.com/YounisXyz
# Facebook : https://www.facebook.com/xyzhackers
import random
import string
import time
from faker import Faker
while True:
    time.sleep(.1)
    khan = ''.join(random.choice(string.digits) for _ in range(11))
    numbers = ('1000'+khan)
    faker = Faker('ar') # ar k jga ager aap ko chahye k English name Waly IDs dump kry TU ar k jga en lagalo 
    name = faker.name()
#    print(''.join(str(num) for num in numbers), name)
    result = f"\x1b[38;5;105m{numbers} \x1b[38;5;106m| \x1b[38;5;85m{name} \x1b[38;5;38m"
    xyz = (f"{numbers} | {name}\n")
    print(result)
    with open('ids_khan.txt','a') as mm:
        mm.write(xyz)
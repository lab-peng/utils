import random
from faker import Faker

fake = Faker(['zh_CN'])




for i in range(3):
    client = fake.company()
    contact_person = fake.name()
    contact = fake.phone_number()
    address = fake.street_name() + str(random.randint(1, 100)) + '号'
    obligee = fake.name()
    land_area = random.randint(20,200)
    house_area = random.randint(20, 200)
    estate = fake.company_prefix() + random.choices(['花园', '花苑', '家园', '一区', ''])[0]
    print(client, contact_person, address, estate)

# pip install Faker --index https://pypi.tuna.tsinghua.edu.cn/simple
import random
import json
from faker import Faker
from pinyin import pinyin

fake = Faker(['zh_CN'])

# project_list = []

# for i in range(50):
#     delegate_date = fake.date_between(start_date='-3y', end_date='today')
#     client = fake.company()
#     market_type = random.choice(['一级市场', '二级市场'])
#     project_name = client + '测绘项目'
#     project_type = random.choice(['不动产测量', '非不动产测量'])
#     project_site = fake.street_address()
#     project_coord = random.random(), random.random()
#     description = fake.paragraph(nb_sentences=5)
#     delegate_contact = fake.name()
#     contact_phone = fake.phone_number()
#     workload = random.randint(1, 100)
#     estimate_output = random.randint(1, 1000)
#     project_allocation = random.choice(['苏拓测', '苏拓绘'])
#     project_num = f'{project_allocation}(2021)第{i+1002}号'
#     d = dict()
#     d['delegate_date'] = str(delegate_date)
#     d['client'] = client
#     d['market_type'] = market_type
#     d['project_name'] = market_type
#     d['project_type'] = project_type
#     d['project_site'] = project_site
#     d['project_coord'] = project_coord
#     d['description'] = description
#     d['delegate_contact'] = delegate_contact
#     d['contact_phone'] = contact_phone
#     d['workload'] = workload
#     d['estimate_output'] = estimate_output
#     d['project_allocation'] = project_allocation
#     d['project_num'] = project_num
#     project_list.append(d)

# # Output a json file
# with open('projects.json', 'w', encoding='utf-8') as fw:
#     json.dump(project_list, fw, ensure_ascii=False, indent=4)


employee_list = []
for _ in range(10):
    name = fake.last_name() + fake.first_name_male()
    username = pinyin(name)
    password = '12341234'
    join_date = fake.date_between(start_date='-10y', end_date='today')  # from 10 years before to today
    gender = '男'
    ethnicity = '汉'
    birthday = fake.date_of_birth(minimum_age=18, maximum_age=50)
    address = fake.address()[:-7]
    email = username + '@qq.com'
    phone = fake.phone_number()
    poli_status = random.choice(['党员', '共青团员', '无党派人士', '群众'])
    d = dict()
    d['name'] = name
    d['username'] = username
    d['password'] = password
    d['join_date'] = str(join_date)
    d['gender'] = gender
    d['ethnicity'] = ethnicity
    d['birthday'] = str(birthday)
    d['address'] = address
    d['email'] = email
    d['phone'] = phone
    d['poli_status'] = poli_status
    employee_list.append(d)

for employee in employee_list:
    print(employee)

# Output a json file
with open('employees.json', 'w', encoding='utf-8') as fw:
    json.dump(employee_list, fw, ensure_ascii=False, indent=4)

# # Populate the Database with data in json files by Django ORM





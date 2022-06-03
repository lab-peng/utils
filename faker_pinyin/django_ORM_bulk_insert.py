import random
import datetime

from mapping.models import Project, Process

employee_id = random.randint(1010, 1018)

projects = Project.objects.all()

for p in projects:
    Process.objects.create(project=p, field_principal=str(employee_id), stages='1,2')

processes = Process.objects.all()

for p in processes[:45]:
    p.field_start = datetime.date(2021, 7, 19)
    p.field_finish = datetime.date(2021, 7, 20)
    p.office_principle = str(employee_id)
    p.stages = '1,2,3'
    p.save()

for p in processes[:40]:
    pass



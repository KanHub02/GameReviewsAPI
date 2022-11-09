from celery import shared_task
from users.services import Viewer
from users.models import Ip
from core.celery import app

#@shared_task(bind=True)
@app.task
def get_view(instance, ip_adress):
    if Ip.objects.filter(ip=ip_adress).exists():
        instance.views.add(Ip.objects.get(ip=ip_adress))
    else:
        Ip.objects.create(ip=ip_adress)
        instance.views.add(Ip.objects.get(ip=ip_adress))

    return "Ok"
from .serializers import GeneralOrderSerializer
from .models import GenOrderTable


def getAllGeneralOrderObjects():
    return GenOrderTable.objects.all()


def getGeneralOrderObject(order_id):
    return GenOrderTable.objects.get(order_id = order_id)


def updateOrderStatus(updated_status, order_id):
    order = getGeneralOrderObject(order_id)
    order.status = updated_status
    order.save() 







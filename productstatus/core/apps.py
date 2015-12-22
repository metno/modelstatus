from django.db.models.signals import post_save
from django.apps import AppConfig
from django.conf import settings

import productstatus.core.zeromq


class ProductstatusConfig(AppConfig):
    name = 'productstatus.core'

    def ready(self):
        """
        Set signal hook for sending ZeroMQ messages for specific Productstatus models/resources.
        """

        self.zmq = productstatus.core.zeromq.ZMQPublisher(settings.ZEROMQ_SUBSCRIBE_SOCKET)

        publish_resources = ['ProductInstance', 'DataInstance', 'Data']
        for resource in publish_resources:
            post_save.connect(self.zmq.publish_resource, sender=self.get_model(resource))
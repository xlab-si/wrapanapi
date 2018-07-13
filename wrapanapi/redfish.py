# coding: utf-8
"""Backend management system classes
Used to communicate with providers without using CFME facilities
"""
from __future__ import absolute_import

from .base import WrapanapiAPIBase


class RedfishSystem(WrapanapiAPIBase):
    """Client to Redfish API
    Args:
        hostname: The hostname of the system.
        username: The username to connect with.
        password: The password to connect with.
    """
    _api = None

    _stats_available = {
        'num_server': lambda self: 1,
    }

    def __init__(self, hostname, username, password, protocol="https", port=None, **kwargs):
        super(RedfishSystem, self).__init__(kwargs)
        self.port = port or kwargs.get('api_port', 443)
        self.auth = (username, password)
        self.url = '{}://{}:{}/'.format(protocol, hostname, self.port)
        self._servers_list = None
        self.kwargs = kwargs

    @property
    def _identifying_attrs(self):
        return {'url': self.url}

    def info(self):
        return 'RedfishSystem url={}'.format(self.url)

    def __del__(self):
        """Disconnect from the API when the object is deleted"""

import etcd
import unittest
import geventhttpclient.response
import json
try:
    import mock
except ImportError:
    from unittest import mock


class TestClientApiBase(unittest.TestCase):

    def setUp(self):
        self.client = etcd.Client()

    def _prepare_response(self, s, d, cluster_id=None):
        if isinstance(d, dict):
            data = json.dumps(d).encode('utf-8')
        else:
            data = d.encode('utf-8')

        r = mock.create_autospec(geventhttpclient.response.HTTPSocketPoolResponse)(None, None)
        r.status_code = s
        r.read.return_value = data
        r.get.side_effect = lambda x, default=None: "abcd1234" if x == "x-etcd-cluster-id" else default
        return r

    def _mock_api(self, status, d, cluster_id=None):
        resp = self._prepare_response(status, d, cluster_id=cluster_id)
        self.client.api_execute = mock.MagicMock(return_value=resp)

    def _mock_exception(self, exc, msg):
        self.client.api_execute = mock.Mock(side_effect=exc(msg))

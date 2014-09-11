import os
import requests

from test_runner import BaseComponentTestCase
from qubell.api.private.testing import instance, environment, workflow, values

@environment({
    "default": {},
    "AmazonEC2_CentOS_63": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-bf5021d6"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "root"
        }]
    },
    "AmazonEC2_Ubuntu_1204": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-967edcff"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "ubuntu"
        }]
    },
    "AmazonEC2_Ubuntu_1004": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-9f3906f6"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "ubuntu"
        }]
    }
})
class SolrDevTestCase(BaseComponentTestCase):
    name = "component-solr-dev"
    meta = "https://raw.githubusercontent.com/qubell-bazaar/component-solr-dev/master/meta.yml"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
  }]

    @classmethod
    def timeout(cls):
        return 30
   
    @instance(byApplication=name)
    def test_zoo_ui(self, instance):
        hosts = instance.returnValues['solr-zoo.zoo-ui']
        for host in hosts:
           resp = requests.get(host, verify=False)
           assert resp.status_code == 200
    
    @instance(byApplication=name)
    def test_solr_hosts(self, instance):
        hosts = instance.returnValues['solr-zoo.solr-url']
        for host in hosts:
           resp = requests.get(host, verify=False)
           assert resp.status_code == 200 

Description
===========
Install and configure Solr with additional Zookeeper support

Version 2.1-39p
-------------

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.tonomi.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-solr-dev/2.1-39p/meta.yml)

Attributes
----------

Configurations
--------------
 - Solr 4.x (latest), Amazon Linux (us-east-1/ami-1ba18d72), AWS EC2 m1.small, ec2-user
 - Solr 4.x (latest), CentOS 6.4 (us-east-1/ami-bf5021d6), AWS EC2 m1.small, root
 - Solr 4.x (latest), Ubuntu 12.04 (us-east-1/ami-967edcff), AWS EC2 m1.small, ubuntu
 - Solr 4.x (latest), Ubuntu 10.04 (us-east-1/ami-9f3906f6), AWS EC2 m1.small, ubuntu

Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Either installed Chef on target compute OR launch under root
 - Internet access from target compute:
  - S3 bucket with Chef recipes: ** (TBD)
  - If Chef is not installed: ** (TBD)

Implementation notes
--------------------
 - Installation is based on Chef recipes from ""

Usage
-----
If you want enable Zookeeper support then `node['cookbook-qubell-solr']['zookeeper']['host']` should be set to zookeeper hosts IP.

- `node['cookbook-qubell-solr']['collection']` must be represented as array ["collection1","collection2"] in this case listed collections will be created.
- `node['cookbook-qubell-solr']['collection']` represented as array ["uri://path"] will download **zip** or **tar.gz** and unpack previosly prepaired collection

**Please note:** archived collection must contain only collection folders *(collection1, collection2)* and *solr.xml* collections configuration file 

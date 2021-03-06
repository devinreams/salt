#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
=================
Nodegroups Pillar
=================

Introspection: to which nodegroups does my minion belong?
Provides a pillar with the default name of `nodegroups`
which contains a list of nodegroups which match for a given minion.

.. versionadded:: Carbon

Command Line
------------

.. code-block:: bash
    salt-call pillar.get nodegroups
    local:
        - class_infra
        - colo_sj
        - state_active
        - country_US
        - type_saltmaster

Configuring Nodegroups Pillar
-----------------------------

.. code-block:: yaml

    extension_modules: /srv/salt/ext
    ext_pillar:
      - nodegroups:
          pillar_name: 'nodegroups'

'''

# Import futures
from __future__ import absolute_import

# Import Salt libs
from salt.minion import Matcher

# Import 3rd-party libs
import salt.ext.six as six

__version__ = '0.0.1'


def ext_pillar(minion_id, pillar, pillar_name=None):
    '''
    A salt external pillar which provides the list of nodegroups of which the minion is a memeber.

    :param minion_id: provided by salt, but not used by nodegroups ext_pillar
    :param pillar: provided by salt, but not used by nodegroups ext_pillar
    :param pillar_name: optional name to use for the pillar, defaults to 'nodegroups'
    :return: a dictionary which is included by the salt master in the pillars returned to the minion
    '''

    pillar_name = pillar_name or 'nodegroups'
    m = Matcher(__opts__)
    all_nodegroups = __opts__['nodegroups']
    nodegroups_minion_is_in = []
    for nodegroup_name in six.iterkeys(all_nodegroups):
        if m.nodegroup_match(nodegroup_name, all_nodegroups):
            nodegroups_minion_is_in.append(nodegroup_name)
    return {pillar_name: nodegroups_minion_is_in}

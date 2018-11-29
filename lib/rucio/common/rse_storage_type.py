# Copyright European Organization for Nuclear Research (CERN)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0OA
#
# Authors:
# - Wen Guan, <wen.guan@cern.ch>, 2015
# - Eric Vaandering, <ewv@fnal.gov>, 2018

# PY3K COMPATIBLE

"""
Get and cache the storage type of an RSE
"""

import logging
import traceback

from dogpile.cache import make_region
from dogpile.cache.api import NoValue

from rucio.core.rse import get_rse_name
from rucio.rse import rsemanager

REGION = make_region().configure('dogpile.cache.memcached',
                                 expiration_time=24 * 3600,
                                 arguments={'url': "127.0.0.1:11211", 'distributed_lock': True})


def get_rse_storage_type(rse_id, session=None):
    """
    Get RSE storage type

    :param rse_id:  The RSE id.
    :param session: The database session in use.

    :returns: A dictionary with RSE attributes for a RSE.
    """

    result = REGION.get(rse_id)

    if isinstance(result, NoValue):
        result = None
        rse_name = None
        rse_id = None
        try:
            rse_name = get_rse_name(rse_id=rse_id)
            rse_info = rsemanager.get_rse_info(rse_name, session=session)
            result = rse_info['type']
            REGION.set(rse_id, result)
        except:
            logging.warning("Failed to get RSE type for RSE ID: %s, name %s, error: %s" %
                            (rse_id, rse_name, traceback.format_exc()))
    return result

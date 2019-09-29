# -*- coding: utf-8 -*-

'''
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   bert_bilstm_crf_entity_extractor.py
 
@Time    :   2019-09-26 11:09
 
@Desc    :
 
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import re
import io

import typing
import pickle

from builtins import str
from typing import Any, Dict, List, Optional, Text, Tuple

from rasa.nlu.extractors import EntityExtractor
from rasa.nlu.model import Metadata
from rasa.nlu.training_data import Message

from chatbot_nlu.utils.bilstm_utils import \
    char_mapping, tag_mapping, prepare_dataset, BatchManager, iob_iobes, \
    iob2, save_model, create_model, input_from_line

from chatbot_nlu.models.model import Model
from multiprocessing import cpu_count
import jieba

logger = logging.getLogger(__name__)

if typing.TYPE_CHECKING:
    import numpy as np
    import tensorflow as tf
    import tensorflow.contrib

try:
    import tensorflow as tf
except ImportError:
    tf = None
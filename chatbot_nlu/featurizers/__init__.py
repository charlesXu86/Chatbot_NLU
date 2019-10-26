import numpy as np

from typing import Any, Text
from chatbot_nlu.training_data import Message
from chatbot_nlu.components import Component
from chatbot_nlu.constants import MESSAGE_VECTOR_FEATURE_NAMES, MESSAGE_TEXT_ATTRIBUTE


class Featurizer(Component):
    @staticmethod
    def _combine_with_existing_features(
        message: Message,
        additional_features: Any,
        feature_name: Text = MESSAGE_VECTOR_FEATURE_NAMES[MESSAGE_TEXT_ATTRIBUTE],
    ) -> Any:
        if message.get(feature_name) is not None:
            return np.concatenate(
                (message.get(feature_name), additional_features), axis=-1
            )
        else:
            return additional_features
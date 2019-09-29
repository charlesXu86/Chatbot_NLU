"""This is a somewhat delicate package. It contains all registered components
and preconfigured templates.

Hence, it imports all of the components. To avoid cycles, no component should
import this in module scope."""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import typing
from chatbot_nlu import utils
from typing import Any
from typing import Optional
from typing import Text
from typing import Type

from chatbot_nlu.classifiers.keyword_intent_classifier import KeywordIntentClassifier
from chatbot_nlu.classifiers.mitie_intent_classifier import MitieIntentClassifier
from chatbot_nlu.classifiers.sklearn_intent_classifier import SklearnIntentClassifier
from chatbot_nlu.classifiers.embedding_intent_classifier import EmbeddingIntentClassifier
from chatbot_nlu.extractors.duckling_extractor import DucklingExtractor
from chatbot_nlu.extractors.duckling_http_extractor import DucklingHTTPExtractor
from chatbot_nlu.extractors.entity_synonyms import EntitySynonymMapper
from chatbot_nlu.extractors.mitie_entity_extractor import MitieEntityExtractor
from chatbot_nlu.extractors.spacy_entity_extractor import SpacyEntityExtractor
from chatbot_nlu.extractors.crf_entity_extractor import CRFEntityExtractor


from chatbot_nlu.extractors.bilstm_crf_entity_extractor import BilstmCRFEntityExtractor # customize
from chatbot_nlu.extractors.jieba_pseg_extractor import JiebaPsegExtractor  # customize
from chatbot_nlu.extractors.pyltp_extractor import PyLTPEntityExtractor  # customize
from chatbot_nlu.classifiers.entity_edit_intent import EntityEditIntent  # customize

from chatbot_nlu.featurizers.intent_featurizer_wordvector import WordVectorsFeaturizer  # customize
from chatbot_nlu.featurizers.bert_vectors_featurizer import BertVectorsFeaturizer  # customize

from chatbot_nlu.classifiers.embedding_bert_intent_classifier import EmbeddingBertIntentClassifier  # customize
from chatbot_nlu.classifiers.embedding_bert_intent_estimator_classifier import EmbeddingBertIntentEstimatorClassifier #customize

from chatbot_nlu.featurizers.mitie_featurizer import MitieFeaturizer
from chatbot_nlu.featurizers.ngram_featurizer import NGramFeaturizer
from chatbot_nlu.featurizers.regex_featurizer import RegexFeaturizer
from chatbot_nlu.featurizers.spacy_featurizer import SpacyFeaturizer
from chatbot_nlu.featurizers.count_vectors_featurizer import CountVectorsFeaturizer
from chatbot_nlu.model import Metadata
from chatbot_nlu.tokenizers.mitie_tokenizer import MitieTokenizer
from chatbot_nlu.tokenizers.spacy_tokenizer import SpacyTokenizer
from chatbot_nlu.tokenizers.jieba_tokenizer import JiebaTokenizer
from chatbot_nlu.tokenizers.whitespace_tokenizer import WhitespaceTokenizer
from chatbot_nlu.utils.mitie_utils import MitieNLP
from chatbot_nlu.utils.spacy_utils import SpacyNLP

if typing.TYPE_CHECKING:
    from chatbot_nlu.components import Component
    from chatbot_nlu.config import RasaNLUModelConfig, RasaNLUModelConfig

# Classes of all known components. If a new component should be added,
# its class name should be listed here.
component_classes = [
    SpacyNLP, MitieNLP,
    SpacyEntityExtractor, MitieEntityExtractor, DucklingExtractor,
    CRFEntityExtractor, DucklingHTTPExtractor,
    BilstmCRFEntityExtractor, # customize
    JiebaPsegExtractor, # customize
    EntityEditIntent,  # customize
    WordVectorsFeaturizer,  # customize
    BertVectorsFeaturizer,  # customize
    EmbeddingBertIntentClassifier,  # customize
    PyLTPEntityExtractor, # customize
    EntitySynonymMapper,
    SpacyFeaturizer, MitieFeaturizer, NGramFeaturizer, RegexFeaturizer,
    CountVectorsFeaturizer,
    MitieTokenizer, SpacyTokenizer, WhitespaceTokenizer, JiebaTokenizer,
    SklearnIntentClassifier, MitieIntentClassifier, KeywordIntentClassifier,
    EmbeddingIntentClassifier,EmbeddingBertIntentEstimatorClassifier
]

# Mapping from a components name to its class to allow name based lookup.
registered_components = {c.name: c for c in component_classes}

# To simplify usage, there are a couple of model templates, that already add
# necessary components in the right order. They also implement
# the preexisting `backends`.
registered_pipeline_templates = {
    "spacy_sklearn": [
        "nlp_spacy",
        "tokenizer_spacy",
        "intent_featurizer_spacy",
        "intent_entity_featurizer_regex",
        "ner_crf",
        "ner_synonyms",
        "intent_classifier_sklearn"
    ],
    "keyword": [
        "intent_classifier_keyword",
    ],
    "tensorflow_embedding": [
        "tokenizer_whitespace",
        "ner_crf",
        "intent_featurizer_count_vectors",
        "intent_classifier_tensorflow_embedding",
        "intent_estimator_classifier_tensorflow_embedding_bert"
    ]
}


def pipeline_template(s):
    components = registered_pipeline_templates.get(s)

    if components:
        # converts the list of components in the configuration
        # format expected (one json object per component)
        return [{"name": c} for c in components]

    else:
        return None


def get_component_class(component_name):
    # type: (Text) -> Optional[Type[Component]]
    """Resolve component name to a registered components class."""

    if component_name not in registered_components:
        try:
            return utils.class_from_module_path(component_name)
        except Exception:
            raise Exception(
                    "Failed to find component class for '{}'. Unknown "
                    "component name. Check your configured pipeline and make "
                    "sure the mentioned component is not misspelled. If you "
                    "are creating your own component, make sure it is either "
                    "listed as part of the `component_classes` in "
                    "`chatbot_nlu.registry.py` or is a proper name of a class "
                    "in a module.".format(component_name))
    return registered_components[component_name]


def load_component_by_name(component_name,  # type: Text
                           model_dir,  # type: Text
                           metadata,  # type: Metadata
                           cached_component,  # type: Optional[Component]
                           **kwargs  # type: **Any
                           ):
    # type: (...) -> Optional[Component]
    """Resolves a component and calls its load method to init it based on a
    previously persisted model."""

    component_clz = get_component_class(component_name)
    return component_clz.load(model_dir, metadata, cached_component, **kwargs)


def create_component_by_name(component_name, config):
    # type: (Text, RasaNLUModelConfig) -> Optional[Component]
    """Resolves a component and calls it's create method to init it based on a
    previously persisted model."""

    component_clz = get_component_class(component_name)
    return component_clz.create(config)

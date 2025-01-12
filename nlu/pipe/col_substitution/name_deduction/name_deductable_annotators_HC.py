"""Define annotators for which names should be deducted using the mapped function"""
from nlu.pipe.col_substitution.col_substitution_HC import *
from nlu.pipe.col_substitution.col_substitution_OS import *

from sparknlp_jsl.annotator  import *


name_deductable_HC=[
    MedicalNerModel,
    NerConverterInternal,
    SentenceEntityResolverModel,
    ChunkEntityResolverModel,
    RelationExtractionModel,
    RelationExtractionDLModel,
    PosologyREModel,
    # Chunk2Token,
    ContextualParserModel, # todo
    DrugNormalizer,
    GenericClassifierModel,
    # NerDisambiguatorModel
    # ChunkMergeModel
    # RENerChunksFilter
    NerOverwriter
]



always_name_deductable_HC=[
    SentenceEntityResolverModel,
    ChunkEntityResolverModel,
    RelationExtractionModel,
    RelationExtractionDLModel,
    PosologyREModel,
    # Chunk2Token,
    ContextualParserModel, # todo
    DrugNormalizer,
    GenericClassifierModel,
    # NerDisambiguatorModel
    # ChunkMergeModel
    # RENerChunksFilter
    NerOverwriter
]




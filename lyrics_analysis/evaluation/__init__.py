from .dummy_metrics import eval_random
from .dummy_metrics import eval_line_length
from .syntactic_metrics import count_unique_words
from .syntactic_metrics import proportion_parts_of_speech

__all__ = [
    eval_random,
    eval_line_length
]
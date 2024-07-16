from metaflow.decorators import StepDecorator
from functools import wraps

class huggingface_dataset_deco:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, step_func):

        @wraps(step_func)
        def f(s):
            step_func(s)
        
        from metaflow import _huggingface_dataset, card, current

        _card = card(
            type="huggingface_dataset", 
            id="hf_dataset_outer", 
            options={"dataset_id": self.kwargs.get("id")}
        )

        return _card(_huggingface_dataset(**self.kwargs)(step_func))


class HuggingfaceDatasetDecorator(StepDecorator):

    name = "_huggingface_dataset"
    defaults = {"id": None}
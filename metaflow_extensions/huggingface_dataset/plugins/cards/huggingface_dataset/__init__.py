from metaflow.cards import MetaflowCard 
from metaflow.exception import MetaflowException

class HuggingfaceDatasetCard(MetaflowCard):
    type = "huggingface_dataset"

    def __init__(self, options={'id': None}):
        print('[DEBUG] card init', options)
        if not options.get('id'):
            raise MetaflowException("Dataset ID is required for Huggingface Dataset card.")
        self.dataset_id = options.get('id')

    def render(self, task):
        return f'<html><body><h1>{self.dataset_id}</h1></body></html>'
        # print('[DEBUG] card render', self.dataset_id)
        # dataset_viewer_url = f'https://huggingface.co/datasets/{self.dataset_id}/embed/viewer'
        # return f'<html><body><h1>{self.dataset_id}</h1><iframe src="{dataset_viewer_url}"></iframe></body></html>'

CARDS = [HuggingfaceDatasetCard]
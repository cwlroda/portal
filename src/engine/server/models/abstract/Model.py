"""Contain the factory function <model>"""
from server.models.tensorflow_model import TensorflowModel
from server.models.darknet_model import DarknetModel


def Model(
    model_type: str, directory: str, name: str, description: str, **kwargs
):
    """Factory function that routes the model to the specific class."""

    args = [directory, name, description]

    model_class = {
        "tensorflow": TensorflowModel,
        "darknet": DarknetModel,
    }

    return model_class[model_type](*args, **kwargs)

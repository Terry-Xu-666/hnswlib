import numpy as np
import pytest
import hnswlib


def test_get_layer_graph():
    # Create an instance of the Index class
    index = hnswlib.Index(space="l2", dim=128)
    index.init_index(max_elements=1000, M=16, ef_construction=200, random_seed=42, allow_replace_deleted=False)

    # Add some items to the index
    data = np.random.rand(1000, 128).astype(np.float32)
    index.add_items(data)

    # Retrieve the layer graph for a specific level
    level = 0
    layer_graph = index.get_layer_graph(level)

    # Check if the returned layer graph is a numpy array
    assert isinstance(layer_graph, np.ndarray), "The layer graph should be a numpy array."

    # Check the shape of the layer graph
    expected_shape = (index.get_current_count(), 2*index.M)  # Assuming M is the max number of neighbors
    assert layer_graph.shape == expected_shape, f"Expected shape {expected_shape}, but got {layer_graph.shape}."

    # Check for valid connections (no negative values except for padding)
    assert np.all(layer_graph >= -1), "Layer graph contains invalid values."

# Run the test
pytest.main([__file__])

import hnswlib_noderag
import numpy as np
index = hnswlib_noderag.Index(space="l2", dim=128)
index.init_index(max_elements=1000, M=16, ef_construction=200, random_seed=42, allow_replace_deleted=False)



# Add some items to the index
data = np.random.rand(1000, 128).astype(np.float32)
index.add_items(data)

# Retrieve the layer graph for a specific level
level = 0
layer_graph = index.get_layer_graph(level)

print(layer_graph)


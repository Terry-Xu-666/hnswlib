# Hnswlib - fast approximate nearest neighbor search
Header-only C++ HNSW implementation with python bindings, insertions and updates.

This updated version introduces new bindings for the graph layer visualization in the original [hnswlib project](https://github.com/nmslib/hnswlib). If you are interested in HNSW, please refer to the original GitHub repository. This project is just for specific project (TGRAG use).

### References
HNSW paper:
```
@article{malkov2018efficient,
  title={Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs},
  author={Malkov, Yu A and Yashunin, Dmitry A},
  journal={IEEE transactions on pattern analysis and machine intelligence},
  volume={42},
  number={4},
  pages={824--836},
  year={2018},
  publisher={IEEE}
}
```

The update algorithm supported in this repository is to be published in "Dynamic Updates For HNSW, Hierarchical Navigable Small World Graphs" US Patent 15/929,802 by Apoorv Sharma, Abhishek Tayal and Yury Malkov.

Original work Copyright 2020 Yury Malkov
Modified work Copyright 2024 Tianyang Xu

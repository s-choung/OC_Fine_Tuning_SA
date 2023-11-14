# FineTuneMLP_SA_Design

Welcome to `FineTuneMLP_SA_Design`! 
It provides data generation,training and evaluation code/data for ration design of single atom catalyst. This projects uses GemNet-OC20 + OC22 pretrained model delveloped in [Open Catalyst Project](https://opencatalystproject.org/) (GemNet-OC [[`arXiv`](https://arxiv.org/abs/2204.02782)] [[`code`](https://github.com/Open-Catalyst-Project/ocp/tree/main/ocpmodels/models/gemnet_oc)])
The project focuses on fine-tuning backbone models using a small-sized in-house generated dataset and has several key contributions to the field:



## Project Overview

1. **Rational Design of SA Workflow**: We explore the promise of fine-tuning strategies that leverage small data to improve global optimization. We employ Genetic Algorithms (GA) using an accurate fine-tuned Machine learning potential (MLP) as a surrogate model.We provide two successful fine-tuning approaches for Pt/CeO2 and SA screening, which can serve as benchmarks for the research community.

2. **Dataset and Fine-tuned Models specified on SA/oxide**: We have open-sourced our codes and database, enabling the wider research community to build improved models and accelerate the design of Single Atom Catalytic Active Sites. 



### Acknowledgements

- This codebase was mostly built based on [Open Catalyst Project](https://opencatalystproject.org/) 




## Citing `FineTuneMLP_SA_Design`

Please Tuned on for the upcoming publications:

```bibtex
@article{ft_pt_ceo2_global_optimization,
    author = {Seokhyun Choung†, Wongyu Park† and Jeong Woo Han*},
    title = {Genetic Algorithm Framework for Accelerated Discovery of Global Minimum Configurations of Pt/CeO2 Catalytic Active Site Using Machine Learning Potential},
    journal = {?},
    year = {2024},
    doi = {?},
}
```
```bibtex
@article{ft_sa_screening,
    author = {Seokhyun Choung†, Wongyu Park† and Jeong Woo Han*},
    title = {Rapid mapping of Stable and Active  Single Atom Active Site Motifs Accelerated by MLP based Automated Workflow},
    journal = {?},
    year = {2024},
    doi = {?},
}
```

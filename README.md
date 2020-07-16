# ArbEngVec

Word Embeddings (WE) are getting increasingly popular and widely applied in many Natural Language Processing (NLP) applications due to their effectiveness in capturing semantic properties of words; Machine Translation (MT), Information Retrieval (IR) and Information Extraction (IE) are among such areas.  In this project , we propose an open source ArbEngVec which provides several Arabic-English cross-lingual word embedding models.  To train our bilingual models, we use a large dataset with more than 93 million pairs of Arabic-English parallel sentences. 

## Evaluation

WE perform both extrinsic and intrinsic evaluations for the different word embedding model variants. The extrinsic evaluation assesses the performance of models on the cross-language Semantic Textual Similarity (STS), while the intrinsic evaluation is based on the Word Translation (WT) task.


## Models 

All model variants with GenSim format can be found here: https://drive.google.com/open?id=1S2ugc8pZshYD3mTAkShKoA7He4Ih4gnS

All model variants with Binary format can be found here: https://drive.google.com/open?id=1guk6kNVoJFuaq1_zFRaEKBPZjz7LhOuj



## Visualisation : Random shuffle with SkipGram Model


![Random shuffle with SkipGram](https://raw.githubusercontent.com/Raki22/ArbEngVec/master/random_skip_plot.png)


## Citation

In further research usage of this script please use this citation:


@inproceedings{lachraf-etal-2019-arbengvec,
    title = "{A}rb{E}ng{V}ec : {A}rabic-{E}nglish Cross-Lingual Word Embedding Model",
    author = "Lachraf, Raki  and
      Nagoudi, El Moatez Billah  and
      Ayachi, Youcef  and
      Abdelali, Ahmed  and
      Schwab, Didier",
    booktitle = "Proceedings of the Fourth Arabic Natural Language Processing Workshop",
    month = aug,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-4605",
    doi = "10.18653/v1/W19-4605",
    pages = "40--48",
}

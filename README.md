# Adapter-Tuning for Empathy Prediction

Experimental code for CAISA at WASSA 2022: Adapter-Tuning for Empathy Prediction


## Citation

If you use [our work](https://aclanthology.org/2022.wassa-1.31/), please cite our paper

```
@inproceedings{lahnala-etal-2022-caisa,
    title = "{CAISA} at {WASSA} 2022: Adapter-Tuning for Empathy Prediction",
    author = "Lahnala, Allison  and
      Welch, Charles  and
      Flek, Lucie",
    booktitle = "Proceedings of the 12th Workshop on Computational Approaches to Subjectivity, Sentiment {\&} Social Media Analysis",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.wassa-1.31",
    doi = "10.18653/v1/2022.wassa-1.31",
    pages = "280--285",
    abstract = "We build a system that leverages adapters, a light weight and efficient method for leveraging large language models to perform the task Em- pathy and Distress prediction tasks for WASSA 2022. In our experiments, we find that stacking our empathy and distress adapters on a pre-trained emotion lassification adapter performs best compared to full fine-tuning approaches and emotion feature concatenation. We make our experimental code publicly available",
}
```


## EmotionStack

[Empathy_Distress_Inference.ipynb](./Empathy_Distress_Inference.ipynb): Code to use pretrained empathy and distress adapters (stacked on emotion adapter) to predict empathy and distress scores.

[EmotionStack_EMP.ipynb](./EmotionStack_EMP.ipynb): Code for predicting the empathy and distress at essay level using the EmotionStack approach.

[EmotionStack_EMO.ipynb](./EmotionStack_EMO.ipynb): Code for predicting the emotion labels at essay level using the EmotionStack approach.

## EpitomeFusion

[Train_Empathy_Adapters.ipynb](./Train_Empathy_Adapters.ipynb): Code for training the adapters on each of the EPITOME [1](#references) classes of empathy. You can obtain the [epitome dataset here.](https://github.com/behavioral-data/Empathy-Mental-Health/tree/master/dataset)


[EpitomeFusion.ipynb](./EpitomeFusion.ipynb): Code for predicting the emotion labels at essay level using the EpitomeFusion approach.


## Adapters

The adapters we trained for the EMP and EMO tasks are in the [trained_adapters](./trained_adapters) folder. See [Empathy_Distress_Inference.ipynb](./Empathy_Distress_Inference.ipynb) as an example of how to load and use them for inference.

## Predictions

The predictions for distress, empathy, and emotion on the test set are located in the [predictions](./predictions) folder.



## References

[1] Sharma, Ashish, et al. "A Computational Approach to Understanding Empathy Expressed in Text-Based Mental Health Support." Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP). 2020.

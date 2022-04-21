# Adapter-Tuning for Empathy Prediction

Experimental code for CAISA at WASSA 2022: Adapter-Tuning for Empathy Prediction


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
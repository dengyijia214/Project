# Project
## Running UMMKD
### 2D version
To run our 2D version, can directly use the tfrecord data released in our another relevant project from [here](https://github.com/carrenD/Medical-Cross-Modality-Domain-Adaptation)

To train the model, specify the training configurations (can simply use the default setting), in main_combine.py set:

```
restored_model = None
main(restored_model = restored_model, phase='training')
```

To test the model, specify the path of the model to be tested, in main_combine.py set:
```
test_model = '/path/to/test_model.cpkt'
source_dice, target_dice = main(test_model=test_model, phase='testing')
```

Tensorboard will be automatically launched with port specified in main_combine.py

### 3D version
To run our 3D version, first:

```
cd 3d_implementation
```

To train the model, specify the training configurations (can simply use the default setting) in main.py, then run:

```
python main.py
```

To test the model, specify the path of tested model in test.py:
```
test_model = '/path/to/test_model.cpkt'
```
then run:
```
python test.py
```

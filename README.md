# Artistic camera filter 

Author: Gilbert François

## About

This program transforms your live camera feed into a very colourful and funky looking world with help of Deep Learning. It is almost being together with Lucy in the Sky with Diamonds :) The networks consist of autoencoders, trained on microscopic images. Some of the models have their effect by early stopping.



## Dependencies

The program depends on:

- Qt for Python
- OpenCV
- Tensorflow
- Keras

The easiest is to install with `pipenv install` inside the project folder.



## Running

```bash
$ cd src
$ python main.py
```

*Note: Starting up the application takes a long time due to long loading times of the ML models in memory.*



## Screenshot

![Screenshot](resources/ae-filter.gif)

## Todo

- [ ] Make a nice progress bar that shows the progress of loading the models during startup.
- [ ] Write the whole app in C++


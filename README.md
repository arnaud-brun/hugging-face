# hugging-face
Hugging face resources


## Certification path

### Unit 1 - Introduction to Deep Reinforcement Learning

Course: [Introduction to Deep Reinforcement Learning](https://huggingface.co/learn/deep-rl-course/unit1/introduction)
Project: [unit1](./unit1)

Getting started: 
```bash
cd unit1
PIPENV_VENV_IN_PROJECT=1 pipenv install swig "gymnasium[box2d]" huggingface_sb3==2.2.5 "numpy<2.0"
# Testing scripts
pipenv run python discovery.py
pipenv run python model.py
```

# Dependances

## Système

!apt install swig cmake

## Project

!pip install stable-baselines3==2.0.0a5
!pip install swig
!pip install gymnasium
!pip install box2d-py

!pip install huggingface_sb3

!pip install -r https://raw.githubusercontent.com/huggingface/deep-rl-class/main/notebooks/unit1/requirements-unit1.txt




pipenv install stable-baselines3==2.0.0a5 swig gymnasium box2d-py huggingface_sb3


Hence the following cell will install virtual screen libraries and create and run a virtual screen 🖥

## [OPTIONAL] Virtual Display

!sudo apt-get update
!sudo apt-get install -y python3-opengl
!apt install ffmpeg
!apt install xvfb
!pip3 install pyvirtualdisplay


```python
from pyvirtualdisplay import Display

virtual_display = Display(visible=0, size=(1400, 900))
virtual_display.start()
```
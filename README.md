## Sound Instructions
### create virtual environment 
python -m venv .tower

### activate
source .tower/bin/activate

### install requirements
pip install requirements.txt 

### If you are running WSL 2 on VSCode

#### Get sound drivers?
sudo apt install -y \
    libpulse0 \
    libasound2t64 \
    pulseaudio-utils

#### Access sound file
paplay utilities/assets/scissors.wav 
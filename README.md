# English to German Translator using Flask

This project implements an English to German translator using Flask. It utilizes a pretrained model obtained from OpenNMT-py and converts it using CTranslate2 and Sentencepiece for translation purposes.

#### Download the Pretrained Model

- Download the pretrained model from the following link:
  - [Transformer EN-DE WMT OpenONMT-py](https://s3.amazonaws.com/opennmt-models/transformer-ende-wmt-pyOnmt.tar.gz)
 - The pretrained model directory will contain two file:
    - `averaged-10-epoch.pt`
    - `sentencepiece.model`
 - For more information through the turorials provided in the reporsitory.

#### Convert the Model using CTranslate2

- Install CTranslate2 from the official repository available at:
  - [CTranslate2 GitHub Repository](https://github.com/OpenNMT/CTranslate2)
- Follow the instructions provided in the repository to install and set up CTranslate2.
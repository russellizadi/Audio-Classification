# Rethinking CNN Models for Audio Classification

This repository contains the PyTorch code for our paper [Rethinking CNN Models for Audio Classification](https://arxiv.org/abs/2007.11154). The experiments are conducted on the following three datasets which can be downloaded from the links provided:
1. [ESC-50](https://github.com/karolpiczak/ESC-50)
2. [UrbanSound8K](https://urbansounddataset.weebly.com/urbansound8k.html)
3. [GTZAN](https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification)

### Setup
```console
source setup.sh
```

### Preprocessing

The preprocessing is done separately to save time during the training of the models.

For ESC-50: 
```console
python preprocessing/preprocessingESC.py --csv_file /path/to/file.csv --data_dir /path/to/audio_data/ --store_dir /path/to/store_spectrograms/ --sampling_rate 44100
```

```console
python preprocessing/preprocessingESC.py --csv_file ~/russellizadi/datasets/ESC-50/meta/esc50.csv --data_dir ~/russellizadi/datasets/ESC-50/audio/ --store_dir ./spectrograms/ESC/ --sampling_rate 44100
```

For UrbanSound8K:
```console
python preprocessing/preprocessingUSC.py --csv_file /path/to/csv_file/ --data_dir /path/to/audio_data/ --store_dir /path/to/store_spectrograms/
```

```console
python preprocessing/preprocessingUSC.py --csv_file ~/russellizadi/datasets/UrbanSound8K/metadata/UrbanSound8K.csv --data_dir ~/russellizadi/datasets/UrbanSound8K/audio/ --store_dir ./spectrograms/USC/ 
```

For GTZAN:
```console
python preprocessing/preprocessingGTZAN.py --data_dir /path/to/audio_data/ --store_dir /path/to/store_spectrograms/ --sampling_rate 22050
```

```console
python preprocessing/preprocessingGTZAN.py  --data_dir ~/russellizadi/datasets/GTZAN/genres_original/ --store_dir ./spectrograms/GTZAN/ 
```

### Training the Models

The configurations for training the models are provided in the config folder. The sample_config.json explains the details of all the variables in the configurations. The command for training is: 
```console
python train.py --config_path /config/your_config.json
```

```console
python train.py --config_path ./config/esc_densenet.json
python train.py --config_path ./config/gtzan_densenet.json
python train.py --config_path ./config/usc_densenet.json
```

### Update the environment
After installing any package
```
conda env export --no-builds | grep -v "^prefix" > environment.yml
```

### Tensorboard
```
tensorboard --logdir=./runs/
```
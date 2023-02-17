# uresnet_pytorch
PyTorch implementations of dense and sparse UResNet

This README is very rough and will be completed soon. Stay tuned!

## Software containers
Singularity containers are available on https://www.singularity-hub.org/containers/6596.

## Dataset
LArTPC simulation dataset are publicly available on https://osf.io/9b3cv/.

## Run
All options can be found in `uresnet/flags.py`. 

To train sparse U-ResNet you can use for example:
```
python bin/uresnet.py train -chks 1 -wp weights/snapshot -io larcv_sparse -bs 1 --gpus 0 -nc 5 -rs 1 -ss 512 -dd 3 -uns 5 -uf 16 -dkeys data,fivetypes -mn uresnet_sparse -it 1 -ld log -if ../dlp_opendata_api/dlprod_ppn_v10/dlprod_192px_00.root
```

To run the inference:
```
python bin/uresnet.py inference --full -mp weights/snapshot-0.ckpt -io larcv_sparse -bs 1 --gpus 0 -nc 5 -rs 1 -ss 512 -dd 3 -uns 5 -uf 16 -dkeys data,fivetypes -mn uresnet_sparse -it 1 -ld log -if ../dlp_opendata_api/dlprod_ppn_v10/dlprod_192px_00.root
```

Main command-line parameters:
* `-mn` model name, can be `uresnet_dense` or `uresnet_sparse`
* `-io` I/O type, can be `larcv_sparse` or `larcv_dense`
* `-nc` number of classes
* `-chks` save checkpoint every N iterations
* `-wp` weights directory
* `-bs` batch size
* `--gpus` list gpus
* `-rs` report every N steps in stdout
* `-ss` spatial size of images
* `-dd` data dimension (2 or 3)
* `-uns` U-ResNet depth
* `-uf` U-ResNet initial number of filters 
* `-dkeys` data keys in LArCV ROOT file
* `-it` number of iterations
* `-ld` log directory
* `-if` input file
* `-mp` weight files to load for inference


## Authors
Laura Domine & Kazuhiro Terao

Dataset **DefectsPDC** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/5/3/6h/TJXRxC2jfKMtJPCBfaA1LtWBHUGaxAzmYnneqrMezTRGxbcAY2AmMHFtv93G845430bHtsCbg8W4Vweb8pCR4rHym4zMaceETySvcnIdwrQQsyl6pRgscpcyNbUy.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='DefectsPDC', dst_path='~/dtools/datasets/DefectsPDC.tar')
```
The data in original format can be 🔗[downloaded here](https://zenodo.org/record/3972451/files/Electricity%20Components%20Defects.zip?download=1)
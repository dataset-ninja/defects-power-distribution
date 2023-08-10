Dataset **Defects in Power Distribution Components** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/H/P/oc/jySPB1HAsSC0MwBzixvF1pR7iBU37NgStKTbfE5JRJjg050DBf5q4ahsf81RQH4tIoB3RYRw8KWO9T8YXiwOpVebUVCUhevthQ5FfNHf0YTUZBGwnz74RbM0h58Y.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Defects in Power Distribution Components', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://zenodo.org/record/3972451/files/Electricity%20Components%20Defects.zip?download=1)
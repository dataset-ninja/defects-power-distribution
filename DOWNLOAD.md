Dataset **Defects in Power Distribution Components** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/W/d/jE/Y5V0jOaEgdiQg45YvcpWQAkFrbAiv3Rr93DBcQexyTZXTASRYSH0W1H1uQYlL5HVsTOb1gRxkFKnFrI7MiVqP682VMZETb4EPJimimHuPpBnGR2PedPlySmL78QJ.tar)

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

The data in original format can be [downloaded here](https://zenodo.org/record/3972451/files/Electricity%20Components%20Defects.zip?download=1).
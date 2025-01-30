Dataset **Defects in Power Distribution Components** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEwMTFfRGVmZWN0cyBpbiBQb3dlciBEaXN0cmlidXRpb24gQ29tcG9uZW50cy9kZWZlY3RzLWluLXBvd2VyLWRpc3RyaWJ1dGlvbi1jb21wb25lbnRzLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogImNaYnJsQmlVNFJpS2t6am1ZZ1JITGw4REpaVk5QdTkxeU1NVnl3NFA3R1E9In0=)

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
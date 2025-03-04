from unstructured.staging.base import dict_to_elements
from unstructured.partition.pdf import partition_pdf
from unstructured_client.models.errors import SDKError
from unstructured_client.models import shared
from unstructured_client import UnstructuredClient


s = UnstructuredClient(api_key_auth="", server_url="")

filename = "example_files/el_nino.pdf"
pdf_elements = partition_pdf(filename=filename, strategy="fast")

for element in pdf_elements[:10]:
    print(f"{element.category.upper()}: {element.text}")

# Invoking hosted models
filename = "pages-14-17.pdf"
with open(filename, "rb") as f:
    files=shared.Files(
        content=f.read(),
        file_name=filename,
    )

req = shared.PartitionParameters(
    files=files,
    strategy="hi_res",
    hi_res_model_name="yolox",
)

try:
    resp = s.general.partition(req)
    dld_elements = dict_to_elements(resp.elements)
except SDKError as e:
    print(e)

for element in dld_elements[:10]:
    print(f"{element.category.upper()}: {element.text}")

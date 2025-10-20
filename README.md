This service is able to receive BIOMED clinical data and raw clinical text and to write output to the Azure  FHIR API. 

# Config
There are 3 preconfigured environment profiles (test, development, production):
`FLASK_ENV=development`
	
Connection to Azure FHIR API is provided by getting an access token from `https://login.microsoftonline.com/`.  The required values can be supplied in a single JSON file named `user_settings.json` located in the project root:

```
{
  "MDL_FHIR_TENANT_ID": "<tenant-id>",
  "MDL_FHIR_CLIENT_ID": "<client-id>",
  "MDL_FHIR_CLIENT_SECRET": "<client-secret>",
  "MDL_FHIR_AZURE_USERNAME": "fhir_user@yoursite.onmicrosoft.com",
  "MDL_FHIR_PASSWORD": "<password>",
  "MDL_FHIR_API_URL": "https://text2phenotype.azurehealthcareapis.com/",
  "MDL_FHIR_API_BASE": "http://localhost:5000"
}
```

An example file `user_settings.example.json` is provided.  Copy it to `user_settings.json` and fill in your values.

Access to FHIR resources is provided by using url: https://text2phenotype.azurehealthcareapis.com/

# FHIR Adapter Service
This project is based on Flask API and used flask-api-spec for automatically generating docs and Swagger markup. (http://localhost:5000/docs)

# Usage

Before running FHIR Adapter ensure that BIOMED is started.
To run FHIR Adapter for dev you need to execute `python fhirhydrant.fhir_server` with environmental variable FLASK_ENV. There are 2 values in which FLASK_ENV can be set: 'development' and 'test'.
For now FHIR Adapter is not ready for production.

## Google Colab Usage

The script `scripts/clinical_notes_to_bundle.py` can be used in Google Colab to
convert clinician notes to a FHIR bundle.

Clone the repository, install the requirements and run the script:

```python
!git clone <repository-url>
%cd text2fhir
!pip install -r requirements.txt -r fhirhydrant/client-requirements.txt

# upload your user_settings.json if it differs from the default
from google.colab import files
files.upload()  # choose user_settings.json

!python scripts/clinical_notes_to_bundle.py -o bundle_output.txt
```

When executed in Colab the script will prompt you to upload a `.txt` file with
the clinician notes and will save the resulting FHIR bundle to
`bundle_output.txt`.

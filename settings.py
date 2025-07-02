import os
import json
from pathlib import Path

DEFAULT_SETTINGS = {
    "MDL_FHIR_TENANT_ID": "",
    "MDL_FHIR_CLIENT_ID": "",
    "MDL_FHIR_CLIENT_SECRET": "",
    "MDL_FHIR_AZURE_USERNAME": "fhir_user@yoursite.onmicrosoft.com",
    "MDL_FHIR_PASSWORD": "",
    "MDL_FHIR_API_URL": "https://text2phenotype.azurehealthcareapis.com/",
    "MDL_FHIR_API_BASE": "http://localhost:5000"
}


def load_env(settings_path: Path = Path(__file__).with_name('user_settings.json')):
    """Populate os.environ with values from the user settings file."""
    data = DEFAULT_SETTINGS.copy()
    if settings_path.exists():
        with settings_path.open() as f:
            try:
                loaded = json.load(f)
                data.update({k: v for k, v in loaded.items() if v is not None})
            except Exception:
                pass
    for key, value in data.items():
        os.environ.setdefault(key, str(value))

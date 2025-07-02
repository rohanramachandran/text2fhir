from pathlib import Path
import os


class EnvironmentVariable:
    """Minimal replacement for text2phenotype EnvironmentVariable."""

    def __init__(self, name: str, legacy_name: str, value: str):
        self.name = name
        self.legacy_name = legacy_name
        self.default = value

    @property
    def value(self) -> str:
        return os.getenv(self.name, os.getenv(self.legacy_name, self.default))


class Environment:
    """Simple base class used only for grouping variables."""
    config_file_dir: Path


class FhirClientEnv(Environment):
    config_file_dir = Path(__file__).parent

    API_BASE = EnvironmentVariable(name='MDL_FHIR_API_BASE',
                                   legacy_name='FHIR_API_BASE',
                                   value='http://0.0.0.0:5000')
    TENANT_ID = EnvironmentVariable(name='MDL_FHIR_TENANT_ID',
                                    legacy_name='TENANT_ID',
                                    value='4a2074e8-3007-4341-b8eb-80f1448985de')


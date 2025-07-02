import argparse
import json
from pathlib import Path

try:
    from google.colab import files
except ImportError:  # not running in Colab
    files = None

from fhirhydrant.fhir_client.utils.fhir_hydrant_client import FhirHydrantClient


def read_text(path: Path) -> str:
    with path.open('r', encoding='utf-8') as f:
        return f.read()


def main():
    parser = argparse.ArgumentParser(description="Convert clinician notes to a FHIR bundle using the FHIR Hydrant API")
    parser.add_argument('input', nargs='?', help='Path to clinician notes text file')
    parser.add_argument('-o', '--output', default='bundle_output.txt', help='Output file for the resulting bundle')
    args = parser.parse_args()

    if args.input:
        clinical_text = read_text(Path(args.input))
    else:
        if files is None:
            parser.error('Input file is required when not running in Google Colab.')
        uploaded = files.upload()
        if not uploaded:
            print('No file uploaded.')
            return
        name, data = next(iter(uploaded.items()))
        clinical_text = data.decode('utf-8')
        print(f'Read {len(clinical_text)} characters from {name}')

    client = FhirHydrantClient()
    bundle = client.post_clinical_summary(clinical_text)

    output_path = Path(args.output)
    with output_path.open('w', encoding='utf-8') as f:
        json.dump(bundle, f, indent=2)
    print(f'FHIR bundle written to {output_path}')

    if files is not None:
        files.download(str(output_path))


if __name__ == '__main__':
    main()

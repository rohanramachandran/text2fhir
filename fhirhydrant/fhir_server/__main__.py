from text2phenotype.common.log import operations_logger

from settings import load_env
from fhirhydrant.fhir_server.app.factory import create_app
from fhirhydrant.fhir_server.fhir_server_env import FhirServerEnv

load_env()


operations_logger.info('Starting service...')
app = create_app()

if __name__ == '__main__':
    if FhirServerEnv.FLASK_ENV.value in {'development', 'test'}:
        app.run(debug=app.config.get('DEBUG', False))

rm -rf docs test build/ dupr_backend .openapi-generator-ignore .openapi-generator/
OPENAPI_GENERATOR_VERSION=7.16.0 openapi-generator-cli generate -i api-docs.json -g python --package-name dupr_backend
git restore pyproject.toml

# Troubleshooting

## Jenkins
### Problema: Error de autenticación con Docker Hub
Solución: Verifica que las credenciales de Docker Hub estén configuradas correctamente en Jenkins.

### Problema: Fallo al clonar el repositorio
Solución: Asegúrate de que el ID de credenciales de GitHub esté configurado correctamente y tenga los permisos necesarios.

## Travis CI
### Problema: Fallo en la construcción de Docker
Solución: Revisa el archivo `.travis.yml` y asegúrate de que todos los servicios de Docker estén configurados correctamente.

## Codeship
### Problema: El paso de despliegue falla
Solución: Verifica la configuración de `codeship-steps.yml` y asegúrate de que los comandos de despliegue sean correctos.

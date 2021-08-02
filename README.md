# Admin Smart - Backend

_Backend del proyecto AdminSmart. Sistema web creado para la administración, gestión, comunicación y contabilidad de comunidades_

### Pre-requisitos técnicos

_Es necesario tener instalado docker. https://docs.docker.com/engine/install/_

### Instalación

_Hay que buildear la imagen. Esto genera la imagen desde python alpine, le instala todas las dependencias y deja listo el proyecto_

```
docker-compose -f dev-compose.yml build
```

### Ejecución

_Hay que correr la imagen. Esto corre las migraciones y corre el servidor_

```
docker-compose -f dev-compose.yml up
```

### Consideraciones de db

_Si se necesita generar una migración porque se creó o se modificó un modelo hay que hacer lo siguiente_

```
docker-compose -f dev-compose.yml run --rm django python manage.py makemigrations
```

_Y luego, al ejecutarse el "up", se migra sola_

---
⌨️ con ❤️ por [ElPano](https://github.com/mpvaldez) 😊

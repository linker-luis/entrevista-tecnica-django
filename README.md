# Proyecto de Rutinas de Ejercicio con Django

- Registro y autenticación de usuarios con **JWT**.
- CRUD para creacion de eprfiles de usaurios en **userProfiles**.
- CRUD completo de **Ejercicios**.
- CRUD completo de **Rutinas** asociadas a un usuario.
- Cada rutina contiene una lista de ejercicios.
- Filtros en el **Django Admin** para gestionar fácilmente usuarios, rutinas y ejercicios.
- Base de datos PostgreSQL corriendo en Docker.

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/linker-luis/entrevista-tecnica-django.git
  
2. Inicializa y activa un entorno virtual:
    ```bash
    virtualenv env

    venv\Scripts\activate

3. Ingresa a la carpeta principal e instala las dependencias usadas
    ```bash
    cd rutinaEjercicios

    pip install -r requirements.txt

4. Levanta PostgreSQL con Docker:
    ```bash
    docker-compose up -d
5. Realiza las migraciones:
    ```bash
    python manage.py makemigrations

    python manage.py migrate

6. Crea un superusuario:
    ```bash
    python manage.py createsuperuser
7. Inicia el servidor:
    ```bash
    python manage.py runserver

## 📌 Endpoints de la API

| Recurso                 | Método | Endpoint                         | Descripción                                   | Auth |
| ----------------------- | ------ | -------------------------------- | --------------------------------------------- | ---- |
| **Auth**                | POST   | `/api/auth/register/`            | Registro de un nuevo usuario                  | ❌ No |
|                         | POST   | `/api/token/`                    | Login (obtiene `access` y `refresh` token)    | ❌ No |
|                         | POST   | `/api/token/refresh/`            | Refrescar el `access token`                   | ❌ No |
| **Perfil**              | GET    | `/api/profile/`                  | Obtener perfil del usuario autenticado        | ✅ Sí |
|                         | PUT    | `/api/profile/`                  | Actualizar perfil del usuario autenticado     | ✅ Sí |
| **Ejercicios**          | GET    | `/api/exercises/`                | Listar todos los ejercicios                   | ✅ Sí |
|                         | POST   | `/api/exercises/`                | Crear un ejercicio                            | ✅ Sí |
|                         | GET    | `/api/exercises/<id>/`           | Detalle de un ejercicio                       | ✅ Sí |
|                         | PUT    | `/api/exercises/<id>/`           | Actualizar un ejercicio                       | ✅ Sí |
|                         | PATCH  | `/api/exercises/<id>/`           | Actualizar parcialmente un ejercicio          | ✅ Sí |
|                         | DELETE | `/api/exercises/<id>/`           | Eliminar un ejercicio                         | ✅ Sí |
| **Rutinas**             | GET    | `/api/routines/`                 | Listar rutinas del usuario autenticado        | ✅ Sí |
|                         | POST   | `/api/routines/`                 | Crear rutina (con ejercicios asociados)       | ✅ Sí |
|                         | GET    | `/api/routines/<id>/`            | Detalle de una rutina del usuario autenticado | ✅ Sí |
|                         | PUT    | `/api/routines/<id>/`            | Actualizar rutina                             | ✅ Sí |
|                         | PATCH  | `/api/routines/<id>/`            | Actualizar parcialmente una rutina            | ✅ Sí |
|                         | DELETE | `/api/routines/<id>/`            | Eliminar rutina                               | ✅ Sí |
| **Rutinas por Usuario** | GET    | `/api/routines/users/<user_id>/` | Listar rutinas de un usuario (vista pública)  | ❌ No |

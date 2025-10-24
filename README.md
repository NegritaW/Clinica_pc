# 🖥️ Clínica del PC - Sistema de Gestión

Este proyecto es una simulación de un **sistema de gestión para la actividad Clínica del PC de INACAP**, donde estudiantes de informática reciben, diagnostican y entregan equipos tecnológicos traídos por personas de la comunidad.

El desarrollo se basa en **Django**, organizado en **4 aplicaciones independientes** que se comunican entre sí mediante rutas, vistas y templates.  

---

## 🚀 Instalación y ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/usuario/clinica-pc.git
cd clinica-pc

2️⃣ Crear entorno virtual

python -m venv venv
source venv/bin/activate      # En Linux/Mac
venv\Scripts\activate         # En Windows

3️⃣ Instalar dependencias

pip install -r requirements.txt

4️⃣ Configurar variables de entorno

Crea un archivo .env en la raíz del proyecto (al mismo nivel que manage.py).

Ejemplo para PostgreSQL (pgAdmin):

DB_NAME=tu_db
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432

    ⚠️ Asegúrate de tener PostgreSQL corriendo y que el usuario postgres tenga permisos para crear y modificar la base de datos.

5️⃣ Aplicar migraciones

Crea la estructura de la base de datos con los modelos definidos:

python manage.py makemigrations
python manage.py migrate

Esto generará automáticamente todas las tablas de las aplicaciones:
login, recepcion, diagnostico y entrega.
6️⃣ Crear superusuario (Administrador)

Para acceder al panel de administración de Django:

python manage.py createsuperuser

Completa los datos solicitados:

    Nombre de usuario

    Correo electrónico (opcional)

    Contraseña

Luego podrás iniciar sesión en
👉 http://127.0.0.1:8000/admin/
7️⃣ Ejecutar el servidor

python manage.py runserver

Abre en tu navegador:
👉 http://127.0.0.1:8000
🧩 Aplicaciones
Aplicación	Función principal
Login	Controla la autenticación, registro y asignación de roles.
Recepción	Registra el ingreso de los equipos y observaciones.
Diagnóstico	Permite asignar técnicos y registrar el diagnóstico del equipo.
Entrega	Registra la devolución del equipo y genera comprobantes en PDF.
📦 Dependencias principales

    Python 3.11+

Django 5.x

psycopg2-binary

(para conexión PostgreSQL)

python-dotenv

reportlab

(Todas listadas en requirements.txt)
🗂️ Estructura del proyecto

clinica_pc/
│
├── login/              # Gestión de usuarios y roles
├── recepcion/          # Registro de ingreso de equipos
├── diagnostico/        # Asignación y registro de diagnóstico
├── entrega/            # Registro y comprobante de entrega
│
├── static/             # Archivos CSS e imágenes
├── templates/          # Templates base y herencia
├── .env                # Variables de entorno (no subir al repo)
├── manage.py
└── requirements.txt

👩‍💻 Contribución

    Haz un fork del proyecto.

    Crea una branch con tu feature:

git checkout -b feature/nueva-funcion

Haz commit de tus cambios:

git commit -m "Agrega nueva función X"

Haz push a la branch:

    git push origin feature/nueva-funcion

    Abre un Pull Request.

📜 Licencia

Este proyecto es de uso académico en INACAP.
No tiene fines comerciales.
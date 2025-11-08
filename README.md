# 🖥️ Clínica del PC — Sistema de Gestión

![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-lightblue?logo=postgresql)
![License](https://img.shields.io/badge/Licencia-Académica-red)
![Status](https://img.shields.io/badge/Estado-En%20Desarrollo-orange)

---

**Clínica del PC** es un sistema web desarrollado en **Django**, diseñado para gestionar el proceso completo de atención técnica en la actividad académica *“Clínica del PC” de INACAP*.  
Permite **recepcionar, diagnosticar y entregar equipos** de clientes de forma centralizada y segura, con manejo de roles y flujo completo de trabajo.

---

## ⚙️ Tecnologías utilizadas

- 🐍 **Python 3.11+**
- 🌐 **Django 5.x**
- 🐘 **PostgreSQL + psycopg2**
- 🔒 **python-dotenv** (manejo seguro de variables de entorno)
- 🎨 **HTML + CSS personalizado (estilo INACAP)**

---

## 🚀 Instalación y ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/usuario/clinica-pc.git
cd clinica-pc
```

### 2️⃣ Crear entorno virtual
```bash
python -m venv venv
# Activar entorno
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variables de entorno

Crea un archivo **`.env`** en la raíz del proyecto (junto a `manage.py`):

```env
DB_NAME=tu_db
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
```

⚠️ **Importante:**  
Asegúrate de tener PostgreSQL corriendo y que el usuario `postgres` tenga permisos de creación y modificación en la base de datos.

---

### 5️⃣ Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```
Esto creará las tablas correspondientes a:
- `login`
- `recepcion`
- `diagnostico`
- `entrega`

---

### 6️⃣ Crear superusuario (Administrador)
```bash
python manage.py createsuperuser
```
Completa los campos solicitados. Luego podrás acceder al panel de administración en:  
👉 **http://127.0.0.1:8000/admin/**

---

### 7️⃣ Ejecutar el servidor
```bash
python manage.py runserver
```

Abre tu navegador en:  
👉 **http://127.0.0.1:8000**

---

## 🧩 Aplicaciones del sistema

| Aplicación | Función principal |
|-------------|------------------|
| **Login** | Autenticación, registro y asignación de roles. |
| **Recepción** | Registra el ingreso de los equipos y observaciones. |
| **Diagnóstico** | Permite asignar técnicos y registrar el diagnóstico. |
| **Entrega** | Registra la devolución del equipo y genera comprobantes en PDF. |

---

## 📁 Estructura del proyecto
```
clinica_pc/
│
├── login/              # Gestión de usuarios y roles
├── recepcion/          # Registro de ingreso de equipos
├── diagnostico/        # Asignación y registro técnico
├── entrega/            # Registro y comprobantes de entrega
│
├── static/             # Archivos CSS e imágenes
├── templates/          # Templates base y herencia
├── .env                # Variables de entorno (ignorado por git)
├── manage.py
└── requirements.txt
```

---

## 🧠 Flujo del sistema

1. El **cliente** entrega el equipo → *Recepción* crea el registro.  
2. El **técnico** revisa el equipo → *Diagnóstico* registra el estado.  
3. El **administrador** confirma la **entrega** → se genera comprobante PDF.  
4. Los usuarios acceden según su **rol (admin, técnico, recepción o cliente)**.

---

## 🧾 Roles y permisos

| Rol | Permisos principales |
|------|----------------------|
| 🧑‍💼 **Administrador** | Gestiona usuarios, activa cuentas y supervisa todo el flujo. |
| 🧰 **Técnico** | Registra diagnósticos y actualiza estados. |
| 📦 **Recepción / Entrega** | Gestiona ingreso y salida de equipos. |
| 👤 **Cliente** | Consulta el estado del equipo. |

---

## 💡 Características destacadas

- 🔐 Sistema de **autenticación y roles personalizados** (`Usuario` basado en `AbstractUser`).
- 🧾 **Generación automática de comprobantes PDF**.
- 🔄 Flujo completo **Recepción → Diagnóstico → Entrega**.
- 🧩 Integración entre aplicaciones mediante modelos relacionados.
- 🎨 Interfaz visual coherente con el estilo **INACAP (rojo institucional)**.
- 💬 Validaciones, formularios y mensajes completamente en **español**.

---

## 📦 Dependencias principales
```
Django==5.x
psycopg2-binary
python-dotenv
```

---

## 👩‍💻 Contribución

1. Haz un **fork** del proyecto.  
2. Crea una **branch** con tu feature:
   ```bash
   git checkout -b feature/nueva-funcion
   ```
3. Haz commit de tus cambios:
   ```bash
   git commit -m "Agrega nueva función X"
   ```
4. Haz push a tu rama:
   ```bash
   git push origin feature/nueva-funcion
   ```
5. Abre un **Pull Request** 🚀

---

## 🧍‍♀️ Créditos

Proyecto académico desarrollado por estudiantes de **INACAP**(Ivy Pradines y Benjamin Torres)  
para la asignatura **Clínica del PC — Desarrollo de Aplicaciones Web**.

---

## 🪪 Licencia

Este proyecto es de uso **educativo y académico**.  
No tiene fines comerciales ni autorización para redistribución sin permiso.


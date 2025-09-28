# 🖥️ Clínica del PC - Sistema de Gestión

Este proyecto es una simulación de un **sistema de gestión para la actividad Clínica del PC de INACAP**, donde estudiantes de informática reciben, diagnostican y entregan equipos tecnológicos traídos por personas de la comunidad.

El desarrollo se basa en **Django**, organizado en **4 aplicaciones independientes** que se comunican entre sí mediante rutas, vistas y templates.  

---

## 🚀 Instalación y ejecución

1. **Clonar repositorio**
   ```bash
   git clone https://github.com/usuario/clinica-pc.git
   cd clinica-pc
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate      # En Linux/Mac
   venv\Scripts\activate         # En Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar servidor**
   ```bash
   python manage.py runserver
   ```

5. Abrir en navegador 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧩 Aplicaciones

- **Recepción** → Registra el ingreso de los equipos.
- **Diagnóstico** → Permite simular fallas detectadas.
- **Reparación** → Simula el flujo de reparación asignada.
- **Entrega** → Confirma la devolución del equipo al cliente.

---

## 📦 Dependencias principales

- [Python 3.11+](https://www.python.org/)  
- [Django 5.x](https://www.djangoproject.com/)

*(Todas listadas en `requirements.txt`)*

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
4. Haz **push** a la branch:
   ```bash
   git push origin feature/nueva-funcion
   ```
5. Abre un **Pull Request**.

---

## 📜 Licencia

Este proyecto es de uso académico en **INACAP**.  
No tiene fines comerciales.

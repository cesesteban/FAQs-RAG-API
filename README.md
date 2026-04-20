# FAQs RAG API
[English](#english) | [Español](#español)

---

<a name="english"></a>
## 🇬🇧 English

A modern, production-ready FastAPI codebase for a RAG (Retrieval-Augmented Generation) system focused on FAQs.

### Features
- **FastAPI**: High performance, easy to use.
- **Pydantic v2**: Strict data validation and serialization.
- **Modular Structure**: Clean separation of concerns.
- **Asynchronous**: Built with `async/await` for I/O efficiency.
- **Lifespan Management**: Proper resource initialization and cleanup.

### Knowledge Base
The system is indexed with a comprehensive HR Policy Manual (`app/data/faq_document.txt`), covering:
- Remote work and Home Office stipends.
- Vacation accrual (PTO) and health benefits.
- Performance reviews and code conduct.

### Setup
1. **Install Dependencies**: `pip install -r requirements.txt`
2. **Configure Environment**: Edit the `.env` file with your `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION`.
3. **Automatic Re-indexing**: The system automatically scans the `app/data` folder at startup. Start the app to refresh the knowledge base.

### Usage
- **Bilingual Support**: Auto-detects between English or Spanish queries.
- **Query CLI**: `docker exec -it faqs-rag-api-api-1 python -m app.scripts.query_cli "Your Question?"`

Once running, visit `http://localhost:8000/` to access the interactive Swagger documentation.

---

<a name="español"></a>
## 🇪🇸 Español

Un código base moderno y adaptado para entornos de producción usando FastAPI, que implementa un sistema RAG (Generación Aumentada por Recuperación) enfocado en Preguntas Frecuentes.

### Características
- **FastAPI**: Alto rendimiento y facilidad de uso.
- **Pydantic v2**: Validación y serialización estricta de datos.
- **Estructura Modular**: Separación limpia de responsabilidades (API, esquemas, servicios).
- **Asíncrono**: Construido completamente usando `async/await`.
- **Gestión de Ciclo de Vida**: Optimización de la indexación al arrancar la app.

### Base de Conocimiento
El sistema está indexado con un completo Manual de Políticas de RRHH (`app/data/faq_document.txt`), detallando:
- Trabajo remoto y un subsidio de Home Office.
- Acumulación de vacaciones (PTO) y beneficios y seguro médico.
- Revisiones de desempeño y el código de conducta.

### Configuración
1. **Instalar Dependencias**: `pip install -r requirements.txt`
2. **Configurar Entorno**: Añade tus credenciales a un archivo `.env` (`GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`).
3. **Re-indexación Automática**: El sistema escanea la carpeta `app/data` automáticamente al iniciarse. Reiniciá el contenedor o la app para recargar el conocimiento.

### Uso
- **Soporte Bilingüe**: Detecta automáticamente español o inglés en las preguntas y responde iterativamente.
- **CLI de Consulta**: `docker exec -it faqs-rag-api-api-1 python -m app.scripts.query_cli "¿Cuál es la política?"`

Al estar corriendo el servicio, visitá `http://localhost:8000/` para utilizar el explorador interactivo Swagger.

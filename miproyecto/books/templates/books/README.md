Este es un proyecto web desarrollado con Django.
El proyecto implementa el patrón MVT, herencia de plantillas y manejo de formularios.

¿Qué incluye este proyecto?

- Proyecto Django con estructura completa  
- Herencia de plantillas
- Tres modelos con sus respectivos formularios  
- Un formulario de búsqueda en la base de datos  
- Interfaz para cargar y consultar datos  
- README con instrucciones

Estructura del proyecto

- `books/models.py` → contiene los 3 modelos: Autor, Libro y Editorial  
- `books/forms.py` → formularios para cada modelo y para buscar  
- `books/views.py` → lógica para crear, listar y buscar  
- `templates/` → herencia de HTML desde `base.html`  
- `urls.py` → rutas configuradas  
- `db.sqlite3` → base de datos local

Modelos utilizados

1. **Autor**  
   - nombre  
   - nacionalidad  

2. **Libro**  
   - título  
   - autor (relación ForeignKey)  
   - editorial (relación ForeignKey)  
   - año  

3. **Editorial**  
   - nombre  
   - ciudad  

Formularios disponibles

- `/books/crear_autor/` → Cargar un nuevo autor  
- `/books/crear_libro/` → Cargar un nuevo libro  
- `/books/crear_editorial/` → Cargar una nueva editorial  
- `/books/buscar_libro/` → Buscar libros por título

¿Cómo probar el proyecto?

1. Clonar el repositorio
   git clone https://github.com/LayLM/TuPrimeraPagina_LopezMorist.git
   
2. Entrar a la carpeta del proyecto
      cd TuPrimeraPagina_LopezMorist
   
3. **Activá el entorno virtual y corré el servidor**
   python -m venv env
   env\Scripts\activate 
   pip install -r requirements.txt
   python manage.py runserver
   
4. **Abrí tu navegador y probá estas URLs:**
   - http://127.0.0.1:8000/books/crear_autor/
   - http://127.0.0.1:8000/books/crear_libro/
   - http://127.0.0.1:8000/books/crear_editorial/
   - http://127.0.0.1:8000/books/buscar_libro/

Notas

- El proyecto fue desarrollado con Django 5.x  
- La base está preconfigurada para sqlite3  
- No es necesario autenticarse para usar el sitio  

Autora: Lucila López Morist
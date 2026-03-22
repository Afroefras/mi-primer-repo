
# 🚀 De Colab al Mundo Real

Vamos a aprender cómo encapsular proyectos, usar rutas inteligentes y colaborar sin destruir el código del compañero.

## 🛠️ Fase 1: Preparando tu Entorno Local

Abre tu IDE (Antigravity) y abre la terminal integrada: En la barra superior dice Terminal -> New Terminal.

**1. Clona el repositorio y entra a la carpeta:**

```bash
git clone https://github.com/Afroefras/mi-primer-repo.git
cd mi-primer-repo
```

**2. Crea "La Burbuja" (El Entorno Virtual)**

Nunca instales librerías globalmente. Vamos a crear un `.venv` (virtual environment) para aislar este proyecto. Esto se hace **UNA SOLA VEZ**:
* **Mac / Windows:** `python -m venv .venv` *(En Mac, si falla, intenta con `python3`)*

**3. Activa "La Burbuja"**
Esto lo debes hacer **SIEMPRE** que abras el proyecto para trabajar.
* **Mac:** `source .venv/bin/activate`
* **Windows (CMD):** `.venv\Scripts\activate`
* **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
*(Sabrás que funcionó porque verás un `(.venv)` al inicio de tu línea de comandos).*

**4. Instala las dependencias y revisa el `.gitignore`**
```bash
pip install -r requirements.txt
```
*💡 Tip pro: Abre el archivo `.gitignore`. Ahí le decimos a Git qué archivos **jamás** debe subir a la nube (como nuestra pesada carpeta `.venv` o datos confidenciales).*

---

## 💻 Fase 2: Tu Misión (Git Flow)

Vamos a trabajar colaborativamente usando ramas (branches). La regla de oro: **Nunca trabajamos directo en `main`**.

**1. Muévete a la rama base de la clase:**
```bash
git checkout alumnos
```

**2. Crea tu propia rama de trabajo (reemplaza con tu nombre sin espacios):**
```bash
git checkout -b juan_perez
```

**3. Escribe tu código:**
* Ve a la carpeta `src/osos_estudiantes/`.
* Crea un archivo Python con tu nombre, ej: `juan_perez.py`.
* Copia esta estructura y pon tu historia (¡mantenlo apto para todo público!):

```python
# src/osos_estudiantes/juan_perez.py

def mi_peor_oso():
    nombre = "Juan Pérez"
    oso = "Le dije 'mamá' a la maestra en la universidad."
    return nombre, oso
```

**4. Guarda, Empaqueta y Sube a la Nube (Commit & Push):**
En tu terminal, ejecuta uno por uno:
```bash
git add .
git commit -m "Agrego el oso de Juan Perez"
git push origin juan_perez
```

---

## 🔀 Fase 3: El Pull Request (PR)

1. Ve a la página del repositorio en GitHub desde tu navegador.
2. Verás un botón verde que dice **"Compare & pull request"**. ¡Dale clic!
3. **¡MUY IMPORTANTE!** Asegúrate de que la rama *base* a la que apuntas sea `alumnos` (NO `main`).
4. Ponle un título a tu PR y dale a "Create pull request".

¡Listo! El profesor revisará tu código, lo unirá a la rama principal y ejecutará un script maestro (usando `pathlib` para rutas dinámicas multiplataforma) que leerá todas nuestras historias al mismo tiempo.

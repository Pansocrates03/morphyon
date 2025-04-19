# Importar y exponer las clases principales
from .components import Component, Button, Header
from .styles import Style
from .utils import builder
from typing import List
import uvicorn
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading

# Puedes definir __all__ para controlar lo que se expone con "from mi_libreria import *"
__all__ = ['Component', 'Button', 'Header', 'Style']

class Morphyon:
    def __init__(self):
        self.content: List[Component] = []
        self.dist_dir = "build"  # Directorio donde se generan los archivos
    
    def addComponent(self, newComponent):
        self.content.append(newComponent)

    def build(self):
        if(len(self.content) <= 0):
            print("ERROR: App cannot be empty")
            return
        builder(self.content)

    def listen(self, port: int = 5050, watch_dir: str = "./src", watch_patterns: list = ["*..py"]):
        # Construir inicialmente
        self.build()
        
        # Configurar servidor FastAPI
        app = FastAPI()
        
        ########################

        # Montar los archivos estáticos desde /dist
        app.mount("/static", StaticFiles(directory=self.dist_dir), name="static")
        
        @app.get('/')
        def read_root():
            # Servir el index.html desde el directorio dist
            index_path = Path(f"{self.dist_dir}/index.html")
            if index_path.exists():
                with open(index_path, "r") as file:
                    html_content = file.read()
                return HTMLResponse(content=html_content)
            else:
                return HTMLResponse(content="<h1>Error: index.html not found</h1>")
        
        # Ruta para servir style.css directamente
        @app.get('/style.css')
        def get_css():
            css_path = Path(f"{self.dist_dir}/style.css")
            if css_path.exists():
                return FileResponse(css_path, media_type="text/css")
            else:
                return HTMLResponse(content="CSS file not found", status_code=404)
        
        # Ruta para activar la reconstrucción manual si es necesario
        @app.get('/rebuild')
        def rebuild():
            if auto_rebuild:
                self.build()
                return {"status": "rebuilt"}
            return {"status": "auto-rebuild disabled"}
        
        #########################3
        
        # Configurar observador para reconstrucción automática
        if watch_dir:
            class ChangeHandler(FileSystemEventHandler):
                def on_modified(self, event):
                    if any(event.src_path.endswith(pattern) for pattern in watch_patterns):
                        print(f"Detected change in {event.src_path}. Rebuilding...")
                        self.build()
            
            observer = Observer()
            observer.schedule(ChangeHandler(), path=watch_dir, recursive=True)
            
            # Iniciar el observador en un hilo separado
            threading.Thread(target=observer.start, daemon=True).start()
        
        # Iniciar el servidor
        print(f'Server running at http://localhost:{port}')
        uvicorn.run(app, host="0.0.0.0", port=port)
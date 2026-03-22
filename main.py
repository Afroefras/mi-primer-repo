import os
import importlib.util
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

def main():
    console = Console()
    path_alumnos = os.path.join("src", "alumnos")
    function_to_call = "mi_peor_oso"

    if not os.path.exists(path_alumnos):
        console.print(f"[bold red]Error:[/bold red] La carpeta '{path_alumnos}' no existe.")
        return

    # Creamos una tabla para presentar los resultados con estilo
    table = Table(title="", show_header=True, header_style="bold magenta")
    table.add_column("Estudiante", style="cyan", width=20)
    table.add_column("🐻 épico", style="yellow")

    # Obtenemos todos los archivos .py en la carpeta alumnos
    files = [f for f in os.listdir(path_alumnos) if f.endswith(".py") and f != "__init__.py"]

    if not files:
        console.print("[yellow]No se encontraron archivos de alumnos en [/yellow][bold]src/alumnos/[/bold]")
        return

    for file in files:
        file_path = os.path.join(path_alumnos, file)
        module_name = file[:-3] # Quitamos el .py

        try:
            # Importación dinámica del archivo
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Buscamos la función si existe
            if hasattr(module, function_to_call):
                func = getattr(module, function_to_call)
                nombre, oso = func()
                table.add_row(nombre, oso)
            else:
                table.add_row(f"[red]{module_name}[/red]", "[italic red]No tiene definida la función mi_peor_oso()[/italic red]")
        
        except Exception as e:
            table.add_row(f"[bold red]{file}[/bold red]", f"[red]Error al cargar: {str(e)}[/red]")

    console.print(table)
    console.print("\n[bold green]✅ ¡Proceso finalizado! Todos los archivos han sido leídos.[/bold green]\n")

if __name__ == "__main__":
    main()

import openai  # pip install openai
import typer  # pip install "typer[all]"
from rich import print  # pip install rich
from rich.table import Table

def main():
    #variables de mi api    
    openai.api_key = "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"
     #configuramos las lineas
    print("💬 [bold green]ChatGPT API en Python[/bold green]")
     #creamos una tanble con filas y colums   
    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)
        #Tu Eres un asistente de formulacion de proyectos con 10 años de experiencia.
        #Tu Eres un asistente de gestión del conocimiento con 10 años de experiencia
    # Contexto del asistente
    context = {"role": "assistant",
               "content": "Tu Eres un asistente de tesnting con 10 años de experiencia"}
    messages = [context]

    while True:
            #llamos la funcion recursiva  
        content = __prompt()
            #si igual a new creamos la conversacion
        if content == "new":
            print("🆕 Nueva conversación creada")
            # con mgs se mantiene el contexto de la conversacuion 
            messages = [context]
            content = __prompt()
    
        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    #si es igual a new inicia la conversacion
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if prompt == "exit":
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)
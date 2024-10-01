import typer

app = typer.Typer()

@app.command()
def hello_world(
    name: str = typer.Option(..., help="your name"), 
    shout: bool = typer.Option(False, help="whether to shout")
) -> None:
    """
    say hello to the user
    """
    greeting = f"Hello, {name}!"
    if shout:
        greeting = greeting.upper() 
    print(greeting) 

if __name__ == "__main__":
    app()
#!/usr/bin/env python

"""
This module is used to create calculations functions such as addition, substraction, multiplication, division, etc.
This module will also be invoked as a command line script using click
"""

import click

def add(a, b):
    """
    This function adds two numbers
    """
    return a + b

def sub(a, b):
    """
    This function subtracts two numbers
    """
    return a - b

def mul(a, b):
    """
    This function multiplies two numbers
    """
    return a * b

def div(a, b):
    """
    This function divides two numbers
    """
    return a / b


#build a click group
@click.group()
def cli():
    """
    This is a calculator application
    """

#build a click command  
@cli.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_command(a, b):
    """
    This function adds two numbers
    """

    # invoke the add function with colored output
    click.echo(click.style("Result: ", fg="green") + click.style(str(add(a, b)), bg="blue", fg="white"))
    
    

#build a click command
@cli.command("sub")
@click.argument("a", type=int)
@click.argument("b", type=int)
def subs_command(a, b):
    """
    This function subtracts two numbers
    """
    # invoke the add function with colored output
    click.echo(click.style("Result: ", fg="green") + click.style(str(sub(a, b)), bg="blue", fg="white"))
  

#build a click command
@cli.command("mul")
@click.argument("a", type=int)
@click.argument("b", type=int)
def mul_command(a, b):
    """
    This function multiplies two numbers
    """
    click.echo(mul(a, b))

#build a click command
@cli.command("div")
@click.argument("a", type=int)
@click.argument("b", type=int)
def div_command(a, b):
    """
    This function divides two numbers
    """
    click.echo(div(a, b))


if __name__ == "__main__":
    cli()
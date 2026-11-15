"""Operaciones matemáticas básicas de la calculadora."""

AUTOR = "Ioav Mizrahi | Mateo Muñoz"


def sumar(a, b):
    """Suma dos números."""
    return a + b


def restar(a, b):
    """Resta el segundo número del primero."""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b


def dividir(a, b):
    """Divide el primer número entre el segundo."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def potencia(a, b):
    """Eleva el primer número a la potencia del segundo."""
    return a**b


def modulo(a, b):
    """Devuelve el residuo de dividir el primer número entre el segundo."""
    if b == 0:
        raise ZeroDivisionError("No se puede calcular el módulo con divisor cero")
    return a % b

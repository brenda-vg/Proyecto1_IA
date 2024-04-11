# Proyecto 1 de Inteligencia Artificial - Implementación del algoritmo UCS en Python

Este proyecto es parte de la materia de Inteligencia Artificial y tiene como objetivo implementar el algoritmo de búsqueda de costo uniforme (UCS) en un grafo específico, representado por el mapa de Rumania.

## Propósito

El propósito principal de este proyecto es proporcionar una implementación funcional del algoritmo UCS en Python para resolver problemas de búsqueda de rutas en un grafo ponderado, específicamente aplicado al mapa de Rumania.

## Problema a Resolver

El problema que aborda este proyecto es encontrar la ruta más corta entre dos ciudades en el mapa de Rumania utilizando el algoritmo UCS.

## Características Principales

- Implementación de la clase `WeightedGraph` para representar el grafo ponderado.
- Función `uniform_cost_search(graph, start, goal)` para resolver el problema de encontrar la ruta más corta.

## Público Objetivo

El público objetivo de este proyecto son el profesor de la materia y los compañeros de equipo para el proyecto en la materia de Inteligencia Artificial.

## Tecnologías Utilizadas

- Python 3
- Modelo de desarrollo mixto propio de Python: Paradigma Orientado a Objetos únicamente para la clase WeightedGraph y Estructurado para el resto del proyecto
- Se espera utilizar Sphinx para la documentación (aún no implementado)

## Instalación

El único requisito es tener instalado Python 3. Para ejecutar el programa, simplemente ejecuta el intérprete de Python 3, en automático se ejecuta el programa siempre y cuando este esté siendo ejecutado como el programa principal (if __name__ == "__main__")

## Uso

Una vez ejecutado el programa se solicita una ciudad de partida y una ciudad de destino, al finalizar, da la ruta resultante y da la opción de ejecutar el programa de nuevo.

## Estructura de Directorios

El proyecto consta de un único archivo, `P1.py`, que contiene todas las funciones y la lógica del programa.
Puede ser divisible a dos archivos, uno con la lógica del grafo y la búsqueda, otro con la interacción con el usuario.

## Contribuciones y Reporte de Problemas

Los usuarios pueden contribuir al proyecto o informar sobre problemas a través de la sección de issues y discusiones en el repositorio de GitHub.

## Notas Adicionales

- Desarrollado en MacOS, no ha sido probado en otras plataformas.

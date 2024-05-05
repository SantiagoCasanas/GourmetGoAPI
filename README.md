# GourmetGoAPI

In the kitchen, we are often faced with the challenge of deciding what to cook with the ingredients available in our refrigerator. Sometimes we come across ingredients that we don't know how to use or we would like to try new recipes but we don't know where to start. Plus, it can be a little difficult to remember all the recipes we know or look for new recipes that fit the ingredients we have on hand.
GourmetGo is an innovative and versatile culinary application that takes advantage of web scraping technology and the BeautifulSoup library to facilitate the search for recipes adapted to the ingredients entered by the user. With this tool, users can explore a wide variety of culinary options, even when faced with the challenge of having unknown or unusual ingredients in their pantry.

## To run the API locally you will need to follow the steps below:

1. Clone the repository to the desired location.
2. Open a terminal of your choice in the folder of the cloned repository. (For the instructions it will be 
assumed that you used Git Bash).
3. Create a virtual environment using:
```
python -m venv venv
```
4. Activate the virtual environment:
```
source venv/Scripts/activate
```
5. Install the requirements using:
```
pip install -r requirements.txt
```
6. Create an .env file in the repository root that has the following structure:
```
origins = [
    "http://localhost",
    "http://localhost:8080",
    "127.0.0.1"
]
```
Adding in origins the addresses from which you wish to allow requests, or in case you wish to allow any addresses
```
origins = ["*"]
```
In case you want to allow any address.

7. Execute the following command to run the API:
```
uvicorn main:app --reload
```
8. Access the following path to see the available endpoint's and their parameters
```
http://127.0.0.1:8000/docs
```


En la cocina, a menudo nos enfrentamos al desafío de decidir qué cocinar con los ingredientes disponibles en nuestra nevera. A veces nos encontramos con ingredientes que no sabemos cómo utilizar o nos gustaría probar nuevas recetas pero no sabemos por dónde empezar. Además, puede ser un poco difícil recordar todas las recetas que conocemos o buscar nuevas recetas que se adapten a los ingredientes que tenemos a la mano.
GourmetGo es una aplicación culinaria innovadora y versátil que aprovecha la tecnología de web scraping y la librería BeautifulSoup para facilitar la búsqueda de recetas adaptadas a los ingredientes ingresados por el usuario. Con esta herramienta, los usuarios pueden explorar una amplia variedad de opciones culinarias, incluso cuando se enfrentan al desafío de tener ingredientes desconocidos o poco comunes en su despensa.


## Para ejecutar la API de manera local deberá seguir los siguientes pasos:
1. Clone el repositorio en la ubicación deseada.
2. Abra una terminal de su preferencia en la carpeta del repositorio clonado. (Para las instrucciones se supondrá
que usó Git Bash)
3. Cree un ambiente virtual usando:
```
python -m venv venv
```
4. Active el ambiente virtual:
```
source venv/Scripts/activate
```
5. Instale los requerimientos usando:
```
pip install -r requirements.txt
```
6. Cree un archivo .env en la raíz del repositorio que tenga la siguiente estructura:
```
origins = [
    "http://localhost",
    "http://localhost:8080",
    "127.0.0.1"
]
```
Agregando en origins las direcciones desde las cuales desea permitir las peticiones, o en caso de desear permitir cualquier dirección
```
origins = ["*"]
```
En caso de desear permitir cualquier dirección.


7. Ejecute el siguiente comando para correr la API:
```
uvicorn main:app --reload
```
8. Acceda a la siguiente ruta para ver los endpoint's disponibles y sus parametros
```
http://127.0.0.1:8000/docs
```

# taller_mlops
Taller de curso MLOps
*********************
- Se implementa el código app.py con la lógica del chatbot asistente de aerolínea.
- Se asocia un Dockerfile para crear una imagen de la aplicación en Docker, alojada localmente en Minikube.
- Mediante Uvicorn, se publica el código en FastAPI como interfaz a la que se conecta el cliente y realiza una pregunta.
- Para generar una respuesta, se integra con la API de OpenAI y responde al cliente, con el modelo gpt-4.

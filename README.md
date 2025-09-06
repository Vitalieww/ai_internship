# llm_expert_internship
**This is my internship repository where I will document each step.**

## Week 1
Firstly I installed docker. I went through the documentation provided from the desktop docker app, where I learned about:
- Images
- Containers (and how to run them)
- Multi-container applications
- How to publish images
- How to access local folders from a container (using bind mount)
- How to persist data between containers (using volumes)
- How to containerize my application

After this I connected two containers using an .yaml file. One container being a Flask Server and the other the Ollama Server.
I pull from the Ollama server an AI agent ( I used mistral) and then I am able to give a prompt to the AI, and receive the response in a simple HTML page.

import random
from locust import HttpUser, task, between
from utils.data_loader import get_payload, get_random_post_id

class APIUser(HttpUser):
    # Cada "usuário" virtual vai esperar entre 1 e 5 segundos entre as ações
    wait_time = between(1, 5)
    
    # Base URL pode ser definida no comando de execução ou aqui:
    host = "https://jsonplaceholder.typicode.com"

    @task(3) # Peso 3: Essa ação ocorre mais frequentemente (ex: ler posts)
    def get_posts_list(self):
        """Simula a listagem de todos os posts."""
        self.client.get("/posts")

    @task(4)
    def get_specific_post(self):
        """Simula o acesso a um post específico (ID aleatório)."""
        post_id = get_random_post_id()
        self.client.get(f"/posts/{post_id}")

    @task(2)
    def get_comments(self):
        """Simula a leitura de comentários de um post."""
        post_id = get_random_post_id()
        # Testando ambos os caminhos possíveis do seu guia
        path = f"/posts/{post_id}/comments" 
        # Ou self.client.get(f"/comments?postId={post_id}")
        self.client.get(path)

    @task(1)
    def create_new_post(self):
        """Simula a criação de um novo post (POST)."""
        data = get_payload("new_post")
        self.client.post("/posts", json=data)

    @task(1)
    def update_existing_post(self):
        """Simula a atualização de um post existente (PUT)."""
        data = get_payload("update_post")
        self.client.put("/posts/1", json=data)

    @task(1)
    def patch_post(self):
        """Simula uma atualização parcial (PATCH)."""
        self.client.patch("/posts/1", json={"title": "Partial Update"})

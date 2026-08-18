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

    @task(1)
    def delete_post(self):
        """Simula a exclusão de um post (DELETE)."""
        post_id = get_random_post_id()
        self.client.delete(f"/posts/{post_id}")
    @task(1)
    def get_album_photos(self):
        """Simula a busca de fotos em um álbum (Nested Route)."""
        album_id = random.randint(1, 100)
        self.client.get(f"/albums/{album_id}/photos")

    @task(1)
    def get_user_todos(self):
        """Simula a busca de tarefas de um usuário (Nested Route)."""
        user_id = random.randint(1, 100)
        self.client.get(f"/users/{user_id}/todos")

    @task(1)
    def get_filtered_posts(self):
        """Simula a listagem de posts filtrados por usuário (Query Param)."""
        self.client.get("/posts?userId=1")
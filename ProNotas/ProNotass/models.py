from django.db import models

# Create your models here.

class Topic(models.Model):
    """Modelo que representa um assunto de aprendizado do usuário."""
    
    # Campo que armazena o nome ou título do assunto
    text = models.CharField(max_length=200)
    
    # Campo que registra a data e hora em que o assunto foi criado
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna uma representação em string do modelo, exibindo o título do assunto."""
        return self.text

class Entry(models.Model):
    """Modelo que representa uma entrada específica sobre um tópico de aprendizado."""
    
    # Relacionamento com o modelo 'Topic'. Cada entrada pertence a um tópico.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    # Campo que armazena o conteúdo detalhado da entrada, podendo ser um texto mais longo
    text = models.TextField()
    
    # Campo que registra a data e hora em que a entrada foi criada
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Define o nome plural para o modelo, que será usado no admin e em outros lugares
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Retorna uma representação em string da entrada, limitando a 50 caracteres para visualização."""
        return self.text[:50] + ' (...)'

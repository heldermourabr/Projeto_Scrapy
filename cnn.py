import scrapy


class CnnNoticias(scrapy.Spider):
    name = 'cnn_brasil'
    start_urls = ['https://www.cnnbrasil.com.br/internacional/']

    def parse(self, response):
        """
        O metodo parse extrai a lista de urls a serem "raspadas" pelo metodo parse_news.
        """
        urls = response.xpath("//div//a[re:test(@href, 'internacional')]/@href").getall()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_news)
            
    
    def parse_news(self, response):
        """
        O metodo parse_news é chamado para cada URL de noticia e faz as requisições dos nossos dados
        - Titulo da noticia
        - Data de postagem
        - Texto da noticias
        - Tags usadas

        Retorna um dicionário com essas informações.
        """
        titulo = response.css('.post__title::text').get()
        data = response.css('.post__data::text').get()
        texto = " ".join(response.xpath('//div/p').getall())
        tags = ",".join(response.css('.tags__list__item a::text').getall()).strip()
        url = response.url

        yield{"url": url, 'titulo': titulo, 'publicacao': data, 'texto': texto, 'tags': tags}
        
import scrapy


class UolNoticias(scrapy.Spider):
    name = 'uol'
    start_urls = ['https://noticias.uol.com.br/internacional']

    def parse(self, response):
        """
        O metodo parse estrai a lista de urls a serem "raspadas" pelo metodo parse_news.
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

        Retorna um dicionário com essas informações.
        """
        titulo = response.css('h1 span i::text').get()
        data = response.css('.image-content-pad .author .time::text').get().strip()
        texto = " ".join(response.css('.text p::text').getall())
        url = response.url

        yield{"url": url, 'titulo': titulo, 'publicacao': data, 'texto': texto}

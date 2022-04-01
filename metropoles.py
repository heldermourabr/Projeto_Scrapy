import scrapy


class MetropolisNoticias(scrapy.Spider):
    name = 'metropolis_brasil'
    start_urls = ['https://www.metropoles.com/mundo']

    def parse(self, response):
        """
        O metodo parse estrai a lista de urls a serem "raspadas" pelo metodo parse_news.
        """
        urls = response.xpath("//div//a[re:test(@href, 'mundo')]/@href").getall()
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
        titulo = response.css('.m-title-single::text').get()
        data = response.css('.m-pub-date time::text').get()
        texto = " ".join(response.css('.m-content p::text').getall())
        tags = " ".join(response.css('.rs_skip a::text').getall())
        url = response.url

        yield{"url": url, 'titulo': titulo, 'publicacao': data, 'texto': texto, 'tags': tags}

import scrapy


class BbcNoticias(scrapy.Spider):
    """
    Configuração da Spider scrapy para acessar e extrair os dados de noticias da BBC
    """
    name = 'bbc'
    start_urls = ['https://www.bbc.com/portuguese/topics/cmdm4ynm24kt']


    def parse(self, response):
        """
        O metodo parse estrai a lista de urls a serem "raspadas" pelo metodo parse_news.
        """
        urls = response.xpath("//div//a[re:test(@href, 'internacional')]/@href").getall()
        for i, url in enumerate(urls):
            urls[i] = 'https://www.bbc.com/' + url # Laço para adiconar o domínio nas URLs recebidas.

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
        titulo = response.css('#content::text').get()
        data = response.xpath('//div//main//div//time').get().split('"')
        texto = " ".join(response.css('.e1cc2ql70::text').getall())
        tags = ", ".join(response.css('.e1hq59l0 a::text').getall())
        url = response.url
        yield{'url': url, 'titulo': titulo, 'publicacao': data[1], 'texto': texto, 'tags': tags}

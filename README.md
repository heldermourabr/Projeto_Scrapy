# __Projeto Scrapy__
### __Objetivo__

_O objetivo do projeto é desenvolver um sistema de web crawling para estruturar dados de portais de notícias concorrentes de forma incremental, disponibilizando as métricas em um data base._
___
### __Desenvolvimento__

1. _Escolha da estratégia de crawling/scraping_
    - Framework - Scrapy
    - [Documentação](https://docs.scrapy.org/en/latest/)
    <br/><br/>

2. _Escolha dos websites para crawling_
    - UOL Notícias
    - BBC News
    - CNN Brasil
    - Metrópoles
<br/><br/>
3. _Foram configuradas 4 spiders do scrapy, uma para cada website_
    - Cada spider retorna o título, data de postagem, texto da notícia e as tags usadas
    - OBS: O UOL Notícias não utiliza tags
<br/><br/>
4. _Os dados adquiridos são tratados com os módulos Pandas e Numpy antes da inserção no DB_
    - O tratamento consiste em limpeza de informações desnecessárias como marcadores HTML/CSS e mudança de tipo de dado
    - Os dados são armazenados de forma incremental em um DB MySQL
____
### __Desempenho__
<br/>

<table class="tg">
<thead>
  <tr>
    <th class="tg-6o7p">Teste</th>
    <th class="tg-6o7p">BBC</th>
    <th class="tg-6o7p">CNN</th>
    <th class="tg-6o7p">Metrópoles</th>
    <th class="tg-6o7p">UOL</th>
    <th class="tg-6o7p">ETL</th>
    <th class="tg-6o7p">Total</th>
    <th class="tg-6o7p">Notícias</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-mums">01</td>
    <td class="tg-jbyd">4.85s</td>
    <td class="tg-jbyd">3.15s</td>
    <td class="tg-jbyd">3.64s</td>
    <td class="tg-jbyd">3.36s</td>
    <td class="tg-jbyd">1.37s</td>
    <td class="tg-jbyd">16.37s</td>
    <td class="tg-jbyd">52</td>
  </tr>
  <tr>
    <td class="tg-fm1b">02</td>
    <td class="tg-j4pq">4.53s</td>
    <td class="tg-j4pq">2.66s</td>
    <td class="tg-j4pq">3.42s</td>
    <td class="tg-j4pq">2.46s</td>
    <td class="tg-j4pq">1.5s</td>
    <td class="tg-j4pq">14.57s</td>
    <td class="tg-j4pq">55</td>
  </tr>
  <tr>
    <td class="tg-mums">03</td>
    <td class="tg-jbyd">2.38s</td>
    <td class="tg-jbyd">3.06s</td>
    <td class="tg-jbyd">4.61s</td>
    <td class="tg-jbyd">2.51s</td>
    <td class="tg-jbyd">1.62s</td>
    <td class="tg-jbyd">14.18s</td>
    <td class="tg-jbyd">53</td>
  </tr>
</tbody>
</table>

<br/>
A solução pode ser escalável configurando novas spiders para todos os websites desejados, assim como o Database. O pipeline e as funções aplicaveis são funcionais para dados com o mesmo esquema organizacional.
<br/>

________


  ### __Instalação__


 - Clone o repositório para usá-lo
```
$ git clone https://github.com/heldermourabr/Projeto_Scrapy
```
   
<br/>

 - Requerimentos
    - numpy - 1.21.4
    - pandas - 1.3.4
    - Scrapy - 2.6.1
    - mysql-connector - 2.2.9<br/>
<br/>

No cmd/terminal navegue até o diretório do projeto e execute: 
```
$ pip install -r requirements.txt
```
<br/>

 - Se estiver no linux, após instalar os requerimentos execute:
```
$ sudo apt install python3-scrapy
```

 - Crie o database MySQL a partir do script [noticias.sql](https://github.com/heldermourabr/Projeto_Scrapy/blob/master/noticias.sql)

 - Abra o arquivo [__main__.py](https://github.com/heldermourabr/Projeto_Scrapy/blob/master/__main__.py) e preencha os argumentos de acesso ao seu DB.

```
news = Interface_sql("user", "Password", "Host", "Database")
```
<br/>

 - Pelo CMD/terminal navegue até o diretório do projeto e execute:
```
$ python __main__.py
```
____
 ### __Análise dos dados__

 A base de dados adiquirida permite analisarmos os padrões de publicações de notícias como:

 - Assuntos mais comentados (tags)

 - Volume de novas públicações diárias dos portais

 - Tamanho médio dos textos, visando manter o interesse do leitor sem textos muito extensos

A análise dessas métricas podem contribuir para o planejamento de publicações de um site/blog de noticias, baseando-se em portais com estruturas sólidas no mercado

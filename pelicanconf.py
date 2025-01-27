#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Tema
THEME = "themes/pjecz-2025-01"

# Para desarrollo
SITEURL = "http://localhost:8000"
RELATIVE_URLS = False

# Metadatos de todo el sitio web
SITENAME = "Poder Judicial del Estado de Coahuila de Zaragoza"
SITELOGO = "theme/images/pjecz.png"
SITEPREVIEW = "theme/images/generic.jpg"
SITEDESCRIPTION = "Responsables de impartir justicia en el Estado, de dirimir diferencias entre particulares, de conciliar, y de promover con el ejemplo una cultura de la legalidad y justicia cotidiana."
SITETWITTER = "@PJCoah"

# Autor por defecto
AUTHOR = "PJECZ"

# Directorio donde esta el contenido
PATH = "content"

# Directorios que tienen los articulos
ARTICLE_PATHS = [
    "acuerdos-del-consejo",
    "acuerdos-del-pleno",
    "comunicados",
    "entrevistas",
    "news-letters",
    "noticias",
    "sesiones",
]

# Directorios que tienen páginas fijas, no artículos
PAGE_PATHS = [
    "armonizacion-contable",
    "aviso-de-privacidad",
    "boletines-judiciales",
    "buzon-electronico",
    "calendario-de-labores",
    "citas",
    "comisiones",
    "conocenos",
    "convocatorias",
    "derechos-humanos-e-igualdad-de-genero",
    "edictos-de-declaracion-de-ausencia",
    "justicia-para-ti",
    "inicial",
    "licencias",
    "magistrados",
    "mujer-segura",
    "observatorio-judicial",
    "podcasts",
    "poder-en-linea",
    "politicas-de-uso",
    "ponte-trucha",
    "pontetrucha",
    "sistemas",
    "tramites-y-servicios",
    "transparencia",
    "transparencia-proactiva",
    "transparencia-tca",
]

# Directorios y archivos que son fijos
# Agregue también los directorios que tienen archivos para artículos y páginas
STATIC_PATHS = [
    "acuerdos-del-consejo",
    "armonizacion-contable",
    "boletines-judiciales",
    "buzon-electronico",
    "calendario-de-labores",
    "citas",
    "comisiones",
    "comunicados",
    "conocenos",
    "convocatorias",
    "derechos-humanos-e-igualdad-de-genero",
    "edictos-de-declaracion-de-ausencia",
    "entrevistas",
    "json",
    "justicia-para-ti",
    "magistrados",
    "mujer-segura",
    "news-letters",
    "noticias",
    "observatorio-judicial",
    "poder-en-linea",
    "ponte-trucha",
    "sesiones",
    "sistemas",
    "tramites-y-servicios",
    "transparencia",
    "transparencia-proactiva",
    "transparencia-tca",
    "CNAME",
    "favicon.ico",
    "robots.txt",
]

# Directorio de salida
OUTPUT_PATH = "output/"
DELETE_OUTPUT_DIRECTORY = True

# Para evitar que se hagan summary automaticos
SUMMARY_MAX_LENGTH = 0

# NO usar el directorio como la categoria
USE_FOLDER_AS_CATEGORY = False

# Lenguaje y zona horaria
DEFAULT_LANG = "es"
TIMEZONE = "America/Monterrey"

# Formato para las fechas d) dia, B) nombre del mes, Y) año
DEFAULT_DATE_FORMAT = "%d de %B de %Y"

# Feeds
# En página inicial la sección Tramisiones de las sesiones
# Toma output/feeds
# Con el programa themes/pjecz-2020-10/static/js/inicial-noticias-eventos.js
# Lea https://www.pjecz.gob.mx/consultas/fuentes-rss/
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
FEED_ALL_RSS = "feeds/all.rss.xml"
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
FEED_MAX_ITEMS = 48
RSS_FEED_SUMMARY_ONLY = True

# NO BORRAR de output los siguientes directorios y archivos
OUTPUT_RETENTION = [".git", ".gitignore"]

# Paginacion
DEFAULT_PAGINATION = 12
DEFAULT_ORPHANS = 3

# Crear indices como index1.html, index2.html, index3.html...
# La página inicial será index.html con content/inicial/inicial.html
PAGINATION_PATTERNS = ((1, "{name}{number}{extension}", "{name}{number}{extension}"),)

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["articles_lists_json", "pelican_javascript", "sitemap"]

# Plugin articles_lists_json
# Sirve para crear listados de los artículos por categorías
# La página inicial toma output/json/comunicados-noticias.json
# Gracias al programa themes/pjecz-2020-10/static/js/inicial-comunicados-noticias.js
ARTICLES_LISTS_JSON_OUTPUT_PATH = "json"
ARTICLES_LISTS_JSON_OUTPUT_ALL = None
ARTICLES_LISTS_JSON_CATEGORIES_FILTERS = [
    (
        "acuerdos.json",
        [
            "Acuerdos del Consejo",
            "Acuerdos del Pleno",
        ],
    ),
    (
        "comunicados-noticias.json",
        [
            "Comunicados",
            "Entrevistas",
            "Noticias",
        ],
    ),
    (
        "transmisiones-sesiones.json",
        [
            "Pleno del Tribunal Superior de Justicia",
            "Sala Civil y Familiar",
            "Sala Penal",
            "Sala Regional",
            "Tribunal Constitucional",
        ],
    ),
]
ARTICLES_LISTS_JSON_LIMIT = 400

# Plugin sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 1,
        "indexes": 0.5,
        "pages": 1,
    },
    "changefreqs": {
        "articles": "daily",
        "indexes": "daily",
        "pages": "weekly",
    },
    "exclude": [
        "archives.html",
        "categories.html",
        "tags.html",
        "author/",
        "category/",
        "tag/",
    ],
}

# Activar el caché
LOAD_CONTENT_CACHE = True

# NO hay cargas de dependencias de Internet
USE_REMOTE_SERVICES = False

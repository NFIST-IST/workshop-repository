Title: Parte 2
Author: NFIST
Slug: latex2
Category: Workshop LaTeX
Date:13
Series: Workshop LaTeX
Series_index: 2
Summary: \LaTeX
Tags: LaTeX, Documentos


# VIII. Secções

O LaTeX está organizado numerando, por capítulos e secções, o documento. Existem 7 níveis de dependência, em função da *document class*:

| Nível | Nome                          |
| ----- | ----------------------------- |
| -1    | \part{part}                   |
| 0     | \chapter{chapter}             |
| 1     | \section{section}             |
| 2     | \subsection{subsection}       |
| 3     | \subsubsection{subsubsection} |
| 4     | \paragraph{paragraph}         |
| 5     | \subparagraph{subparagraph}   |

Normalmente, as secções são o principal nível usado, as partes e capítulos são mais para, e.g., livros.

## Numeração

Por defeito, a numeração das secções, etc., é feita automaticamente. Para alterar o modo de numeração, veremos mais à frente, em ***Layout***. Para retirar simplesmente a numeração, basta adicionar um asterisco antes dos { }, tal como acontecia no modo Matemática. Estes não serão adicionados no Índice.

    :::latex
    \section*{Introduction}


## Table of Content - Índice

Não iremos entrar em detalhe sobre a construção do Índice, dado não ser um tema
muito utilizado, mas colocaremos o
[link](https://www.overleaf.com/learn/latex/Table_of_contents), que redireciona
para o site do Overleaf.


---

# IX. Preamble e Packages

Já foi mencionado várias vezes o **Preamble**; este é a primeira coisa que
aparece no ficheiro a seguir à *document class*, antes do texto do documento.
Este dará informações extra ao LaTeX de como formatar e incluir texto no
documento.

Neste incluir-se-ão, muitas vezes, packages. Muitos dos comandos e environments
aqui falados já estão incluídos no LaTeX (excepto os do modo Matemática, onde
já está incluindo um pacote, *amsmath*). 
**Packages** são bibliotecas de comandos e environments extra. Existem milhares disponíveis.

Incluir uma package - incluir no ***preamble***:

    :::latex
    % Document class
    \documentclass[12pt,a4paper]{article}
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    % >>> Preamble
    % Packages
    \usepackage[setting1, setting2,...]{package_name} %preamble
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % >>> Main body
    \begin{document}
    
    Hello World!
    % now we can use commands from package_name here...
    
    \end{document}

Cada package tem o seu objetivo, como por exemplo incluir imagens, cores, entre outros, que o LaTeX não disponibiliza por si automaticamente.

Vemos também que algumas packages têm opções para incluir definições especiais do pacote.


## Lista de Packages

A lista de todas as packages disponíveis pode ser encontrada na *Comprehensive
TEX Archive Network*: [CTAN](http://www.ctan.org). Aqui, o detalhe de cada
pacote é dado por cada autor.


Segue-se um pdf para uma lista mais abreviada de packages, habitualmente
mostrados num exemplo e com o link para a package direta: [pdf
link](/content/LaTeX_packages.pdf)
- Créditos do *Bernardo Silva* por fazer este pdf.

Exemplos de pacotes usados:

| Package  | Description                                                |
| -------- | ---------------------------------------------------------- |
| amsmath  | AMS mathematical facilities                                |
| amsfonts | TeX fonts from the American Mathematical Society           |
| babel    | Multilingual support for plain TEX or LaTeX                |
| color    | Color control for LaTeX documents                          |
| fancyhdr | Extensive control of page headers and footers in LaTeX     |
| graphicx | Enhanced support for graphics                              |
| hyperref | Extensive support for hypertext in LaTeX                   |
| natbib   | Flexible bibliography support                              |
| TikZ     | Create PostScript and PDF graphics in TeX                  |
| xcolor   | Driver-independent color extensions for LaTeX and pdfLaTeX |


## Criar Packages

Também dá para criar os nossos próprios Packages, sendo este processo mais
complicado, de forma a personalizar o documento - [link para
overleaf](https://www.overleaf.com/learn/latex/Writing_your_own_package) ou
[link para wikibooks](https://en.wikibooks.org/wiki/LaTeX/Creating_Packages).


---

# X. Layout

## Títulos, Subtítulos, Autores, Data

Para declarar o título e outras informações de um documento, existem comandos específicos.
Estes comandos podem ser incluídos no *preamble* do documento e são "chamados" pelo comando `\maketitle`.



| Comando                           | Utilidade                                                                                                   |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| \title{First document}            | Título                                                                                                      |
| \author{A. Author \and B. Author} | Nome(s) do(s) autor(es)                                                                                       |
| \thanks{C. Author}                | Adicionar à frente do(s) autor(es) dentro dos \{ \}. Sobrescrito com uma footnote com os agradecimentos. |
| \affil{IST}                       | Filiação                                                                                                    |
| \date{\today}                     | Data manualmente ou usar comando **\today** para ser automático à data de compilação                        |


Exemplo:

    :::latex
    \documentclass{article}
    
    \title{The Title}
    \author{A. Author \and B. Author \thanks{C. Author}}
    \date{\today}
    
    \begin{document}
    
    \begin{titlepage}
    \maketitle
    \end{titlepage}
    
    \par Hello World
    \end{document}

Para colocar o subtítulo depois dos autores, basta redefinir o comando *\subtitle* da forma:

    :::latex
    \newcommand{\subtitle}[1]{
      \postauthor{
        \end{tabular}\par\end{center}
        \begin{center}\large#1\end{center}
        }
    }


### Title Page

É possível colocar o título numa só página, como foi feito no exemplo, usando o
environment *titlepage*. Este bloco terá um comportamento dependente do tipo de
documento em causa.


## Cabeçalho e Rodapé

A maneira mais simples de colocar um certo estilo para os cabeçalhos e rodapés é usando o comando: `\pagestyle{''style''}`

Com 3 estilos:
- empty: Both the header and footer are cleared (blank) in this page style.
- plain: This is the default style. The header is empty and the footer contains page numbers in the centre.
- myheadings: As shown in the introduction,The footer is empty in this page
 style. The header contains the page number on right side (on even pages) or
 on left side (on odd pages) along with other user-supplied information; there
 is an exception for the first page of each chapter, where the footer contains
 centred page number while the header is blank.

Mas estilos podem ser modificados em relação ao básico com o package
[***fancyhdr***](https://mirrors.up.pt/pub/CTAN/macros/latex/contrib/fancyhdr/fancyhdr.pdf).
Eis um exemplo:

    :::latex
    \usepackage{fancyhdr}
    
    \pagestyle{fancy}
    \fancyhf{}
    \rhead{Overleaf}
    \lhead{Guides and tutorials}
    \rfoot{Page \thepage}

Aqui temos o seguinte: 
Depois do estilo "fancy" ser defenido por `\pagestyle{fancy}`. 

- O comando `\fancyhf{}` apaga o estilo existente, para não haver sobreposições dos elementos novos com os padrões falados anteriormente.

| Comando                | Utilidade                                                                                                               |
|:---------------------- |:----------------------------------------------------------------------------------------------------------------------- |
| \rhead{Right Text}     | Texto entre parênteses à direita no cabeçalho                                                                           |
| \lhead{Left Text}      | Texto entre parênteses à esquerda no cabeçalho                                                                          |
| \chead{Center Text}    | Texto entre parênteses no centro no cabeçalho                                                                           |
| \rfoot{Right Text}     | Texto entre parênteses à direita no rodapé                                                                              |
| \lfoot{Left Text}      | Texto entre parênteses à esquerda no rodapé                                                                             |
| \cfoot{Page \thepage } | Texto entre parênteses no centro no rodapé. O comando `*\thepage*`  irá criar automaticamente a paginação no centro |

### Linhas
Para além do texto, ainda temos duas linhas "decorativas" no cabeçalho e
rodapé. Por default, são de *0pt* de espessura, dai estarem invisíveis. Para
mudar, é fácil:

    :::latex
    \renewcommand{\headrulewidth}{1pt}
    \renewcommand{\footrulewidth}{1pt}

Finalmente, existem uns outros comandos, não tão usados, referidos no site do
Overleaf,
[link](https://www.overleaf.com/learn/latex/Headers_and_footers#Reference_guide).

### Last Page

Também podemos referenciar a última página do documento usando o package `lastpage`. Exemplo:

    :::latex
    \usepackage{fancyhdr,lastpage}
    
    \cfoot{\thepage\ de \pageref{LastPage}}

## Section Modifier

Com a package
[titlesec](https://ftp.eq.uc.pt/software/TeX/macros/latex/contrib/titlesec/titlesec.pdf),
é possível personalizar as secções, subsecções, etc., de forma fácil:


    :::latex
    \usepackage{titlesec}
    
    \titleformat
    {\section} % command
    [hang] % shape
    {\bfseries\Large} % format
    {Roman{section}.} % label
    {2mm} % sep
    {} % before-code
    [] % after-code
    
    \titleformat{\subsection}[hang]
    {\large\bfseries}{\thesection.\arabic{subsection}.}
    {1.5mm}{}[]
    
    ...

Este exemplo segue o seguinte formato:

> \titleformat{"command"}["shape"]{"format"}{"label"}{"sep"}{"before-code"}["after-code"]

onde *\["shape"\]* e *\["after-code"\]* são parâmetros opcionais. E temos as seguintes definições:

- **\<command\>** é o comando da seção em questão a ser mo dificado: \part, \chapter, \section, \subsection, \subsubsection, \paragraph or \subparagraph.
- **\<shape\>** é a forma do parágrafo a seguir à seção, valores possíveis: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame.
- **\<format\>** é o formato a ser aplicado ao título e ao texto, e.g.: \normalfont\Large\bfseries.
- **\<label\>** especificar a label/números antes do texto.
- **\<sep\>** tamanho da separação horizontal entre o *label* e o *texto*.
- **\<before-code\>** código que precede a seção.
- **\<after-code\>** código que sucede a seção.

Esta informação, incluindo ainda os espaços antes e depois da secção, pode ser vista neste [link](https://www.overleaf.com/learn/latex/Sections_and_chapters)

## Margens, Geometry

Falta saber como definir o tamanho e as margens de um documento. Para tal, com
o **package**
[geometry](https://mirrors.up.pt/pub/CTAN/macros/latex/contrib/geometry/geometry.pdf),
é fácil personalizar o documento acrescentando no **preamble** o necessário.
*Exemplo:* Criar uma folha A4 com texto que não exceda 6in de largura e 8in de altura:

    ```latex
    \usepackage[a4paper, total={6in, 8in}]{geometry}

Os parâmetros colocados entre os parênteses \[ \] determinaram o layout.

O tamanho do papel, a orientação e as margens são os elementos mais usados
deste pacote. Outra maneira será definir os parâmetros no preamble fora do
package:

Exemplo: criar um paper A4, portrait orientation e 2cm de margem, 2cm no topo e 1.5cm em baixo:

    :::latex
    \usepackage[a4paper,portrait,margin=2cm,top=2cm,bottom=1.5cm]{geometry}
OU

    :::latex
    \usepackage{geometry}
    \geometry{a4paper,portrait,margin=2cm,top=2cm,bottom=1.5cm}

### Dimensões Específicas das Margens

Por padrão, o LaTeX coloca as seguintes dimensões (com uma imagem
representativa retirada do Overleaf)
([link](https://www.overleaf.com/learn/latex/Page_size_and_margins#Fine_tuning_your_LaTeX_page_dimensions)):

![layout](https://i.imgur.com/BqUjM5X.png)

Com o pacote **geometry**, é intuitivo mudar o layout da página.
Segue-se uma lista de elemento do documento cuja tamanho é alterável:

| Parâmetro                 | Alteração                                                                                                                                                                                                          |
| ------------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| textwidth                 | Elemento 8 da figura                                                                                                                                                                                               |
| textheight                | Elemento 7 da figura                                                                                                                                                                                               |
| total                     | Por defeito, as dimensões do corpo dependem de outros, mas é combinação dos comandos includehead, includefoot, includeheadfoot and includemp, mudando o tamanho do cabeçalho, corpo e rodapé e margens todos juntos |
| left, lmargin, inner      | Estes três alteram o tamanho da margem esquerda, elementos 1 e 3 em conjunto da figura                                                                                                                             |
| right, rmargin, outer     | Estes três alteram o tamanho da margem esquerda, elementos 9 e 10 em conjunto da figura                                                                                                                            |
| top, tmargin              | Elementos 2 e 6 em conjunto da figura                                                                                                                                                                              |
| bottom, bmargin           | Estes representam a distância da parte debaixo do documento à *baseline*.                                                                                                                                          |
| headheight                | Altura do Cabeçalho, elemento 5 da figura                                                                                                                                                                          |
| headsep                   | Separação entre o cabeçalho (baseline) e o texto, elemento 6 da figura.                                                                                                                                            |
| footnotesep               | Separação entre a parte de baixo do texto (baseline) e o topo das footnotes.                                                                                                                                     |
| footskip                  | Separação ente a baseline da última linha do texto e do rodapé                                                                                                                                                     |
| marginparwidth, marginpar | Largura das notas de margens, elemento 10 da figura                                                                                                                                                                |

Para alterar estes parâmetros é necessário escrever na forma:

    ```latex
    %parameter = value_units
    \headheight = 20pt

Nota: usar as unidades *standard* do LaTeX (mm, cm, pt, in)


---


# XI. Typesetting 2

## Tipos de Fontes

### Font Families
Existe uma grande diversidade de famílias de fontes, tal como no Word. Alguns exemplos comuns incluem a Times, Courier, ou Helvetica.
As fontes são geralmente agrupadas em 3 categorias: *serif*, *sans serif*, e *monospaced*, abreviadas em LaTeX para rm, sf, e tt, respetivamente.

O texto em documentos de LaTeX está, por defeito, em *Roman* (serif). Para mudar, colocar no *preamble*, antes do início do documento

    :::latex
    \renewcommand{\familydefault}{<family>}

Onde a <<span style="color:green">family</span>> pode assumir os diferentes tipos:

- \rmdefault
- \sfdefault
- \ttdefault



### Catálogo de Fontes:

Para uma maior variedade, existe um site que mostra todos os estilos existentes
nos diferentes modos, e como aplicar no LaTeX:
[Link](https://tug.org/FontCatalogue/)

O próprio Overleaf dá um catálogo mais simples e fácil de utilizar, mas mais pequeno:
[Link para o Overleaf](https://pt.overleaf.com/learn/latex/Font_typefaces)


## Size 

Para reescalar o tamanho do texto em relação ao predefinido, usar os seguintes comandos:

<img align="center" src="https://i.imgur.com/v4Fecow.png" width="250">

A seguinte sintaxe muda-o no meio do texto:

    :::latex
    In this example the {\huge huge font size} is set and 
    the {\footnotesize Foot note size also}. There's a fairly 
    large set of font sizes.

Existe um site do Overleaf que tem uma lista com estes comandos:
[Link](https://pt.overleaf.com/learn/latex/Font_sizes,_families,_and_styles#Font_sizes)

Por defeito, `\normalsize` tem 10 points, mas podemos mudar isto, como
referimos no início, na declaração da `\documentclass`, e.g.
`\documentclass[12pt]{article}`.



Title: Parte 3
Author: NFIST
Slug: latex3
Category: Workshop LaTeX
Date:13
Series: Workshop LaTeX
Series_index: 3
Summary:
Tags: LaTeX, Documentos


# XII. Environment - Items, Tabelas e Figuras

`Environments` são usados para formatar blocos de texto. Iremos explicar e mostrar como definir e usar environments.

Já introduzimos alguns Environments no modo Matemática com as equações, e logo no início com o `\begin{document}`.

O <span style="color:red"> *\begin* </span> e o <span style="color:red"> *\end*
</span> são usados para criar diversos Environments, tais como listas de
pontos, números, figuras, tabelas e muitos outros.


Em baixo, temos um exemplo simples de como usar um Environment.

    :::latex
    \begin{center}
    This text will be centred since it is inside a special 
    environment. Environments provide a efficient way of modifying 
    blocks of text within your document.
    \end{center}

Seguem-se os Environments mais usados:


## Items

Para fazer listas em forma de itens, números ou outro, é usado Environments.
Dentro destas listas, o comando de `\item` é usado para identificar um item na
lista.

Colocando o Environment dentro do próprio Environment, cria-se uma sublista associada.



### Itemize

O famoso ***itemize environment*** cria listas não numeradas, normalmente chamado de "bulleted" list.

    :::latex
    \begin{itemize}
    \item First item
    \item Second item
    ...
    \end{itemize}

Os níveis associados ao *itemize* são quatro:

![itemize](https://i.imgur.com/M49iXpe.png)

Por padrão, os níveis assumem o seguinte esquema:
- Nível 1 é **\textbullet** (•),
- Nível 2 é **\textendash** (–) ,
- Nível 3 é **\textasteriskcentered** (*)
- Nível 4 é **\textperiodcentered** (·).

#### Mudar o estilo das listas

Este esquema é alterável, redefinindo o comando do tipo de número ou letra do nível da lista. Eis um exemplo:

    :::latex
    \usepackage{amssymb}
    ...
    
    \renewcommand{\labelitemi}{$\blacksquare$}
    \renewcommand{\labelitemii}{$\square$}
    \begin{itemize}
      \item  First Level
      \begin{itemize}
        \item  Second Level
        \begin{itemize}
          \item  Third Level
          \begin{itemize}
            \item  Fourth Level
          \end{itemize}
        \end{itemize}
      \end{itemize}
    \end{itemize}

![itemize2](https://i.imgur.com/svq2sLm.png)

Os símbolos matemáticos do exemplo usam o ***amssymb package***, daí adicionar-se `\usepackage{amssymb}` ao **preamble**.

O comando `\renewcommand{\labelitem...}{;;;}` muda o marcador do ... nível para outro marcador(;;;):

- **\labelitemi** for Level 1
- **\labelitemii** for Level 2
- **\labelitemiii** for Level 3
- **\labelitemiv** for Level 4

Para mudar um item em específico, usar (com o respetivo package):

    :::latex
    \begin{itemize}
      \item  Default item label for entry one
      \item  Default item label for entry two
      \item[$\square$]  Custom item label for entry three
    \end{itemize}

### Enumerações

O ***enumerate environment*** produz listas numeradas. A lista numerada gera automaticamente os números de cada item.


    :::latex
    \begin{enumerate}
      \item First item
      \item Second item
        ...
    \end{enumerate}

Os níveis associados ao *enumerate* são quatro:

![enumerate](https://i.imgur.com/MLryvUY.png)

Por padrão, os níveis assumem o seguinte esquema:

- Arabic number (1, 2, 3, ...) para o nível 1;
- Lowercase letter (a, b, c, ...) para o nível 2;
- Lowercase Roman numeral (i, ii, iii, ...) para o nível 3;
- Uppercase letter (A, B, C, ...) para o nível 4.

#### Mudar estilo dos números

Este esquema é alterável redefinindo o comando do tipo de número ou letra do nível da lista. Eis um exemplo:

    :::latex
     \renewcommand{\labelenumii}{\Roman{enumii}}
     \begin{enumerate}
       \item item 1 on level 1
       \begin{enumerate}
         \item item 1 on level 2
         \begin{enumerate}
           \item item 1 on level 3
           \begin{enumerate}
             \item item 1 on level 4
             \item item 2 on level 4
           \end{enumerate}
           \item item 2 on level 3
         \end{enumerate}
         \item item 2 on level 2
       \end{enumerate}
       \item item 2 on level 1
     \end{enumerate}

![enumerate2](https://i.imgur.com/miYh24e.png)

O comando `\renewcommand{\labelenumii}{\Roman{enumii}}` muda o segundo nível
para números romanos maiúsculos. Colocar **\labelenum_** em vez do
**\theenum_** resulta em mudar a label do mesmo, por exemplo tirar os () do
nível existentes por defeito.

1. **\theenumi** for Level 1
2. **\theenumii** for Level 2
3. **\theenumiii** for Level 3
4. **\theenumiv** for Level 4

#### Tabela de estilos de listas numeradas:

| Code    | Description                               |
| ------- | ----------------------------------------- |
| \alph   | Lowercase letter (a, b, c, ...)           |
| \Alph   | Uppercase letter (A, B, C, ...)           |
| \arabic | Arabic number (1, 2, 3, ...)              |
| \roman  | Lowercase Roman numeral (i, ii, iii, ...) |
| \Roman  | Uppercase Roman numeral (I, II, III, ...) |


#### Mudar contador dos números

Os contadores das listas que incrementam os *\item* começam sempre pelo
primeiro número ou letra: 1,a,i,A,I. Isto pode ser mudado com o
`*\setcounter{enum_}*`:

    :::latex
    \begin{enumerate}
      \setcounter{enumi}{4}
      \item item 5 on level 1
      \item item 6 on level 1
    \end{enumerate}

![enumerate3](https://i.imgur.com/NgHMXwI.png)


### Descrição

O ***description environment*** produz uma lista com uma certa label. 

    :::latex
    \begin{description}
       \item [label 1] First item
       \begin{description}
          \item [label 1.1] Second item
       \end{description}
          ...
    \end{description}

![description](https://i.imgur.com/dhPZtLa.png)


### Misturar

No LaTeX é possível colocar diferente tipos de listas dentro de outras listas, até quatro níveis.


    :::latex
    \begin{enumerate}
       \item The labels consists of sequential numbers.
       \begin{itemize}
         \item The individual entries are indicated with a black dot, a so-called bullet.
         \item The text in the entries may be of any length.
       \end{itemize}
       \item The numbers starts at 1 with every call to the enumerate environment.
    \end{enumerate}

![misturar](https://i.imgur.com/xOcsjFY.png)


### Formatar espaços das listas 

Existe uma série de comandos de espaçamentos para as listas, que podem ser mudados:

|          |           |             |              |                |
| -------- | --------- | ----------- | ------------ | -------------- |
| \itemsep | \labelsep | \labelwidth | \leftmargin  | \listparindent |
| \parsep  | \parskip  | \partopsep  | \rightmargin | \topsep        |


#### Exemplo para Separação entre Items

    :::latex
    \begin{itemize}
    \addtolength{\itemsep}{-0.5\baselineskip}
    \item Item 1
    \item Item 2
    \item Item 3
    \end{itemize}
    
    \begin{itemize}
    \setlength{\itemsep}{0pt}
    \item Item 1
    \item Item 2
    \item Item 3
    \end{itemize}

![listsep](https://i.imgur.com/B1t2avI.png)



## Tabelas

Inserir tabelas é uma das coisas mais essenciais a fazer num documento. O LaTeX
permite personalizar as tabelas em tamanho, combinar células, mudar a cor, etc. 

    :::latex
    \begin{table}[<placement>]
       % table body
       \begin{tabular}[pos]{cols}
          column 1 entry & column 2 entry ... & column n entry \\
          ...
       \end{tabular}
       \caption{<table title>}
    \end{table}

O posicionamento da tabela, ***placement***, será explicado melhor na próxima secção.

A legenda, ***\caption*** da tabela pode ser colocado tanto em baixo como no
topo da tabela; dependerá onde o comando aparece, antes ou depois do corpo da
tabela.

No corpo da tabela, *table body*, é normalmente usado o **tabular
environment**. Este recebe dois parâmetros, um opcional, \[pos\], e outro
obrigatório, \{cols\}

- **\[pos\]** define a posição vertical, pode tomar os seguintes valores: t, b,
 c, significando linha do topo alinhada com o texto, linha debaixo alinhado
 com o texto, tabela centrada no texto, respetivamente.
- **\{cols\}** define o número, o alinhamento e as fronteiras das colunas, que podem assumir os seguintes valores:

| Parâmetro     | Significado                                             |
| ------------- | ------------------------------------------------------- |
| l             | alinhar o texto à esquerda                              |
| c             | alinhar o texto ao centro                               |
| r             | alinhar o texto à direita                               |
| p{\<width\>}  | Fixar largura da coluna com texto alinhado no topo     |
| m{\<width\>}  | Fixar largura da coluna com texto alinhado no centro * |
| b{\<width\>}  | Fixar largura da coluna com texto alinhado em baixo *  |
| \|            | linha vertical                                          |
| \|\|          | linha vertical dupla                                    |
| \*{num}{form} | formata a forma com *num* nº de vezes                    |

Aqui está um exemplo:

    :::latex
    \begin{tabular}{ |c|c|c| } 
     \hline
     cell1 & cell2 & cell3 \\ 
     cell4 & cell5 & cell6 \\ 
     cell7 & cell8 & cell9 \\ 
     \hline
    \end{tabular}

![table](https://i.imgur.com/tlfZMiX.png)

Para entender alguns pormenores deste exmplo, vejamos:

- **\{ |c|c|c| \}**: 
Declara as 3 colunas separadas por linhas verticais. Cada c significa que o conteúdo está centrado, 
- **\hline**:
Linha horizontal entres duas linhas. Na secção seguinte mostramos mais.
- **cell1 & cell2 & cell3 \\\\**:
Cada célula é separada pelo &, e com \\\\ para separar linhas.

### Separação entre células:

Para separar as células temos os seguintes comandos:

| Comando     | Descrição                                                   |
| ----------- | ----------------------------------------------------------- |
| &           | Separar colunas                                             |
| \\          | Começar nova linha (adicionar mais espaço, e.g. \\\\\[6pt\]) |
| \hline      | linha horizontal entre linhas                               |
| \newline    | começar nova linha dentro de uma célula                     |
| \cline{i-j} | linha parcial horizontal da coluna i à coluna j             |

Temos aqui um exemplo:

    :::latex
    \begin{tabular}{|r|c|l|}
    \hline
    & col 1 & col 2 \\
    \hline
    row 1 & entry A1 & entry B1 \\
    row 2 & entry A2 & entry B2 \\
    \hline
    \end{tabular}

![table2](https://i.imgur.com/bHeKySc.png)

#### Tamanhos fixos

    :::latex
    \begin{table}\centering
      \begin{tabular}{ | m{5em} | m{1cm}| m{1cm} | } 
         \hline
         cell1 dummy text dummy text dummy text& cell2 & cell3 \\    
         \hline
         cell1 dummy text dummy text dummy text & cell5 & cell6 \\ 
         \hline
         cell7 & cell8 & cell9 \\ 
         \hline
         \end{tabular}
    \end{table}

![table33](https://i.imgur.com/9tyPT7H.png)

Primeiro, para usar estes parâmetros é necessário ter no **preamble** o *package array*.

    :::latex
    \usepackage{array}

Na *tabular*, o parâmetro ***m{5em}*** coloca a primeira coluna com um tamanho de 5em e centra o texto no meio da célula.

### Posição

Para colocar a tabela num certo sítio da página, o environment ***table*** recebe um parâmtro que explicita como a colocar. Eis um exemplo:

    :::latex
    \begin{table}[h!]
      \centering
      \begin{tabular}{||c c c||} 
        \hline
        Col1 & Col2 & Col2  \\ [0.5ex] 
        \hline\hline
        1 & 6 & 87837  \\ 
        2 & 7 & 78  \\
        3 & 88 & 788 \\ [1ex] 
        \hline
      \end{tabular}
    \end{table}
![table4](https://i.imgur.com/CNGIrcD.png)

Este exemplo também mostra linhas duplas e espaço entre 2 linhas.

O parâmetro adicional `*\[h!\]*` determina a posição da tabela no local do código. Em baixo está uma tabela com as várias opções disponíveis:

| Parâmetro | Position                                                                                                         |
| --------- | ---------------------------------------------------------------------------------------------------------------- |
| h         | Coloca a imagem, aqui (here), i.e., aproximadamente no local onde está o código fonte                               |
| t         | Coloca no topo da página.                                                                                        |
| b         | Coloca em baixo da página.                                                                                       |
| p         | Coloca numa página especial só para imagens e outros floats.                                                     |
| !         | Sobrepõem-se ao parâmetro do LaTeX que consideram um "bom" local.                                                |
| H         | Coloca no local específico onde está o código. Necessita do `*\usepackage{float}*`. É equivalente a usar h!. |

No exemplo acima, o comando `\centering` centra a imagem; por defeito, é alinhada à esquerda.


### Juntar/Merge colunas e linhas

É possível juntar colunas, usando o comando 
`\multicolumn`, e linhas, com o comando `**multirow**`.

#### Colunas

    :::latex
    \begin{tabular}{ |p{3cm}||p{2cm}|p{2cm}|p{2cm}|  }
     \hline
     \multicolumn{4}{|c|}{Country List} \\
     \hline
     Afghanistan   & AF    &AFG&   004\\
     \hline
     Aland Islands&   AX  & ALA   &248\\
     Albania &AL & ALB&  008\\
     \hline
    \end{tabular}

![table5](https://i.imgur.com/QJsNQ2Y.png)

Vemos os vários parâmetros do comando `\multicolumn\{4\}\{|c|\}\{Country List\}` :

- \{4\}
O número de colunas em conjunto, neste caso 4.
- \{|c|\}
Delimitadores e alinhamento da célula juntos, neste caso centrada e com linha vertical.
- \{Country List\}
Texto a ser mostrado na célula.

#### Linhas:

Para combinar linhas, é necessário o `**package multirow**` no **preamble** 
    :::latex
    \usepackage{multirow}

Exemplo:

    :::latex
    \begin{table}\centering
      \begin{tabular}{ |c|c|c|c| } 
        \hline
        col1 & col2 & col3 \\
        \hline
        \multirow{3}{4em}{Multiple row} & cell2 & cell3 \\ 
        & cell5 & cell6 \\ 
        & cell8 & cell9 \\ 
        \hline
      \end{tabular}
    \end{table}

![table6](https://i.imgur.com/SnGaG0G.png)

O comando **multirow** recebe 3 parâmetros:

- **\{3\}: 1º** - nº de linhas a juntar
- **\{4em\}: 2º** - largura da coluna; 4em por exemplo. Caso seja o tamanho da coluna inicialmente declarada, colocar \{!\}
- **\{Multiple row\}: 3º** - conteúdo da célula

### Tabelas de múltiplas páginas

Para inserir tabelas muito grandes que ocupam mais de uma página do documento, é necessário usar o `**longtable package**` ao **preamble**.
    :::latex
    \usepackage{longtable}

Ver [link](https://www.overleaf.com/learn/latex/Tables#Multi-page_tables) do Overleaf para exemplo.

De seguida, referimos alguns dos comandos e o seu significado (que também aparece no link):

| Comando | Significado |
| -------- | -------- |
|\endfirsthead|Everything above this command will appear at the beginning of the table, in the first page.
|\endhead|Whatever you put before this command and below endfirsthead will be displayed at the top of the table in every page except the first one.
|\endfoot|Similar to \endhead, what you put after \endhead and before this command will appear at the bottom of the table in every page except the last one.
|\endlastfoot|Similar to endfisthead. The elements after \endfoot and before this command will be displayed at the bottom of the table but only in the last page where the table appears.

### Formatar, Estilo

Não se irá entrar em detalhe sobre como mudar a grossura das linhas, a cor das
células, etc., mas aqui
[link](https://www.overleaf.com/learn/latex/Tables#Changing_the_appearance_of_a_table)
pode ver-se como fazê-lo.

### Tabelas ao lado de texto

Para colocar uma tabela no meio do texto, é necessário primeiro colocar no **preamble** o seguinte package:

    :::latex
    \usepackage{wrapfig}

E agora é possível usar o `environment wraptable`, que recebe dois parâmetros:

1. Um para alinhar o bloco da tabela, que pode assumir l, r, c, i ou o, para esquerda, direita, centro, inner e outer, respetivamente.
2. Um para a largura do bloco com a tabela, relembrando que não é a mesma coisa que o tamanho da própria tabela.

Exemplo:

    :::latex
    Praesent in sapien. Lorem ipsum dolor sit amet, consectetuer 
    adipiscing elit. 
    
    \begin{wraptable}{r}{10em}
      \centering
      \begin{tabular}{ |c|c|  }
         \hline
         Country Name &   \\
         \hline
         Albania    &AL  \\
         \hline
      \end{tabular}
      \caption{Table inside a wraptable}
      \label{table:ta2}
    \end{wraptable}
    
    Praesent in sapien. Lorem ipsum dolor sit amet, consectetuer 
    adipiscing elit. Duis fringilla tristique neque. Sed interdum 
    libero ut metus. Pellentesque placerat. Nam rutrum augue a leo. 
    Morbi sed elit sit amet ante lobortis sollicitudin...
    
![table7](https://i.imgur.com/5iIPVpK.png)


## Figuras

Inserir imagens é uma das coisa mais habituais a fazer num documento.

    :::latex
    \usepackage{graphicx}
    \graphicspath{ {./images/}}
    ...
    
    \begin{figure}[<placement>]
       % figure body
       \centering
       \includegraphics[<options>]{<path to file>}
       \caption{<figure title>}
    \end{figure}

O comando **\graphicspath{ {./images/} }** diz ao LaTeX a diretoria, a pasta,
onde as imagens estão. Esta também pode ser adicionada apenas no \<path to
file\>, caso tenham imagens em diferentes pastas.


O posicionamento da figura, ***placement***, será falado melhor na próxima secção.

A legenda, ***\caption***, da imagem pode ser colocada tanto em baixo como no
topo da imagem; dependerá onde o comando aparece, antes ou depois,
respetivamente, do corpo da imagem.

No corpo da imagem, *figure body*, é normalmente usado o `includegraphics
environment`. As opções ***options*** é uma lista que contém informação sobre
a figura: 

| options |                      |
| ------- | -------------------- |
| angle   | rotating angle (CCW) |
| scale   | scaling factor       |
| width   | width of image       |
| height  | height of image      |

<div class="alert alert-warning">
Não esquecer de colocar o tipo de ficheiro .png, .pdf, .jpg, .jpeg, etc.
Não esquecer de colocar no <b>preamble</b> o package associado \usepackage{graphicx}
</div>

### Tamanho da imagem

Existem algumas macros em LaTeX para especificar quantidades do documento, para posteriormente usar no tamanho da imagem. As mais úteis são:

- **\pagewidth** largura da página, incluindo margens;
- **\textwidth** largura da corpo de texto; 
- **\linewidth** largura do parágrafo atual do código, e.g. se tivermos em 2 colunas será o tamanho de uma coluna - `*recomendado*`.

Eis um exemplo para colocar uma imagem centrada com o tamanho de matade de página, usando `width=0.5\textwidth`:

    :::latex
    \begin{figure}[!htb]
      \centering
      \includegraphics[width=0.5\textwidth]{./images/IST_Logo.png}
      \caption{Logo do IST!}
    \end{figure}

Existem outros comandos para escalar a imagem em relação ao tamanho real da imagem: `*\includegraphics\[scale=1.5\]{./images/IST_Logo.png}*`



- includegraphics: para importar imagens, ajustar tamanho.
- begin{figure}: para criar numeração, legenda e referência.

### Posição

Para colocar a imagem num certo sítio da página, o environment ***figure*** recebe um parâmetro para esse efeito. Eis um exemplo:

    :::latex
    In the next example the figure will be positioned 
    right below this sentence.
    
    \begin{figure}[h]
       \includegraphics[width=8cm]{Plot}
       \centering
    \end{figure

O parâmetro adicional `*\[h\]*` determina a posição da figura no local do código. Em baixo está uma tabela com as várias opções dispoívies:

| Parâmetro | Position                                                                                                         |
| --------- | ---------------------------------------------------------------------------------------------------------------- |
| h         | Coloca a imagem, aqui (here), i.e., aproximadamente no local onde está o código fonte                               |
| t         | Coloca no topo da página.                                                                                        |
| b         | Coloca em baixo da página.                                                                                       |
| p         | Coloca numa página especial só para imagens e outros floats.                                                     |
| !         | Sobrepõem-se ao parâmetro do LaTeX que consideram um "bom" local.                                                |
| H         | Coloca na local específico onde está o código. Necessita do `*\usepackage{float}*`. É equivalente a usar h!. |

No exemplo acima, o comando `\centering` centra a imagem; por defeito é alinhada à esquerda.


### Wrap Images - Texto ao lado de imagem

Também é possível colocar imagens ao lado de texto, para caso de figuras pequenas.
O `**package wrapfig**` é o que fornece as ferramentas para tal. Exemplo:


    :::latex
    Praesent in sapien. Lorem ipsum dolor sit amet, consectetuer 
    adipiscing elit. Duis fringilla tristique neque. Sed interdum 
    libero ut metus. Pellentesque placerat.
    
    \begin{wrapfigure}{l}{0.25\textwidth}
    \includegraphics[width=0.9\linewidth]{overleaf-logo} 
    \caption{Caption1}
    \label{fig:wrapfig}
    \end{wrapfigure}
    
    Praesent in sapien. Lorem ipsum dolor sit amet, consectetuer 
    adipiscing elit. Duis fringilla tristique neque. Sed interdum

![fig](https://i.imgur.com/Jvg6GxP.png)

Primeiro, importar o pacote, adicionando ao **preamble** o seguinte:

    :::latex
    \usepackage{wrapfig}

Agora definimos um environment de wrapfigure com o comando `\begin{wrapfigure}{l}{0.25\textwidth} \\end{wrapfigure}`. Notamos que este aceita 2 argumentos dentro dos parêntesis \{ \}. Expliquemos o que cada um significa:

- {l}:
Definie o alinhamento da figura. Pode ser definido como **l, r, c, i ou o**, que significam esquerda, direita, centro, inner e outer. Estes últimos dois costumam ser usados em two-sided documents, e.g., livros.

- {0.25\textwidth}
Define a largura da caixa da figura, não necessariamente a imagem em si; se quisermos tal, mudar no comando *\includegraphics* para o espaço alocado à imagem no meio do texto. Unidades habituais de usar: cm, in, mm, etc.

###  Várias imagens numa figura

É ainda possível colocar mais que uma imagem numa só imagem, cada uma delas tendo a sua referência. Eis um exemplo:

    :::latex
    Praesent in sapien. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Duis fringilla tristique neque...
    
    \begin{figure}[H]
    
      \begin{subfigure}{0.5\textwidth}
        \includegraphics[width=0.9\linewidth, height=6cm]  {overleaf-logo} 
        \caption{Caption1}
        \label{fig:subim1}
      \end{subfigure}
      \begin{subfigure}{0.5\textwidth}
        \includegraphics[width=0.9\linewidth, height=6cm]{mesh}
        \caption{Caption 2}
        \label{fig:subim2}
      \end{subfigure}
    
      \caption{Caption for this figure with two images}
      \label{fig:image2}
    \end{figure}
    
    Praesent blandit blandit mauris. Praesent lectus tellus, aliquet aliquam, 
    luctus a, egestas a, turpis. Mauris lacinia lorem sit amet ipsum. 
    Nunc quis urna dictum turpis accumsan semper.

![fig2](https://i.imgur.com/US9i6vf.png)

Primeiro, importar o pacote, adicionando ao **preamble** o seguinte:

    :::latex
    \usepackage{subcaption}

O environment `*\subfigure*` pede só um parâmetro, que corresponde à largura da
figura. Este environment tem de ser usado dentro da **figure environment**.
Tanto a legenda como a label podem ser definidas para cada subfigura.


### Legendas aos lados

Podemos ainda colocar figuras com a legenda de lado. O `**package sidecap**` tem as ferramentas para tal.

    :::latex
    \usepackage[rightcaption]{sidecap}

    ...
    
    \begin{SCfigure}[0.5][h]
    \caption{Using again the picture of the universe.
    This caption will be on the right}
    \includegraphics[width=0.6\textwidth]{universe}
    \end{SCfigure}

![fig3](https://i.imgur.com/5Tu5OG9.png)

Temos dois novos comandos:

- **\usepackage\[rightcaption\]{sidecap}**
Importa-se o pacote sidecap. Com o parâmetro adicional `rightcaption`,
estabelece-se a posição da legenda à direita da imagem (também é possível usar
`leftcaption`). Para livros, outercaption e innercaption também estão
disponíveis.
- **\begin{SCfigure}\[0.5\][h] \\end{SCfigure}**
É um environment parecido com o *figure*. O `primeiro parâmetro` representa a
**largura da legenda** relativamente ao tamanho da imagem declarado no
*\includegraphics*. O `segundo parãmetro` funciona de forma exatamente igual à
**posição da figura** como no *figure environment*. Ver a secção de
Posicionamento para mais informações.


## Definir novos Environments

Pode-se ainda criar novos environments que dêem jeito. Para tal usa-se o comando ***\newenvironment*** no *Preamble*:

    :::latex
    % ------ Preable:
    \newenvironment{boxed}
        {\begin{center}
        \begin{tabular}{|p{0.9\textwidth}|}
        \hline\\
        }
        { 
        \\\\\hline
        \end{tabular} 
        \end{center}
        }
	    
    %--------------------------------------------------
    
    Below this line a boxed environment is used
    
    \begin{boxed}
    This is the text formatted by the boxed environment
    \end{boxed}
    
    This text is again outside the environment

![env](https://i.imgur.com/lNr8fU2.png)

Neste exemplo temos a criação de um environment que desenha uma caixa à volta de texto.

A seguir ao *\newenvironment* temos o nome do novo environment, **boxed**. Por
baixo temos outros **dois** parentêsis. O **1º** coloca o código antes do
texto, e o **2º** tem dentro o que aparece depois do texto.


Finalmente ainda é possível criar environments que recebem argumentos e muito
mais. Segue-se um
**[link](https://www.overleaf.com/learn/latex/Environments#Defining_a_new_environment)**
com mais informação sobre tal.

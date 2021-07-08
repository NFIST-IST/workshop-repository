Title: Parte 4
Author: NFIST
Slug: latex4
Category: Workshop LaTeX
Date:13
Series: Workshop LaTeX
Series_index: 4
Summary: 
Tags: LaTeX, Documentos

# XIII. Paper Layout

## Abstract

Em documentos científicos, é costume colocar um breve resumo do documento. em LaTeX, o `abstract environment` serve para isso. Eis um exemplo:

    :::latex
    \hrule
    \begin{abstract}
    This is a simple paragraph at the beginning of the document.
    A brief introduction to the main subject.
    \end{abstract}
    \hrule\vspace{5mm}
    
    This is the document

![abstract](https://i.imgur.com/Xa2PIWZ.png)


Outra forma para colocar o Abstract será:

    :::latex
    % Preamble
    \usepackage{abstract}
    \setlength{\absleftindent}{4mm}
    \setlength{\absrightindent}{4mm}
    \setlength{\abstitleskip}{-4mm}
    ...
    
    \hrule\begin{abstract}
      % text
    \end{abstract}
    \hrule\vspace{5mm}

Pode-se personalizar alguns dos espaços do Abstract no **preamble**.


## Documento em colunas

Para criar um documento de duas colunas, basta colocar um parâmetro na *document class*: `\twocolumn`.

Para maior flexibilidade, podemos simplesmente criar um *article* com múltiplas
colunas. O package `multicol` fornece os comandos para isso. Eis um exemplo:

    :::latex
    \documentclass{article}
    \usepackage{blindtext}
    \usepackage{multicol}
    
    \begin{document}
    
    \begin{multicols}{3}
    [
    \section{First Section}
    All human things are subject to decay. And when fate summons, Monarchs must obey.
    ]
    \blindtext\blindtext
    \end{multicols}
    
    \end{document}

![column](https://i.imgur.com/AxYmdc3.png)

Primeiro, importar o seguinte package no *preamble*: `\usepackage{multicol}`

Agora, podemos usar o environment `multicols`, que recebe como argumento o
**número de colunas**, 3 neste caso. Eventualmente, pode receber um segundo
argumento para inserir um texto antes das colunas no topo, tal como no exemplo.

O texto das colunas insere-se dentro do ` \begin{multicols}` e `\end{multicols}`.

### Separador de colunas

Para colocar um separador entre as colunas, basta definir o `\columnsep` com um certo tamanho no **preamble**

    :::latex
    \setlength{\columnsep}{1cm}
    

- **\columnbreak**: Este comando insere uma quebra de coluna em causa.

Segue-se o [link](https://ftp.eq.uc.pt/software/TeX/macros/latex/required/tools/multicol.pdf) para a documentação do package multicol.
	
## Índice - Table of Content

Não iremos entrar em detalhe sobre a construção do Índice, dado não ser muito
utilizado em relatórios, mas este
[link](https://www.overleaf.com/learn/latex/Table_of_contents) redireciona para
o site do Overleaf que explica o procedimento.

---

# XIV. Label Cross-References

Informações retiradas do [link](https://www.overleaf.com/learn/latex/Cross_referencing_sections,_equations_and_floats) do Overleaf.

If you need to insert cross-references to numbered elements in the document,
(like equations, sections and figures) there are commands to automate it in
LATEX. This article explains how.

O comando `\label{ }` é usado para identificar um número/letra, seja uma
secção, equação ou tabela. Isto para depois ser referenciada com o comando
`\ref{ }`, ou referenciando a sua página, `\pageref{ }`.

## Secções

Exemplo:

    :::latex
    \section{Introduction} \label{introduction}
    This is an introductory paragraph with some dummy text. This section will be referenced later.
    
    \begin{figure}[h]
    \centering
    \includegraphics[width=0.3\linewidth]{overleaf-logo}
    \caption{This image will be referenced below.}
    \label{fig:leaf}
    \end{figure}
    
    You can reference images; for instance, Figure \ref{fig:leaf} shows the \textit{Overleaf} logo.
    \vspace{0.5cm}
    
    \section{Math references} \label{mathrefs}
    As mentioned in section \ref{introduction}, different elements can be referenced within a document.
    
![label](https://i.imgur.com/p4xTSca.png)

A **label** é colocada depois do código `\section`. Isto também resulta para subsections e subsubsections.

## Equações

Exemplo:

    :::latex
    section{Math references} \label{mathrefs}
    As mentioned in section \ref{introduction}, different elements can be referenced within a document.
    
    \subsection{Powers series} \label{subsection}
    
    \begin{equation} \label{eq:1}
    \sum_{i=0}^{\infty} a_i x^i
    \end{equation}
    
    Equation \ref{eq:1} is a typical power series.
    
![eq](https://i.imgur.com/IbnxULU.png)

E de igual modo para as tabelas

## Referenciar página

    :::latex
    \section{Last section}
    In subsection \ref{subsection} on page \pageref{eq:1} an example of a power series was presented.
    
![ref](https://i.imgur.com/uvBLzoy.png)

O comando **\pageref** irá inserir a página onde o elemento referenciado aparece. No exemplo, a página da equação 1 do exemplo anterior a este.

---

# XV. Bibliografia

Uma bibliografia standard usa comandos semelhantes às listas.

    :::latex
    \begin{thebibliography}{9}
      \bibitem{latexcompanion} 
      Michel Goossens, Frank Mittelbach, and Alexander Samarin. 
      \textit{The \LaTeX\ Companion}. 
      Addison-Wesley, Reading, Massachusetts, 1993.
    \end{thebibliography}
    
![bibl](https://i.imgur.com/leXc3gj.png)

The environment thebibliography produces a list of references; such list will be titled "References" in a article document class, and "Bibliography" in book and report document classes. A parameter inside braces, 9 in the example, indicates the number of entries to be added; this parameter can not be greater than 99.

To create a bibliography entry the command \bibitem is used. A parameter inside braces is set to label this entry and can later be used as identifier for this reference. After the closing brace the text with the name of the author, the book title, publisher and so on is entered.

## Citar

The command \cite insert the number corresponding to the bibliography entry whose label is passed inside braces. For example, the output of \cite{latexcompanion} is \[1\].

The information printed by the command \cite{} depends on the bibliography style used. See Bibtex bibliography styles.

    :::latex
    \section{First section}
    
    This document is an example of \texttt{thebibliography} environment using 
    in bibliography management, cited: \textit{The \LaTeX\ Companion} 
    book \cite{latexcompanion}. 
    

## Bibliografia com o Bibtex

Outra maneira de fazer uma bibliografia é usar o `BibTeX`. A bibliografia é colocada num ficheiro separado e depois importado na *main*.

    :::latex
    \bibliographystyle{unsrt}
    \bibliography{sample}
    

Este usa os seguintes comandos:

- **\bibliography{sample}**:
Importa o **ficheiro "sample.bib"** em Bibtex.

- **\bibliographystyle{unsrt}**:
Coloca um certo estilo para a bibliografia. A informação mostrada depende do estilo usado. 
Ver o [Bibtex bibliography styles](https://www.overleaf.com/learn/latex/Bibtex_bibliography_styles), que contém os vários estilos da bibliografia disponíveis no LaTeX.

## Ficheiro .bib

Como foi dito anteriormente, as referêncicas bibliográficas estão usualmente num ficheiro separado com a extensão `.bib`. Este ficheiro consiste numa lista das referências, em que cada um tem as informações relativas à entrada. Exemplo de um artigo:

    :::latex
    @article{einstein,
        author =       "Albert Einstein",
        title =        "{Zur Elektrodynamik bewegter K{\"o}rper}. ({German})
            [{On} the electrodynamics of moving bodies]",
        journal =      "Annalen der Physik",
        volume =       "322",
        number =       "10",
        pages =        "891--921",
        year =         "1905",
        DOI =          "http://dx.doi.org/10.1002/andp.19053221004"
    }
    
Este ficheiro tem a informção sobre um certo elemento, que primeiro é definido por:

- @article{...}:
Descreve o **tipo de referência** bibliográfica. O *BibTeX* sabe o tipo de informação que recebe e dispõe-na de acordo com as normas associadas. Neste caso, será um artigo - mostrar-se-á o autor, o título, etc. do artigo. Ver o [link](https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex#Reference_guide) para mais estilos.
- einstein:
É o label para a referência que é identificada. Sempre que se quer citar no documento esta referência bibliográfica, usa-se este nome.
- author = "Albert Einstein",
O autor do artigo é uma das muitas informações que pode ser colocada na entradao. Existem muitas mais informações, separadas entre vírgulas com a seguinte sintaxe: key = value. Ver o [link](https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex#Reference_guide) para mais possibilidades de informações que ultilizadas, e este [link](https://www.overleaf.com/learn/latex/Bibliography_management_with_biblatex#Reference_guide) para uma lista mais detalhada.


Existem vários sites na internet que criam as entradas descritas com base num url ou o nome do artigo ou livro em causa.


## XVI. Bibliografia com o Biblatex

Finalmente, outra maneira de fazer uma bibliografia é usar o `Biblatex`. Eis um exemplo simples de como o fazer:

    :::latex
    \usepackage{biblatex}
    \addbibresource{sample.bib}
    
    \begin{document}
    Lets cite! The Einsteins journal paper \cite{einstein} and the Dirac's 
    book \cite{dirac} are physics related items. 
    
    \printbibliography
    
    \end{document}
    
![bibtex](https://i.imgur.com/sLn64Vb.png)

Com os seguintes comandos:

- **\usepackage{biblatex}**
Para importar o `package biblatex`.
- **\addbibresource{sample.bib}**
**Importar o ficheiro bibtex**, sample.bib, com as referências que contêm as informações de cada referência. Ver secção anterior sobre este ficheiro.
- **\cite{einstein}**
Este comando insere a citação da referência no documento - \[1\], neste caso, que corresponde ao elemento bibliográfico "einstein".
- \printbibliography
Imprime a lista de citações referenciadas, com o título "References" ou "Referências", dependendo da língua usada.

O Overleaf fornece uma série de templates com diferentes estilos de bibliografia. Ver exemplo neste [link](https://www.overleaf.com/latex/templates/tagged/bibliography).


### Package Biblatex

Muitos parâmetros podem ser colocados ao importar o pacote biblatex. Eis um exemplo:

    :::latex
    \usepackage[
    backend=biber,
    style=alphabetic,
    sorting=ynt
    ]{biblatex}
    \addbibresource{sample.bib}
    ...
    
    \begin{document}
    
    \maketitle
    
    Using \texttt{biblatex} you can display bibliography divided into sections, 
    depending of citation type. 
    ...
    Knuth's items \cite{knuth-fa,knuth-acp} are dedicated to programming. 
    
    \medskip
    
    \printbibliography
    
    \end{document}
    
![biber](https://i.imgur.com/DIf8qpt.png)
Segue-se o significado de cada parâmetro:
- **backend=biber**:
Define o *backend* para ordenar a bibliografia, **biber** é o padrão recomendado, mas pode-se mudar para bibtex.
- **style=alphabetic**
Define o estilo da bibliografia e das citações; neste caso está *alphabetic*, mas podemos colocar *numeric*, que é mais usual. Mais estilos estão disponíveis. Ver [bibliography styles](https://www.overleaf.com/learn/latex/Bibtex_bibliography_styles) e [citation styles](https://www.overleaf.com/learn/latex/Natbib_citation_styles) para mais informações sobre estilos e citações, respetivamente.
- **sorting=ynt**
Determinar o ordenamento de informações, neste caso ordenadar por ano, nome e título; *none* também é usual usar. Ver a lista de possibilidade no seguinte [link](https://www.overleaf.com/learn/latex/Bibliography_management_with_biblatex#Reference_guide)


### Personalizar Bibliografia

Não iremos entrar em detalhe, mas deixamos um [link](https://www.overleaf.com/learn/latex/Bibliography_management_with_biblatex#Customizing_the_bibliography) do Overleaf que pode ajudar.


## Exemplo 

    :::latex
    \usepackage{csquotes}
    \usepackage[
    backend=biber,
    % style=alphabetic,
    style=numeric,
    sorting=none
    ]{biblatex}
    
    \addbibresource{Bibliography.bib}
    ...
    
    \printbibliography
    
    
---


# XVII. Macros e Helpers

## Comandos

Até aqui usámos vários comandos definidos pelo LaTeX ou por packages. Veremos agora como criar os nossos próprios comandos.

Novos comandos são definidos por `\newcommand`. Vejamos um exemplo simples:

    :::latex
    \newcommand{\R}{\mathbb{R}}
    ...
    
    The set of real numbers are usually represented 
    by a blackboard bold capital r: \( \R \).
    
![command](https://i.imgur.com/doUJrki.png)

O código recebe 2 parâmetros:

- **\R**: Este será o nome do novo comando. Isto de modo a declará-lo no meio do texto.
- **\mathbb{R}**: Isto é o que o novo comando faz. Neste caso, escreve os números reais $\mathbb{R}$ (comando *\mathbb* necessita do *package amssymb*).


Também é possível criar **comando com parâmetros**. Eis um exemplo:

    :::latex
    \newcommand{\bb}[1]{\mathbb{#1}}
    
    Other numerical systems have similar notations. 
    The complex numbers \( \bb{C} \), the rational 
    numbers \( \bb{Q} \) and the integer numbers \( \bb{Z} \).
    

Na linha ==\newcommand{\bb}\[1\]{\mathbb{#1}}== define o comando anterior, mas desta vez recebe um argumento que será o texto a colocar em modo *\mathbb{}* 
- **\[1\]**: número de prâmetros a receber.
- **\mathbb{#1}**: Este comando referencia o parâmetro 1 - irá substituir o texto que recebe em 1º lugar no lugar do #1. Estes podem ir até 9 parâmetros, #1, #2, etc.

Também é possível criar comandos com parâmetros opcionais. Exemplo:

    :::latex
    \newcommand{\plusbinomial}[3][2]{(#2 + #3)^#1}
    
    To save some time when writing too many expressions 
    with exponents is by defining a new command to make simpler:
    
    \[ \plusbinomial{x}{y} \]
    
    And even the exponent can be changed
    
    \[ \plusbinomial[4]{y}{y} \]
    
![command2](https://i.imgur.com/wgjHUke.png)

Expliquemos a sintaxe da linha ==\newcommand{\plusbinomial}\[3\]\[2\]{(#2 + #3)^#1}==

- **\plusbinomial**: Nome do novo comando
- **\[3\]**: número de parâmetros, no caso de receber os parâmetros adicionais.
- **\[2\]**: Este é o valor padrão para o primeiro parâmetro, que será opcional. Neste caso, temos 1 parâmetro opcional, que será logo o primeiro, o #1. 
- **(#2 + #3)^#1**: É o que o comando faz. Neste caso, coloca um 2 no parãmetro 1 caso nao seja colocado nada dentro dos parênteses retos. Os parâmetros opcionais vêm sempre primeiro, antes dos obrigatórios.
- \newcomand: como criar e utilidade

Também podemos definir ou mudar comandos existentes, usando o código `\renewcommand`. Eis um exemplo:

    :::latex
    \renewcommand{\S}{\mathbb{S}}
    
    The Riemann sphere (the complex numbers plus $\infty$) is 
    sometimes represented by \( \S \)
    
![command3](https://i.imgur.com/b5Lzfxf.png)

Neste exemplo, o comando \S, $\S$, é reescrito para escrever um *blackboard bold* S, $\mathbb{S}$.

`\renewcommand` usa a mesma sintaxe do `\newcommand`, definida anteriormente.

## Tratar Erros

- Erros acontecem. Quando acontecerem, ter o mesmo "mindset" de programação - tentar fazer um debug das linhas de código que originaram o erro. Em LaTeX, os típicos **erros a vermelho** que se têm são falta de parênteses e erros ortográficos nos comandos, entre outros.
- Alguns **erros a amarelo** não são muito relevantes e não há muito problema em deixá-los, mas devemos evitá-los. Repeticões de label e falta de referenciação são exemplos destes erros.
- Quanto aos **erros a azul**, normalmente ocorrem por falta de espaço e sobreposição de *floats*; não são preocupantes.

Em casos graves, ir ao histórico e reaver o último documento que esteja bem:
![erros](https://i.imgur.com/rTvbxxa.png)

Também é possível comparar várias versões do documento para ver as modificações que ocorreram, muitas das vezes para encontrar erros:
![erros2](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/3/3d/History-compare-view.gif)


## Spread-LaTeX

Este é uma `extensão, add-on,` para converter tabelas de excel no [Google Spreadsheet](https://docs.google.com/spreadsheets/) para tabela de LaTeX e vice versa. Isto porque *it's a pain in the ass* para fazer estar transições.

- [Spread-LaTeX Link](https://workspace.google.com/marketplace/app/spreadlatex/218144906748)


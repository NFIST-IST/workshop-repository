Title: Workshop LaTeX
Author: NFIST
Slug: latex1
Category: Workshop LaTeX
Date:13
Series: Workshop LaTeX
Series_index: 1
Summary: \LaTeX
Tags: LaTeX, Documentos

# WorkShop de LaTeX (Overleaf) - página 1


# I. LaTeX/Overleaf

## LaTeX *vs* Word

![xkcd](https://i.imgur.com/cpt0Jks.png)

À primeira vista, pode parecer mais complicado do que o típico Word, mas
torna-se mais natural e até fácil de usar, especialmente quando são comuns
fórmulas complexas e física mais avançada, o que não é tão "palavreado",
tornando o Word mais complicado. O LaTeX, sendo criado por cientistas, torna o
documento de um físico com melhor aspeto e fácil de usar. 

Assim, o LaTeX irá permitir uma maior flexibilidade e foco no conteúdo ao
escrever relatórios, papers, entre outros. Não são precisas preocupações com a
aparência - o LaTeX trata disso automaticamente com os templates default.


## Web Application - Overleaf

- Permite colaborar e comunicar com outras pessoas em equipa rapidamente e sem problemas.
- Permite salvar e recuperar facilmente versões antigas do LaTeX.
- Permite compilar o LaTeX automaticamente, mostrando logo os resultados.

<div class="alert alert-info">
 Devem tentar colocar o código à medida que mostramos para treinar!
</div>

### 1º Documento no Overleaf
- Um novo documento é criado em `New Project`. Estão disponíveis vários
 *templates*. Pode também fazer-se o *upload* de um projeto anterior, em
 formato zip.
- Escolhendo a opção **Blank Project**, é automaticamente criado um ficheiro
 **main.text**, onde vamos desenvolver o documento. Para compilar o que
 escrevemos, seleciona-se `Recompile`, atualizando-se o ficheiro em formato
 pdf.
- Na ferramenta à direita de `Recompile`, podemos ler os avisos de erro e fazer
 o *download* de vários ficheiros correspondentes ao projeto. Mais à direita,
 extrai-se diretamente o documento em formato pdf.
- A partilha do projeto, útil para edição comum, faz-se em `Share`. Em
 `History` podemos aceder às versões anteriores do projeto e fazer o seu
 *download*.


---

# II. Estrutura/Sintaxe

Primeiramente, comecemos por criar um novo documento dos mais simples:

    :::latex
    \documentclass[12pt]{article}
    \begin{document}
    Hello World! % o contéudo fica dentro do document ...
    \end{document}

Todos os documentos começam com o commando `\documentclass`, sendo que o que
aparece dentro de `\{ \}` é o tipo de documento (colocar *beamer* para
apresentações, por exemplo) e `\[ \]` é o argumento opcional, neste caso para
dizer o tamanho das letras. Os argumentos de um comando serão melhor explicados
nas packages. Mas os argumentos típicos na `documentclass` serão o tamanho de
letra e o tipo de folha: a4paper, twocolumn, etc.

Escrever o texto simples é igual ao que se faz no Word. Resta ver os comandos,
blocos e environments integrados no meio do texto para descrever a estrutura
que se pretende e como deve aparecer.

Há quatro tipos fundamentais de escrita/estrutura em LaTeX no Overleaf:


| Objeto | Função              |
|:------:|---------------------|
| \      | Comando e parâmetros|
| %      | Comentário          |
| $      | Modo matemático     |
| ---    | Blocos e Environment|

---

# III. Typesetting 1

!Tal como referimos antes, o texto estará dentro do `\\begin{document}` e `\\end{document}`.


Tal como no Word, é possível editar o texto, seja o estilo, a fonte, o tamanho
da letra ou os espaços entre linhas. Estes não são mais difíceis de mudar em
LaTeX, apenas é preciso habituação.

Relembrar que quando aparecem erros, devemos tentar resolvê-los e nao deixar
acumular, excepto se forem os a azul e a amarelo, continuando a tentar
evitá-los!

[basics-exercise-1.tex](https://www.overleaf.com/docs?snip\_uri=https://raw.github.com/jdleesmiller/latex-course/master/en/basics-exercise-1.tex\&splash=none)



## Estilo de letra - Comandos

- Negrito, Itálico, código:

Os Estilos normalmente vêm em variadíssimas formas e tamanhos, tal como
*itálico* ou **negrito**. Em seguida, temos uma lista de todos os comandos
habitualmente usados e que estão disponíveis sem acesso a outras packages.

![Tabela dos diferentes Estilos Disponíveis](https://i.imgur.com/HFirmei.png)

O próprio Overleaf dá uma lista mais pequena de consulta:
[Link para o Overleaf](https://pt.overleaf.com/learn/latex/Font_sizes,_families,_and_styles#Font_styles)

- HotKeys do Overleaf:

Existe uma série de hotkeys, a.k.a. atalhos para escrever no Overleaf. Por
exemplo, uns dos mais comuns são colocar em bold: `Ctrl+B`, colocar linhas
selecionadas em comentário `Ctrl+/`, entre outros. Para aceder, ir ao menu no
topo superior esquerdo, e no final aparece, "Show Hotkeys":

<img align="center" src="https://i.imgur.com/YlRbfAp.png" width="500">

---


# IV. Modo Matemática

## Inline Equations

O `$` serve para iniciar o modo Matemática no meio do texto. Não esquecer: os
`$`'s vêm sempre em pares — um para começar e outro para acabar. Muitas das
vezes, os erros aparecem por não se fechar o modo Matemática ou por falta
deles.

    :::latex
    In physics, the mass-energy equivalence is stated by the equation $E=mc^2$, discovered in 1905 by Albert Einstein.

Existem outras maneiras de introduzir modo Matemática no meio do texto: `\( \)`,
`$ $` ou `\\begin{math} \\end{math}`. Todos estes fazem o mesmo, depende do gosto
pessoal.


## Display equations:

Também podemos colocar equações numeradas e não numeradas sem ser no meio do
texto. Para o fazer, normalmente usam-se os seguintes comandos: `\[ \]`,
`\\begin{displaymath} \\end{displaymath}` or `\\begin{equation} \\end{equation}`:

    :::latex
    The mass-energy equivalence is described by the famous equation

    \[E=mc^2\]

    discovered in 1905 by Albert Einstein. 
    In natural units ($c$ = 1), the formula expresses the identity

    \begin{equation}
    E=m
    \end{equation}

![einstein_example](https://i.imgur.com/uUaipGK.png)

Dentro dos Environments, existem diferentes tipos, melhor explicados no seu
tópico. No modo Matemática, para colocar equações grandes na sua própria linha,
sem ser no meio do texto: 

- **equation** e **equation***:  Para colocar uma equação numerada e centrada ou não numerada;
- **align** e **align***: Para colocar várias equações em várias linhas
 seguidas, mas alinhadas de um certo modo, por exemplo, tudo a seguir ao =;
- **gather** e **gather***: Para colocar várias equações em várias linhas
 seguidas, todas centradas, e todas numeradas ou nenhuma.

No site do Overleaf, há estes comandos e outros para situações mais
específicas, neste
[link](https://www.overleaf.com/learn/latex/Aligning_equations_with_amsmath).

<div class="alert alert-warning">
Neste tipo de Environment, é necessário colocar uma package externa que é
habitualmente usada para equações; consultar o artigo
<a href=https://www.overleaf.com/learn/latex/Aligning_equations_with_amsmath>amsmath</a>.
</div>

## Espaçamento no modo Matemática

É de referir que o modo Matemática ignora os espaços colocados no meio do
código. Ele reconhece todos os carateres como uma única palavra. Para colocar
espaço entre símbolos, existe uma lista de comandos para vários tamanhos de
espaço disponível: 

Spaces in mathematical mode:

    :::latex 
    \begin{align*}
    f(x) &= x^2\! +3x\! +2 \\
    f(x) &= x^2+3x+2 \\
    f(x) &= x^2\, +3x\, +2 \\
    f(x) &= x^2\: +3x\: +2 \\
    f(x) &= x^2\; +3x\; +2 \\
    f(x) &= x^2\ +3x\ +2 \\
    f(x) &= x^2\quad +3x\quad +2 \\
    f(x) &= x^2\qquad +3x\qquad +2
    \end{align*}

\begin{align*}
f(x) &= x^2\! +3x\! +2 \\
f(x) &= x^2+3x+2 \\
f(x) &= x^2\, +3x\, +2 \\
f(x) &= x^2\: +3x\: +2 \\
f(x) &= x^2\; +3x\; +2 \\
f(x) &= x^2\ +3x\ +2 \\
f(x) &= x^2\quad +3x\quad +2 \\
f(x) &= x^2\qquad +3x\qquad +2
\end{align*}


Em termos de tamanho específico:

| LaTeX code | Description                                    |
|:---------- | ---------------------------------------------- |
| \quad      | space equal to the current font size (= 18 mu) |
| \\,        | 3/18 of \quad (= 3 mu)                         |
| \\:        | 4/18 of \quad (= 4 mu)                         |
| \\;        | 5/18 of \quad (= 5 mu)                         |
| \\!        | -3/18 of \quad (= -3 mu)                       |
| \          | equivalent of space in normal text             |
| \qquad     | twice of \quad (= 36 mu)                       |


## Notação e Lista de Símbolos:

- Usar o caráter `^` para sobrescrito e `_` para subescrito. Usar \{ \} para colocar mais do que uma letra em sub/sobrescrito.
- Para colocar letras gregas e outra notação comum, como frações e raiz
quadrada, são usados comandos, normalmente intuitivos, como `\sqrt{}` para
raiz quadrada. Pesquisar na internet o comando matemático/físico necessário
costuma resultar. Na subseção seguinte disponibilizaremos links para essas
listas.
- A **[package physics](http://mirrors.ibiblio.org/CTAN/macros/latex/contrib/physics/physics.pdf)**
 contém muitos comandos usados para escrever fórmulas físicas.

<div class="alert alert-success">
De qualquer das formas, apresentamos uma lista de muitos comandos habitualmente
usados pelo
<a href=https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols> link</a>
do Overleaf ou deste
<a href=https://en.wikibooks.org/wiki/LaTeX/Mathematics#List_of_mathematical_symbols> site</a>
</div>

Por fim, este é um link para uma lista de artigos do Overleaf com vários
aspetos não mencionados aqui que eventualmetne poderão dar jeito:
[link](https://www.overleaf.com/learn/latex/Mathematical_expressions#Further_Reading)



---

# V. Parágrafos e Indentações

Muitas das informações podem ser vistas no seguinte [link](https://www.overleaf.com/learn/latex/Paragraph_formatting)

## Começar um novo parágrafo
Para começar um novo parágrfo em LaTeX, aquele tem de ter uma linha em branco entre linhas. 

    :::latex
    This is the text in first paragraph.

    This is the text in second paragraph. 

Outra maneira é escrevendo um `\par` quando for nencessário fazer um parágrafo, não sendo necessária a linha extra:

    :::latex
    This is the text in first paragraph. \par
    This is the text in second paragraph. 

## Indentação e Espaçamento entre parágrafos

Por defeito, o LaTeX identa todos os parágrafos, com a excepção do 1º parágrafo
a seguir a uma secção. Para mudar o tamanho desta indentação, é necesseário, no
**preamble**, mudar o tamanho do `\parindent`:


    :::latex
    %Tamanho da identação
    \setlength{\parindent}{4em} 
    
    %Espaço entre parágrafos
    \setlength{\parskip}{1em}

No final do código, mostramos, também, como se muda o espaço entre parágrafos, característica esta definida pelo `*\parskip*`.

Por defeito, estes tamanhos são definidos pela *document class* usada. Estes
podem ser usados no meio do texto para mudar a estrutura do texto que segue o
código, ou colocar entre `{ }` para apenas afetar essa parte do código:

    :::latex
    {\setlength{\parindent}{4em}
    \par This is the text in first paragraph.
    \par This is the text in second paragraph.
    }
    \par This is the text in third paragraph.



### Identação do 1ºParagrafo

Para contornar o facto de que o LaTeX não indenta automaticamente o 1º
parágrafo a seguir a uma secção, é necessário incluir um `package` no
**preamble**

    :::latex
    \usepackage{indentfirst}

Todos os parágrafos iniciais terão o mesmo tamanho que os outros.

### Não Identar Parágrafo

Se não se quiser indentar um certo parágrafo, basta usar o comando `\noindent`:

    :::latex
    This is the first paragraph.
    
    \noindent This is the second paragraph with no indentation.

Para ter um documento não indentado, apenas colocar no **preamble** o tamanho da indentação a zero: `\setlength{\parindent}{0pt}`


## Espaçamento entre linhas

Para controlar o espaçamento entre linhas de um parágrafo temos 3 comandos.

O comando: `\renewcommand{\baselinestretch}{1.5}` muda o espaço entre linhas 1.5 do valor padrão.

Usando *\baselineskip*, determina-se o espaço mínimo entre 2 linhas sucessivas num parágrafo. Para mudar, colocar no preamble: `\setlength{\baselineskip}{value}`

Ou ainda usando `\linespread{value}`, onde o valor é dado desta maneira:

| Value |      Line spacing      |
|:----- |:----------------------:|
| 1.0   |     single spacing     |
| 1.3   | one-and-a-half spacing |
| 1.6   |     double spacing     |

# VII. Breaks ans Spaces

Por fim, colocamos um tabela, deste
[link](https://en.wikibooks.org/wiki/LaTeX/Paragraph_Formatting), para fazer um
breve resumo dos vários tipos de parágrafos e breaks que se podem fazer no
LaTeX.

![table_format](https://i.imgur.com/YJdBmN5.png)


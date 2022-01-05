# NFIST Workshop Repository
---
This is a description of the project. The website can be opend [here](https://nfist-ist.github.io/workshop-repository/).

# Usage
---
Start by cloning the repo to a local folder

```
$ git clone https://github.com/NFIST-IST/workshop-repository.git
```

In order to use the `pelican-plugins` submodule, we need to initialize and 
recursively update it.

```
$ git submodule init 
$ git submodule update --init --recursive
```

Since we will be working with some Python libraries, it is advised to use a 
virtual environment. 
Here we used python's venv, but you can use the tool of your choosing such as pyevn or conda environments.

```
$ python -m venv ~/.envs/workshop-repository
```

Here we created it with the name `workshop-repository` in a folder inside the 
`home` directory. You can set the name and directory as you please, as long as
you don't commit the created folder to git.

After the environment is created, we need to activate it.
```
$ source ~/.envs/workshop-repository/bin/activate
```

You should now see an indication of the environment name in your terminal.
```
(workshop-repository)$
```
To leave the virtual environment simply run `deactivate`.

We can now install the necessary python libraries.
```
$ pip install pelican markdown bs4 ghp-import pelican-jupyter
```

You should now be able to make changes to the project.

## Adding and modifying content

All content should be placed inside the `content` folder. It is configured to
work with both markdown and jupyter notebooks. Each file must be accompanied 
be the respective Metadata.

For further information, please refer to the 
[Pelican Docs](https://docs.getpelican.com/en/latest/).

## Modifying the theme
The theme used for this website is based on
[pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3).

Each page is generated automatically through [Jinja](jinja.palletsprojects.com)
templates, and the `css` used can be found in the file `static/css/bootstrap.sandstone.min.css`,
inside the theme folder.

## Compiling and previewing
To compile the website and preview it locally, run

```
(workshop-repository)$ make html
(workshop-repository)$ make serve
```
You should now be able to open it at [localhost:8000](localhost:8000).

## Applying changes
After you're done with your changes, the website is now ready to publish. 
To compile the published version, run the command:
```
(workshop-repository)$ pelican content -s publishconf.py
```

You can now add and commit everything to the main branch, followed by a
push/push request.

```
(workshop-repository)$ git add .
(workshop-repository)$ git commit -m "Decription of changes made"
(workshop-repository)$ git push origin main

```
To publish the site, we will use `ghp-import` and push the changes to the 
`gh-pages` branch.

```
(workshop-repository)$ ghp-import output
(workshop-repository)$ git push origin gh-pages
```
It could take a couple of minutes for the changes to be visible in the public
website.




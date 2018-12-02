Pelican Static Web Generation
#############################


:title: Pelican Static Web Generation
:date: 2018-12-02 22:00:00
:modified: 2018-12-02 22:00:00
:tags: python, pelican, static, web
:category: Python Projects
:slug: Pelican Static Web Generation
:authors: Deepak Ramanath
:summary: A brief instruction about getting started with `Pelican <http://docs.getpelican.com/en/stable/index.html>`_, a static web generator is discussed here. `Pelican <http://docs.getpelican.com/en/stable/index.html>`_ can be then be hosted on `GitHub <https://github.com>`_ as a repository. **Pelican** content can be in many formats including the popular ones, `reStructutedText <http://docutils.sourceforge.net/rst.html>`_ or `Markdown <https://daringfireball.net/projects/markdown/>`_ which makes an ideal choice for writing articles, in particular, blog posts.

Introduction
============
In the world of static web or site generators, `jekyll <https://jekyllrb.com/>`_ and `Hugo <https://gohugo.io/>`_ are well know and is an obvious choice for many web developers who are into blogging. **Jekyll** is developed using `Ruby <https://www.ruby-lang.org/en/>`_ while **Hugo** is developed using `Go <https://golang.org/>`_ and both are open source programming languages. However, `Pelican <http://docs.getpelican.com/en/stable/index.html>`_ is relatively new and is gaining popularity due to the fact that it is developed using `Python <https://www.python.org/>`_. There are several features within **Pelican**, most notable is `jinja2 <http://jinja.pocoo.org/>`_ templating for theme creation. I will allow you to go through other features of **Pelican**.

Installation
============

As recommended by `Pelican docs <http://docs.getpelican.com/en/stable/quickstart.html>`_, **Pelican** can be installed using `pip` as given below in a terminal.

.. code-block:: bash

   sudo pip install pelican


Project building
================

It is assumed that a Linux distribution will be used here and therefore all instructions are only relevant to Linux. Firstly, it is recommended to create two repositories on `GitHub <https://github.com>`_, one for the complete source of the Pelican project and the second one for the HTML files that renders the site. Following are these two repositories mentioned

.. code-block:: html

   https://github.com/deepakramanath/pelican-site.github.io
   https://github.com/deepakramanath/pelican-site-src

Once the above repositories are created on **GitHub**, let us clone the `pelican-site-src` repository into our project directory, which would be `**pelican-project**`

.. code-block:: bash

   cd ~/

   git clone https://github.com/deepakramanath/pelican-site-src.git pelican-project
   Cloning into 'pelican-project'...
   remote: Enumerating objects: 3, done.
   remote: Counting objects: 100% (3/3), done.
   remote: Compressing objects: 100% (2/2), done.
   remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
   Unpacking objects: 100% (3/3), done.

   cd ~/pelican-project

Now, we can use `pelican quick start` to initiate a **Pelican** project. This has to be performed within the previously created `pelican-project` directory. Pelican quick start begins with asking a few questions which then sets up the necessary structure and files.

.. code-block:: python

   pelican-quickstart

   Welcome to pelican-quickstart v4.0.1.

   This script will help you create a new Pelican-based website.

   Please answer the following questions so this script can generate the files needed by Pelican.

    
   > Where do you want to create your new web site? [.] 
   > What will be the title of this web site? Pelican Website
   > Who will be the author of this web site? Deepak Ramanath
   > What will be the default language of this web site? [en] en
   > Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) y
   > What is your URL prefix? (see above example; no trailing slash) https://pelican-site.github.io
   > Do you want to enable article pagination? (Y/n) y
   > How many articles per page do you want? [10] 
   > What is your time zone? [Europe/Paris] Australia/Sydney
   > Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) y
   > Do you want to upload your website using FTP? (y/N) n
   > Do you want to upload your website using SSH? (y/N) n
   > Do you want to upload your website using Dropbox? (y/N) n
   > Do you want to upload your website using S3? (y/N) n
   > Do you want to upload your website using Rackspace Cloud Files? (y/N) n
   > Do you want to upload your website using GitHub Pages? (y/N) y
   > Is this your personal page (username.github.io)? (y/N) y
   Done. Your new project is available at /home/deepak/pelican-project


Now, the basic **Pelican** directory structure should be created successfully. Let us list the files and other directories. Assuming that we are still in the pelican-project directory

.. code-block:: bash

   ls
   content  Makefile  output  pelicanconf.py  publishconf.py  tasks.py

Before proceeding any further, the `output` directory should be disabled from getting deleted every time the web-site is built. This behaviour of **Pelican** is not necessarily bad, however, for managing via version control using git, we need the `output` directory intact. It will be apparent shortly the need for this. Open the `publishconf.py` and modify the following using a text editor such as vim and look for the line, `DELETE_OUTPUT_DIRECTORY = True`. **True** should be changed to **False**. Save the file.

.. code-block:: bash

   vim publishconf.py

   DELETE_OUTPUT_DIRECTORY = False

Let us begin by adding a sample article by creating a new file in the `content` directory. The **reStructuredText** format will be used in this example. Enter the contents as shown below and save the file.

.. code-block:: bash

   touch ~/pelican-project/content/first_article.rst
   vim ~/pelican-project/content/first_article.rst

   First Article uisng Pelican
   ###########################

   :title: First Article using Pelican
   :date: 2018-12-02 17:00:00
   :modified: 2018-12-02 17:00:00
   :tags: python, JSON, OpenWeather, API
   :category: Python Projects
   :slug: Pelican
   :authors: Deepak Ramanath
   :summary: This is a first article written using **Pelican**, a statci web generator.
   
Now that we have a sample file, we can run a few **Pelican** specific commands and view the site. These should be executed from the root diretory.

.. code-block:: bash

   cd ~/pelican-project
   make html
   Done: Processed 1 article, 0 drafts, 0 pages, 0 hidden pages and 0 draft pages in 0.09 seconds.

   make serve
   127.0.0.1 - - [02/Dec/2018 20:56:35] "GET /category/python-projects.html HTTP/1.1" 200 -
   WARNING: Unable to find `/favicon.ico` or variations:
     | /favicon.ico.html
     | /favicon.ico/index.html
     | /favicon.ico/
     | /favicon.ico

Now the site should be accessible on localhost at port 8000. Open a web browser and in the address bar type

.. code-block:: html

   http://localhost:8000

Given that your site is up and running, its time to add further articles into the content directory. Refer `Pelican Documentation <http://docs.getpelican.com/en/stable/index.html>`_ for different types of content that can be added. 

Publishing the project
======================

Once the content is added, we can make use of `publish` within Pelican so that the content is ready to be published. In the terminal, navigate to root directory

.. code-block:: bash

   cd ~/pelican-project
   make publish

At this stage, the contents of the `output` directory can be hosted on **GitHub**. In the begining of this article two github repositories were created and the source repository was cloned to the project directory. Now, we use the **git** **sub-module** to clone the output directory. But first, let us delete the **output** directory before using git sub-module to clone.

Navigate to the root directory

.. code-block:: bash

   cd ~/pelican-project
   rm -rf output

   git submodule add https://github.com/deepakramanath/pelican-site.github.io.git output
   Cloning into '~/pelican-project/output'...
   remote: Enumerating objects: 3, done.
   remote: Counting objects: 100% (3/3), done.
   remote: Compressing objects: 100% (2/2), done.
   Unpacking objects: 100% (3/3), done.
   remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0

Now that the output directory has been clone. We can regenerate the contents within the output directory.

.. code-block:: bash

   cd ~/pelican-project
   make html
   make publish

Time to commit, push and done...

This part is critical, since we have used git submodule, git tracking should occur first on the **output** directory and then the **root** directory. Remember this direction (inside to outside).

Further, ensure that **`DELETE_OUTPUT_DIRECTORY = False`** is set in the **`publishconf.py`** file.

.. code-block:: bash

   cd ~/pelican-project/output
   git add --add
   git commit -m "My fisrt post commit"
   git push -u origin master
   46 files changed, 1960 insertions(+)
   Username for 'https://github.com':
   Password for 'https://deepakramanath@github.com':
   Enumerating objects: 58, done.
   Counting objects: 100% (58/58), done.
   Delta compression using up to 8 threads
   Compressing objects: 100% (54/54), done.
   Writing objects: 100% (57/57), 131.41 KiB | 10.11 MiB/s, done.
   Total 57 (delta 13), reused 0 (delta 0)
   remote: Resolving deltas: 100% (13/13), done.
   To https://github.com/deepakramanath/pelican-site.github.io.git
   6f01234..296789d  master -> master
   Branch 'master' set up to track remote branch 'master' from 'origin'.


Similarly, the entire root directory should be commited and pushed.

.. code-block:: bash

   cd ~/pelican-project
   git add --add
   git commit -m "My fisrt source commit"
   git push -u origin master
   9 files changed, 245 insertions(+)
   Username for 'https://github.com': deepakramanath
   Password for 'https://deepakramanath@github.com':
   Enumerating objects: 12, done.
   Counting objects: 100% (12/12), done.
   Delta compression using up to 8 threads
   Compressing objects: 100% (10/10), done.
   Writing objects: 100% (11/11), 4.38 KiB | 1.46 MiB/s, done.
   Total 11 (delta 0), reused 0 (delta 0)
   To https://github.com/deepakramanath/pelican-site-src.git
   b98e161..ca21f73  master -> master
   Branch 'master' set up to track remote branch 'master' from 'origin'.

The site should now be accessible over

.. code-block:: html

   https://pelican-site.github.io/










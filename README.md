# Warning!
Before install ensure, that your locale settings was properly installed. The problem described here - https://www.digitalocean.com/community/questions/language-problem-on-ubuntu-14-04 If you have the same, put the following text into `/etc/default/locale`

```
    LANGUAGE=en_US.UTF-8
    LC_ALL=en_US.UTF-8
    LANG=en_US.UTF-8
    LC_TYPE=en_US.UTF-8
```

Then run following commands

```
#!bash

    locale-gen en_US.UTF-8
    dpkg-reconfigure locales

```

And restart session in terminal



To install system dependencies run the following commands

```
#!bash
    
    sudo apt-get update

    sudo apt-get install git-core nginx python3-dev libjpeg-dev zlib1g-dev libpng12-dev build-essential libpcre3 libpcre3-dev postgresql postgresql-contrib python-psycopg2 python python-setuptools libpq-dev

```

To prepare environment need to do the next steps

1.Clone project from git repository. For example, into `/var/www/liquidround/` directory. 


```
#!bash

  cd /var/www/ # if does'nt exist mkdir /var/www/ && cd /var/www/ 
  git clone <remote git repo path>

```

2.Instasll pip
  

```
#!bash

  easy_install pip
```

  
3.Install virtualenvwrapper. To install this package it is recommended to read the [official documentation](https://virtualenvwrapper.readthedocs.org/en/latest/install.html) first.

Shortly - 

```
#!bash


  pip install virtualenvwrapper
  echo 'export WORKON_HOME=/home/.virtualenvs' >> ~/.bashrc
  echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
  source ~/.bashrc
  
```
  
4.Create new virtual environment and install requirements
  
```
#!bash


  cd /var/www/liquidround-website/
  
  mkvirtualenv liquidround_env -a . --python=/usr/bin/python3
  
  workon liquidround_env
  
  pip install -r liquidround/requirements.txt
  
```

5.Create database and user.
  First run `psql`
  
```
#!bash


  sudo -u postgres psql
  
```

  Then run following
  
  
```
#!SQL
  
  CREATE DATABASE liquidround;
  
  CREATE USER root WITH password '1111';
  
  GRANT ALL privileges ON DATABASE liquidround TO root;
  
  GRANT ALL privileges ON DATABASE liquidround TO root;
  
```

  
  Exit from psql with ctrl+D
  And migrate
  
  
```
#!bash

  python liquidround/manage.py migrate
  
```

  Also, you can create superuser
  

```
#!bash

  python liquidround/manage.py createsuperuser
```

  
6.You must setup your webserver. The configuration files examples you can find in `conf/` directory.
  
  - First, change the files to suit your work environment
  
  - Then create a symlink in `/etc/nginx/sites-enabled/` to your nginx project config in `/<project path>/conf/nginx/<config file>`
  

```
#!bash

  cd /etc/nginx/sites-enabled/
  
  sudo ln -s /var/www/liquidround-website/conf/nginx.conf liquidround
  
  cd /var/www/liquidround-website/
  
```

  
  
  - Setup upstart init script
  
  
```
#!bash


  cd /etc/init/
  
  sudo ln -s /var/www/liquidround-website/conf/upstart.conf liquidround.conf
  
  cd /var/www/liquidround-website/
  
```

  - Then update server configuration and reload nginx
  
  
```
#!bash

  initctl reload-configuration
  
  sudo service nginx restart
  
```


------


Now the project is running
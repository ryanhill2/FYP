FROM python:3.7

# Install everything that you need exept libraries specific to your Django project - these come later.
RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y --no-install-recommends --no-install-suggests install libgdal-dev nginx supervisor

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt
# add (the rest of) our code
COPY . /usr/src/app

# Set up all the configfiles
COPY nginx.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

# Expose the image's ports. We'll bind different host ports to these later
EXPOSE 80
EXPOSE 443

# When a new container is created, we'll run supervisord to start uwsgi and nginx.
CMD ["supervisord", "-n"]
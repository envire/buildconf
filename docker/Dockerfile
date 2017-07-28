FROM ubuntu:16.04

LABEL maintainer="Alexander.Fabisch@dfki.de"

RUN apt-get update
RUN apt-get install -y sudo wget ruby ruby-dev git

# We install EnviRe with autoproj
# We have to configure git, otherwise we will get an error during autoproj
# installation!
RUN git config --global user.email docker.user@example.com
RUN git config --global user.name Docker
RUN mkdir -p /opt/envire/.autoproj
ADD config.yml /opt/envire/.autoproj
WORKDIR /opt/envire
RUN wget --quiet http://rock-robotics.org/autoproj_bootstrap
ENV AUTOPROJ_BOOTSTRAP_IGNORE_NONEMPTY_DIR 1
RUN ruby autoproj_bootstrap git https://github.com/envire/buildconf.git branch=minimalInstall
RUN bash -c "source env.sh && aup"
RUN bash -c "source env.sh && amake"

ADD .bashrc /root/.bashrc

# For GUIs:
ENV DISPLAY ":0"
ENV QT_X11_NO_MITSHM "1"

ENTRYPOINT ["bash"]

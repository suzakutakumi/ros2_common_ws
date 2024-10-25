FROM ros:foxy

RUN apt update

RUN apt install ros-foxy-rqt* -y
RUN apt install ros-foxy-turtlesim -y

RUN apt install nano curl -y
RUN apt install wget -y

RUN touch /root/.bashrc
RUN echo "umask 0000" >> /root/.bashrc
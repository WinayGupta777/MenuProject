FROM centos

RUN yum install python3 -y
RUN yum install net-tools -y
RUN yum install ncurses -y
RUN pip3 install scikit-learn
RUN pip3 install gdown
RUN gdown https://drive.google.com/uc?id=1V1v0xPot5n35zHJkihwIfFk67GK0zlcT
RUN gdown https://drive.google.com/uc?id=1-np1b01PNoHXtX2eKwDHEN2b9FOooc67
RUN gdown https://drive.google.com/uc?id=1xt3ePWF0GKZWsJWh9BzVNyTZADhMOSPu


ENTRYPOINT [ "python3", "MLcode.py" ]

CMD ["1"]
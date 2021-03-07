FROM python:3.6

ENV PATH="/app/scripts:${PATH}"


WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./scripts /app/scripts

RUN chmod +x /app/scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

USER user

CMD ["entrypoint.sh"]
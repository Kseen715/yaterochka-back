# YaTёrochka-back
<p align="center">
  <img src="https://raw.githubusercontent.com/Kseen715/imgs/main/favicon.ico" />
</p>

## Description
This is backend part of YaTёrochka project. It's a web application written as a course work for the 3rd year of study at the university. 

The project is a web application for a fictional company that sells random goods. The application allows you to view the catalog of goods, view the history of orders, and also allows you to log in to your Admin account.

Backend written in Django framework.

## Usage
Docker-compose:
```
version: '3'
services:
  yaterochka-back:
    image: kseen/yaterochka-back:latest
    container_name: yaterochka-back
    ports:
      - '8000:8000'
    restart: unless-stopped
    environment:
      - NAME=<database name>
      - HOST=<database container name or host>
      - PORT=<database port>
      - PASSWORD=<database password>
      - USER=<database user>
```

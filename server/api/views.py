from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.cache import cache

import socket
import threading

# Create your views here.

games = {"21": "game fun"}
connections = {"21": None}

def sock_create_game():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    s.bind(("192.168.1.38", 1234))
    s.listen()

    client_socket, client_address = s.accept()

    client_socket.send(bytes("connected.\n", "utf-8"))

def create_game(request: HttpRequest):

    thread = threading.Thread(target=sock_create_game)

    thread.start()


    return HttpResponse("Hello")

def join_game(request, **kwargs):

    if kwargs["id"] in games:
        print(games[kwargs["id"]])

    games

    return HttpResponse("Hello")

# From flask import Flask
# from werkzeug.datastructures import CombinedMultiDict 


# @app.route('/success')
# def success():
#   return "success"
# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(name)
#     return "hello "+name
# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id
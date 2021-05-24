# from flask import Flask, render_template
# from werkzeug.datastructures import CombinedMultiDict  # Import Flask to allow us to create our app.
# app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
#                          # directly, or importing it as a module.
# print(__name__) 
#          # Just for fun, print __name__ to see what it is
# @app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
#                          # function to the '/' route. This means that whenever we send a request to
#                          # localhost:5000/ we will run the following "hello_world" function.


# def tresbox():
#     return render_template("tresbox.html")
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response.

# # #localhost5000  
# # # def Dojo():
# # #     return 'Dojo' #server will return Dojo

# # # def Hi_Flask():
# # #     return 'Hi Flask' #it will reeturn Hi Flask

# # # def Hi_Michael():
# # #     return 'Hi Michael' #this will return Hi Michael

# # # def Hi_John():
# # #     return 'Hi John' #this will return Hi John

# # # def hello():
# # #     return "hello" #should say hello 35 times

# def dogs():
#     return "dogs"



# # # @app.route('/success')
# # # def success():
# # #     print("hello Sucess!")
# # #     return "sucess"

# # # @app.route('/hello/name') #for a route '/hello/'____' anything after the '/hello/' gets passed 
# # # def hello(name):
# # #     print(name)
# # #     return "hello"+name

# if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
#                            # it from a different module
#     app.run(debug=True)    # Run the app in debug mode.





# # # User()


# # # class User:
# # #     def run():
# # #         # run code
# # # # user.get_mile()
# # # # user1.run()

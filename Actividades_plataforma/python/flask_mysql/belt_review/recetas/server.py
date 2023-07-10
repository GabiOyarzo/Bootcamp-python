from server_app import app

from server_app.control import users,recipes

if __name__=="__main__":
    app.run(debug=True)
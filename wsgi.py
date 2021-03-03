from services.app import home

application = home()

if __name__ == "__main__":
    application.run(debug=True, host='127.0.0.1', port=2000)

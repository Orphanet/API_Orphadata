import swagger_server.API_main as swagger_app

application = swagger_app.main()


if __name__ == '__main__':
    application.run(debug=True)
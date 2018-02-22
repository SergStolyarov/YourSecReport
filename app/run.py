if __name__ == '__main__':
    app.secret_key = 'key'
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    load_database()
    

    app.run()

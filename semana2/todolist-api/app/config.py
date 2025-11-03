class Config:
    SECRET_KEY = "customsecretkey"
    # Query database connection string
    SQLALCHEMY_DATABASE_URI = "mysql://root:password@127.0.0.1:3306/codigo_15_flask"
    SQLALCHEMY_TRACKS_MODIFICATIONS = False

    # JWT configuration
    JWT_SECRET_KEY = "customjwtsecretkey"

from connexion.resolver import RestyResolver 
import connexion

if __name__ == '__main__':
    app = connexion.App('__name__', 9090, specification_dir='swagger/')
    app.add_api('my_supper_app.yaml', resolver=RestyResolver('api'))
    app.run()


from flask import Flask
from flask_graphql import GraphQLView
import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, argument):
        return 'Hello ' + argument


schema = graphene.Schema(query=Query)

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


@app.route("/")
def hello():
    return "Hello World"


if __name__ == '__main__':
    app.run()

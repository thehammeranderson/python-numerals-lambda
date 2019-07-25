from aws_cdk import (
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    core,
)


class LambdaNumeralsStack(core.Stack):
    def __init__(self, app: core.App, id: str) -> None:
        super().__init__(app, id)

        lambdaFn = lambda_.Function(
            self, "NumeralConverterHandler",
            code=lambda_.Code.asset('lambda'),
            handler="numeral-converter.main",
            timeout=core.Duration.seconds(300),
            runtime=lambda_.Runtime.PYTHON_3_7,
        )

        api = apigateway.LambdaRestApi(
            self, "lambdaNumerals", handler=lambdaFn, proxy=False,)

        items = api.root.add_resource('numerals')
        item = items.add_resource('{numerals+}')
        item.add_method('GET')

app = core.App()
LambdaNumeralsStack(app, "LambdaNumerals")
app.synth()

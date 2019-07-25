from aws_cdk import (
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    aws_ec2 as ec2,
    core,
)

class LambdaNumeralsStack(core.Stack):
    def __init__(self, app: core.App, id: str) -> None:
        super().__init__(app, id)

        vpc = ec2.Vpc(self, "NumeralsVpc")

        lambdaFn = lambda_.Function(
            self, "NumeralConverterHandler",
            code=lambda_.Code.asset('lambda'),
            handler="numeral-converter.main",
            timeout=core.Duration.seconds(300),
            runtime=lambda_.Runtime.PYTHON_3_7,
            vpc=vpc,
        )

        api = apigateway.LambdaRestApi(
            self, "lambdaNumerals", handler=lambdaFn, proxy=False,)

        items = api.root.add_resource('numerals')
        item = items.add_resource('{numerals+}')
        item.add_method('GET')

app = core.App()
stack = LambdaNumeralsStack(app, "LambdaNumerals")
stack.node.apply_aspect(core.Tag('Owner','Gregg Anderson'))
app.synth()

import json

numeralMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def main(event, context):
    return calculateNumeral(event['pathParameters']['numerals'])
    
def calculateNumeral(numeral):
    response = validate(numeral)
    
    if response['statusCode'] != 200:
        return response

    sum = 0
    pos = 0
    while pos < len(numeral):
        numeralChar = numeral[pos]

        if pos + 1 < len(numeral) and numeralMap[numeralChar] < numeralMap[numeral[pos + 1]]:

            if sum != 0 and sum < numeralMap[numeral[pos + 1]]:
                return respond(400, "invalid roman numeral.  numeral characters must decrease in value except when subractor characters are being used (i.e. IIIV is invalid and should be written as VIII)")
            thisDigit = numeralMap[numeral[pos + 1]] - numeralMap[numeralChar]
            sum += thisDigit
            pos += 1
        else:
            thisDigit = numeralMap[numeral[pos]]
            sum += thisDigit

        pos += 1

    return respond(200,sum)

def validate(numeral):
    upTimes = 0

    for pos in range(len(numeral)):
        numeralChar = numeral[pos]

        if numeralChar not in numeralMap:
            return respond(400, "invalid character input " + numeralChar)

        if pos + 1 < len(numeral):
            if numeralMap[numeralChar] < numeralMap[numeral[pos + 1]]:
                if numeralChar in ['I', 'X', 'C']:
                    upTimes += 1
                    if upTimes > 1:
                        return respond(400, "invalid roman numeral.  numeral characters can increase in value one time when preceeded by a subractor numeral (ie. IV)")
                else:
                    return respond(400, "invalid subtractor character.  can only subtract using I, X, or C")
            elif upTimes == 1 and numeralChar == numeral[pos + 1]:
                return respond(400, "invalid roman numeral. same numeral character cannot follow a subractor sequence of that numeral character (ie. IVV should be VIV or IXX should be XIX)")
            else:
                upTimes = 0
    return respond(200, "OK")

def respond(code, message):
    return {
        "statusCode": code,
        "body": message
    }
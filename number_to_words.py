def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def convert(num):
    unit_digits = (
        "", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ",
        "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens_digits = ("", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety ")

    if num < 0:
        return "minus " + convert(-num)

    if num < 20:
        return unit_digits[num]

    if num < 100:
        return tens_digits[num // 10] + unit_digits[int(num % 10)]

    if num < 1000:
        if num % 100 == 0:
            return unit_digits[num // 100] + "hundred " + convert(int(num % 100))
        else:
            return unit_digits[num // 100] + "hundred and " + convert(int(num % 100))

    if num < 100000:
        return convert(num // 1000) + "thousand " + convert(int(num % 1000))

    if num < 10000000:
        return convert(num // 100000) + "Lakh " + convert(int(num % 100000))

    if num > 10000000:
        return ""


def numberToWord(submitted_number):
    print ("Conversion to word for given Currency Value of Rs." + str(submitted_number) + " is")
    if isNumber(submitted_number):
        numbers = str(submitted_number).split('.')
        result = convert(int(numbers[0]));
        if result != "":
            if len(numbers) > 1:
                result = "Rs. " + result + "" + str(int(numbers[1])) + "/100 only"
            else:
                result =  "Rs. " + result + "only"
        else:
            result = "number out of range"
    else:
        result = "string must be number"

    print(result+" \n\n")
    return result

if __name__ == "__main__":
    submitted_number = input("The conversion of given Currency Value in to word : ")
    numberToWord(submitted_number)



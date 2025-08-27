def phone(question, min, max):
    error = f'Please enter a valid phone number between {8} and {10} numbers long'

    while True:

        try:

            response = input(question)

            if response.isdigit() and min <= len(response) <= max:
                return response
            elif len(response) > max:
                print("Sorry, That isn't a legal phone number")
                print(error)
            elif len(response) < min:
                print("Sorry, That isn't a legal phone number")
                print(error)
            else:
                print(error)

        except ValueError:
            print(error)
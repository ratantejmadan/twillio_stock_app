from main import program_masterbase, numbers


def add_user(number):
    # new_user = User(number)
    program_masterbase[number] = {'Day': [], 'Week': [], 'Month': [],
                                    'Quarter': [], 'Year': [], 'Forever': []}
    # numbers.append(new_user.number)

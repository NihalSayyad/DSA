def check_vow(string, vowels):
    final = [i for i in string if i in vowels]
    print(len(final))
    print(final)

string = "Geeks for Geeks"
vowels = "AaEeIiOoUu"
check_vow(string, vowels)
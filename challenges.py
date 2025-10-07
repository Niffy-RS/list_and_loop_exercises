def add_chocolate(shopping_list: list):
    """My housemate is a real health-nut, but I like chocolate. This function 
    adds the string "chocolate" to any list it receives, and returns the 
    modified list. That way our shopping list is always correct.

    Arguments:
        - shopping_list: a list of strings

    Returns:
        - the same list, with the string "chocolate" added to the end
    """
    shopping_list.append("chocolate")
    return shopping_list

def lou_bega(lyrics_list: list):
    """This function accepts a list of strings and adds the words 
    "A little bit of " to the front of each.
    
    Arguments:
        - lyrics_list: a list of strings
    
    Returns:
        - the same list, but each string now has "A little bit of " 
        prepended to it.

    Example input: 
        [
            "Monica in my life", 
            "Erica by my side", 
            "Rita's all I need"
        ]
        
    Example output: 
        [
            "A little bit of Monica in my life", 
            "A little bit of Erica by my side", 
            "A little bit of Rita's all I need"
        ]
    """
    # 1. Make a list to put our stuff in
    new_lyric_list = []
    # 2. Going over everything in our original list
    for lyric in lyrics_list:
        # 3. Do some stuff to it
        new_lyric = f"A little bit of {lyric}"
        # 4. Add the result of some stuff to our list in step 1
        new_lyric_list.append(new_lyric)
    # 5. Return our list with stuff done to it
    return new_lyric_list

def assemble_guest_list():
    """This function repeatedly prompts the user for the name of a dinner guest.
    Each string the user supplies is added to a list. If/when the user hits 
    "Enter" without typing anything, the function stops asking and 
    returns the list.
    
    Arguments: None!
    
    Returns:
        - a list of strings supplied by the user
    """
    # 1. Make a list for our names
    names = []
    # 2. Ask for the names
    name = input("What's the guests name? ")
    # 3. Until the user enters nothing
    while name != "":
        # 4. Add name to list
        names.append(name)
        # 5. Ask for a name again
        name = input("What's the guests name? ")
        # 6. Return the list of names
    return names


def is_prime(some_number: int): # A bit trickier!
    """This function tests to see if the input is a prime number.
    Whenever a prime number is divided by an integer larger than 1 and smaller
    than itself, the result includes a remainder.

    NOTE: The lowest prime number is 2. 1 and 0 are not prime.
    
    Arguments:
        - some_number: an integer to be tested for prime-ness

    Returns:
        - a boolean representing whether or not some_number is prime
    """

    # 1. If our input is 1 or 0, return false
    if some_number < 2:
        return False
    # 2. Get our devisors and iterate over them
    for i in range(2, some_number):
        # 3. If there's no remainder, we've found a divisor
        if some_number % i == 0:
            return False
    # 4. If we get here without any other divisors - this is prime
    return True


    
    # Hint: 
    #   int(1.5) == 1.0


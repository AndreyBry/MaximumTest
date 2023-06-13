def palindrome(s):
    """
    Полученная на входе строка переворачивается и сравнивается с исходной,
    если они равны, то возвращается True, иначе - False
    :param s: str
    :return: True or False
    """
    return True if s == s[::-1] else False


print(palindrome('лепсспел'))
print(palindrome('helloworld'))

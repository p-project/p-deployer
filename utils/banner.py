def banner(color, bullet, string):
    return '\n   {color} {bullet} \033[0m\033[0;30;47m {string} \033[0m\n'.format(color=color, bullet=bullet, string=string)


def info(string):
    return banner('\033[1;37;44m', '•', string)


def success(string):
    return banner('\033[1;37;42m', '✓', string)


def error(string):
    return banner('\033[1;37;41m', '✗', string)

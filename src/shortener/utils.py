import random
import string

def code_generator(size=7, chars='abcdefghijklmnopqrstuvwxyz'):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=7):
    new_code = code_generator(size=size)
    SClass = instance.__class__
    qs_exists = SClass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
from .models import Contact, Category
from random import choice, choices
from string import digits


def gen_contacts(n: int) -> None:
    """Generates random contacts for testing purposes

    Args:
        n (int): Number of contacts to generate.
    """
    
    names = [
        'Felipe',
        'Thiago',
        'Pedro',
        'Mayara',
        'Iasmin',
        'Yasmin',
        'João',
        'Michael',
        'Igor',
        'Otavio',
        'Luis',
        'John',
        'Maria',
        'Sam',
        'Dean',
        'Robert',
        'Amanda',
        'Nathalia',
        'Lais',
    ]
    
    surnames = [
        'Almeida',
        'Azevedo',
        'Braga',
        'Barros',
        'Campos',
        'Cardoso',
        'Castro',
        'Fontes',
        'Serra',
        'Smith',
        'Jones',
        'Brown',
        'Miller',
        'Davis',
        'Wilson',
        'Taylor',
        'Clark',
        'Harris',
        'Lewis',
        'Lopez',
        'Baker',
    ]
    
    domains = [
        'hotmail.com',
        'gmail.com',
        'yahoo.com',
        'aluno.ufabc.edu.br',
        'harvard.edu',
    ]
    
    categories = Category.objects.all()
    
    for i in range(n):
        name = choice(names)
        surname = choice(surnames)
        category = choice(categories)
        domain = choice(domains)
        phone = ''.join(choices(digits, k = 13))
        email = f'{name.lower()}.{surname.lower()}@{domain}'
        
        Contact.objects.create(name=name, surname=surname, phone=phone, email=email, category=category)
        
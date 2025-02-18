from faker import Faker

fake = Faker()

print("Fake Name:", fake.name())
print("Fake Address:", fake.address())
print("Random Number:", fake.random_int(min=1, max=100))

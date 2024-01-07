class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class StringManipulation:
    def reverse_string(self, text):
        return text[::-1]

    def capitalize_string(self, text):
        return text.capitalize()

    def is_palindrome(self, text):
        return text == text[::-1].lower()


class UserInputValidation:
    def __init__(self):
        pass

    def validate_username(self, username):
        # Verificăm dacă numele de utilizator respectă anumite criterii (de exemplu, să conțină doar litere și cifre)
        if username.isalnum() and len(username) >= 4 and len(username) <= 20:
            return True
        else:
            return False

    def validate_password(self, password):
        # Verificăm dacă parola respectă anumite criterii (de exemplu, să aibă o lungime între 6 și 20 de caractere)
        if len(password) >= 6 and len(password) <= 20:
            return True
        else:
            return False


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]
        else:
            raise ValueError("Item not found in cart")

    def get_item_quantity(self, item):
        return self.items.get(item, 0)


class UserAuthentication:
    def __init__(self):
        self.users = {
            "user1": "password1",
            "user2": "password2"
        }

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False


class OnlineShopping:
    def __init__(self):
        self.shopping_cart = ShoppingCart()
        self.user_auth = UserAuthentication()

    def add_item_to_cart(self, item, quantity=1):
        self.shopping_cart.add_item(item, quantity)

    def remove_item_from_cart(self, item, quantity=1):
        self.shopping_cart.remove_item(item, quantity)

    def calculate_total_price(self):
        # Simulăm calculul total al prețului în coșul de cumpărături
        # Acesta poate fi un calcul complex bazat pe prețurile produselor, cantități etc.
        # În acest exemplu simplu, vom presupune că prețul fiecărui produs este 10 lei
        total_items = sum(self.shopping_cart.items.values())
        total_price = total_items * 10  # Prețul fiecărui produs este 10 lei

        return total_price

    def validate_user_login(self, username, password):
        return self.user_auth.login(username, password)


class DatabaseInteraction:
    def __init__(self):
        # Simulăm o bază de date cu utilizatori și produse
        self.users = {
            "user1": {"password": "pass1", "email": "user1@example.com"},
            "user2": {"password": "pass2", "email": "user2@example.com"}
        }

        self.products = {
            "Apple": {"price": 10, "stock": 100},
            "Orange": {"price": 8, "stock": 50},
            "Banana": {"price": 12, "stock": 75}
        }

    def get_user_info(self, username):
        return self.users.get(username)

    def get_product_info(self, product_name):
        return self.products.get(product_name)

    def update_product_stock(self, product_name, new_stock):
        if product_name in self.products:
            self.products[product_name]["stock"] = new_stock
        else:
            raise ValueError("Product not found in database")


class BillingSystem:
    def __init__(self):
        self.invoice = {}  # Dicționar pentru a stoca elementele facturii

    def add_item_to_invoice(self, item, price):
        # Adăugăm un element nou în factură
        if item in self.invoice:
            self.invoice[item] += price
        else:
            self.invoice[item] = price

    def remove_item_from_invoice(self, item):
        # Ștergem un element din factură
        if item in self.invoice:
            self.invoice.pop(item)  # Elimină complet cheia și valoarea asociată din dicționar
        else:
            raise ValueError("Item not found in invoice")

    def calculate_total(self):
        # Calculăm totalul facturii
        total = 0
        for item, price in self.invoice.items():
            total += price
        return total

    def apply_discount(self, discount_percentage):
        # Aplicăm o reducere la totalul facturii
        discount_factor = 1 - (discount_percentage / 100)
        for item in self.invoice:
            self.invoice[item] *= discount_factor

    def apply_tax(self, tax_percentage):
        # Aplicăm o taxă la totalul facturii
        tax_factor = 1 + (tax_percentage / 100)
        for item in self.invoice:
            self.invoice[item] *= tax_factor


class UserManagement:
    def __init__(self):
        self.users = {}

    def register_user(self, username, email):
        # Înregistrăm un utilizator
        self.users[username] = {"email": email}

    def remove_user(self, username):
        # Ștergem un utilizator
        if username in self.users:
            del self.users[username]
        else:
            raise ValueError("User not found")

    def get_user_email(self, username):
        # Obținem adresa de email a unui utilizator
        return self.users.get(username, {}).get("email", None)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def update_price(self, new_price):
        self.price=new_price


class OrderManagement:
    def __init__(self, user_manager, billing_system):
        self.user_manager = user_manager
        self.billing_system = billing_system
        self.orders = {}

    def place_order(self, username, products_list):
        # Plasăm o comandă pentru un utilizator
        if self.user_manager.get_user_email(username):
            self.orders[username] = products_list
        else:
            raise ValueError("User not found")

    def get_order(self, username):
        # Obținem comanda unui utilizator
        if username in self.orders:
            return self.orders[username]
        else:
            raise ValueError("Order not found")

    def cancel_order(self, username):
        # Anulăm comanda unui utilizator
        if username in self.orders:
            del self.orders[username]
        else:
            raise ValueError("Order not found")

    def process_payment(self, username):
        # Procesăm plata pentru o comandă a unui utilizator
        order = self.get_order(username) 
        total_price = sum(product.get_price() for product in order)
        self.billing_system.add_item_to_invoice(f"Order_{username}", total_price)
        return total_price



# Teste pentru clasa Calculator
def test_calculator():
    calc = Calculator()

    assert calc.add(3, 5) == 8
    assert calc.subtract(10, 4) == 6
    assert calc.multiply(2, 3) == 6
    assert calc.divide(8, 2) == 4

    try:
        calc.divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

    print("Teste pentru Calculator au trecut cu succes!")


# Teste pentru clasa StringManipulation
def test_string_manipulation():
    string_manipulator = StringManipulation()

    assert string_manipulator.reverse_string("hello") == "olleh"
    assert string_manipulator.capitalize_string("python") == "Python"
    assert string_manipulator.is_palindrome("racecar") is True
    assert string_manipulator.is_palindrome("hello") is False

    print("Teste pentru StringManipulation au trecut cu succes!")

# Teste pentru clasa UserInputValidation
def test_user_input_validation():
    input_validation = UserInputValidation()

    # Teste pentru validarea numelui de utilizator
    assert input_validation.validate_username("user123") is True
    assert input_validation.validate_username("usr") is False
    assert input_validation.validate_username("username_with_long_character_limit") is False

    # Teste pentru validarea parolei
    assert input_validation.validate_password("password123") is True
    assert input_validation.validate_password("pass") is False
    assert input_validation.validate_password("password_with_long_character_limit") is False

    print("Teste pentru UserInputValidation au trecut cu succes!")

# Teste pentru clasa ShoppingCart
def test_shopping_cart():
    cart = ShoppingCart()

    cart.add_item("Apple", 3)
    cart.add_item("Orange", 5)
    cart.add_item("Apple")  # Adaugă un alt măr

    assert cart.get_item_quantity("Apple") == 4
    assert cart.get_item_quantity("Orange") == 5

    cart.remove_item("Orange", 2)
    assert cart.get_item_quantity("Orange") == 3

    try:
        cart.remove_item("Banana")  # Încearcă să șteargă un element care nu există în coș
    except ValueError as e:
        assert str(e) == "Item not found in cart"

    print("Teste pentru ShoppingCart au trecut cu succes!")


# Teste pentru clasa UserAuthentication
def test_user_authentication():
    user_auth = UserAuthentication()

    assert user_auth.login("user1", "password1") is True
    assert user_auth.login("user2", "password2") is True
    assert user_auth.login("user3", "password3") is False

    print("Teste pentru UserAuthentication au trecut cu succes!")

# Testare interacțiunea cu clasa OnlineShopping
def test_online_shopping():
    online_shop = OnlineShopping()

    online_shop.add_item_to_cart("Apple", 3)
    online_shop.add_item_to_cart("Orange", 5)

    assert online_shop.calculate_total_price() == 80  # Totalul este de 80 lei (8 produse * 10 lei/produs)

    assert online_shop.validate_user_login("user1", "password1") is True
    assert online_shop.validate_user_login("user3", "password3") is False

    print("Teste pentru OnlineShopping au trecut cu succes!")


# Teste pentru clasa DatabaseInteraction
def test_database_interaction():
    db_interaction = DatabaseInteraction()

    # Teste pentru obținerea informațiilor despre utilizatori
    assert db_interaction.get_user_info("user1") == {"password": "pass1", "email": "user1@example.com"}
    assert db_interaction.get_user_info("user3") is None

    # Teste pentru obținerea informațiilor despre produse
    assert db_interaction.get_product_info("Apple") == {"price": 10, "stock": 100}
    assert db_interaction.get_product_info("Grapes") is None

    # Teste pentru actualizarea stocului produselor
    db_interaction.update_product_stock("Apple", 80)
    assert db_interaction.get_product_info("Apple")["stock"] == 80

    try:
        db_interaction.update_product_stock("Mango", 60)  # Încearcă să actualizezi un produs inexistent
    except ValueError as e:
        assert str(e) == "Product not found in database"

    print("Teste pentru DatabaseInteraction au trecut cu succes!")

# Teste pentru clasa BillingSystem
def test_billing_system():
    billing = BillingSystem()

    # Adăugăm elemente în factură
    billing.add_item_to_invoice("Product A", 50)
    billing.add_item_to_invoice("Product B", 75)

    # Verificăm totalul inițial al facturii
    assert billing.calculate_total() == 125

    # Aplicăm o reducere de 10%
    billing.apply_discount(10)
    assert billing.calculate_total() == 112.5  # 10% reducere aplicată la total

    # Aplicăm o taxă de 5%
    billing.apply_tax(5)
    assert billing.calculate_total() == 118.125  # 5% taxă aplicată la totalul cu reducere

    # Ștergem un element din factură
    billing.remove_item_from_invoice("Product B")
    assert billing.calculate_total() == 47.25  # Doar Product A rămâne în factură - cu noua valoare de dupa operatiile aplicate

    print("Teste pentru BillingSystem au trecut cu succes!")


def test_user_management():
    user_manager = UserManagement()

    # Teste pentru înregistrarea și obținerea adresei de email a unui utilizator
    user_manager.register_user("User1", "user1@example.com")
    assert user_manager.get_user_email("User1") == "user1@example.com"

    # Teste pentru ștergerea unui utilizator
    user_manager.remove_user("User1")
    assert user_manager.get_user_email("User1") is None

    print("Teste pentru UserManagement au trecut cu succes!")


# Teste pentru clasa OrderManagement folosind BillingSystem
def test_order_management_with_billing():
    user_manager = UserManagement()
    user_manager.register_user("User1", "user1@example.com")

    billing_system = BillingSystem()
    order_manager = OrderManagement(user_manager, billing_system)

    # Teste pentru plasarea comenzii și procesarea plății
    prod_a = Product('ProductA',100)
    prod_b = Product('ProductB',200)
    order_manager.place_order("User1", [prod_a, prod_b])
    assert order_manager.process_payment("User1") == 300  

    print("Teste pentru OrderManagement cu BillingSystem au trecut cu succes!")


# Rularea testelor
test_calculator()
test_string_manipulation()
test_user_input_validation()
test_shopping_cart()
test_user_authentication()
test_online_shopping()
test_database_interaction()
test_billing_system()
test_user_management()
test_order_management_with_billing()

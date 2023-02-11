# Define a Client class to store client information
class Client:
    def __init__(self, name, surname, position, email, company, linkedin):
        self.name = name
        self.surname = surname
        self.position = position
        self.email = email
        self.company = company
        self.linkedin = linkedin
        self.payment_potential = 0

    # Method to calculate payment potential based on company size and position
    def calculate_payment_potential(self):
        # Dummy calculation for payment potential
        company_size_factor = 1
        position_factor = 1
        if self.company.size > 1000:
            company_size_factor = 1.5
        if self.position.upper() == "CEO" or self.position.upper() == "CFO":
            position_factor = 2
        self.payment_potential = company_size_factor * position_factor

    # Method to display client information
    def display_client_info(self):
        print("Name: ", self.name, self.surname)
        print("Position: ", self.position)
        print("Email: ", self.email)
        print("Company: ", self.company.name)
        print("LinkedIn: ", self.linkedin)
        print("Payment Potential: ", self.payment_potential)

# Define a Company class to store company information
class Company:
    def __init__(self, name, size):
        self.name = name
        self.size = size

# Create a list of clients
clients = [
    Client("John", "Doe", "CEO", "john.doe@company.com", Company("ACME Inc.", 5000), "https://linkedin.com/john-doe"),
    Client("Jane", "Doe", "CFO", "jane.doe@company.com", Company("XYZ Corp.", 2000), "https://linkedin.com/jane-doe"),
    Client("John", "Smith", "Manager", "john.smith@company.com", Company("ABC Inc.", 1000), "https://linkedin.com/john-smith"),
    Client("Jane", "Smith", "Manager", "jane.smith@company.com", Company("PQR Ltd.", 500), "https://linkedin.com/jane-smith"),
]

# Calculate payment potential for each client
for client in clients:
    client.calculate_payment_potential()

# Sort clients based on payment potential
clients.sort(key=lambda x: x.payment_potential, reverse=True)

# Display information for the top three clients with the largest payment potential
print("Top Three Clients with the Largest Payment Potential:")
for i in range(3):
    clients[i].display_client_info()
    print("\n")

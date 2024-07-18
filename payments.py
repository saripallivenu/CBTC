# Importing the required classes from the reportlab.pdfgen module
from reportlab.pdfgen import canvas
# Importing the colors module to add colors to the text
from reportlab.lib import colors
# Importing the required classes from the reportlab.lib.pagesizes module to set page size
from reportlab.lib.pagesizes import letter
# Defining a function to create a payment receipt
def create_receipt(transaction_id, date, customer_name, items, total_amount):
    # Creating a canvas object and setting the page size to letter
    c = canvas.Canvas(f"receipt_{transaction_id}.pdf", pagesize=letter)

    # Setting the title of the receipt
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Payment Receipt")

    # Adding transaction details
    c.setFont("Helvetica", 12)
    c.drawString(50, 700, f"Transaction ID: {transaction_id}")
    c.drawString(50, 680, f"Date: {date}")
    c.drawString(50, 660, f"Customer Name: {customer_name}")

    # Adding a line separator
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.line(50, 640, 550, 640)

    # Adding the items purchased
    c.drawString(50, 620, "Items Purchased:")
    y = 600
    for item, price in items.items():
        c.drawString(50, y, f"{item}: ${price:.2f}")
        y -= 20

    # Adding a line separator before the total amount
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.line(50, y, 550, y)

    # Adding the total amount
    c.drawString(50, y - 20, f"Total Amount: ${total_amount:.2f}")

    # Adding a thank you note
    c.drawString(50, y - 60, "Thank you for your purchase!")

    # Saving the PDF
    c.save()

# Sample data to test the function
transaction_id = "123456789"
date = "2024-07-18"
customer_name = "John Doe"
items = {
    "Product 1": 29.99,
    "Product 2": 45.50,
    "Product 3": 12.75
}
total_amount = sum(items.values())

# Calling the function to create the receipt
create_receipt(transaction_id, date, customer_name, items, total_amount)

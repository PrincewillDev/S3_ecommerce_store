import enum

# Define an enumeration class for roles
class Role(enum.Enum):
    CUSTOMER = "customer"
    VENDOR = "vendor"
    ADMIN = "admin"

class OrderStatus(enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class PaymentStatus(enum.Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"

class PaymentMethod(enum.Enum):
    Paypal = "paypal"
    CREDITCARD = "creditcard"
    ANKTRANSFER = "banktransfer"
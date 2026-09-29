class InvoiceCalculator:
    def total(self, items): return sum(items)
class InvoicePrinter:
    def print(self, total): return f"Total: {total}"
calculator=InvoiceCalculator(); printer=InvoicePrinter()
print(printer.print(calculator.total([10,20,30])))
class EmailNotifier:
    def send(self,msg): return f"Email: {msg}"
class SmsNotifier:
    def send(self,msg): return f"SMS: {msg}"
def notifier(kind):
    return EmailNotifier() if kind=="email" else SmsNotifier()
print(notifier("email").send("Hello"))
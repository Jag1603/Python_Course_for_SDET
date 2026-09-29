from string import Template
message = Template("Hello $name")
print(message.substitute(name="Developer"))
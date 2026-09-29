class RequestBuilder:
    def __init__(self): self.request={}
    def method(self,m): self.request["method"]=m; return self
    def url(self,u): self.request["url"]=u; return self
    def build(self): return self.request
print(RequestBuilder().method("GET").url("/users").build())
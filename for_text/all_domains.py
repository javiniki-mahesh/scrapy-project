class Domain:
    def __init__(self, name):
        self.name = name # Domain name (e.g., "example.com")

    def com_domain(self):
        com_result = self.name[:self.name.index('.com')+4] # example.com
        return com_result
    
    def in_domain(self):
        in_result = self.name[:self.name.index('.in')+3] # example.in
        return in_result
    
    def org_domain(self):
        org_result = self.name[:self.name.index('.org')+4] # example.org
        return org_result
    
    def io_domain(self):
        io_result = self.name[:self.name.index('.io')+3] # example.io
        return io_result
    
    def ai_domain(self):
        ai_result = self.name[:self.name.index('.ai')+3] # example.ai
        return ai_result
    

    def logic_for_domains(self):
        if '.com' in self.name:
            return self.com_domain()
        elif '.in' in self.name:
            return self.in_domain()
        elif '.org' in self.name:
            return self.org_domain()
        elif '.io' in self.name:
            return self.io_domain()
        elif '.ai' in self.name:
            return self.ai_domain()

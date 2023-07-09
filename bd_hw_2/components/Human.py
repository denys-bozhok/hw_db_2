class Human:
    def __init__(self, 
                 pasport_id: str, 
                 name: str, 
                 surname: str, 
                 ref_to_auto: int):
        
        self.pasport_id = pasport_id
        self.name = name
        self.surname = surname
        self.ref_to_auto = ref_to_auto


        @property
        def get_id(self):
            return self.pasport_id
        
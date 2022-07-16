class gramatica:

    def __init__(self):
        self.l={}
        self.letras =f"[a-z]"
        self.id=f"{self.letras}*"
        self.reserved=["EN TABLA","DE TABLA","CREAR","AGREGAR","FORANEA","Tabla","CON"]
        self.simbols2=["\-","\_","[0-9]","\+","\{","\}"]
        self.simbols=["\(","\)","\;","\.","\,"]
        self.tokens=["ET","DT","CR","A","FO","T","CON","PA","PC","PUC","P","CO"]
        # self.qf = f"\{self.a,self.fo,self.pa,self.id,self.pc,self.f}"
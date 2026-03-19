def tipo_magia(fogo, agua):
    if fogo and agua:
        return "Vapor"
    
    if fogo:
        return "Fogo"
    
    if agua:
        return "Água"
    
    return "Sem magia"
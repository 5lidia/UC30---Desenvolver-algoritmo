def verificar_acesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Bloqueado"

    if usuario == "admin":
        if senha == "1234":
            return "Acesso total"
        else:
            return "Senha incorreta"

    return "Usuário inválido"
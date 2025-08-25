import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contatos"
    
    input_nome = ft.TextField(
        label="Nome",
        hint_text="Digite seu nome",   
        
    )

    input_email = ft.TextField(
        label="Email",
        hint_text="Digite seu email",
        
    )

    input_mensagem = ft.TextField(
        label="Mensagem",
        hint_text="Digite sua mensagem",
        multiline=True,
        min_lines=4,
        max_lines=None
    )   

    
    lista_de_usuarios=[]
    
    def salvar_dados(e):
        usuario = [input_nome.value, input_email.value, input_mensagem.value]
        lista_de_usuarios.append(usuario)
        page.dialog = caixa_confirmacao
        page.dialog.open = True
        page.update()

    caixa_confirmacao = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirmação"),
        content=ft.Text("Dados salvos com sucesso!"),
        on_dismiss=lambda e: print("Pronto!"),
        title_padding=ft.padding.all(25)
    )
        

    
    page.add(
        input_nome,
        input_email,
        input_mensagem,
        ft.ElevatedButton(text="Salvar",on_click=lambda e: page.open(caixa_confirmacao))
    )
    
page = ft.app(target=main)
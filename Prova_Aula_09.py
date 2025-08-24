import flet as ft
def main(page: ft.Page):
  
    page.title = "Lista de Tarefas"
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    input_tarefa = ft.TextField(
        label="Nova tarefa",
        hint_text="Digite a tarefa...",
        expand=True
    )
    botao_de_adicionar = ft.ElevatedButton(text="Adicionar")

    tarefas = ft.ListView(expand=True, spacing=8, padding=10, auto_scroll=False)

    def adicionar_tarefa(_: ft.ControlEvent) -> None:
        value = (input_tarefa.value or "").strip()
        if not value:
            return
        tarefas.controls.append(ft.ListTile(title=ft.Text(value)))
        input_tarefa.value = ""
        page.update()

    botao_de_adicionar.on_click = adicionar_tarefa
    input_tarefa.on_submit = adicionar_tarefa

    page.add(
        ft.Column(
            controls=[
                ft.Row([input_tarefa, botao_de_adicionar]),
                ft.Divider(),
                ft.Text("Tarefas:", weight=ft.FontWeight.BOLD),
                tarefas,
            ],
            expand=True,
        )
    )

ft.app(target=main)

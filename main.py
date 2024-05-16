import flet as ft

formData = {}
tableData = {"table":None, "rows":[]}
table_reference = None

def app_form_input_field(id:str, name:str, expand:int):

    textField = ft.TextField(
        border_color="transparent",
        height=20,
        text_size=13,
        content_padding=0,
        cursor_color="black",
        cursor_width=1,
        cursor_height=18,
        color="black"
    )

    formData[id] = textField

    return ft.Container(
        expand=expand,
        height=45,
        bgcolor="#ebebeb",
        border_radius=6,
        padding=8,
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Text(
                    value=name,
                    size=9,
                    color="black",
                    weight="bold"
                ),
                textField
            ]
        )
    )

def get_input_data(e):

    data = [
        formData["field1"].value,
        formData["field2"].value,
        formData["field3"].value,
        formData["field4"].value,   
    ]

    for _, field in formData.items():
        field.value = ""
        field.update()

    tableData["rows"].append(data)
    tableData["table"].rows = return_table_rows()
    tableData["table"].update()


def return_table_rows(filter_col1=""):

    rows = [
        row for row in tableData["rows"] if filter_col1 in row[0]
    ]

    return [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(t)) 
                for t in data
            ],
        )
        for data in rows
    ]    

def data_table():

    table = ft.DataTable(
        width=999999,
        border=ft.border.all(2, "#ebebeb"),
        border_radius=8,
        horizontal_lines=ft.border.BorderSide(1, "#ebebeb"),
                                                
        columns=[
            ft.DataColumn(
                ft.Text("Colunm One", size=12, color="black",weight="bold")
            ),
            ft.DataColumn(
                ft.Text("Colunm One", size=12, color="black",weight="bold")
            ),
            ft.DataColumn(
                ft.Text("Colunm One", size=12, color="black",weight="bold")
            ),
            ft.DataColumn(
                ft.Text("Colunm One", size=12, color="black",weight="bold")
            )
        ],
        rows=return_table_rows()
    )

    tableData["table"] = table
    
    return table


def search_for_table(e):
    
    tableData["table"].rows = return_table_rows(e.control.value)
    tableData["table"].update()

def main(page: ft.Page):
    
    page.bgcolor = "#fdfdfd"
    page.padding = 20
    page.add(
        ft.Column(
            expand=True,
            controls=[


                #region HEADER
                ft.Container(
                    height=60,
                    bgcolor="#081d33",
                    border_radius=ft.border_radius.only(top_left=15, top_right=15),
                    padding=ft.padding.only(left=15, right=15),
                    content=ft.Row(
                        expand=True,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            # HEADER BRAND
                            ft.Container(
                                content=ft.Text(
                                    "Line Indent",
                                    size=15
                                )
                            ),
                            # HEADER SEARCH
                            ft.Container(
                                width=320,
                                bgcolor="white10",
                                border_radius=6,
                                content=ft.Row(
                                    spacing=10,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Icon(
                                            name=ft.icons.SEARCH_ROUNDED,
                                            size=17,
                                            opacity=0.85
                                        ),
                                        ft.TextField(
                                            on_change=search_for_table,
                                            border_color="transparent",
                                            height=20,
                                            text_size=14,
                                            content_padding=0,
                                            cursor_color="white",
                                            cursor_width=1,
                                            hint_text="Search"
                                        )
                                    ]
                                )
                            ),
                            # HEADER AVATAR
                            ft.Container(
                                content=ft.IconButton(
                                    ft.icons.PERSON
                                )
                            )
                        ]
                    )
                ),
                #endregion


                ft.Divider(
                    height=2,
                    color="transparent"
                ),


                #region FORM
                ft.Container(
                    height=190,
                    bgcolor="white10",
                    border=ft.border.all(1, "#ebebeb"),
                    border_radius=8,
                    padding=15,
                    content=ft.Column(
                        expand=True,
                        controls=[
                            ft.Row(
                                controls=[
                                    app_form_input_field("field1","Field*", True),
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    app_form_input_field("field2","Field One*", 3),
                                    app_form_input_field("field3","Field Two*", 1),
                                    app_form_input_field("field4","Field Three*", 1),
                                ]
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.END,
                                controls=[
                                    ft.Container(
                                        alignment=ft.alignment.center,
                                        content=ft.ElevatedButton(
                                            on_click=lambda e: get_input_data(e),
                                            bgcolor="081d33",
                                            content=ft.Row(
                                                controls=[
                                                    ft.Icon(
                                                        name=ft.icons.ADD_ROUNDED,
                                                        size=12
                                                    ),
                                                    ft.Text(
                                                        "Add Input Field To Table",
                                                        size=12,
                                                        weight="bold"
                                                    )
                                                ]
                                            ),
                                            style=ft.ButtonStyle(
                                                shape={
                                                    "": ft.RoundedRectangleBorder(radius=6)
                                                },
                                                color={
                                                    "": "white"
                                                }
                                            ),
                                            height=42,
                                            width=220
                                        )
                                    )
                                ]
                            )
                        ]
                    )
                ),
                #endregion


                #region TABLE
                
                ft.Column(
                    scroll='hidden',
                    controls=[
                        data_table()
                    ]
                )
                #endregion



            ]
        )
    )

    page.update()



ft.app(main)

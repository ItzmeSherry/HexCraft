import flet as ft

def main(page: ft.Page):
    page.title = "Witch's Potion Mixer"
    page.update()

    # Define UI elements
    title = ft.Text("Witch's Potion Mixer", style="headlineMedium")
    description = ft.Text("Select ingredients to mix into your potion:")
    
    # Ingredient checkboxes
    ingredients = ["Frog Legs", "Bat Wings", "Eye of Newt", "Wolfsbane", "Mandrake Root"]
    checkboxes = [ft.Checkbox(label=ingredient) for ingredient in ingredients]

    # Potion result text
    potion_result = ft.TextField(label="Your Potion", multiline=True, expand=True, width=400)

    # Button to mix ingredients
    mix_button = ft.IconButton(text="Mix Ingredients", on_click=lambda e: mix_ingredients(e, checkboxes, potion_result))

    # Layout with alignment
    form = ft.Column(
        controls=[title, description] + checkboxes + [mix_button, potion_result],
        spacing=10,
        alignment=ft.MainAxisAlignment.START
    )

    # Wrap the form in another column to center it on the page
    centered_form = ft.Column(
        controls=[form],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        cross_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(centered_form)

def mix_ingredients(event, checkboxes, result_field):
    selected_ingredients = [cb.label for cb in checkboxes if cb.value]
    if not selected_ingredients:
        result_field.value = "Please select at least one ingredient."
    else:
        potion_desc = f"You have created a potion with {' and '.join(selected_ingredients)}."
        result_field.value = potion_desc
    event.control.page.update()

if __name__ == "__main__":
    ft.app(target=main)


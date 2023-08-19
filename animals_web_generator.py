import data_fetcher


OUTPUT_FILE_NAME = 'animals.html'


def save_to_file(text, file_name):
    with open(file_name, "w") as fileobj:
        fileobj.write(text)


def serialize_animal(animal_obj):
    """Serializes an animal object into an HTML list item"""
    outcome_string = '<li class="cards__item">\n'
    outcome_string += f'<div class="card__title">{animal_obj.get("name", "")}</div>\n'
    outcome_string += '<p class="card__text">\n'

    locations = animal_obj.get("locations", [])
    location_string = ", ".join(locations)
    outcome_string += f'<strong>Location:</strong> {location_string}<br/>\n'

    taxonomy = animal_obj.get("taxonomy", {})
    animal_type = taxonomy.get("class", "")
    outcome_string += f'<strong>Type:</strong> {animal_type}<br/>\n'

    characteristics = animal_obj.get("characteristics", {})
    animal_diet = characteristics.get("diet", "")
    outcome_string += f'<strong>Diet:</strong> {animal_diet}<br/>\n'

    outcome_string += '</p>\n'
    outcome_string += '</li>\n'
    return outcome_string


def generate_html(animals_data, html_template_path, search_term):
    """Generates HTML outcome_string from animal data and an HTML template"""
    with open(html_template_path, "r") as data_html:
        html_template = data_html.read()
    outcome_string = ""
    if not animals_data:
        outcome_string += f"<h2>The animal '{search_term}' doesn't exist.</h2>\n"
    else:
        for animal in animals_data:
            outcome_string += serialize_animal(animal)
    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", outcome_string)
    return final_html


def main():
    search_term = input("Enter the name of an animal: ")
    animals_data = data_fetcher.fetch_data(search_term)
    html_content = generate_html(animals_data, 'animals_template.html', search_term)
    save_to_file(html_content, OUTPUT_FILE_NAME)
    print(f"Website was successfully generated in the file {OUTPUT_FILE_NAME}")


if __name__ == "__main__":
    main()

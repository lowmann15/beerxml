import os.path

from beerxml.beerxml_handler import BeerxmlHandler


def test_parse_to_beerxml() -> None:
    with open(os.path.join(os.path.dirname(__file__), "assets/Almtaler Weizen.xml")) as file_content:
        xml_content = file_content.read()
    recipe = BeerxmlHandler(xml_content=xml_content).parse_to_beerxml()
    print(recipe)

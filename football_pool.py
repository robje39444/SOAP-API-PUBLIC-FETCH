# football_pool.py
from zeep import Client, helpers  # pyright: ignore[reportMissingImports]

# ------------------------------------------------------------------
# Define the WSDL URL – this is the contract that describes the API.
WSDL_URL = "https://footballpool.dataflex.dev/info.wso?WSDL"

# Create a Zeep client. Internally it parses the WSDL and builds stubs.
client = Client(wsdl=WSDL_URL)


# ------------------------------------------------------------------
def get_football_details(iso_code: str):
    """
    Calls three different operations of FootballPoolService
    and prints the results in plain Python objects.
    """
    # Call the SOAP operation – Zeep returns a custom object.
    football_pool = client.service.footballpool(iso_code)
    country_flag = client.service.CountryFlag(iso_code)

    # The Currency operation returns a struct with two fields
    city_struct = client.service.CityName(iso_code)

    # Convert the Zeep object into a plain dict for easier use.
    city_dict = helpers.serialize_object(city_struct)

    print(f"\nCountry flag: {iso_code}")
    print(f"Full name : {country_flag}")
    print(f"sTeam1Name: {football_pool.sTeam1Name}")
    print("City name :", end=" ")
    print(f"{city_dict['sName']} ({city_dict['sISOCode']})")


# ------------------------------------------------------------------
if __name__ == "__main__":
    # Ask the user for a two‑letter ISO country code.
    iso = input("Enter an ISO country code (e.g. US, NL, BE):").strip().upper()
    try:
        get_football_details(iso)
    except Exception as exc:
        print(f" Something went wrong: {exc}")

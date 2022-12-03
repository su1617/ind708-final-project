import pandas as pd

company_list_original = pd.read_excel('companies_sorted 2.xls.xls')
company_list_original = company_list_original.drop(columns=['Unnamed: 0'])
company_list = company_list_original.dropna()


def get_industry_list():
    industries = company_list['industry'].unique()
    return industries


def get_country_list(company_list_2):
    countries = company_list_2['country'].unique()
    return countries


def print_countries(countries):
    print("Your choices are as follows:")
    countries.sort()
    for i in range(0, len(countries)):
        print(f"{i + 1}. {countries[i]}")


def print_industries(industries):
    print("Your choices are as follows:")
    industries.sort()
    for i in range(0, len(industries)):
        print(f"{i + 1}. {industries[i]}")


def save_possibilities(my_list):
    save_input = input("Would you like to save your possibilities in a csv file? (y/n): ")
    if save_input == "y":
        print("Your possible matches are being saved.")
        save_name = input("What do you want to call the file: ")
        save_name += ".csv"
        my_list.to_csv(save_name, index=False)


def my_company_choices_by_industry(countries_indef, industry_choice):
    if industry_choice == "information" or industry_choice == "technology":
        industry_choice = "information technology and services"
    my_choices = countries_indef[countries_indef['industry'] == industry_choice]
    # print(my_choices.to_markdown())
    print(f"There are {len(my_choices)} options available after industry filter.")
    return my_choices


def my_company_choices_by_country(countries_indef, country_choice):
    my_choices = countries_indef[countries_indef['country'] == country_choice]
    # print(my_choices.to_markdown())
    print(f"There are {len(my_choices)} options available after country filter.")
    return my_choices


def main():
    print("In this program you will first be asked to choose a industry (there will be a list for available) "
          ", a country you wish to work in, and than a city. Please make sure you are giving your input correctly "
          "because if "
          "you don't, program will NOT be able to work for your specifics. Thank you very much...")
    while True:
        # Ask if the user wants to see the industry lists and then ask for whatever industry they want to work in
        industry_see_input = input("Do you want to see the industries you can choose? (y/n): ")
        if industry_see_input == "y":
            print_industries(get_industry_list())
            industry_input = input("Choose the industry you want to work in: ")
        else:
            industry_input = input("Choose the industry you want to work in: ")
        # Get the choices by industry
        choices_by_industry = my_company_choices_by_industry(company_list, industry_input)
        user_input1 = input("Do you want to see the company list you might be interested in (y/n): ")
        if user_input1 == "y":
            print(choices_by_industry.to_markdown())
        save_possibilities(choices_by_industry)

        user_input3 = input("Would you like to choose a country next? If no you will exit. (y/n): ")
        if user_input3 == "n":
            break

        # Ask if the user wants to see the country lists and then ask for whatever country they want to work in
        country_see_input = input("Do you want to see the countries you can choose? (y/n): ")

        if country_see_input == "y":
            print_countries(get_country_list(choices_by_industry))
            country_input = input("Choose the country you want to work in: ")
        else:
            country_input = input("Choose the country you want to work in: ")

        choices_by_country = my_company_choices_by_country(choices_by_industry, country_input)

        save_possibilities(choices_by_country)

        last_print = input("Do you still want to see your choices on command line? (y/n): ")
        if last_print == "y":
            print(choices_by_country.to_markdown())

        user_input2 = input("Do you want to go at it again? (y/n): ")
        if user_input2 != "y":
            break


main()

"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('td')
        # print(tags)
        count = 0
        single_number = ''
        male_number = 0
        female_number = 0
        for tag in tags:
            count += 1

            if count % 5 == 4:
                male_number += int(tag.text.replace(',', ''))

            # if count == 4 or (count-4) % 5 == 0:  # 4, 9, 14...
            #     for i in range(len(tag.text)):
            #         if tag.text[i].isdigit():
            #             single_number += tag.text[i]
            #     male_number += int(single_number)
            #     single_number = ''

            elif count == 6 or (count - 6) % 5 == 0 and count != 1:
                female_number += int(tag.text.replace(',', ''))

            # elif count == 6 or (count - 6) % 5 == 0 and count != 1:  # 6, 11, 16...
            #     for i in range(len(tag.text)):
            #         if tag.text[i].isdigit():
            #             single_number += tag.text[i]
            #     female_number += int(single_number)
            #     single_number = ''
        print('Male_number: ' + str(male_number))
        print('Female_number: ' + str(female_number))


if __name__ == '__main__':
    main()

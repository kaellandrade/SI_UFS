'''
Estes dados estão ordenados por cpf para cada municipio.Ex:
[
    [
        (28223741395, 'Rina Barron', '1, 17, 1977', 'Amparo de São Francisco', 'SE', 'Pfizer', '5, 6, 2021')
    ],
    [
        (13040222934, 'Reed Ruiz', '7, 31, 1976', 'Aquidabã', 'SE', 'AstraZeneca', '1, 18, 2021'), 
        (15931101758, 'Forrest Eaton', '9, 4, 1983', 'Aquidabã', 'SE', 'Pfizer', '4, 3, 2021'), 
        (33535922592, 'Uriah Wiggins', '12, 14, 1979', 'Aquidabã', 'SE', 'AstraZeneca', '6, 2, 2022'), 
        (65488358420, 'Maisie Vasquez', '3, 24, 1979', 'Aquidabã', 'SE', 'AstraZeneca', '5, 21, 2021')
    ]
    Note que cada tupla é uma determinada pessoa, naquele municipio. 
    Assim, o primeiro município Amparo contém uma pessoa, Aquidabã contém 4 pessoas e assim por diante.
    Além disso, para cada município, temos que as pessoas estão ordenadas por CPF.
]
'''
cadastro = [
    [
        (16196924314, 'Rina Barron', '1, 17, 1977', 'Amparo de São Francisco', 'SE', 'Pfizer', '5, 6, 2021'), 
        (18414903687, 'Maisie Vasquez', '3, 24, 1979', 'Amparo de São Francisco', 'SE', 'AstraZeneca', '5, 21, 2021'), 
        (25166032161, 'Uriah Wiggins', '12, 14, 1979', 'Amparo de São Francisco', 'SE', 'AstraZeneca', '6, 2, 2022')
    ], 
    [
        (19744741227, 'Reed Ruiz', '7, 31, 1976', 'Aquidabã', 'SE', 'AstraZeneca', '1, 18, 2021')
    ], 
    [
        (82095389298, 'Forrest Eaton', '9, 4, 1983', 'Aracaju', 'SE', 'Pfizer', '4, 3, 2021')
    ], 
    [
        (17761356567, 'Laurel Warner', '11, 19, 1988', 'Arauá', 'SE', 'Pfizer', '8, 6, 2022'),
        (23709573638, 'Guy Wyatt', '4, 10, 1985', 'Arauá', 'SE', 'Pfizer', '7, 24, 2021'),
        (93035984199, 'Uma Hooper', '2, 22, 1997', 'Arauá', 'SE', 'coronavac', '4, 29, 2021')
    ],
    [
        (13021466741, 'Christian Patton', '8, 29, 1964', ' Areia Branca', 'SE', 'Pfizer', '8, 26, 2021'), 
        (16493897356, 'Kirby Morin', '1, 28, 1966', ' Areia Branca', 'SE', 'coronavac', '10, 30, 2021'),
        (24746259780, 'Blossom Hendricks', '10, 8, 1978', ' Areia Branca', 'SE', 'AstraZeneca', '1, 25, 2022'), 
        (32290578981, 'Stewart Greer', '7, 16, 1983', ' Areia Branca', 'SE', 'AstraZeneca', '3, 4, 2021')
    ]
]
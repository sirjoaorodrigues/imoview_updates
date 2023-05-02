from gerador.adjectives import fem_adj, fem_adj2, masc_adj, mid_text, mid_text2, financing_text, exchange_text, final_text


class Realty:
    def __init__(self, type_of, price, dorms, suites, baths, parking_lot, c_area, t_area, district, city,
                 financing=False, exchange=False):

        self.type_realty = None
        self.type_of = type_of
        self.price = price
        self.dorms = dorms
        self.suites = suites
        self.baths = baths
        self.parking_lot = parking_lot
        self.c_area = c_area
        self.t_area = t_area
        self.district = district
        self.city = city
        self.financing = financing
        self.exchange = exchange

    def get_realty(self):
        
        if self.type_of == 'Sobrado':
            self.type_realty = f' {fem_adj} casa de dois pavimentos, localizada'
        elif self.type_of == 'Casa Térrea':
            self.type_realty = f' {fem_adj} casa térrea, localizada'
        elif self.type_of == 'Casa':
            self.type_realty = f' {fem_adj} casa térrea, localizada'
        elif self.type_of == 'Chácara':
            self.type_realty = f' {fem_adj} e espaçosa Chácara, localizada'
        elif self.type_of == 'Terreno':
            self.type_realty = f' {masc_adj} terreno em excelente localização'
        elif self.type_of == 'Apartamento':
            self.type_realty = f' {masc_adj} apartamento em excelente localização'
        elif self.type_of == 'Imóvel':
            self.type_realty = f'{masc_adj} Imóvel em excelente localização'
        elif self.type_of == 'Barracão':
            self.type_realty = f' {masc_adj} Barracão, localizado'
        elif self.type_of == 'Área':
            self.type_realty = f' {fem_adj} Área, localizada'
        elif self.type_of == 'Prédio':
            self.type_realty = f' {masc_adj} Prédio, localizado'
        return self.type_realty

    def get_locate(self):
        location = f'no bairro {self.district} na {fem_adj2.lower()} cidade de {self.city}.\n\n'
        return location

    def get_terrain(self):

        if self.type_of == 'Apartamento':
            terrain = f'São no total {self.c_area} metros quadrados.\n\n'
        elif self.type_of == 'Terreno':
            terrain = f'São no total {self.c_area} metros quadrados para você construir.\n\n'
        elif self.type_of == 'Barracão':
            terrain = f'São no total {self.c_area} metros quadrados.\n\n'
        else:
            terrain = f'São no total {self.c_area} metros quadrados de construção em um terreno de {self.t_area} ' \
                      f'metros.\n\n'
        return terrain

    def get_rooms(self):
        room = f'O imóvel apresenta {self.dorms} dormitórios, sendo {self.suites} deles suítes, possui {self.baths}' \
               f' banheiros, além de {self.parking_lot} vagas de garagem.\n\n'
        return room

    def get_financing(self):

        if self.financing is True:
            return financing_text
        else:
            return '\n'

    def get_exchange(self):

        if self.exchange is True:
            return exchange_text
        else:
            return '\n'

    def run(self):

        if self.type_of == 'Terreno':
            self.cabecalho = f'{self.type_of} em {self.city} - {self.district} - {self.c_area}M² - R${self.price}\n(Valor sujeito a alterações)\n\nÁrea de Terreno: ' \
                         f'{self.t_area} M²\nCidade: {self.city}\nBairro: {self.district}\nValor de Negociação: R$ {self.price}\n\n'

            values = f'{self.cabecalho}{self.get_realty()} {self.get_locate()} {self.get_terrain()} ' \
                     f'{self.get_financing()} {self.get_exchange()} {final_text}'
        else:
            self.cabecalho = f'{self.type_of} em {self.city} - {self.district} - {self.c_area}M² - R${self.price}\n(Valor sujeito a alterações)\n\nÁrea de Terreno: ' \
                         f'{self.t_area} M²\nÁrea de Construção: {self.c_area} M²\nCidade: {self.city}\nBairro: {self.district}\nValor de Negociação: R$ {self.price}\n\n' \
                         f'Layout do Imóvel:\n{self.dorms} Dormitórios\n{self.baths} Banheiros\n{self.parking_lot} Vagas de Garagem\n\n'

            values = f'{self.cabecalho}{self.get_realty()} {self.get_locate()} {mid_text[0]} {self.get_terrain()} {mid_text2[0]} ' \
                     f'{self.get_rooms()} {self.get_financing()} {self.get_exchange()} {final_text}'

        return values

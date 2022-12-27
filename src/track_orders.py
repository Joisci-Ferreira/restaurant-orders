from collections import Counter


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.lista_pedidos = []
        pass

    def __len__(self):
        pass
        return len(self.lista_pedidos)

    def add_new_order(self, customer, order, day):
        pass
        self.lista_pedidos.append({
            'customer': customer,
            'order': order,
            'day': day
        })
        return self.lista_pedidos    

    def get_most_ordered_dish_per_customer(self, customer):
        pass
        customer_list = []
        for pedidos in self.lista_pedidos:
            if pedidos['customer'] == customer:
                customer_list.append(pedidos['order'])

        orders_statistics = Counter(customer_list)

        mais_pedida = orders_statistics.most_common()

        return mais_pedida[0][0]     

    def get_never_ordered_per_customer(self, customer):
        pass
        customer_list = []
        all_orders = []

        for pedidos in self.lista_pedidos:
            all_orders.append(pedidos['order'])

            if pedidos['customer'] == customer:
                customer_list.append(pedidos['order'])

        all_unique_orders = set(all_orders)
        customer_unique_orders = set(customer_list)

        return all_unique_orders.difference(customer_unique_orders)        

    def get_days_never_visited_per_customer(self, customer):
        pass
        customer_days = []
        all_days = []

        for pedidos in self.lista_pedidos:
            all_days.append(pedidos['day'])

            if pedidos['customer'] == customer:
                customer_days.append(pedidos['day'])

        all_unique_days = set(all_days)
        customer_unique_days = set(customer_days)

        return all_unique_days.difference(customer_unique_days)

    def get_all_days_list(self):
        all_days = []
        for pedidos in self.lista_pedidos:
            all_days.append(pedidos['day'])

        return all_days        

    def get_busiest_day(self):
        pass
        all_days = self.get_all_days_list()
        all_unique_days = Counter(all_days)
        days_statistics = all_unique_days.most_common()

        return days_statistics[0][0]
        

    def get_least_busy_day(self):
        pass
        all_days = self.get_all_days_list()
        all_unique_days = Counter(all_days)
        days_statistics = all_unique_days.most_common()

        return days_statistics[-1][0]

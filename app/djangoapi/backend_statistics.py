from collections import defaultdict
import requests
import statistics
import numpy
from cacheops import cached


def get_currencies_values_dict(date_start, date_end, currency):
    request = f"https://api.exchangeratesapi.io/history?start_at={date_start}&end_at={date_end}&base={currency}"
    response = requests.get(request)
    print(response.text)
    json = response.json()
    rates = json["rates"]
    currencies_values = dict()
    for year_statistics in rates.values():
        for currency_name, currency_value in year_statistics.items():
            if currency_name not in currencies_values:
                currencies_values[currency_name] = list()
            currencies_values[currency_name].append(currency_value)
    return currencies_values, rates.keys()


def get_standard_deviation(currencies_values, base_currency):
    standard_dev = dict()
    for cur_name, cur_values in currencies_values.items():
        if cur_name != base_currency:
            standard_dev[cur_name] = statistics.stdev(cur_values)
    return standard_dev


def get_average_value(currencies_values, base_currency):
    def average(lst):
        return sum(lst) / len(lst)

    average_dict = dict()
    for cur_name, cur_values in currencies_values.items():
        if cur_name != base_currency:
            average_dict[cur_name] = average(cur_values)
    return average_dict


def get_correlation(currencies_values, base_currency):
    correlation_dict = defaultdict(dict)
    for cur_name_1, cur_values_1 in currencies_values.items():
        for cur_name_2, cur_values_2 in currencies_values.items():
            if cur_name_1 != base_currency and cur_name_2 != base_currency:
                X = cur_values_1
                Y = cur_values_2
                print(f" {X} \n {Y}")
                correlation_dict[cur_name_1][cur_name_2] = numpy.corrcoef(X, Y)[0, 1]
                print(correlation_dict[cur_name_1][cur_name_2])
    return correlation_dict


@cached(timeout=24 * 60 * 60)
def get_all_statistics(date_start, date_end, currency):
    currencies_values, dates = get_currencies_values_dict(date_start, date_end, currency)
    standard_deviation = (get_standard_deviation(currencies_values, currency))
    average_value = get_average_value(currencies_values, currency)
    correlation = get_correlation(currencies_values, currency)
    final_dict = defaultdict(dict)

    for cur_name, value in standard_deviation.items():
        if cur_name not in final_dict:
            final_dict[cur_name]["std_dev"] = value

    for cur_name, value in average_value.items():
        final_dict[cur_name]["avg"] = value

    for cur_name, value in correlation.items():
        final_dict[cur_name]["cor"] = value

    return final_dict

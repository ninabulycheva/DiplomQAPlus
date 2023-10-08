import configuration
import requests
import data


#   создание заказа
def post_new_order(order_body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
	                     json = order_body,
	                     headers = data.headers)


#   получения заказа по треку заказа
def get_order_from_track(track):
	return requests.get(configuration.URL_SERVICE + configuration.TRACK_FOR_ORDER_PATH + str(track),
	                    headers = data.headers)
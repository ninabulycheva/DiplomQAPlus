import data
import sender_stand_request
#Булычева Нина, 9-я когорта Марс — Диплом.Финальный проект. Инженер по тестированию плюс

# запрос на получения заказа по треку заказа
def request_code():
	response_post_new_order = sender_stand_request.post_new_order(data.order_body)
	track = response_post_new_order.json()["track"]
	return sender_stand_request.get_order_from_track(track).status_code


# проверка кода ответа
def test_code_200():
	assert request_code() == 200
from bd_app import *

client = Client_DB()

"""Клиенты. Еесли клиента с таким логином нет - запишет и вернет True, иначе False. дата - время записи"""
print(client.add_client("test_client", "hash_pass", "example@email.com", "555.555.555.555"))

"""вернет все поля клиенета, кроме _id"""
print(client.get_client("test_client"))

print("*" * 10)
"""можно отдельно получать поля соответствующими методами. target (ip для скана) можно редактировать"""
print(client.add_target("test_client", "555.555.555.556"))
print(client.get_target("test_client"))
print(client.del_target("test_client", "555.555.555.556"))
print(client.get_target("test_client"))
print(client.del_target("test_client", "555.555.555.556"))


report = Report_DB()
print("*" * 10)

"""Отчеты. можно записать, изменять потом нельзя"""
print(report.add_report("test_client", "555.555.555.555", "test_report"))
report.add_report("test_client", "555.555.555.555", "test_report2")
report.add_report("test_client", "555.555.555.556", "test_report")

"""есть фильтры по лошину и ip"""
print(report.get_report(login="test_client"))
print(report.get_report(login="test_client", target="555.555.555.556"))

"""можно получить последний отчет, тоже есть фильтры"""
print(report.get_last_report(login="test_client", target="555.555.555.555"))

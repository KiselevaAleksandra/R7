import create
import send
import check

while(1):
    print("Собрать файлы - 1\nОтправить запросы - 2\nПроверить состояние запросов - 3\nВыход - 0\n")
    n = input()
    if (n == '1'):
        create.create()
    elif (n == '2'):
        send.send()
    elif (n == '3'):
        check.check()
    elif (n == '0'):
        print("Работа завершена.")
        exit()
    else:
        print("Введено неверное значение!\n")
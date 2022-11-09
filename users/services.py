class LastActivity:
    def get_correct_str_time_ru(n, format):
        days = ["день", "дня", "дней"]
        hours = ["час", "часа", "часов"]
        minutes = ["минуту", "минуты", "минут"]
        seconds = ["секунду", "секунды", "секунд"]
        p = "Был(а) недавно"
        if n % 10 == 1 and n % 100 != 11:
            p = 0
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            p = 1
        else:
            p = 2

        return (
            f"Был(а) в сети {n} {days[p]} назад"
            if format == "d"
            else f"Был(а) в сети {n} {hours[p]} назад"
            if format == "h"
            else f"Был(а) в сети {n} {minutes[p]} назад"
            if format == "m"
            else f"Был(а) в сети {n} {seconds[p]} назад"
        )


class Viewer:
    def get_client_ip(request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip




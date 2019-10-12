class TimeParser():
    def parse_time(time, param="web->git"):
        try:
            if param == "web->git":
                return f'{time[6:10]}-{time[3:5]}-{time[0:2]}T{time[11:16]}:00Z'
            elif param == "git->web":
                return f'{time[8:10]}.{time[5:7]}.{time[0:4]} {time[11:19]}'
            else:
                raise Exception()
        except Exception:
            return "Invalid Time Format"

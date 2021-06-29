

class CheckAPI:

    @classmethod
    def check_single_page_url(cls, part_url, line, dbg_api):
        part_line = line.split(part_url, 1)
        if len(part_line) == 2 and part_line[1][:6].isdigit():
            return True
        return False


class CheckAPI:

    @classmethod
    def check_single_page_url(cls, part_url, line, num_after=0):
        part_line = line.split(part_url, 1)
        if len(part_line) == 2 and part_line[1][:num_after].isdigit():
            return True
        return False